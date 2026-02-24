from __future__ import annotations

from pathlib import Path


def project_root() -> Path:
    return Path(__file__).resolve().parents[3]


def path_from_root(*parts: str) -> Path:
    return project_root().joinpath(*parts)


def resolve_from_root(raw_path: str | Path) -> Path:
    path = Path(raw_path)
    if path.is_absolute():
        return path
    return project_root() / path
