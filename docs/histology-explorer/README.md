# Histology Databank Explorer

A static web resource for browsing the Roberts Lab histology databank — search and
filter samples by species, project, year, tissue, and researcher, and view the slide
images stored on owl.

Built to run on **GitHub Pages** (or any static host). No server or database required.

## What's here

```
histology-explorer/
├── index.html              # the explorer (open this)
├── data/
│   ├── samples.json        # unique samples + attached images (the app reads this)
│   ├── orphans.json        # images on owl with no databank sample ("Unmatched images" tab)
│   ├── images.json         # flat index of every image file found on owl
│   ├── qc_report.md         # human-readable coverage / orphan report
│   └── qc_report.json       # machine-readable QC counts
└── build/
    ├── histology_databank.csv          # export of the Google Sheet
    ├── build_index.py                   # regenerates everything in data/
    ├── make_derivatives.py              # makes browser JPEGs from archival .tif files
    ├── derivatives_manifest.csv         # (generated) maps each .tif to its JPEGs
    └── listings/SPECIES__PROJECT.txt    # captured owl directory listings
```

## Two views

- **Samples** — the databank, deduped by `unique-sample-id`, with linked images.
- **Unmatched images** — specimens that have slide images on owl but **aren't in the sheet yet**
  (e.g. `O_angasi` 45–146, `O_lurida` 241–386, the Larken clam set). A ready-made backfill worklist.

## How it works

- **Samples** come from the databank sheet, deduped by `unique-sample-id`.
- **Images** come from `owl.fish.washington.edu/hesperornis/<species>/<project>/`.
- Each image filename is parsed into `timestamp · sample-label · magnification · variant · ext`.
- Samples are linked to images via the sheet's `Image_ID` (a base filename or a project-folder URL)
  and by matching sample labels (`angasi 50` ↔ `angasi050`, `oly-82` ↔ `slide_82`, etc.).

### The `.tif` note

Many images (all of `O_angasi`, the 2026 geoduck gonad set) are archival **`.tif`** files,
which browsers cannot display. The explorer shows browser-viewable `.jpg`/`.png` inline and
offers `.tif` as a download link. A sample with only `.tif` images shows a "TIF only" card.
To give those real thumbnails, generate `.jpg` derivatives (see next section).

## Generating JPEG derivatives for `.tif` images

`build/make_derivatives.py` turns each archival `.tif` into a downsized web JPEG (≤1600 px) and a
thumbnail (≤400 px). It reads the same `listings/` files, so it always knows which tifs exist.

```bash
cd build
pip install Pillow            # one-time (large tifs may also need: pip install imagecodecs)

# Option A — stream the tifs straight from owl (needs network):
python3 make_derivatives.py --from-owl --species O_angasi --outdir ../_derivatives

# Option B — convert tifs you've already downloaded:
python3 make_derivatives.py --tif-dir ~/owl_tifs --outdir ../_derivatives

# Tip: add --limit 10 for a quick test run first.
```

This writes `../_derivatives/<species>/<project>/derivatives/<stem>-web.jpg` (+ `-thumb.jpg`) and
updates `build/derivatives_manifest.csv`. Then:

1. Upload each `_derivatives/<species>/<project>/derivatives/` folder into the matching owl
   project directory (so files live at `…/<project>/derivatives/<stem>-web.jpg`).
2. Re-run `python3 build_index.py`. The manifest is folded in automatically, and the `.tif`
   samples switch from "TIF only" placeholders to real thumbnails (the originals stay
   downloadable).

## Current coverage (from the last build)

- 1,308 sheet rows → **940 unique samples**
- **100 samples** have at least one image; **56** have a browser-viewable image
- **918 image files** indexed; ~651 are "orphans" — imaged on owl but **not yet entered in the sheet**
  (e.g. `O_angasi` 45–146, `O_lurida` 241–386, the Larken clam set). See `data/qc_report.md`.

## Viewing locally

`fetch()` needs http, so don't open `index.html` as a `file://`. From this folder:

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

## Publishing to GitHub Pages

1. Put this `histology-explorer/` folder in a RobertsLab repo (or its own repo).
2. Repo **Settings → Pages → Build from branch**, pick the branch and the folder.
3. The site is live at the Pages URL. Images load directly from owl (public).

## Refreshing the data

When the sheet changes, or new images are added to owl:

1. **Re-export the sheet** to `build/histology_databank.csv` (File → Download → CSV).
2. **Re-capture owl listings** if images were added: for each
   `owl.fish.washington.edu/hesperornis/<species>/<project>/`, save the list of filenames
   (one per line) to `build/listings/<species>__<project>.txt`
   (use an empty project, i.e. `<species>__.txt`, for files at the species root).
3. **Rebuild:**
   ```bash
   cd build
   python3 build_index.py
   ```
   This rewrites everything in `data/` and prints fresh QC counts.
4. Commit and push — Pages redeploys automatically.
