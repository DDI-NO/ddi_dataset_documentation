from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

from dataset_docs.model.sidecar_schema import (
    DerivationAnnotation,
    SemanticsAnnotation,
)


@dataclass(frozen=True)
class Variable:
    id: str
    label: str
    definition: str
    schema_element: Optional[str]
    semantics: SemanticsAnnotation
    allowed_values: List[str]
    synonyms: List[str]
    sensitivity: str
    derivation: DerivationAnnotation
    export_column: Optional[str]


@dataclass(frozen=True)
class ComputedVariable:
    name: str
    definition: str
    level: str
    domain: str
    depends_on: List[str]
    algorithm: str


@dataclass(frozen=True)
class DatasetColumn:
    name: str
    label: str
    definition: str
    level: str
    domain: str
    value_type: str
    units: Optional[str]
    sensitivity: str
    source: str
    derivation: str
    depends_on: List[str] = field(default_factory=list)
    allowed_values: List[str] = field(default_factory=list)
    synonyms: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class Experiment:
    experiment_id: str
    slug: str
    scope_path: Optional[str]
    description: str
    variables: List[Variable]


@dataclass(frozen=True)
class DatasetRegistry:
    display_version: str
    experiments: List[Experiment]
    dataset_columns: List[DatasetColumn]
    computed_variables: List[ComputedVariable]
