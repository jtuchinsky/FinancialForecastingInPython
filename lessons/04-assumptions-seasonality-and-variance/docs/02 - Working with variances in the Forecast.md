# Working with variances in the Forecast

The goal is to explore variances in a forecast and how to handle them.

* **TODO:** define variance and calculate it per period in absolute and percentage terms.
* **TODO:** classify variances as favorable or unfavorable.
* **TODO:** summarise forecast accuracy across periods with error metrics (MAE, RMSE, MAPE).

Example Code:
```python
forecast = [5000, 5200, 5400, 5600]
actual   = [5100, 5000, 5500, 5400]
variances = [a - f for f, a in zip(forecast, actual)]
print(variances)  # [100, -200, 100, -200]
```

#### 1. What is variance?

No forecast is ever exactly right. Variance is the gap between what we forecast
and what actually happened. Measuring it tells us how good our assumptions were
and where the forecast needs adjusting. For a single period it is simply
`actual - forecast`: a positive number means the actual came in above forecast,
a negative number means below.

#### 2. Absolute and percentage variance

The raw difference is the **absolute variance**, expressed in currency units. On
its own it can be misleading — a variance of 100 is large against a 5,000
forecast but trivial against 500,000. So we also compute the **percentage
variance**, `(actual - forecast) / forecast * 100`, which puts every period on a
comparable scale.

#### 3. Favorable and unfavorable variances

Variances are labelled to show whether they helped or hurt. For a **revenue**
line such as sales, an actual figure at or above forecast is **favorable** and
below forecast is **unfavorable**. For a **cost** line the logic reverses:
spending less than forecast is favorable. Getting the sign convention right for
each line item is essential when interpreting a forecast.

#### 4. Summarising accuracy across periods

Per-period variances are detailed, but managers usually want a single measure of
how accurate the forecast was overall. Three standard error metrics do this:

- **MAE** (mean absolute error): the average size of the variance, in currency
  units.
- **RMSE** (root mean squared error): like MAE but squares the errors first, so
  large misses are penalised more heavily.
- **MAPE** (mean absolute percentage error): the average variance as a
  percentage of actuals.

The shared helper `error_report(y_true, y_pred)` returns all three at once.

#### 5. A gap analysis

It is important to know why the forecast differed from the actual results. On top of 
this, now that the actual results are different, we can no longer rely on the original 
forecast and have to investigate how the forecast will evolve when taking this change 
into account. Identifying, quantifying and investigating this difference between the old 
forecast and the updated forecast is called a gap analysis. 
This is usually represented as per the graph here, where you can see the gap between the 
original forecast and the new forecast.

#### 6. Gap analysis and alternative forecasts

Let's look at an example. A company forecast sales of 1200 in 2018. However, 
halfway through the year, the sales were only 300, with six months to go. It 
is probably unrealistic to expect sales to more than double for the next six months. 
So there is a gap. 
The first thing to do is perform a gap analysis - what caused this? Usually, there is 
an underlying dependency, in this case, sales were based on volumes of 120 to a key supplier, 
but they have only bought 30 thus far and only expect to buy a maximum of 45 in the next 6 months 
meaning the total volumes for the year will be only 75, not 120. This is the dependency. 
We have to adjust the forecasted volumes. So, an alternate forecast must be calculated. 
Using our skills with defining Python functions and working with dependencies, we can now see how 
to work with these scenarios in Python in the following exercises.  

### Recap

You learned that variance is the difference between forecast and actual, and how
to measure and interpret it. Key points:

- **Per-period variance:** `actual - forecast`, in absolute and percentage terms.

```
months   = ['Jan', 'Feb', 'Mar', 'Apr']
forecast = [5000, 5200, 5400, 5600]
actual   = [5100, 5000, 5500, 5400]
for i in range(len(months)):
    var = actual[i] - forecast[i]
    pct = var / forecast[i] * 100
    print(months[i], var, round(pct, 1))
```

- **Favorable vs unfavorable:** for a revenue line, actual at or above forecast
  is favorable.

```
status = "favorable" if actual[i] >= forecast[i] else "unfavorable"
```

- **Summary metrics:** MAE, RMSE and MAPE condense many variances into one
  accuracy figure.

```
from ffp import error_report
report = error_report(actual, forecast)
print(report)  # {'mae': 150.0, 'rmse': 158.11..., 'mape': 2.87...}
```

This completes the chapter on assumptions, seasonality and variance: you can now
set the drivers of a forecast, reflect seasonal patterns, and measure how far the
outcome diverged from the plan.
