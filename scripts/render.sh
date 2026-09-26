#!/usr/bin/env bash
# Render a PPTX to PDF (output/pdf) and per-slide PNGs (output/renders/<deck>/).
# Usage: bash scripts/render.sh output/pptx/<deck>.pptx
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/install_fonts.py
PPTX="$1"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
NAME="$(basename "${PPTX%.*}")"
mkdir -p "$ROOT/output/pdf" "$ROOT/output/renders/$NAME"
soffice --headless --convert-to pdf --outdir "$ROOT/output/pdf" "$PPTX" >/dev/null 2>&1
test -s "$ROOT/output/pdf/$NAME.pdf"
python3 scripts/qa_pdf.py "$ROOT/output/pdf/$NAME.pdf" "${@:2}"
rm -f "$ROOT/output/renders/$NAME"/*.png
pdftoppm -png -r 80 "$ROOT/output/pdf/$NAME.pdf" "$ROOT/output/renders/$NAME/slide"
echo "PDF:     output/pdf/$NAME.pdf"
echo "Renders: output/renders/$NAME/ ($(ls "$ROOT/output/renders/$NAME" | wc -l) slides)"
echo "Now open and inspect EVERY PNG before delivery."
