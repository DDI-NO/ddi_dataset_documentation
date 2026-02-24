# DDI Dataset Documentation Builder

This repository builds the GitHub Pages dataset documentation site for DDI from XNAT display-field sidecar metadata.
It separates hand-authored content from generated pages and produces a MkDocs site.

## Quick Start

1) Create a Python 3.11+ environment and install dependencies.

```
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

2) Point the parser config at the plugin sidecar roots.

Edit [config/parser.yaml](config/parser.yaml) and ensure `sidecar_roots` and
any `sidecar_path` entries reference the local XNAT plugin repository.

3) Build documentation.

```
ddi_dataset_documentation build
mkdocs build
```

Generated markdown is written to [generated](generated) and a unified MkDocs
docs directory is assembled in [docs](docs).

## CLI

- `ddi_dataset_documentation build` generates pages and assembles `docs/`.
- `ddi_dataset_documentation validate` validates config, sidecars, and registry.
- `ddi_dataset_documentation serve` runs `mkdocs serve`.

## Content vs Generated Pages

- Hand-edited content lives under [content](content).
- Generated pages are written under [generated](generated).
- The build step assembles [docs](docs) from both sources.

Experiment scope pages must include the marker:

```
<!-- AUTO:VARIABLES -->
```

## Sidecar Inputs

Sidecar metadata is read from the external plugin repository using relative
paths configured in [config/parser.yaml](config/parser.yaml). Example:

```
sidecar_roots:
	- "../xnat-apgem-plugin/src/main/resources/schemas"
```

## Computed Variables

Computed variables are configured in [config/computed.yaml](config/computed.yaml).
These are merged into the flat dataset catalogue.

## GitHub Pages Deployment (Option A)

This repo expects local generation of the static site. A typical flow is:

1) Build the site locally:

```
ddi_dataset_documentation build
mkdocs build
```

2) Publish the contents of `site/` to the `gh-pages` branch root.
	 A common approach is to use a git worktree:

```
git worktree add /tmp/gh-pages gh-pages
rsync -av site/ /tmp/gh-pages/
cd /tmp/gh-pages && git add . && git commit -m "Publish site" && git push
```

The workflow in [.github/workflows/gh-pages.yml](.github/workflows/gh-pages.yml)
deploys the contents of the `gh-pages` branch to GitHub Pages. It does not
require access to the external XNAT plugin repository.

## Vendoring Strategy for CI Builds

If you want CI to build the site, mirror sidecar files into this repository
and update [config/parser.yaml](config/parser.yaml) to point at the local copies.
This avoids any dependency on external repositories during builds.
