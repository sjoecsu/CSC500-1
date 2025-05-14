books = int(input("Enter the number of books purchased this month: "))

if books < 2:
    points = 0
elif books < 4:
    points = 5
elif books < 6:
    points = 15
elif books < 8:
    points = 30
else:
    points = 60

print(f"\nBooks Purchased: {books}")
print(f"Points Awarded: {points}")

input("\nPress enter to exit.")
