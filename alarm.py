current_time = int(input("\nWhat is the current hour (0-23)? "))
hours_to_wait = int(input("How many hours before the alarm goes off? "))

alarm_time = (current_time + hours_to_wait) % 24

print(f"Current Time: {current_time}:00")
print(f"Hours to Wait: {hours_to_wait}")
print(f"The alarm will go off at {alarm_time}:00 on a 24-hour clock.")

input("\nPress Enter to exit the program")