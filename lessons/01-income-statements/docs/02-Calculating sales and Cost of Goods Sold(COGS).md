# Calculating Sales & Cost of Goods Sold (COGS)
You learned about the basics of financial statements, specifically focusing on the income statement. 
This included understanding key components like sales and the cost of goods sold (COGS), and how these contribute to gross profit. Here are the main points you covered:

* **Sales Calculation:** Sales, also known as income, revenue, or turnover, are calculated by multiplying the sales price per unit by the number of units sold. Complexities such as discounts, credit sales, and sales mix were also discussed.
* **Cost of Goods Sold (COGS):** COGS includes both fixed and variable costs. Fixed costs are incurred regardless of production volume, while variable costs depend on the number of units produced. The formula for COGS is:

$$\text{COGS} = \text{Opening Stock} - \text{Closing Stock} + \text{Fixed Costs} + \text{Variable Costs}$$
* **Gross Profit:** Gross profit is the difference between sales and COGS, providing insight into the profitability of core products. It is expressed as a percentage of sales, known as the gross profit margin (GP margin).
* **Break-Even Point:** This is the point where total revenue equals total costs, calculated using the formula:

$$\text{Break-Even Point (Units)} = \frac{\text{Fixed Costs}}{\text{Sales Price per Unit} - \text{Variable Cost per Unit}}$$

Example Code:
```python
# Set variables units sold and sales price of the T-shirts (basic and custom)
salesprice_basic = 15
salesprice_custom = 25

# Calculate the combined sales price taking into account the sales mix
average_sales_price = (salesprice_basic * 0.6) + (salesprice_custom * 0.4)

# Calculate the total sales for next month
sales_USD = average_sales_price * forecast_units

# Print the total sales
print("Next month's forecast sales figure is {:.2f} USD.".format(sales_USD))
```
This summary encapsulates the key learning points from your last lesson, helping you to recall the essential concepts and calculations.

