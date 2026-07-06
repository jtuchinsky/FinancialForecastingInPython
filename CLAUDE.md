# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project state

This is a freshly scaffolded [uv](https://docs.astral.sh/uv/) project associated with the DataCamp course "Financial Forecasting in Python." As of now it contains only a `main.py` stub and no real source code, dependencies, or tests. Expect to build out the course material (forecasting scripts/notebooks) from scratch.

## Environment

- Python is pinned to 3.11 (`.python-version`); `pyproject.toml` requires `>=3.11`.
- Dependency management is via `uv`. There is no `uv.lock` yet — it is created on the first `uv add` / `uv sync`.

## Commands

- Run the entry point: `uv run main.py` (or `uv run python main.py`)
- Add a dependency: `uv add <package>` (e.g. `uv add pandas statsmodels`)
- Sync the environment from `pyproject.toml`: `uv sync`

No lint or test tooling is configured yet. If tests are added, prefer `pytest` run via `uv run pytest` (and `uv run pytest path::test_name` for a single test).