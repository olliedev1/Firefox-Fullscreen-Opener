#!/usr/bin/env bash
# open_fullscreen.sh — convenience wrapper around firefox_fullscreen_opener.py
#
# Usage:
#   ./open_fullscreen.sh <url> [--no-kiosk]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

exec python3 "${SCRIPT_DIR}/firefox_fullscreen_opener.py" "$@"
