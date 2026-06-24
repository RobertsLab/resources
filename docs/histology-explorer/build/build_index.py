#!/usr/bin/env python3
"""
Build the Histology Explorer data files.

Inputs (in this build/ folder):
  - histology_databank.csv          : export of the Google Sheet
  - listings/SPECIES__PROJECT.txt   : one file per owl directory, one image filename per line
                                      (filename encodes the owl path: SPECIES/PROJECT/<name>)
                                      Larken_clam__.txt has an empty PROJECT => images live at SPECIES/ root.

Outputs (written to ../data/):
  - images.json      : flat list of every image file found on owl, parsed
  - samples.json     : unique databank samples (deduped by unique-sample-id) with attached images
  - qc_report.json   : machine-readable QC counts
  - qc_report.md     : human-readable QC summary

No network access is used: the owl listings were captured into listings/*.txt.
Re-run after re-exporting the Sheet and/or re-capturing the listings.
"""
import csv, json, re, os, glob
from collections import defaultdict, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, "..", "data"))
os.makedirs(DATA, exist_ok=True)

OWL_BASE = "https://owl.fish.washington.edu/hesperornis"
WEB_EXT = {"jpg", "jpeg", "png", "gif"}     # browser-displayable
ARCHIVE_EXT = {"tif", "tiff"}               # archival, not browser-displayable

MAG_RE = re.compile(r"^(\d+)[xX](.*)$")
DATE8_RE = re.compile(r"^(\d{8})[-_](.*)$")

# species_scientific (and common) -> owl folder name
SPECIES_FOLDER = {
    "o_angasi": "O_angasi", "australian flat oyster": "O_angasi",
    "o_lurida": "O_lurida", "olympia oyster": "O_lurida",
    "p_generosa": "P_generosa", "geoduck": "P_generosa",
    "pacific geoduck": "P_generosa", "pacific_geoduck": "P_generosa",
    "c_gigas": "C_gigas", "c. gigas": "C_gigas",
    "pacific oyster": "C_gigas", "pacific_oyster": "C_gigas",
}
# Friendly species display names keyed by owl folder
SPECIES_DISPLAY = {
    "O_angasi": "Ostrea angasi (Australian flat oyster)",
    "O_lurida": "Ostrea lurida (Olympia oyster)",
    "P_generosa": "Panopea generosa (Pacific geoduck)",
    "C_gigas": "Crassostrea gigas (Pacific oyster)",
    "Larken_clam": "Larken clam",
}


def species_folder(sci, common):
    for v in (sci, common):
        if v and v.strip().lower() in SPECIES_FOLDER:
            return SPECIES_FOLDER[v.strip().lower()]
    return ""


def parse_filename(fname):
    """Return dict with stem, ext, timestamp, label, magnification, variant."""
    ext = fname.rsplit(".", 1)[1].lower() if "." in fname else ""
    stem = fname.rsplit(".", 1)[0] if "." in fname else fname
    m = DATE8_RE.match(stem)
    if m:
        timestamp, rest = m.group(1), m.group(2)
    else:
        timestamp, rest = "", stem
    tokens = re.split(r"[-_]", rest)
    mag, variant_tokens, label_tokens = "", [], []
    mag_idx = None
    for i, t in enumerate(tokens):
        mm = MAG_RE.match(t)
        if mm and mag_idx is None:
            mag = mm.group(1) + "x"
            if mm.group(2):
                variant_tokens.append(mm.group(2))
            mag_idx = i
    if mag_idx is None:
        label = rest
    else:
        label = "-".join(tokens[:mag_idx])
        variant_tokens = variant_tokens + tokens[mag_idx + 1:]
    variant = "-".join([v for v in variant_tokens if v])
    return {"ext": ext, "stem": stem, "timestamp": timestamp,
            "label": label, "magnification": mag, "variant": variant}


def norm_label(label):
    """Normalize a label for joining across the sheet <-> filenames."""
    if not label:
        return ""
    l = label.strip().lower().replace(" ", "").replace(".", "")
    m = re.match(r"^angasi[-_]?0*(\d+)$", l)
    if m:
        return "angasi" + str(int(m.group(1)))
    m = re.match(r"^oly[-_]?0*(\d+)$", l)
    if m:
        return "oly" + str(int(m.group(1)))
    m = re.match(r"^slide[-_]?0*(\d+)$", l)
    if m:
        return "slide" + str(int(m.group(1)))
    if re.match(r"^\d+$", l):
        return str(int(l))
    # collapse remaining separators (e.g. "4-m-in" -> "4min")
    return re.sub(r"[-_]", "", l)


