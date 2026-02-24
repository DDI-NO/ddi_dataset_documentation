from __future__ import annotations

from pathlib import Path
from typing import Dict

import yaml
from pydantic import ValidationError

from dataset_docs.model.sidecar_schema import Sidecar


def load_sidecar(path: Path) -> Sidecar:
    if not path.exists():
        raise FileNotFoundError(f"Missing sidecar file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    try:
        return Sidecar.model_validate(data)
    except ValidationError as exc:
        raise ValueError(f"Sidecar schema validation failed for {path}: {exc}") from exc


def load_sidecars_by_experiment(mapping: Dict[str, Path]) -> Dict[str, Sidecar]:
    return {experiment_id: load_sidecar(path) for experiment_id, path in mapping.items()}
