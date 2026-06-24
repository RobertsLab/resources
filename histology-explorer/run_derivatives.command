#!/bin/bash
# Double-click this file (Finder) to generate browser JPEGs from the archival .tif images.
# It runs entirely on your Mac: convert from owl -> rebuild -> (optional) upload back to owl.
set -e
cd "$(dirname "$0")/build"

echo "=============================================="
echo " Histology derivatives: .tif  ->  web JPEGs"
echo "=============================================="

# 1. dependencies
echo "[1/4] Checking Python image libraries (Pillow, imagecodecs)…"
python3 -m pip install --quiet --user Pillow imagecodecs || python3 -m pip install --quiet Pillow imagecodecs

# 2. choose scope
read -r -p "[2/4] Species folder to convert [O_angasi] (blank = all tif folders): " SP
SP="${SP:-O_angasi}"
SPARG=""; [ -n "$SP" ] && SPARG="--species $SP"

read -r -p "      Test run first? Convert only N files (blank = convert ALL): " LIM
LIMARG=""; [ -n "$LIM" ] && LIMARG="--limit $LIM"

# 3. convert (streamed from owl) + rebuild
echo "[3/4] Converting from owl … (large sets stream several GB; this can take a while)"
python3 make_derivatives.py --from-owl $SPARG $LIMARG --outdir ../_derivatives

echo "      Rebuilding explorer data…"
python3 build_index.py >/dev/null
echo "      Done. Local JPEGs are in:  $(cd ..; pwd)/_derivatives"

# 4. optional upload back to owl
echo "[4/4] Upload JPEGs to owl so the website can use them."
echo "      They must land in a 'derivatives/' folder inside each owl project directory."
read -r -p "      Paste an rsync/scp destination base (e.g. user@owl…:/…/hesperornis) or leave blank to skip: " DEST
if [ -n "$DEST" ]; then
  echo "      Uploading…"
  ( cd ../_derivatives && \
    find . -type d -name derivatives | while read -r d; do
      rel="${d#./}"
      echo "        $rel"
      rsync -av "$d/" "$DEST/${rel}/"
    done )
  echo "      Upload complete. Re-run build once more to be safe:"
  python3 build_index.py >/dev/null
  echo "      Refresh your browser — the .tif samples now show thumbnails."
else
  echo "      Skipped upload. When ready, copy each _derivatives/<species>/<project>/derivatives/"
  echo "      folder into the matching owl project directory, then run: python3 build_index.py"
fi

echo "Finished. Press any key to close."
read -r -n 1 -s
