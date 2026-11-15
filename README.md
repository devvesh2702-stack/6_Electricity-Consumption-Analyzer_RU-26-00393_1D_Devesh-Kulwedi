# Electricity Consumption Analyzer - Project Report (PS 6)

Rungta International Skills University | School of Computer Science and Engineering | B.Tech CSE, First Semester

**Name:** Devesh Kulwedi
**Section:** 1-D (SA-04)
**ERP No.:** RU-26-00393

## 1. Problem Statement

In this project I made a Python program that reads a CSV file of monthly electricity usage and tells us useful things about it, like the total units used, the average, and which months used the most and the least. Most of us never really look at our monthly readings, so it is hard to know which months push the bill up.

The CSV file has two columns, Month and Units. I used NumPy and Pandas to do the calculations and Matplotlib to draw charts, so the trend is easy to see. If a row has wrong data (like text instead of a number, or a negative number), the program says which row it skipped and carries on instead of crashing.

## 2. Objectives

The problem sheet gives six minimum requirements, so these were my goals:

1. Write everything in one Python 3 file (`electricity_analyzer.py`) that runs from the console.
2. Load the CSV file with Pandas and remove wrong or missing readings.
3. Use NumPy to find the total, mean, maximum, minimum and standard deviation.
4. Find the highest, lowest and above-average months using boolean filtering.
5. Draw at least two Matplotlib charts (a bar chart and a line chart) with a title and labels.
6. Make sure all four given test cases give the right output.

## 3. Tools and Technologies

I wrote the program in Python 3 and used three libraries. This is what I used each one for:

| Tool | What I used it for |
| --- | --- |
| Python 3 | The main program, the menu, loops and checking the input |
| Pandas | Reading the CSV file, cleaning the rows and picking out the above-average months |
| NumPy | Total, mean, maximum, minimum and standard deviation |
| Matplotlib | The bar chart and the line chart |

## 4. Approach and Logic

The program works in these steps:

1. **Read the file.** The file name is written at the top of the program (`filename = "usage.csv"`). I read both columns as plain text first, so a bad value like `abc` does not cause an error while loading. If the file cannot be read, the program prints a message and stops.
2. **Skip the header.** If the first row is `Month,Units`, it is removed. The sample files in the problem sheet have no header, so the program works with both.
3. **Check each row with a loop.** Rows are counted from 1. A row is skipped (with a message) if the month or units are empty, if the units are not a number, or if the units are negative. Good rows are added to two lists, one for months and one for units, and then made into a Pandas table. If any row was skipped, the program also prints how many valid rows are left and their total.
4. **Calculate.** NumPy finds the total, mean, maximum, minimum and standard deviation of the units. The month names for the highest and lowest come from the position of those values in the table.
5. **Find above-average months.** A boolean condition, `Units > average`, picks the months that used more than the average.
6. **Show the menu in a loop.** Option 1 prints the summary, option 2 prints the above-average months and draws the bar chart and the line chart, and option 3 exits. If someone types anything else, it says the choice is wrong and shows the menu again.

One thing I had to be careful about was the standard deviation. The problem sheet says to use the population value (the default of `np.std`), so it divides by n. That is why a single row gives 0.00.

## 5. Implementation

All the code is in one file, `electricity_analyzer.py`. It runs from top to bottom like a normal script: first it reads and cleans the data, then it calculates the statistics, and at the end it shows the menu. I used only two functions for the menu options and one small helper function.

| Part of the code | What it does |
| --- | --- |
| `show_number(x)` | Prints whole numbers like 300 without decimals, and other numbers with two decimals |
| Reading and cleaning (top of the program) | Reads the CSV with Pandas, loops over the rows, skips wrong rows with a message and keeps the good ones |
| Statistics (middle of the program) | Uses NumPy to get the total, mean, maximum, minimum and standard deviation, and finds the highest and lowest months |
| `show_summary()` | Prints the three summary lines (menu option 1) |
| `show_above_average()` | Filters the months above the average, prints them and draws the bar chart and the line chart (menu option 2) |
| Menu loop (end of the program) | A `while True` loop that shows the menu and calls the right function until the user chooses Exit |

I made two small choices. First, the file name is kept in one variable at the top, so it can be changed in one place. Second, when a CSV has bad rows, the program prints `Valid rows: N | Total: X units` right after the skip messages, because Test Case 3 expects it.

## 6. Test Cases and Results

I ran all four test cases from the problem sheet, and the output matched the expected output every time. The screenshots are in the `Testcases` folder.

| Test case | Input (usage.csv, menu option) | Expected output | Actual output | Result |
| --- | --- | --- | --- | --- |
| 1. Normal input | Jan,200 / Feb,250 / Mar,300; option 1 | Total: 750 units, Average: 250.00; Highest: Mar (300), Lowest: Jan (200); Std Dev: 40.82 | Same as expected | Pass |
| 2. Boundary (one row) | Jan,150; option 1 | Total: 150 units, Average: 150.00; Highest: Jan (150), Lowest: Jan (150); Std Dev: 0.00 | Same as expected | Pass |
| 3. Invalid input | Jan,200 / Feb,abc / Mar,-30; option 1 | Row 2 skipped: invalid Units 'abc'. Row 3 skipped: Units cannot be negative. Valid rows: 1, Total: 200 units | Same as expected | Pass |
| 4. Different valid scenario | Same file as test 1; option 2 | Months above average (250.00): Mar (300); bar chart 'Monthly Consumption' displayed | Same as expected; the bar chart and the line chart open in windows | Pass |

I also checked Test Case 1 by hand. The mean is 250, the squared differences are 2500, 0 and 2500, so their average is 1666.67, and the square root of that is 40.82. This matches what the program prints.

## 7. Conclusion and Future Scope

In this project I built a program that finds the total, average, highest, lowest and above-average months from a CSV file and shows the trend in charts. It meets all the minimum requirements and passes all four test cases. Through it I learned how Pandas, NumPy and Matplotlib can work together: Pandas loads and cleans the data, NumPy does the calculations and Matplotlib shows the result. I also saw why handling wrong input matters, because the program keeps running and tells the user which rows it skipped.

Some things I could add in the future:

- A cost estimate, by multiplying the units by a price per unit.
- Sorting the months in calendar order and handling more than twelve months.
- A year column, so two years can be compared.
- Saving the summary to a text or Excel file.
- A simple window with buttons instead of the console menu.

## How to Run

1. Install Python 3 and the three libraries:

   ```
   pip install pandas numpy matplotlib
   ```

2. Keep `electricity_analyzer.py` and `usage.csv` in the same folder.
3. Open the terminal in that folder and run:

   ```
   python electricity_analyzer.py
   ```

4. Choose an option from the menu:

   ```
   1. Summary
   2. Above-average months and chart
   3. Exit
   ```

The CSV file has two columns, Month and Units, and a header row is optional:

```
Jan,200
Feb,250
Mar,300
```

## Files

| File | Description |
| --- | --- |
| `electricity_analyzer.py` | The main program |
| `usage.csv` | Sample data (Test Case 1) |
| `README.md` | This report |
