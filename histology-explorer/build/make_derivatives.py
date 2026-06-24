#!/usr/bin/env python3
"""
make_derivatives.py — generate browser-viewable JPEG derivatives from archival .tif images.

Many histology images on owl are 15 MB .tif files that browsers cannot display. This script
produces, for each .tif, a downsized web JPEG and a small thumbnail JPEG, and writes a
manifest the build step reads to wire them into the explorer.

It discovers which .tif files exist by reading build/listings/<species>__<project>.txt
(the same captured owl listings the indexer uses), so it stays in sync automatically.

OUTPUT layout (ready to upload to owl):
    <outdir>/<species>/<project>/derivatives/<stem>-web.jpg     (long side <= --web-px)
    <outdir>/<species>/<project>/derivatives/<stem>-thumb.jpg   (long side <= --thumb-px)
Then upload each `<species>/<project>/derivatives/` folder into the matching owl project
directory, so the files live at:
    owl.fish.washington.edu/hesperornis/<species>/<project>/derivatives/<stem>-web.jpg

It also writes/updates  build/derivatives_manifest.csv  (columns: species,project,filename,
web_jpg,thumb_jpg). Re-run `python3 build_index.py` afterward and the .tif samples will show
real thumbnails instead of "TIF only" placeholders.

SOURCE of the .tif pixels — choose one:
  --tif-dir DIR    Convert .tif files already downloaded locally. DIR is searched recursively;
                   files are matched to listings by basename.
  --from-owl       Stream each .tif straight from owl, convert, and discard (needs network).

Requires Pillow:  pip install Pillow   (TIFFs may also need:  pip install imagecodecs)

EXAMPLES
    # Just the tif-only species, streamed from owl:
    python3 make_derivatives.py --from-owl --species O_angasi --outdir ../_derivatives

    # Convert a local folder of tifs you already rsynced down:
    python3 make_derivatives.py --tif-dir ~/owl_tifs --outdir ../_derivatives
"""
import argparse, csv, glob, io, os, sys, urllib.request
from collections import OrderedDict

OWL_BASE = "https://owl.fish.washington.edu/hesperornis"
HERE = os.path.dirname(os.path.abspath(__file__))


def load_listings(species_filter):
    """Return list of (species, project, filename) for every .tif in the captured listings."""
    out = []
    for path in sorted(glob.glob(os.path.join(HERE, "listings", "*.txt"))):
        base = os.path.basename(path)[:-4]
        species, project = base.split("__", 1)
        if species_filter and species != species_filter:
            continue
        for line in open(path):
            fn = line.strip()
            if fn.lower().endswith((".tif", ".tiff")):
                out.append((species, project, fn))
    return out


def _download(url, attempts=4, timeout=300):
    """Download a URL fully, retrying on truncated/partial reads (owl drops big streams)."""
    import time, http.client
    last = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "histology-derivatives/1.0",
                                                       "Connection": "close"})
            buf = io.BytesIO()
            with urllib.request.urlopen(req, timeout=timeout) as r:
                expected = r.length  # may be None
                while True:
                    chunk = r.read(1 << 20)   # 1 MB
                    if not chunk:
                        break
                    buf.write(chunk)
            data = buf.getvalue()
            if expected and len(data) < expected:
                raise http.client.IncompleteRead(len(data), expected - len(data))
            return data
        except Exception as e:           # IncompleteRead, timeout, ConnectionReset, etc.
            last = e
            if i < attempts - 1:
                time.sleep(2 * (i + 1))   # back off: 2s, 4s, 6s
    raise last


def open_image(species, project, filename, args, local_index):
    from PIL import Image
    if args.tif_dir:
        p = local_index.get(filename)
        if not p:
            return None
        return Image.open(p)
    # --from-owl
    url = f"{OWL_BASE}/{species}/" + (f"{project}/" if project else "") + filename.replace(" ", "%20")
    data = _download(url)
    return Image.open(io.BytesIO(data))


