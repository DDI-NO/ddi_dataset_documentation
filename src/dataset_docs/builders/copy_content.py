from __future__ import annotations

import shutil
from pathlib import Path


def assemble_docs(content_dir: Path, generated_dir: Path, docs_dir: Path) -> None:
    if docs_dir.exists():
        shutil.rmtree(docs_dir)
    docs_dir.mkdir(parents=True, exist_ok=True)

    if content_dir.exists():
        shutil.copytree(content_dir, docs_dir, dirs_exist_ok=True)
    if generated_dir.exists():
        shutil.copytree(generated_dir, docs_dir, dirs_exist_ok=True)

    generated_index = generated_dir / "index_experiments.md"
    if generated_index.exists():
        experiments_index = docs_dir / "experiments" / "index.md"
        experiments_index.parent.mkdir(parents=True, exist_ok=True)
        experiments_index.write_text(generated_index.read_text(encoding="utf-8"), encoding="utf-8")