def numeric_of(label):
    m = re.search(r"(\d+)", label or "")
    return str(int(m.group(1))) if m else ""


# ---------------------------------------------------------------------------
# 1. Parse owl listings into image records, grouped by (species_folder, label)
# ---------------------------------------------------------------------------
images = []
# group key -> list of image indices
group_by_species_label = defaultdict(list)        # (species, norm_label) -> [idx]
group_by_proj_numeric = defaultdict(list)         # (species, project, numeric) -> [idx]
group_by_proj_normlabel = defaultdict(list)       # (species, project, norm_label) -> [idx]

for path in sorted(glob.glob(os.path.join(HERE, "listings", "*.txt"))):
    base = os.path.basename(path)[:-4]            # strip .txt
    species, project = base.split("__", 1)
    url_dir = OWL_BASE + "/" + species + ("/" + project if project else "") + "/"
    with open(path) as fh:
        for line in fh:
            fname = line.strip()
            if not fname:
                continue
            p = parse_filename(fname)
            rec = {
                "species_folder": species,
                "project": project,
                "filename": fname,
                "url": url_dir + fname.replace(" ", "%20"),
                "timestamp": p["timestamp"],
                "label": p["label"],
                "magnification": p["magnification"],
                "variant": p["variant"],
                "ext": p["ext"],
                "web_viewable": p["ext"] in WEB_EXT,
                "derivative_url": "",      # web jpg generated from a .tif (if any)
                "thumb_url_self": "",      # small thumb jpg (if any)
            }
            idx = len(images)
            images.append(rec)
            nl = norm_label(p["label"])
            group_by_species_label[(species, nl)].append(idx)
            group_by_proj_normlabel[(species, project, nl)].append(idx)
            num = numeric_of(p["label"])
            if num:
                group_by_proj_numeric[(species, project, num)].append(idx)

# ---------------------------------------------------------------------------
# 1b. Optional: fold in TIF->JPG derivatives produced by make_derivatives.py
#     build/derivatives_manifest.csv columns: species,project,filename,web_jpg,thumb_jpg
#     web_jpg / thumb_jpg are filenames living in <species>/<project>/derivatives/ on owl.
# ---------------------------------------------------------------------------
by_key = {}
for idx, im in enumerate(images):
    by_key[(im["species_folder"], im["project"], im["filename"])] = idx

man_path = os.path.join(HERE, "derivatives_manifest.csv")
n_deriv = 0
if os.path.exists(man_path):
    for m in csv.DictReader(open(man_path)):
        key = (m.get("species", "").strip(), m.get("project", "").strip(), m.get("filename", "").strip())
        idx = by_key.get(key)
        if idx is None:
            continue
        sp, proj = key[0], key[1]
        dir_url = OWL_BASE + "/" + sp + ("/" + proj if proj else "") + "/derivatives/"
        if m.get("web_jpg", "").strip():
            images[idx]["derivative_url"] = dir_url + m["web_jpg"].strip().replace(" ", "%20")
        if m.get("thumb_jpg", "").strip():
            images[idx]["thumb_url_self"] = dir_url + m["thumb_jpg"].strip().replace(" ", "%20")
        n_deriv += 1


def im_is_viewable(im):
    return im["web_viewable"] or bool(im["derivative_url"])


def im_display_url(im):
    return im["derivative_url"] or im["url"]


def im_thumb_url(im):
    if im["thumb_url_self"]:
        return im["thumb_url_self"]
    if im["derivative_url"]:
        return im["derivative_url"]
    if im["web_viewable"]:
        return im["url"]
    return ""


# ---------------------------------------------------------------------------
# 2. Read databank, dedupe by unique-sample-id, attach images
# ---------------------------------------------------------------------------
rows = list(csv.DictReader(open(os.path.join(HERE, "histology_databank.csv"))))

samples = OrderedDict()   # usid -> merged sample dict
for r in rows:
    usid = (r.get("unique-sample-id") or "").strip()
    if not usid:
        continue
    sci = (r.get("species_scientific") or "").strip()
    common = (r.get("species_common") or "").strip()
    folder = species_folder(sci, common)
    if usid not in samples:
        samples[usid] = {
            "unique_sample_id": usid,
            "species_scientific": sci,
            "species_common": common,
            "species_folder": folder,
            "date": (r.get("date") or "").strip(),
            "tissues": set(),
            "block_labels": set(),
            "slide_labels": set(),
            "image_ids": set(),
            "cabinet": (r.get("cabinet") or "").strip(),
            "drawer": (r.get("drawer") or "").strip(),
            "row": (r.get("row") or "").strip(),
            "slide_case": (r.get("slide_case") or "").strip(),
            "slide_slot": (r.get("slide_slot") or "").strip(),
            "name": (r.get("name") or "").strip(),
            "project_name": (r.get("project") or "").strip(),
            "project_link": (r.get("Link to project") or "").strip(),
            "notes": (r.get("notes") or "").strip(),
        }
    s = samples[usid]
    if not s["species_folder"] and folder:
        s["species_folder"] = folder
    for col, key in [("tissue(s)", "tissues"), ("block_label", "block_labels"),
                     ("slide_label", "slide_labels"), ("Image_ID", "image_ids")]:
        v = (r.get(col) or "").strip()
        if v and v.upper() != "NA":
            s[key].add(v)


