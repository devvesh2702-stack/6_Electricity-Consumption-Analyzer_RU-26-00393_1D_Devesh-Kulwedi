import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = "usage.csv"


def show_number(x):
    if x == int(x):
        return str(int(x))
    else:
        return f"{x:.2f}"


try:
    data = pd.read_csv(filename, header=None, names=["Month", "Units"], dtype=str)
except:
    print("Could not read the file", filename)
    exit()

if len(data) > 0 and data["Month"][0] == "Month":
    data = data.drop(0)
    data = data.reset_index(drop=True)

months = []
units = []
skipped = 0

for i in range(len(data)):
    row_number = i + 1
    month = data["Month"][i]
    value = data["Units"][i]

    if pd.isna(month) or pd.isna(value):
        print("Row", row_number, "skipped: missing data.")
        skipped = skipped + 1
        continue

    try:
        number = float(value)
    except:
        print(f"Row {row_number} skipped: invalid Units '{value}'.")
        skipped = skipped + 1
        continue

    if number < 0:
        print(f"Row {row_number} skipped: Units cannot be negative.")
        skipped = skipped + 1
        continue

    months.append(month.strip())
    units.append(number)

df = pd.DataFrame({"Month": months, "Units": units})

if len(df) == 0:
    print("No valid rows found.")
    exit()

total = np.sum(df["Units"])
average = np.mean(df["Units"])
highest = np.max(df["Units"])
lowest = np.min(df["Units"])
std_dev = np.std(df["Units"])

highest_month = df["Month"][df["Units"].idxmax()]
lowest_month = df["Month"][df["Units"].idxmin()]

if skipped > 0:
    print(f"Valid rows: {len(df)} | Total: {show_number(total)} units")


def show_summary():
    print(f"Total: {show_number(total)} units | Average: {average:.2f}")
    print(f"Highest: {highest_month} ({show_number(highest)}) | Lowest: {lowest_month} ({show_number(lowest)})")
    print(f"Std Dev: {std_dev:.2f}")


def show_above_average():
    above = df[df["Units"] > average]

    names = []
    for i in above.index:
        names.append(f"{above['Month'][i]} ({show_number(above['Units'][i])})")

    if len(names) == 0:
        result = "None"
    else:
        result = ", ".join(names)
    print(f"Months above average ({average:.2f}): {result}")

    plt.figure()
    plt.bar(df["Month"], df["Units"])
    plt.title("Monthly Consumption")
    plt.xlabel("Month")
    plt.ylabel("Units")
    plt.show()

    plt.figure()
    plt.plot(df["Month"], df["Units"], marker="o")
    plt.title("Consumption Trend")
    plt.xlabel("Month")
    plt.ylabel("Units")
    plt.show()

    print("Bar chart 'Monthly Consumption' displayed")


while True:
    print()
    print("1. Summary")
    print("2. Above-average months and chart")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        show_summary()
    elif choice == "2":
        show_above_average()
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Wrong choice, please enter 1, 2 or 3.")
