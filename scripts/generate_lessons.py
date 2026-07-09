#!/usr/bin/env python3
"""Interactively scaffold the tutorial.

Prompts for lessons and, within each lesson, sub-lessons. Every sub-lesson
becomes a Jupyter notebook:

    lessons/<NN-lesson-slug>/<NN-sublesson-slug>.ipynb

Re-run any time: existing lessons are reused and new sub-lessons are appended
with continuing numbers. Nothing is overwritten unless you confirm.

Usage:
    uv run python scripts/generate_lessons.py
    .venv/bin/python scripts/generate_lessons.py

It also runs non-interactively (pipe answers on stdin), which is how the test
in this repo drives it.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LESSONS_DIR = ROOT / "lessons"


# --------------------------------------------------------------------------- #
# Notebook construction (nbformat v4, no external deps)
# --------------------------------------------------------------------------- #
def _source(text: str) -> list[str]:
    parts = text.split("\n")
    return [p + "\n" for p in parts[:-1]] + [parts[-1]]


def _md(cell_id: str, text: str) -> dict:
    return {"cell_type": "markdown", "id": cell_id, "metadata": {}, "source": _source(text)}


def _code(cell_id: str, text: str) -> dict:
    return {"cell_type": "code", "id": cell_id, "metadata": {},
            "execution_count": None, "outputs": [], "source": _source(text)}


def build_notebook(lesson_title: str, sub_title: str, description: str) -> dict:
    desc = description.strip() or "_Describe what this sub-lesson covers._"
    cells = [
        _md("title", f"# {sub_title}\n\n"
                     f"**Lesson:** {lesson_title}  \n"
                     f"_Financial Forecasting in Python_"),
        _md("overview", f"## Overview\n\n{desc}"),
        _md("objectives", "## Learning objectives\n\n"
                          "- TODO: objective 1\n- TODO: objective 2\n- TODO: objective 3"),
        _md("setup-md", "## Setup"),
        _code("setup", "import sys; sys.path.insert(0, '../../src')\n"
                       "\n"
                       "import numpy as np\n"
                       "import pandas as pd\n"
                       "import matplotlib.pyplot as plt\n"
                       "\n"
                       "from ffp import sample_prices, error_report  # shared helpers"),
        _md("work-md", "## Walkthrough"),
        _code("work", "# TODO: lesson code here\n"
                      "prices = sample_prices()\n"
                      "prices.plot(figsize=(10, 4), title='Sample price series')\n"
                      "plt.show()"),
        _md("exercise-md", "## Exercise\n\n"
                           "- TODO: describe a task for the reader to complete."),
        _code("exercise", "# TODO: your solution here"),
        _md("summary", "## Summary\n\n"
                       "Recap the key points and point to the next sub-lesson."),
    ]
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.strip().lower()).strip("-")
    return slug or "untitled"


def next_index(directory: Path, pattern: str) -> int:
    """Highest existing NN- prefix + 1 among children matching `pattern`."""
    highest = 0
    if directory.exists():
        for child in directory.glob(pattern):
            m = re.match(r"(\d+)-", child.name)
            if m:
                highest = max(highest, int(m.group(1)))
    return highest + 1


def prompt(label: str) -> str:
    try:
        return input(label).strip()
    except EOFError:
        return ""


def make_sublesson(lesson_dir: Path, index: int, lesson_title: str,
                   sub_title: str, description: str) -> Path:
    path = lesson_dir / f"{index:02d}-{slugify(sub_title)}.ipynb"
    if path.exists():
        if prompt(f"    ! {path.name} exists. Overwrite? [y/N] ").lower() != "y":
            print(f"    - skipped {path.name}")
            return path
    with path.open("w") as f:
        json.dump(build_notebook(lesson_title, sub_title, description), f, indent=1)
        f.write("\n")
    print(f"    + {path.relative_to(ROOT)}")
    return path


# --------------------------------------------------------------------------- #
# Main interactive flow
# --------------------------------------------------------------------------- #
def main() -> int:
    LESSONS_DIR.mkdir(exist_ok=True)
    print("Financial Forecasting in Python — lesson scaffolder")
    print("Leave a title blank and press Enter to finish a level.\n")

    created = 0
    while True:
        lesson_title = prompt("Lesson title (blank to finish): ")
        if not lesson_title:
            break

        lesson_idx = next_index(LESSONS_DIR, "[0-9]*-*")
        lesson_dir = LESSONS_DIR / f"{lesson_idx:02d}-{slugify(lesson_title)}"
        lesson_dir.mkdir(parents=True, exist_ok=True)
        print(f"  Lesson {lesson_idx:02d}: {lesson_title}  ->  {lesson_dir.relative_to(ROOT)}/")

        while True:
            sub_title = prompt("    Sub-lesson title (blank to end lesson): ")
            if not sub_title:
                break
            description = prompt("    One-line description (optional): ")
            sub_idx = next_index(lesson_dir, "[0-9]*-*.ipynb")
            make_sublesson(lesson_dir, sub_idx, lesson_title, sub_title, description)
            created += 1
        print()

    print(f"Done. Created {created} sub-lesson notebook(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
