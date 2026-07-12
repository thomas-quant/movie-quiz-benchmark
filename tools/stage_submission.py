#!/usr/bin/env python3
"""Copy a submission into a metadata-free staging directory."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


EXCLUDED_DIRS = {".git", ".venv", "venv", "env", "__pycache__", ".pytest_cache", "node_modules"}
EXCLUDED_FILES = {"readme.md", "scorecard.md"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--destination", type=Path, required=True)
    parser.add_argument("--force", action="store_true")
    return parser.parse_args()


def ignore(_directory: str, names: list[str]) -> set[str]:
    excluded: set[str] = set()
    for name in names:
        path = Path(name)
        if name.lower() in EXCLUDED_FILES or name.lower() in EXCLUDED_DIRS:
            excluded.add(name)
    return excluded


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    destination = args.destination.resolve()
    if not source.is_dir():
        raise SystemExit(f"source directory does not exist: {source}")
    if destination.exists():
        if not args.force:
            raise SystemExit(f"destination exists; use --force to replace it: {destination}")
        shutil.rmtree(destination)
    shutil.copytree(source, destination, ignore=ignore)
    print(destination)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
