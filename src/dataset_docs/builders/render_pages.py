from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List

import re

from jinja2 import Environment, FileSystemLoader, select_autoescape

from dataset_docs.model.registry import DatasetColumn, DatasetRegistry, Experiment, Variable
from dataset_docs.utils.paths import resolve_from_root


MARKER = "<!-- AUTO:VARIABLES -->"
OVERVIEW_MARKER = "<!-- AUTO:OVERVIEW -->"
OVERVIEW_HEADER_RE = re.compile(r"(^##\s+Overview\s*$)", flags=re.IGNORECASE | re.MULTILINE)


@dataclass(frozen=True)
class TableCell:
    id: str
    label: str
    definition: str
    level: str
    domain: str
    value_type: str
    sensitivity: str


@dataclass(frozen=True)
class VariableTableRow:
    id: str
    label: str
    definition: str
    level: str
    domain: str
    value_type: str
    sensitivity: str


@dataclass(frozen=True)
class VariableDetail:
    id: str
    label: str
    definition: str
    schema_element: str
    semantics: str
    allowed_values: str
    synonyms: str
    sensitivity: str
    derivation: str


@dataclass(frozen=True)
class VariableView:
    title: str
    table: VariableTableRow
    detail: VariableDetail


@dataclass(frozen=True)
class DatasetTableRow:
    name: str
    label: str
    definition: str
    level: str
    domain: str
    value_type: str
    sensitivity: str
    source: str


@dataclass(frozen=True)
class DatasetDetail:
    name: str
    label: str
    definition: str
    source: str
    semantics: str
    allowed_values: str
    synonyms: str
    sensitivity: str
    derivation: str
    depends_on: str


@dataclass(frozen=True)
class DatasetView:
    title: str
    table: DatasetTableRow
    detail: DatasetDetail


@dataclass(frozen=True)
class ExperimentLink:
    name: str
    description: str
    link_text: str
    href: str


def _escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", "<br>")


def _clean(value: str | None) -> str:
    if not value:
        return "TODO"
    return value


def _join_list(values: Iterable[str]) -> str:
    if not values:
        return "-"
    return ", ".join(values)


def _truncate_description(description: str, *, limit: int = 160) -> str:
    if len(description) <= limit:
        return description
    trimmed = description[: limit - 1].rstrip()
    return f"{trimmed}..."


def _inject_overview_description(scope_content: str, description: str) -> str:
    if OVERVIEW_MARKER in scope_content:
        return scope_content.replace(OVERVIEW_MARKER, description)
    if description in scope_content:
        return scope_content

    match = OVERVIEW_HEADER_RE.search(scope_content)
    if not match:
        return f"## Overview\n{description}\n\n{scope_content}"

    insert_at = match.end()
    before = scope_content[:insert_at]
    after = scope_content[insert_at:]
    return f"{before}\n{description}\n{after}"


def _variable_views(variables: List[Variable]) -> List[VariableView]:
    views: List[VariableView] = []
    for variable in variables:
        label = _clean(variable.label)
        definition = _clean(variable.definition)
        schema_element = variable.schema_element or "-"
        semantics = f"{variable.semantics.level} / {variable.semantics.domain} / {variable.semantics.value_type}"
        derivation = variable.derivation.kind
        views.append(
            VariableView(
                title=_escape(label or variable.id),
                table=VariableTableRow(
                    id=_escape(variable.id),
                    label=_escape(label),
                    definition=_escape(definition),
                    level=_escape(variable.semantics.level),
                    domain=_escape(variable.semantics.domain),
                    value_type=_escape(variable.semantics.value_type),
                    sensitivity=_escape(variable.sensitivity),
                ),
                detail=VariableDetail(
                    id=_escape(variable.id),
                    label=_escape(label),
                    definition=_escape(definition),
                    schema_element=_escape(schema_element),
                    semantics=_escape(semantics),
                    allowed_values=_escape(_join_list(variable.allowed_values)),
                    synonyms=_escape(_join_list(variable.synonyms)),
                    sensitivity=_escape(variable.sensitivity),
                    derivation=_escape(derivation),
                ),
            )
        )
    return views


