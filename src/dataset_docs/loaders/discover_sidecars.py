from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List


@dataclass(frozen=True)
class SidecarDiscovery:
    experiment_id: str
    path: Path


DISPLAY_SUFFIX = "_display.meta.yaml"


def infer_experiment_id(path: Path) -> str:
    name = path.name
    if name.endswith(DISPLAY_SUFFIX):
        return name[: -len(DISPLAY_SUFFIX)]
    return path.stem


def discover_sidecars(sidecar_roots: Iterable[Path]) -> List[SidecarDiscovery]:
    discoveries: List[SidecarDiscovery] = []
    for root in sidecar_roots:
        if not root.exists():
            continue
        for path in root.rglob(f"**/display/*{DISPLAY_SUFFIX}"):
            experiment_id = infer_experiment_id(path)
            discoveries.append(SidecarDiscovery(experiment_id=experiment_id, path=path))
    return discoveries
