# Data

Put shared datasets here (e.g. `prices.csv`, `income_statement.csv`) and load
them from any lesson notebook with a relative path:

```python
import pandas as pd
df = pd.read_csv("../../data/prices.csv", parse_dates=["date"], index_col="date")
```

Until you add real data, the notebooks generate a reproducible sample series via
`ffp.sample_prices()` (see `src/ffp/__init__.py`).