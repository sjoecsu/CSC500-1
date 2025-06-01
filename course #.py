course_rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

course_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

course_times = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

while True:
    user_input = input("Enter a course number (e.g., CSC101): ").strip().upper()
    
    if user_input in course_rooms:
        print(f"\nCourse: {user_input}")
        print(f"Room Number: {course_rooms[user_input]}")
        print(f"Instructor: {course_instructors[user_input]}")
        print(f"Meeting Time: {course_times[user_input]}")
        break
    else:
        print(f"\nCourse number '{user_input}' not found. Please try again.")

input("\nPress Enter to exit...")
