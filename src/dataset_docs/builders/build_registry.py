from __future__ import annotations

from pathlib import Path
from typing import Dict, List

from dataset_docs.loaders.load_config import ComputedVariablesConfig, ParserConfig
from dataset_docs.model.registry import ComputedVariable, DatasetColumn, DatasetRegistry, Experiment, Variable
from dataset_docs.model.sidecar_schema import DisplayFieldAnnotation, Sidecar
from dataset_docs.utils.paths import resolve_from_root


def _build_variable(display_field_id: str, annotation: DisplayFieldAnnotation) -> Variable:
    return Variable(
        id=display_field_id,
        label=annotation.label,
        definition=annotation.definition,
        schema_element=annotation.source.schema_element,
        semantics=annotation.semantics,
        allowed_values=list(annotation.allowed_values),
        synonyms=list(annotation.resolution.synonyms),
        sensitivity=annotation.sensitivity,
        derivation=annotation.derivation,
        export_column=annotation.export.column,
    )


def _is_exported(annotation: DisplayFieldAnnotation, display_version: str) -> bool:
    return annotation.export.included_via_display_version == display_version


def _build_dataset_columns(experiment_id: str, variables: List[Variable]) -> List[DatasetColumn]:
    columns: List[DatasetColumn] = []
    for variable in variables:
        name = variable.export_column or variable.id
        columns.append(
            DatasetColumn(
                name=name,
                label=variable.label,
                definition=variable.definition,
                level=variable.semantics.level,
                domain=variable.semantics.domain,
                value_type=variable.semantics.value_type,
                units=variable.semantics.units,
                sensitivity=variable.sensitivity,
                source=experiment_id,
                derivation=variable.derivation.kind,
                depends_on=list(variable.derivation.depends_on_display_fields),
                allowed_values=list(variable.allowed_values),
                synonyms=list(variable.synonyms),
            )
        )
    return columns


def _build_computed_columns(computed_config: ComputedVariablesConfig) -> List[DatasetColumn]:
    columns: List[DatasetColumn] = []
    for variable in computed_config.variables:
        columns.append(
            DatasetColumn(
                name=variable.name,
                label=variable.name,
                definition=variable.definition,
                level=variable.level,
                domain=variable.domain,
                value_type="computed",
                units=None,
                sensitivity="none",
                source="computed",
                derivation=variable.algorithm,
                depends_on=list(variable.depends_on),
            )
        )
    return columns


def build_registry(
    config: ParserConfig,
    sidecars: Dict[str, Sidecar],
    computed_config: ComputedVariablesConfig,
) -> DatasetRegistry:
    experiments: List[Experiment] = []
    dataset_columns: List[DatasetColumn] = []

    for experiment_id, experiment_config in config.experiments.items():
        if not experiment_config.enabled:
            continue
        sidecar = sidecars.get(experiment_id)
        if sidecar is None:
            raise ValueError(f"No sidecar loaded for experiment {experiment_id}")
        variables = [
            _build_variable(field_id, annotation)
            for field_id, annotation in sidecar.display_field_annotations.items()
            if _is_exported(annotation, config.display_version)
        ]
        slug = experiment_config.page_slug or experiment_id.lower()
        scope_path = experiment_config.scope_md
        experiments.append(
            Experiment(
                experiment_id=experiment_id,
                slug=slug,
                scope_path=scope_path,
                variables=variables,
            )
        )
        dataset_columns.extend(_build_dataset_columns(experiment_id, variables))

    computed_variables = [
        ComputedVariable(
            name=spec.name,
            definition=spec.definition,
            level=spec.level,
            domain=spec.domain,
            depends_on=list(spec.depends_on),
            algorithm=spec.algorithm,
        )
        for spec in computed_config.variables
    ]
    dataset_columns.extend(_build_computed_columns(computed_config))

    return DatasetRegistry(
        display_version=config.display_version,
        experiments=experiments,
        dataset_columns=dataset_columns,
        computed_variables=computed_variables,
    )


def resolve_sidecar_paths(config: ParserConfig, discoveries: Dict[str, Path]) -> Dict[str, Path]:
    resolved: Dict[str, Path] = {}
    for experiment_id, experiment_config in config.experiments.items():
        if not experiment_config.enabled:
            continue
        if experiment_config.sidecar_path:
            resolved[experiment_id] = resolve_from_root(experiment_config.sidecar_path)
            continue
        if experiment_id not in discoveries:
            raise ValueError(f"No discovered sidecar for experiment {experiment_id}")
        resolved[experiment_id] = discoveries[experiment_id]
    return resolved
