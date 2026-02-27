#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

# Build MkDocs site into a temp dir (avoid cleanup when switching branches)
SITE_DIR="$(mktemp -d)"
mkdocs build --clean -d "$SITE_DIR"

CURRENT_BRANCH="$(git rev-parse --abbrev-ref HEAD)"

# Ensure gh-pages branch exists locally
if git show-ref --verify --quiet refs/heads/gh-pages; then
  git checkout gh-pages
else
  git checkout -b gh-pages
fi

# Remove everything in gh-pages branch root
git rm -r --ignore-unmatch .

# Copy built site to branch root
cp -R "$SITE_DIR"/. .

rm -rf "$SITE_DIR"

# Ensure GitHub Pages does not run Jekyll
touch .nojekyll

git add .
git commit -m "Publish site" || echo "No changes to commit."
git push -u origin gh-pages

# Return to the original branch
git checkout "$CURRENT_BRANCH"

echo "Published to gh-pages. Configure GitHub Pages to serve gh-pages /(root)."
