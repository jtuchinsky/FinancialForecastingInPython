# Balance Sheet Efficiency Ratios - Part 1

You started working with efficiency ratios derived from the balance sheet, which measure how effectively a company turns its assets and liabilities into sales and cash.

* **TODO:** define the first set of efficiency ratios covered (e.g. days sales outstanding, days inventory outstanding).
* **TODO:** give the formula for each ratio.
* **TODO:** explain how to interpret the ratios for forecasting.

#### 1. Balance sheet efficiency ratios - Part 1

We will now look at a few balance sheet efficiency ratios or ratios that will be able to tell us a little bit more about the financial health of the company and how well it is managed and use this information to guide the forecasting process.

#### 2. Debtors and creditors

A company creates a sale, but does not receive the cash straight away, creating an asset called "debtors" on their balance sheet, or a company buys something, but does not settle their obligation to pay straight away, meaning a liability is created, which is called "creditors", to whom they need to pay at a later date. Now, let us have a look at some ratios that specifically deal with these two concepts.

#### 3. The debtor days ratio

The debtor days ratio is the ratio that calculates and shows how many days, on average, it takes to receive a payment from our debtors. Depending on the industry and company, the general rule is the sooner, the better, or in the case of this ratio, the lower, the better! You can imagine if your salary was late, what a difficult position this would put you in and you would either need to go in debt or rely on your savings to fulfill your obligations. A company has the same reality. But this can be managed as well, and good companies are able to manage their debtors without ending up in a bad cash flow situation. So how do we calculate the debtor days ratio? The formula is as follows: ending balance of debtors divided by sales.

$$\text{Debtor Days} = \left( \frac{\text{Ending Balance Debtors}}{\text{Sales}} \right) \times \text{Days in Financial Year}$$

The result is multiplied by the number of days in the financial year; usually, 365 days is used. We will become more familiar with this ratio in the exercises.

#### 4. Days payable outstanding (DPO ratio)

The days payable outstanding, or DPO, ratio, has to do, you might have guessed, with accounts payable, or creditors, a liabilities account. This result is similar to the debtor day ratio, except that it calculates the number of days on average it takes to pay our creditors. For the DPO, the longer the payment period, the better; however, the obligation is only deferred, so it will have to be paid sometime. This gives a company time to make more sales and be in a better position to pay their debt, and thus improve their cash flow position. The formula is: the closing balance creditors divided by the total cost of goods sold multiplied by the number of days in the financial year. 

$$\text{DPO} = \left( \frac{\text{Ending Balance Creditors}}{\text{Total Cost of Goods Sold}} \right) \times \text{Days in Financial Year}$$

Remember, for both this ratio and also the debtor days ratio, the results are best compared per industry and specific company, and not looked at in isolation. These ratios can give great insights on a company and its operations and also provide guidance for forecasting.

### Key Takeaways

You learned about balance sheet efficiency ratios, which help evaluate a 
company's financial health and management efficiency. These ratios are crucial for forecasting and understanding how well a company handles its receivables and payables.

- **Debtor Days Ratio:** This ratio calculates the average number of days it 
takes to receive payment from debtors. A lower ratio is generally better, indicating quicker payment collection.

**Formula:**
  $$\text{Debtor Days} = \frac{\text{Ending Balance of Debtors}}{\text{Sales}} \times \text{Days in Financial Year}$$

**Example:**
```python
debtors_end = 650
sales_tot = 12500
ddays_ratio = (debtors_end / sales_tot) * 365
print("The debtor days ratio is {}.".format(ddays_ratio))
```
- **Days Payable Outstanding (DPO):** This ratio measures the average number of 
days a company takes to pay its suppliers. A higher ratio can be beneficial for cash flow but must be managed carefully.

**Formula:**
  $$\text{DPO} = \frac{\text{Ending Balance of Creditors}}{\text{Total Cost of Goods Sold}} \times \text{Days in Financial Year}$$

**Example**:  
```
cogs_tot = 4000
creditors_end = 650
dpo = (creditors_end / cogs_tot) * 365
print("The days payable outstanding is {}.".format(dpo))
```
These ratios provide valuable insights into a company's operations and are best compared within the same industry.

The goal of the next lesson is to learn how to use financial ratios to forecast a company's future performance.




