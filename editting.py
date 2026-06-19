# Set of all students in class (at least 10 names)
all_students = {"Chukwuemeka", "Williams", "Anthony", "Emeka", "Tega", "Kemi", "Ngozi", "Samuel", "Tunde", "Yoshua", "Amara", "Obinna"}

# Sets for attendance
monday = {"Chukwuemeka", "Williams", "Anthony", "Tega", "Kemi", "Ngozi", "Tunde"}
Tuesday = {"Williams", "Anthony", "Emeka", "Tega", "Samuel", "Tunde", "Yoshua"}
Wednesday = {"Chukwuemeka", "Anthony", "Emeka", "Kemi", "Samuel", "Tunde", "Amara"}

# Who attended all 3 days
all_3_days = monday & Tuesday & Wednesday

# Who missed at least one day
missed_one = all_students - all_3_days

# Who only came once
only_monday = monday - Tuesday - Wednesday
only_tuesday = Tuesday - monday - Wednesday
only_wednesday = Wednesday - monday - Tuesday
only_once = only_monday | only_tuesday | only_wednesday

# Who never attended
never_attended = all_students - monday - Tuesday - Wednesday

print("=== Exercise 6: Class Attendance Tracker ===")
print(f"Total students: {len(all_students)}")
print(f"Attended all 3 days: {all_3_days}")
print(f"Missed at least one day: {missed_one}")
print(f"Only came once: {only_once}")
print(f"  - Only Monday: {only_monday}")
print(f"  - Only Tuesday: {only_tuesday}")
print(f"  - Only Wednesday: {only_wednesday}")
print(f"Never attended: {never_attended}")
print()