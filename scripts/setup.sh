#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
npm ci
if [ "$(id -u)" -eq 0 ]; then SUDO=(); else SUDO=(sudo); fi
"${SUDO[@]}" apt-get update
"${SUDO[@]}" env DEBIAN_FRONTEND=noninteractive apt-get install -y libreoffice poppler-utils fontconfig
python3 -m pip install -r scripts/requirements.txt
python3 scripts/install_fonts.py
