from __future__ import annotations

import os
import subprocess
from pathlib import Path

import typer

from dataset_docs.builders.build_registry import build_registry, resolve_sidecar_paths
from dataset_docs.builders.copy_content import assemble_docs
from dataset_docs.builders.render_pages import (
    render_dataset_catalog,
    render_experiment_pages,
    render_experiments_index,
)
from dataset_docs.loaders.discover_sidecars import discover_sidecars
from dataset_docs.loaders.load_config import load_computed_variables, load_parser_config
from dataset_docs.loaders.load_sidecars import load_sidecars_by_experiment
from dataset_docs.validators.validate_registry import validate_registry
from dataset_docs.utils.paths import resolve_from_root

app = typer.Typer(add_completion=False)


def _resolve_sidecar_roots(config_roots: list[str]) -> list[Path]:
    env_value = os.environ.get("DDI_SIDECAR_ROOTS", "").strip()
    if env_value:
        roots = [path.strip() for path in env_value.split(os.pathsep) if path.strip()]
    else:
        roots = config_roots
    return [resolve_from_root(path) for path in roots]


@app.command()
def build(config: str = "config/parser.yaml") -> None:
    """Build generated documentation pages and assemble docs/ for MkDocs."""
    parser_config = load_parser_config(config)
    sidecar_roots = _resolve_sidecar_roots(parser_config.sidecar_roots)
    discoveries = {d.experiment_id: d.path for d in discover_sidecars(sidecar_roots)}
    sidecar_paths = resolve_sidecar_paths(parser_config, discoveries)
    sidecars = load_sidecars_by_experiment(sidecar_paths)
    computed_config = load_computed_variables(parser_config.flat_dataset.computed_variables_spec)

    registry = build_registry(parser_config, sidecars, computed_config)
    validate_registry(registry)

    templates_dir = resolve_from_root("templates")
    generated_dir = resolve_from_root("generated")
    render_experiment_pages(registry, templates_dir, generated_dir)
    render_dataset_catalog(registry, templates_dir, generated_dir)
    render_experiments_index(registry, templates_dir, generated_dir)

    content_dir = resolve_from_root("content")
    docs_dir = resolve_from_root("docs")
    assemble_docs(content_dir, generated_dir, docs_dir)

    typer.echo("Docs generated in docs/ and generated/")


@app.command()
def validate(config: str = "config/parser.yaml") -> None:
    """Validate sidecars, computed variables, and registry assembly."""
    parser_config = load_parser_config(config)
    sidecar_roots = _resolve_sidecar_roots(parser_config.sidecar_roots)
    discoveries = {d.experiment_id: d.path for d in discover_sidecars(sidecar_roots)}
    sidecar_paths = resolve_sidecar_paths(parser_config, discoveries)
    sidecars = load_sidecars_by_experiment(sidecar_paths)
    computed_config = load_computed_variables(parser_config.flat_dataset.computed_variables_spec)

    registry = build_registry(parser_config, sidecars, computed_config)
    validate_registry(registry)

    typer.echo("Validation succeeded")


@app.command()
def serve() -> None:
    """Serve the MkDocs site locally."""
    subprocess.run(["mkdocs", "serve"], check=True)


if __name__ == "__main__":
    app()
