from __future__ import annotations

from typing import List

from dataset_docs.model.registry import DatasetRegistry


def validate_registry(registry: DatasetRegistry) -> None:
    errors: List[str] = []

    if not registry.experiments:
        errors.append("No experiments were loaded.")

    for experiment in registry.experiments:
        if not experiment.variables:
            errors.append(f"Experiment {experiment.experiment_id} has no exportable variables.")

    for column in registry.dataset_columns:
        if not column.name:
            errors.append("Dataset column missing name.")
        if not column.definition:
            errors.append(f"Dataset column {column.name} missing definition.")

    if errors:
        raise ValueError("Registry validation failed:\n" + "\n".join(errors))
