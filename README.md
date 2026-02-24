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

## GitHub Pages

This repo uses the GitHub Pages "Deploy from a branch" option with `gh-pages`.

### Configure GitHub Pages

In GitHub: Settings -> Pages -> Deploy from a branch -> `gh-pages` + `/(root)`.

### Publish locally

Build and publish the static site by running:

```
bash scripts/publish_gh_pages.sh
```

This script runs `mkdocs build --clean`, publishes the contents of `site/` to the
root of the `gh-pages` branch, creates `.nojekyll`, and then returns you to your
original branch.

### Notes

- The static site output is in `site/` and is not committed on `main`.
- Built artifacts are committed to `gh-pages` only.
