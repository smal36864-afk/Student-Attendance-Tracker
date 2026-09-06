students = []
day_names = []
day_records = []


def add_student():
    name = input("Enter student name: ").strip().title()
    if name in students:
        print("Student already exists.")
    elif name == "":
        print("Name cannot be empty.")
    else:
        students.append(name)
        print(f"{name} added successfully.")


def mark_attendance():
    if not students:
        print("No students registered yet.")
        return
    day = input("Enter day label (e.g. Day1): ").strip()
    if day in day_names:
        print("Attendance for this day already recorded.")
        return
    print("Registered students:", ", ".join(students))
    present_input = input("Enter names present (comma separated): ")
    present = set()
    for name in present_input.split(","):
        cleaned = name.strip().title()
        if cleaned in students:
            present.add(cleaned)
    day_names.append(day)
    day_records.append(present)
    print(f"Attendance recorded for {day}. Present: {len(present)}")


def view_absentees():
    if not day_names:
        print("No attendance records available.")
        return
    day = input("Enter day label to check: ").strip()
    if day not in day_names:
        print("No record found for this day.")
        return
    index = day_names.index(day)
    present = day_records[index]
    absentees = set(students) - present
    print(f"Present on {day}: {', '.join(sorted(present)) if present else 'None'}")
    print(f"Absent on {day}: {', '.join(sorted(absentees)) if absentees else 'None'}")


def attendance_percentage():
    if not day_names:
        print("No attendance records available.")
        return
    total_days = len(day_names)
    print("\n----- ATTENDANCE PERCENTAGE -----")
    for student in students:
        present_count = 0
        for record in day_records:
            if student in record:
                present_count += 1
        percentage = (present_count / total_days) * 100
        print(f"{student:<15} {present_count}/{total_days} days  ->  {percentage:.2f}%")


def perfect_attendance():
    if not day_records:
        print("No attendance records available.")
        return
    all_present = set(students)
    for record in day_records:
        all_present = all_present & record
    if all_present:
        print("Present on all days:", ", ".join(sorted(all_present)))
    else:
        print("No student was present on all days.")


def menu():
    while True:
        print("\n===== STUDENT ATTENDANCE TRACKER =====")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Present/Absent for a Day")
        print("4. Attendance Percentage")
        print("5. Students Present on All Days")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            view_absentees()
        elif choice == "4":
            attendance_percentage()
        elif choice == "5":
            perfect_attendance()
        elif choice == "6":
            print("Exiting Student Attendance Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


menu()
