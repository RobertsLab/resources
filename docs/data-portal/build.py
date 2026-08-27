#!/usr/bin/env python3
"""Build the Roberts Lab Data Portal data files.

Produces two JSON files consumed by index.html:
  - nightingales.json : one record per raw sequencing library
  - genomes.json      : one record per species of curated reference assets

Sources:
  - nightingales.csv          (export of the Nightingales Google Sheet)
  - ../docs/Genomic-Resources.md

Re-fetch the Nightingales export with:
  curl -sL "https://docs.google.com/spreadsheets/d/1_XqIOPVHSBVGscnjzDSWUeRL7HUHXfaHxVzec-I-8Xk/export?format=csv" -o nightingales.csv
"""
import csv
import json
import re
from pathlib import Path

HERE = Path(__file__).parent
CSV = HERE / "nightingales.csv"
GENOMES_MD = HERE.parent / "Genomic-Resources.md"

# --- Nightingales -----------------------------------------------------------
# Keep the fields useful for discovery; drop the verbose internal file paths
# (Read1FileLocation etc. point at the lab NAS volume and aren't public).
FIELDS = [
    "SeqID", "Library_ID", "Library_name", "Primary_taxa", "Tissue",
    "Molecule", "Platform", "Sequencer", "Length", "BriefDesc", "Experiment",
    "SeqSubmissionDate", "SeqReceiptDate", "SRA_ID", "SRA_Release_Date",
    "Read1URL", "Read2URL", "Read1FastQC",
]


def build_nightingales():
    rows = []
    with open(CSV, newline="") as fh:
        for r in csv.DictReader(fh):
            rec = {k: (r.get(k, "") or "").strip() for k in FIELDS}
            rec["year"] = (rec.get("SeqReceiptDate") or rec.get("SeqSubmissionDate") or "")[:4]
            rec["has_sra"] = bool(rec.get("SRA_ID"))
            # NCBI link for the accession when present
            sra = rec.get("SRA_ID")
            rec["sra_url"] = (
                f"https://www.ncbi.nlm.nih.gov/sra/?term={sra}" if sra else ""
            )
            rows.append(rec)
    return rows


# --- Genomic Resources ------------------------------------------------------
LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
# Remove markdown emphasis (* always; _ only at word boundaries) while keeping
# underscores inside identifiers like cgigas_uk_roslin_v1 or cbai_genome.fasta.
EMPH_RE = re.compile(r"[*`]|(?<!\w)_|_(?!\w)")


def demph(text):
    return EMPH_RE.sub("", text).strip()


MD5_RE = re.compile(r"MD5\s*=\s*`?([0-9a-fA-F]{32})`?")
DATA_EXT = (
    ".fa", ".fasta", ".fna", ".fa.fai", ".fasta.fai", ".gff", ".gff3",
    ".gtf", ".bed", ".gz", ".tar.gz", ".vcf", ".txt", ".outfmt6",
)


def classify(url):
    u = url.lower().split("?")[0]
    if u.endswith((".fai",)):
        return "index"
    if u.endswith((".gff", ".gff3", ".gtf", ".bed")):
        return "annotation"
    if u.endswith((".fa", ".fasta", ".fna")) or "genome" in u:
        return "genome/transcriptome"
    if u.endswith((".tar.gz", ".gz", ".zip")):
        return "archive"
    if "docs.google.com" in u:
        return "sheet"
    if "github.com" in u:
        return "repo"
    return "other"


def build_genomes():
    species = []
    cur = None
    last_link = None
    for raw in GENOMES_MD.read_text().splitlines():
        line = raw.rstrip()
        if line.startswith("## "):
            name = demph(line[3:])
            cur = {"species": name, "assets": []}
            species.append(cur)
            last_link = None
            continue
        if cur is None:
            continue
        for text, url in LINK_RE.findall(line):
            asset = {
                "label": demph(text),
                "url": url,
                "kind": classify(url),
                "md5": "",
            }
            cur["assets"].append(asset)
            last_link = asset
        m = MD5_RE.search(line)
        if m and last_link is not None:
            last_link["md5"] = m.group(1).lower()
    # drop sections with no assets (stray headings)
    species = [s for s in species if s["assets"]]
    for s in species:
        s["n_assets"] = len(s["assets"])
        s["kinds"] = sorted({a["kind"] for a in s["assets"]})
    return species


def main():
    nightingales = build_nightingales()
    genomes = build_genomes()
    (HERE / "nightingales.json").write_text(json.dumps(nightingales, indent=0))
    (HERE / "genomes.json").write_text(json.dumps(genomes, indent=0))
    print(f"nightingales.json : {len(nightingales)} libraries")
    print(f"genomes.json      : {len(genomes)} species, "
          f"{sum(s['n_assets'] for s in genomes)} assets")


if __name__ == "__main__":
    main()
