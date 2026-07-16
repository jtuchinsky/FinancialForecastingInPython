# Introduction to Balance Sheets

You were introduced to the balance sheet, the financial statement that reports a company's assets, liabilities, and shareholders' equity at a point in time, and how it complements the income statement.

* **TODO:** define assets, liabilities, and equity and the accounting equation (Assets = Liabilities + Equity).
* **TODO:** describe the difference between current and non-current items.
* **TODO:** explain how the balance sheet links to the income statement for forecasting.


**Introduction to the balance sheet**  

You learned about the balance sheet, which is a crucial financial statement that provides a snapshot of a company's financial position at a specific point in time. The balance sheet is divided into three main components: assets, liabilities, and equity.

* Assets: Economic resources owned by a company that can generate future economic benefits. For example, cash, inventory, and accounts receivable.
* Liabilities: Obligations that the company must settle in the future, such as loans and accounts payable.
* Equity: The residual interest in the assets of the company after deducting liabilities. It is calculated as assets minus liabilities.

You also explored how to calculate accounts receivable and accounts payable, which are critical for managing cash flow.

**Key Points:**

* Accounts Receivable (Debtors): Sales made on credit recorded in the balance sheet.
* Accounts Payable (Creditors): Purchases made on credit recorded in the balance sheet.

**Example Code:**  

```
# Calculate accounts receivable
sales = [500, 350, 700]
debtors = [] 
credits = []
month = 0

for mvalue in sales: 
    credits.append(mvalue * 0.6)
    if month > 0:
        debtors.append(credits[month] + credits[month-1]) 
    else:
        debtors.append(credits[month])
    month += 1

print("The ‘Debtors’ are {}.".format(debtors))
```
We have gone through some exercises on accounts payable and receivable (creditors and debtors). Now we will test your understanding of these concepts.

T-Z is a successful company producing custom T-shirts. Their balance sheet for the past three months broken down by month looks as follows:

| Balance Sheet Item            | January | February | March |
|-------------------------------|---------|----------|-------|
| Accounts Receivables\Debtors  | 1000    | 750      | 750   |
| Accounts Payables\Creditors   | 300     | 600      | 900   |
| Bad Debts                     | 0       | 250      | 0     |


Choose the most likely analysis of these balances.

1. T-Z has a large debtors balance, but has received payment in February, the 
creditors have also been increasing each month, which could indicate a longer payback period.
2. <strong style="color:red">T-Z has not reduced their debtors' balance but has written off some bad debts in February, which needs monitoring. The creditors are increasing, which is good for cash flow.</strong>
3. T-Z has increased debtors, which is good for cash flow. However, the 
creditors and bad debts are growing, which could be a risk.

This summary encapsulates the key learning points from this lesson.