def _dataset_views(columns: List[DatasetColumn]) -> List[DatasetView]:
    views: List[DatasetView] = []
    for column in columns:
        label = _clean(column.label)
        definition = _clean(column.definition)
        semantics = f"{column.level} / {column.domain} / {column.value_type}"
        views.append(
            DatasetView(
                title=_escape(label or column.name),
                table=DatasetTableRow(
                    name=_escape(column.name),
                    label=_escape(label),
                    definition=_escape(definition),
                    level=_escape(column.level),
                    domain=_escape(column.domain),
                    value_type=_escape(column.value_type),
                    sensitivity=_escape(column.sensitivity),
                    source=_escape(column.source),
                ),
                detail=DatasetDetail(
                    name=_escape(column.name),
                    label=_escape(label),
                    definition=_escape(definition),
                    source=_escape(column.source),
                    semantics=_escape(semantics),
                    allowed_values=_escape(_join_list(column.allowed_values)),
                    synonyms=_escape(_join_list(column.synonyms)),
                    sensitivity=_escape(column.sensitivity),
                    derivation=_escape(column.derivation),
                    depends_on=_escape(_join_list(column.depends_on)),
                ),
            )
        )
    return views


def _experiment_links(experiments: List[Experiment]) -> List[ExperimentLink]:
    links: List[ExperimentLink] = []
    for experiment in experiments:
        link_text = experiment.experiment_id
        href = f"{experiment.slug}.md"
        links.append(
            ExperimentLink(
                name=experiment.experiment_id,
                description=_escape(_truncate_description(experiment.description)),
                link_text=link_text,
                href=href,
            )
        )
    return links


def _env(templates_dir: Path) -> Environment:
    return Environment(
        loader=FileSystemLoader(str(templates_dir)),
        autoescape=select_autoescape(),
        trim_blocks=True,
        lstrip_blocks=True,
    )


def render_experiment_pages(registry: DatasetRegistry, templates_dir: Path, generated_dir: Path) -> None:
    env = _env(templates_dir)
    template = env.get_template("experiment.md.j2")
    for experiment in registry.experiments:
        if not experiment.scope_path:
            raise ValueError(f"Missing scope_md for experiment {experiment.experiment_id}")
        scope_path = resolve_from_root(experiment.scope_path)
        if not scope_path.exists():
            raise FileNotFoundError(f"Missing scope markdown: {scope_path}")
        scope_content = scope_path.read_text(encoding="utf-8")
        if MARKER not in scope_content:
            raise ValueError(f"Marker {MARKER} not found in {scope_path}")
        scope_content = _inject_overview_description(scope_content, experiment.description)
        variable_section = template.render(variables=_variable_views(experiment.variables))
        output_content = scope_content.replace(MARKER, variable_section)
        out_path = generated_dir / "experiments" / f"{experiment.slug}.md"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output_content, encoding="utf-8")


def render_dataset_catalog(registry: DatasetRegistry, templates_dir: Path, generated_dir: Path) -> None:
    env = _env(templates_dir)
    template = env.get_template("variable_catalog.md.j2")
    dataset_views = _dataset_views(registry.dataset_columns)
    output = template.render(variables=dataset_views)
    out_path = generated_dir / "dataset" / "variables.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(output, encoding="utf-8")


def render_experiments_index(registry: DatasetRegistry, templates_dir: Path, generated_dir: Path) -> None:
    env = _env(templates_dir)
    template = env.get_template("landing_experiments_index.md.j2")
    output = template.render(experiments=_experiment_links(registry.experiments))
    out_path = generated_dir / "index_experiments.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(output, encoding="utf-8")
