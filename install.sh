#!/usr/bin/env bash
# Install the DataForSEO skill into ~/.claude/skills/

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SOURCE_DIR="$SCRIPT_DIR/dataforseo"
DEST_DIR="$HOME/.claude/skills/dataforseo"

if [ ! -d "$SOURCE_DIR" ]; then
  echo "Error: $SOURCE_DIR not found. Run this script from the repo root." >&2
  exit 1
fi

mkdir -p "$HOME/.claude/skills"

if [ -d "$DEST_DIR" ]; then
  rm -rf "$DEST_DIR"
fi

rsync -a --exclude='__pycache__' "$SOURCE_DIR/" "$DEST_DIR/"

echo "Installed dataforseo skill to $DEST_DIR"