def save_jpeg(img, dest, max_px, quality):
    from PIL import Image
    im = img
    if im.mode not in ("RGB", "L"):
        im = im.convert("RGB")
    w, h = im.size
    scale = min(1.0, float(max_px) / max(w, h))
    if scale < 1.0:
        im = im.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.LANCZOS)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    im.save(dest, "JPEG", quality=quality, optimize=True)


def main():
    ap = argparse.ArgumentParser(description="Generate JPEG derivatives from archival .tif histology images.")
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--tif-dir", help="Folder of .tif files already downloaded (searched recursively).")
    src.add_argument("--from-owl", action="store_true", help="Stream .tif files directly from owl.")
    ap.add_argument("--outdir", default=os.path.join(HERE, "..", "_derivatives"),
                    help="Where to write the derivatives tree (default: ../_derivatives).")
    ap.add_argument("--species", default="", help="Limit to one owl species folder (e.g. O_angasi).")
    ap.add_argument("--web-px", type=int, default=1600, help="Max long side of the web JPEG (default 1600).")
    ap.add_argument("--thumb-px", type=int, default=400, help="Max long side of the thumbnail (default 400).")
    ap.add_argument("--quality", type=int, default=85, help="JPEG quality (default 85).")
    ap.add_argument("--limit", type=int, default=0, help="Process at most N files (0 = all). Useful for a test run.")
    args = ap.parse_args()

    try:
        import PIL  # noqa
    except ImportError:
        sys.exit("Pillow is required:  pip install Pillow   (and maybe: pip install imagecodecs)")

    targets = load_listings(args.species)
    if args.limit:
        targets = targets[:args.limit]
    if not targets:
        sys.exit("No .tif files found in listings" + (f" for species {args.species}" if args.species else "") + ".")

    local_index = {}
    if args.tif_dir:
        for p in glob.glob(os.path.join(args.tif_dir, "**", "*.tif*"), recursive=True):
            local_index[os.path.basename(p)] = p

    outdir = os.path.normpath(args.outdir)
    manifest_path = os.path.join(HERE, "derivatives_manifest.csv")
    manifest = OrderedDict()
    if os.path.exists(manifest_path):
        for m in csv.DictReader(open(manifest_path)):
            manifest[(m["species"], m["project"], m["filename"])] = m

    done = skipped = failed = 0
    for species, project, filename in targets:
        stem = filename.rsplit(".", 1)[0]
        web_name, thumb_name = f"{stem}-web.jpg", f"{stem}-thumb.jpg"
        proj_dir = os.path.join(outdir, species, project, "derivatives")
        web_dest, thumb_dest = os.path.join(proj_dir, web_name), os.path.join(proj_dir, thumb_name)
        if os.path.exists(web_dest) and os.path.exists(thumb_dest):
            manifest[(species, project, filename)] = {
                "species": species, "project": project, "filename": filename,
                "web_jpg": web_name, "thumb_jpg": thumb_name}
            skipped += 1
            continue
        try:
            img = open_image(species, project, filename, args, local_index)
            if img is None:
                failed += 1
                print(f"  MISS (no local tif): {filename}")
                continue
            try:
                img.seek(0)  # first page of multipage tiff
            except Exception:
                pass
            save_jpeg(img, web_dest, args.web_px, args.quality)
            save_jpeg(img, thumb_dest, args.thumb_px, args.quality)
            manifest[(species, project, filename)] = {
                "species": species, "project": project, "filename": filename,
                "web_jpg": web_name, "thumb_jpg": thumb_name}
            done += 1
            if done % 20 == 0:
                print(f"  ...{done} converted")
        except Exception as e:
            failed += 1
            print(f"  FAIL {species}/{project}/{filename}: {e}")

    with open(manifest_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["species", "project", "filename", "web_jpg", "thumb_jpg"])
        w.writeheader()
        for row in manifest.values():
            w.writerow(row)

    print(f"\nConverted {done}, already-present {skipped}, failed {failed}.")
    print(f"Derivatives tree: {outdir}")
    print(f"Manifest:         {manifest_path}")
    print("Next: upload each <species>/<project>/derivatives/ folder to the matching owl project,")
    print("      then re-run:  python3 build_index.py")


if __name__ == "__main__":
    main()