def project_from_url(url):
    m = re.search(r"/hesperornis/([^/]+)/([^/]+)/?", url)
    if m:
        return m.group(1), m.group(2)
    return "", ""


matched_idx = set()
for usid, s in samples.items():
    folder = s["species_folder"]
    attached = []

    # (a) authoritative: Image_ID that is a base image filename
    for iid in s["image_ids"]:
        if iid.startswith("http"):
            continue
        p = parse_filename(iid + ".x")   # add dummy ext so parser strips nothing important
        nl = norm_label(p["label"])
        for idx in group_by_species_label.get((folder, nl), []):
            attached.append(idx)

    # (b) Image_ID that is a folder URL -> match within that project
    for iid in s["image_ids"]:
        if not iid.startswith("http"):
            continue
        sp, proj = project_from_url(iid)
        if not sp:
            continue
        cand_norm, cand_num = set(), set()
        for lab in list(s["slide_labels"]) + list(s["block_labels"]) + [usid.split("_")[1] if len(usid.split("_")) > 1 else ""]:
            cand_norm.add(norm_label(lab))
            if numeric_of(lab):
                cand_num.add(numeric_of(lab))
        for nl in cand_norm:
            for idx in group_by_proj_normlabel.get((sp, proj, nl), []):
                attached.append(idx)
        for num in cand_num:
            for idx in group_by_proj_numeric.get((sp, proj, num), []):
                attached.append(idx)

    # (c) no Image_ID: try label match within the species folder
    if not attached and folder:
        cand = set()
        for lab in list(s["slide_labels"]) + list(s["block_labels"]):
            cand.add(norm_label(lab))
        parts = usid.split("_")
        if len(parts) > 1:
            cand.add(norm_label(parts[1]))
        for nl in cand:
            if nl:
                for idx in group_by_species_label.get((folder, nl), []):
                    attached.append(idx)

    attached = sorted(set(attached))
    matched_idx.update(attached)
    imgs = [images[i] for i in attached]
    web = [im for im in imgs if im_is_viewable(im)]
    s["images"] = imgs
    s["image_count"] = len(imgs)
    s["web_image_count"] = len(web)
    s["has_image"] = len(imgs) > 0
    s["has_web_image"] = len(web) > 0
    # thumbnail: prefer a viewable image (jpg or derivative), lowest magnification first
    def mag_key(im):
        m = re.match(r"(\d+)x", im["magnification"] or "")
        return int(m.group(1)) if m else 9999
    s["thumb_url"] = im_thumb_url(sorted(web, key=mag_key)[0]) if web else ""

# finalize: sets -> sorted lists
for s in samples.values():
    for k in ("tissues", "block_labels", "slide_labels", "image_ids"):
        s[k] = sorted(s[k])
    s["species_display"] = SPECIES_DISPLAY.get(s["species_folder"], s["species_common"] or s["species_scientific"] or "Unknown")
    # year from date or usid
    yr = ""
    m = re.match(r"^(\d{4})", s["unique_sample_id"])
    if m:
        yr = m.group(1)
    s["year"] = yr

sample_list = list(samples.values())

# ---------------------------------------------------------------------------
# 3. QC report
# ---------------------------------------------------------------------------
orphans = [images[i] for i in range(len(images)) if i not in matched_idx]
orphan_groups = sorted(set((images[i]["species_folder"], images[i]["project"], images[i]["label"])
                           for i in range(len(images)) if i not in matched_idx))

by_species_samples = defaultdict(lambda: [0, 0])  # folder -> [total, with_image]
for s in sample_list:
    key = s["species_folder"] or "(unmapped)"
    by_species_samples[key][0] += 1
    if s["has_image"]:
        by_species_samples[key][1] += 1

