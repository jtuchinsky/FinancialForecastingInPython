"""Shared helpers for the Financial Forecasting in Python tutorial.

Import from lesson notebooks with:

    import sys; sys.path.insert(0, "../../src")
    from ffp import sample_prices, error_report
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def sample_prices(n: int = 500, seed: int = 42, start: str = "2020-01-01") -> pd.Series:
    """Return a reproducible random-walk price series indexed by business days."""
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start, periods=n, freq="B")
    prices = 100 + np.cumsum(rng.normal(0, 1, size=n))
    return pd.Series(prices, index=dates, name="close")


def error_report(y_true: pd.Series, y_pred: pd.Series) -> dict[str, float]:
    """Return MAE, RMSE and MAPE for a forecast against actuals."""
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    mae = np.abs(y_true - y_pred).mean()
    rmse = np.sqrt(((y_true - y_pred) ** 2).mean())
    mape = np.abs((y_true - y_pred) / y_true).mean() * 100
    return {"mae": float(mae), "rmse": float(rmse), "mape": float(mape)}