# Financial Forecasting in Python

A hands-on tutorial. It is organized into **lessons**; each lesson contains one
or more **sub-lessons**, and every sub-lesson is a Jupyter notebook.

## Lessons

<!-- LESSONS:START -->
### 1. Income Statements

- [1.1 Introduction to financial statements](lessons/01-income-statements/01-introduction-to-financial-statements.ipynb)
- [1.2 Calculating sales and Cost of Goods Sold (COGS)](lessons/01-income-statements/02-calculating-sales-and-cost-of-goods-sold-cogs.ipynb)
- [1.3 Working with raw forecasts datasets](lessons/01-income-statements/03-working-with-raw-forecasts-datasets.ipynb)
<!-- LESSONS:END -->

## Project layout

```
lessons/<NN-lesson-slug>/<NN-sublesson-slug>.ipynb   # a notebook per sub-lesson
data/                                                # shared datasets
src/ffp/                                             # reusable helpers
scripts/generate_lessons.py                          # interactive scaffolder
```

## Getting started

Dependencies are managed with [uv](https://docs.astral.sh/uv/).

```bash
uv sync                # install the environment
uv run jupyter lab     # launch JupyterLab, then open a lesson notebook
```

## Using the shared helpers

From inside a sub-lesson notebook:

```python
import sys; sys.path.insert(0, "../../src")
from ffp import sample_prices, error_report
```