qc = {
    "total_rows_in_sheet": len(rows),
    "unique_samples": len(sample_list),
    "samples_with_any_image": sum(1 for s in sample_list if s["has_image"]),
    "samples_with_web_image": sum(1 for s in sample_list if s["has_web_image"]),
    "total_images_indexed": len(images),
    "images_matched_to_a_sample": len(matched_idx),
    "orphan_images": len(orphans),
    "orphan_image_groups": len(orphan_groups),
    "samples_by_species": {k: {"total": v[0], "with_image": v[1]} for k, v in sorted(by_species_samples.items())},
    "images_by_species": {},
}
img_by_sp = defaultdict(int)
for im in images:
    img_by_sp[im["species_folder"]] += 1
qc["images_by_species"] = dict(sorted(img_by_sp.items()))

# ---------------------------------------------------------------------------
# 3b. Per-image display fields (derivative-aware) + orphan grouping
# ---------------------------------------------------------------------------
for im in images:
    im["viewable"] = im_is_viewable(im)
    im["display_url"] = im_display_url(im)
    im["thumb"] = im_thumb_url(im)

# Group orphan images (no matching sample) by (species, project, label) so the
# explorer can show "imaged but not yet in the databank" specimens.
orphan_map = OrderedDict()
for i in range(len(images)):
    if i in matched_idx:
        continue
    im = images[i]
    key = (im["species_folder"], im["project"], im["label"])
    if key not in orphan_map:
        orphan_map[key] = {
            "species_folder": im["species_folder"],
            "species_display": SPECIES_DISPLAY.get(im["species_folder"], im["species_folder"] or "Unknown"),
            "project": im["project"],
            "label": im["label"],
            "group_id": "|".join(key),
            "timestamp": im["timestamp"],
            "folder_url": OWL_BASE + "/" + im["species_folder"] + ("/" + im["project"] if im["project"] else "") + "/",
            "images": [],
        }
    orphan_map[key]["images"].append(im)


def mag_key(im):
    m = re.match(r"(\d+)x", im["magnification"] or "")
    return int(m.group(1)) if m else 9999


orphan_groups_data = list(orphan_map.values())
for g in orphan_groups_data:
    g["images"].sort(key=lambda im: (mag_key(im), im["filename"]))
    g["image_count"] = len(g["images"])
    viewable = [im for im in g["images"] if im["viewable"]]
    g["has_web_image"] = bool(viewable)
    g["thumb_url"] = (sorted(viewable, key=mag_key)[0]["thumb"] if viewable else "")
orphan_groups_data.sort(key=lambda g: (g["species_folder"], g["project"], norm_label(g["label"])))

# ---------------------------------------------------------------------------
# 4. Write outputs
# ---------------------------------------------------------------------------
with open(os.path.join(DATA, "images.json"), "w") as f:
    json.dump(images, f, indent=1)
with open(os.path.join(DATA, "orphans.json"), "w") as f:
    json.dump(orphan_groups_data, f, indent=1)
with open(os.path.join(DATA, "samples.json"), "w") as f:
    json.dump(sample_list, f, indent=1)
with open(os.path.join(DATA, "qc_report.json"), "w") as f:
    json.dump(qc, f, indent=2)

md = []
md.append("# Histology Databank — Build QC Report\n")
md.append(f"- Rows in sheet export: **{qc['total_rows_in_sheet']}**")
md.append(f"- Unique samples (deduped by unique-sample-id): **{qc['unique_samples']}**")
md.append(f"- Samples with at least one image: **{qc['samples_with_any_image']}**")
md.append(f"- Samples with a browser-viewable (jpg/png) image: **{qc['samples_with_web_image']}**")
md.append(f"- Total image files indexed on owl: **{qc['total_images_indexed']}**")
md.append(f"- Images matched to a sample: **{qc['images_matched_to_a_sample']}**")
md.append(f"- Orphan images (no matching sample): **{qc['orphan_images']}** in {qc['orphan_image_groups']} sample-groups\n")
md.append("## Samples by species\n")
md.append("| Species folder | Samples | With image |")
md.append("|---|---:|---:|")
for k, v in qc["samples_by_species"].items():
    md.append(f"| {k} | {v['total']} | {v['with_image']} |")
md.append("\n## Images by species folder\n")
md.append("| Species folder | Image files |")
md.append("|---|---:|")
for k, v in qc["images_by_species"].items():
    md.append(f"| {k or '(none)'} | {v} |")
md.append("\n## Orphan image groups (images present on owl with no matching databank sample)\n")
for sp, proj, lab in orphan_groups[:200]:
    md.append(f"- `{sp}/{proj}` label `{lab}`")
if len(orphan_groups) > 200:
    md.append(f"- ...and {len(orphan_groups)-200} more")
with open(os.path.join(DATA, "qc_report.md"), "w") as f:
    f.write("\n".join(md) + "\n")

print(json.dumps(qc, indent=2))
