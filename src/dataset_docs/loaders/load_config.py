from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Optional

import yaml
from pydantic import BaseModel, ConfigDict, Field

from dataset_docs.utils.paths import resolve_from_root


class ExperimentConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    enabled: bool = True
    sidecar_path: Optional[str] = None
    page_slug: Optional[str] = None
    scope_md: Optional[str] = None


class FlatDatasetConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    include_experiments: List[str] = Field(default_factory=list)
    computed_variables_spec: str


class ParserConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    display_version: str = "dump"
    sidecar_roots: List[str] = Field(default_factory=list)
    experiments: Dict[str, ExperimentConfig] = Field(default_factory=dict)
    flat_dataset: FlatDatasetConfig


class ComputedVariableSpec(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    definition: str
    level: str
    domain: str
    depends_on: List[str] = Field(default_factory=list)
    algorithm: str


class ComputedVariablesConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    variables: List[ComputedVariableSpec] = Field(default_factory=list)


def _load_yaml(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Missing YAML file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise ValueError(f"YAML root must be a mapping: {path}")
    return data


def load_parser_config(path: str | Path) -> ParserConfig:
    resolved = resolve_from_root(path)
    data = _load_yaml(resolved)
    return ParserConfig.model_validate(data)


def load_computed_variables(path: str | Path) -> ComputedVariablesConfig:
    resolved = resolve_from_root(path)
    data = _load_yaml(resolved)
    return ComputedVariablesConfig.model_validate(data)
