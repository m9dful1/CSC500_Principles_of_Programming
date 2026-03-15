"""Part 1:
Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. 
The program should first ask for the number of years. The outer loop will iterate once for each year. 
The inner loop will iterate twelve times, once for each month. 
Each iteration of the inner loop will ask the user for the inches of rainfall for that month. After all iterations, 
the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.
"""
"""
# ─────────────────────────────────────────
# Rainfall Calculator
# Collects monthly rainfall data over a
# period of years and reports statistics.
# ─────────────────────────────────────────
"""

MONTHS = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

while True:
    num_years = int(input("Enter the number of years: "))
    if num_years > 0:
        break
    print("Please enter a positive number of years.")

total_rainfall = 0.0
total_months = num_years * 12

for year in range(1, num_years + 1):          # Outer loop: each year
    for month in range(12):                   # Inner loop: each month
        while True:
            rainfall = float(input(f"  Year {year}, {MONTHS[month]} - Enter rainfall (inches): "))
            if rainfall >= 0:
                break
            print("  Rainfall cannot be negative. Try again.")
        total_rainfall += rainfall

average_rainfall = total_rainfall / total_months

print("\n--- Rainfall Summary ---")
print(f"Number of months  : {total_months}")
print(f"Total rainfall    : {total_rainfall:.2f} inches")
print(f"Average per month : {average_rainfall:.2f} inches")

"""
**Sample output** (2 years, entering 1.0 for every month):

--- Rainfall Summary ---
Number of months  : 24
Total rainfall    : 24.00 inches
Average per month : 1.00 inches
"""