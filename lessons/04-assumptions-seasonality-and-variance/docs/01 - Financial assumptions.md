# Financial assumptions

The goal is to understand how assumptions drive a forecast, and how to apply
and combine them in Python to project figures forward.

* **TODO:** define what a financial assumption is and why forecasts depend on them.
* **TODO:** apply a growth-rate assumption over multiple periods (loop and formula).
* **TODO:** link assumptions so one line item (e.g. COGS) follows from another (sales).

Example Code:
```python
base_sales = 5000
growth = 0.05
forecast = [round(base_sales * (1 + growth) ** n, 2) for n in range(1, 4)]
print(forecast)
```

#### 1. Financial assumptions

A forecast is only ever as good as the assumptions behind it. An assumption is
a stated expectation about the future — how fast sales will grow, what share of
sales is eaten up by costs, how quickly customers pay — that we apply to a base
figure to project it forward. Making these assumptions explicit is what turns
historical data into a forecast.

#### 2. Growth assumptions

The most common assumption is a growth rate: the percentage by which a figure
changes each period. Applying a growth rate means multiplying by `(1 + growth)`
once per period. Starting from 5,000 sales growing at 5% a year, the next year
is `5000 * 1.05 = 5250`, the year after `5250 * 1.05 = 5512.50`, and so on. In
code we can loop period by period, accumulating each result in a list.

#### 3. Growth as a formula

When the growth rate is constant, repeatedly multiplying is the same as raising
`(1 + growth)` to the power of the number of periods. This compound-growth
formula, `future = base * (1 + growth) ** periods`, lets us jump straight to any
future period without a loop — useful for quick checks or when only the end
value matters.

#### 4. Linking assumptions

Line items in a forecast are rarely independent. A cost assumption is often
expressed as a percentage of sales, so once sales are forecast the cost follows
automatically. Layering a "COGS is 60% of sales" assumption on top of a sales
forecast gives us COGS and, by subtraction, gross profit for every period. This
chaining — one assumption feeding the next — is the backbone of a full financial
model.

#### 5. Different types of Assumptions  

Often in forecasting, we need to understand probability. 
We will not cover the statistical methods of probability in this course but will 
have a look at something called weighted probability, which is simply calculated by 
multiplying each outcome by its probability percentage and adding the total result, 
thereby obtaining a weighted average probability for a specific calculated outcome. 
Another assumption that can be used is market sentiment. 
Market sentiment is the feeling or tone of a market, or its crowd psychology, as revealed 
through the activity and price movement of the securities traded in that market. 
This drives, for example, expected sales growth and is usually based on external market indices. 
There is also demand and supply assumptions that can be set by a company, which is common 
in industries with longer lead times for products where customers can place orders in advance 
or in industries with reliable sales patterns.

#### 6. Working with pairs in Python

Sometimes, we have to build lists that are a little more complex. 
There is an easy way to do this in Python, which we will explore now. 
Take for example this table:

| Outcome | Probability (%) |
|---------|-----------------|
| 1       | 30%             |
| 2       | 20%             |
| 3       | 50%             |

Instead of taking two lists, the outcomes and the probability, 
we can create a combined list by converting the pair values into a string separated by a pipe 
character. 

Have a look at the resulting outcome, the outcome_probability list where you can clearly see the 
combined values. 
`outcome_probability = ['1|0.3', '2|02', '3|0.5']`
This technique is useful when needing to multiply the pairs by each other, as is done 
with weighted probability.

#### 7. Define a Python Function

We will explore a basic Python function, where we can assign the dependency formulas to a function, 
which will become very useful later on and prevent us from retyping a function many times. 

```
def assumption1():
  if marketsentiment = 0.3:
    sales += sales*0.1
  else:
    sales  
```
So, if we look at this example, we simply define our formula for an assumption on market sentiment 
to the assumption1() function

### Recap

You learned that assumptions are the drivers behind every forecast, and how to
apply and combine them in Python. Key points:

- **Assumptions drive forecasts:** an assumption is an explicit expectation
  (growth, cost ratio, etc.) applied to a base figure to project it forward.
- **Growth by loop:** multiply by `(1 + growth)` once per period, collecting the
  results.

```
sales = 5000
growth = 0.05
forecast = []
for year in range(1, 4):
    sales = sales * (1 + growth)
    forecast.append(round(sales, 2))
print(forecast)  # [5250.0, 5512.5, 5788.12]
```

- **Growth by formula:** for a constant rate, `base * (1 + growth) ** periods`
  gives the same answer in one step.

```
print(round(5000 * (1 + 0.05) ** 3, 2))  # 5788.13
```

- **Linked assumptions:** a ratio assumption lets one line item follow from
  another, e.g. COGS as a percentage of forecast sales, and gross profit as the
  remainder.

```
for sales in [5250.0, 5512.5, 5788.12]:
    cogs = sales * 0.60
    print(sales, cogs, sales - cogs)
```

The goal of the next lesson is to move beyond a single flat growth rate and
reflect recurring **seasonal** patterns in the forecast.
