# Financial periods and how to work with them

The goal is to understand how to analyze and interpret financial data across 
different periods.

* **TODO:** define financial periods and how they differ from calendar periods.
* **TODO:** describe how periods appear in raw datasets (e.g. column headers, TTM).
* **TODO:** explain how to align and iterate over periods in Python.

Example Code:
```python
# TODO: lesson code here
```

#### 1. Financial periods and how to work with them

In this chapter, we will go into more detail on financial periods and how to work with them. All forecasts are based on specific financial periods, so let's have a look.

#### 2. The financial year

A company works in a specific framework when it comes to reporting its numbers. This is called the financial year. It is important to have this structure in order to be able to compare years and companies. A financial year does not have to be the same as a calendar year, January to December, but can start and end at any month. For example, the financial year of Microsoft runs from the 1st of July to the 30th of June.

#### 3. Months and quarters

A financial year is broken up into months and quarters. Months are pretty explanatory and quarters are chunks of three months at a time. For example, the first quarter of a calendar year is January to March. However, even when companies have a different starting date to their financial year than 1 January, they almost always have their year start and end at one of the calendar quarters, so either 1 April until 31 March, 1 July until 30 June, or 1 October until 30 September.

#### 4. Abbreviations

In a financial statement or forecast, the months are usually represented by numbers, with the number 1 corresponding to January no matter when the financial year starts. They are not dependent on the financial year. For quarters, the abbreviations Q1, Q2, etc. are used, and these are based on the financial year. Taking the example of Microsoft again, their first quarter would be July until September. The year can either be abbreviated to two digits or the full four digits, depending on the length of time examined. The year is based on the financial year end, for example, Microsoft has a year-end of June; therefore the 2018 financial year would be from 1 July 2017 until 30 June 2018.
This summary encapsulates the key learning points from this lesson.

### Recap  

You learned about the importance of financial periods and how they are structured within a company's reporting framework. Financial periods are essential for accurate forecasting and comparison across different years and companies. Here are the key points you covered:

Financial Year: A company's financial year can start and end on any month, not necessarily January to December. For example, Microsoft's financial year runs from July 1 to June 30.
Quarters and Months: Financial years are divided into quarters (three-month periods) and months. Quarters are labeled as Q1, Q2, etc., based on the financial year.
Date Formatting: Months are represented by numbers (1 for January, 2 for February, etc.), and the year can be abbreviated to two or four digits.
You also practiced converting quarters into months and merging monthly data into quarterly totals:

Converting Quarters to Months:
```
quarters = [700, 650]
qrtlist = []
for qrt in quarters:
    month = round(qrt / 3, 2)
    qrtlist = qrtlist + [month, month, month]
print("The values per month for the first two quarters are {}.".format(qrtlist))
```
Merging Months into Quarters:
```
months = [100, 100, 150, 250, 300, 10, 20]
quarter = 0
quarters = []
index = 1
for sales in months:
    quarter += sales
    if index % 3 == 0 or index == len(months):
        quarters.append(quarter)
        quarter = 0
    index += 1
print("The quarter totals are Q1: {}, Q2: {}, Q3: {}".format(quarters[0], quarters[1], quarters[2]))
```

The goal of the next lesson is to deepen your understanding of managing and formatting dates for financial data analysis using Python's datetime library.


