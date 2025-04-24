food_charge = float(input("Enter the charge for your food: $"))

tip = food_charge * 0.18
sales_tax = food_charge * 0.07

total = food_charge + tip + sales_tax

print(f"Meal Charge: ${food_charge:.2f}")
print(f"Tip (18%): ${tip:.2f}")
print(f"Sales Tax (7%): ${sales_tax:.2f}")
print(f"Total Amount: ${total:.2f}")

input("\nPress Enter to exit the program...")