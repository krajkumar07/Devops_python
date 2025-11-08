student_grades = {}

while True:
    print("\nOptions: 1. Add/Update Student Grade  2. Print All Grades  3. Exit")
    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        name = input("Enter student name: ")
        grade = input("Enter grade: ").upper()

        # Add or update student grade
        student_grades[name] = grade
        print(f"Added/Updated grade for {name}: {grade}")

    elif choice == '2':
        if len(student_grades) == 0:
            print("No student grades available.")
        else:
            print("\nStudent Grades:")
            for student, grade in student_grades.items():
                print(f"{student}: {grade}")

    elif choice == '3':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
