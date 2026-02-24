from __future__ import annotations

from typing import Dict, List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field


class DisplayVersion(BaseModel):
    model_config = ConfigDict(extra="forbid")

    description: Optional[str] = None


class ExportAnnotation(BaseModel):
    model_config = ConfigDict(extra="forbid")

    column: Optional[str] = None
    included_via_display_version: Optional[str] = None


class SourceAnnotation(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_element: Optional[str] = None
    display_field_elements: Dict[str, str] = Field(default_factory=dict)


class DerivationAnnotation(BaseModel):
    model_config = ConfigDict(extra="forbid")

    kind: Literal["sql", "sql_case", "concat", "none"]
    input: Optional[str] = None
    mapping: Dict[str, str] = Field(default_factory=dict)
    else_: Optional[str] = Field(default=None, alias="else")
    depends_on_display_fields: List[str] = Field(default_factory=list)


class SemanticsAnnotation(BaseModel):
    model_config = ConfigDict(extra="forbid")

    level: Literal["subject", "visit", "sample", "experiment"]
    domain: str
    value_type: Literal["categorical", "numeric", "date", "text", "boolean"]
    units: Optional[str] = None
    preferred_representation: Literal["code", "label", "raw"]


class ResolutionAnnotation(BaseModel):
    model_config = ConfigDict(extra="forbid")

    canonical_name: str
    synonyms: List[str] = Field(default_factory=list)


class QualityAnnotation(BaseModel):
    model_config = ConfigDict(extra="forbid")

    notes: Optional[str] = None


class DisplayFieldAnnotation(BaseModel):
    model_config = ConfigDict(extra="forbid")

    export: ExportAnnotation
    label: str
    definition: str
    source: SourceAnnotation
    derivation: DerivationAnnotation
    semantics: SemanticsAnnotation
    resolution: ResolutionAnnotation
    allowed_values: List[str] = Field(default_factory=list)
    sensitivity: Literal["clinical", "pii", "none"]
    quality: QualityAnnotation


class Sidecar(BaseModel):
    model_config = ConfigDict(extra="forbid")

    display: str
    display_versions: Dict[str, DisplayVersion]
    display_field_annotations: Dict[str, DisplayFieldAnnotation]
