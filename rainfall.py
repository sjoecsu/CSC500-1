total_rainfall = 0.0
total_months = 0

years = int(input("Enter the number of years: "))

for year in range(1, years + 1):
    print(f"\nYear {year}")
    for month in range(1, 13):
        rainfall = float(input(f"  Enter rainfall for month {month} in inches: "))
        total_rainfall += rainfall
        total_months += 1

average_rainfall = total_rainfall / total_months

print("\nRainfall Report")
print(f"Total months: {total_months}")
print(f"Total rainfall: {total_rainfall:.2f} inches")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")

input("\nPress enter to exit.")
