#!/usr/bin/env bash
# Optional: make the English stock-* commands available in every Claude Code session,
# not only when working inside this repo.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="${CLAUDE_COMMANDS_DIR:-$HOME/.claude/commands}"

mkdir -p "$DEST"
cp "$ROOT"/.claude/commands/stock-*.md "$DEST"/
chmod +x "$ROOT"/tools/*.py

echo "Installed stock-* commands to $DEST"
echo "They assume this repo is at $ROOT — run them from there so the tools resolve."
