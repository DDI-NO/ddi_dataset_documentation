from __future__ import annotations

import shutil
from pathlib import Path
from typing import Iterable, Set


def _resolve_excluded_paths(content_dir: Path, exclude_paths: Iterable[Path]) -> Set[str]:
    content_root = content_dir.resolve()
    excluded: Set[str] = set()
    for path in exclude_paths:
        resolved = path.resolve()
        try:
            rel = resolved.relative_to(content_root)
        except ValueError:
            continue
        excluded.add(rel.as_posix())
    return excluded


def _make_ignore(content_dir: Path, excluded_paths: Set[str]):
    content_root = content_dir.resolve()

    def _ignore(dir_path: str, names: list[str]) -> set[str]:
        if not excluded_paths:
            return set()
        ignore: set[str] = set()
        try:
            rel_dir = Path(dir_path).resolve().relative_to(content_root)
        except ValueError:
            return ignore
        for name in names:
            rel_path = (rel_dir / name).as_posix()
            if rel_path in excluded_paths:
                ignore.add(name)
        return ignore

    return _ignore


def assemble_docs(
    content_dir: Path,
    generated_dir: Path,
    docs_dir: Path,
    *,
    exclude_content_paths: Iterable[Path] | None = None,
) -> None:
    if docs_dir.exists():
        shutil.rmtree(docs_dir)
    docs_dir.mkdir(parents=True, exist_ok=True)

    if content_dir.exists():
        excluded_paths = _resolve_excluded_paths(content_dir, exclude_content_paths or [])
        ignore = _make_ignore(content_dir, excluded_paths)
        shutil.copytree(content_dir, docs_dir, dirs_exist_ok=True, ignore=ignore)
    if generated_dir.exists():
        shutil.copytree(generated_dir, docs_dir, dirs_exist_ok=True)

    generated_index = generated_dir / "index_experiments.md"
    if generated_index.exists():
        experiments_index = docs_dir / "experiments" / "index.md"
        experiments_index.parent.mkdir(parents=True, exist_ok=True)
        experiments_index.write_text(generated_index.read_text(encoding="utf-8"), encoding="utf-8")
