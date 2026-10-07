import json
import os
FILE_NAME = "students.json"
# ==================== FILE HANDLING ====================

def load_students():
    """Load student data from JSON file."""
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return {}

    return {}


def save_students(students):
    """Save student data to JSON file."""
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)
    except IOError:
        print("Error: Unable to save student data.")


# ==================== VALIDATION ====================

def get_marks(subject):
    """Get valid marks between 0 and 100."""
    while True:
        try:
            marks = float(input(f"Enter marks for {subject}: "))

            if 0 <= marks <= 100:
                return marks

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def get_grade(percentage):
    """Calculate grade based on percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


# ==================== ADD STUDENT ====================

def add_student(students):
    print("\n" + "=" * 55)
    print("                 ADD STUDENT")
    print("=" * 55)

    student_id = input("Enter Student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if student_id in students:
        print("Student ID already exists.")
        return

    name = input("Enter Student Name: ").strip()
    age = input("Enter Age: ").strip()
    gender = input("Enter Gender: ").strip()
    course = input("Enter Course: ").strip()
    semester = input("Enter Semester: ").strip()
    email = input("Enter Email: ").strip()
    phone = input("Enter Phone Number: ").strip()

    print("\nEnter marks:")
    python = get_marks("Python")
    dbms = get_marks("DBMS")
    dsa = get_marks("Data Structures")
    mathematics = get_marks("Mathematics")
    computer_networks = get_marks("Computer Networks")

    total = python + dbms + dsa + mathematics + computer_networks
    percentage = total / 5
    grade = get_grade(percentage)

    students[student_id] = {
        "name": name,
        "age": age,
        "gender": gender,
        "course": course,
        "semester": semester,
        "email": email,
        "phone": phone,
        "marks": {
            "Python": python,
            "DBMS": dbms,
            "Data Structures": dsa,
            "Mathematics": mathematics,
            "Computer Networks": computer_networks
        },
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    save_students(students)

    print("\nStudent added successfully.")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")


# ==================== VIEW STUDENTS ====================

def view_students(students):
    print("\n" + "=" * 90)
    print("                         ALL STUDENTS")
    print("=" * 90)

    if not students:
        print("No student records found.")
        return

    print(
        f"{'ID':<10}"
        f"{'Name':<22}"
        f"{'Course':<15}"
        f"{'Semester':<10}"
        f"{'Percentage':<15}"
        f"{'Grade':<8}"
    )

    print("-" * 90)

    for student_id, student in students.items():
        print(
            f"{student_id:<10}"
            f"{student['name'][:20]:<22}"
            f"{student['course']:<15}"
            f"{student['semester']:<10}"
            f"{student['percentage']:.2f}%{'':<9}"
            f"{student['grade']:<8}"
        )

    print("-" * 90)


# ==================== VIEW STUDENT DETAILS ====================

def display_student(student_id, student):
    print("\n" + "=" * 55)
    print("                 STUDENT DETAILS")
    print("=" * 55)

    print(f"Student ID : {student_id}")
    print(f"Name       : {student['name']}")
    print(f"Age        : {student['age']}")
    print(f"Gender     : {student['gender']}")
    print(f"Course     : {student['course']}")
    print(f"Semester   : {student['semester']}")
    print(f"Email      : {student['email']}")
    print(f"Phone      : {student['phone']}")

    print("\nMarks")
    print("-" * 40)

    for subject, marks in student["marks"].items():
        print(f"{subject:<25}: {marks}")

    print("-" * 40)
    print(f"Total      : {student['total']:.2f}")
    print(f"Percentage : {student['percentage']:.2f}%")
    print(f"Grade      : {student['grade']}")


# ==================== SEARCH STUDENT ====================

def search_student(students):
    print("\n" + "=" * 55)
    print("                 SEARCH STUDENT")
    print("=" * 55)

    keyword = input("Enter Student ID or Name: ").strip().lower()

    found = False

    for student_id, student in students.items():

        if (
            keyword in student_id.lower()
            or keyword in student["name"].lower()
        ):
            display_student(student_id, student)
            found = True

    if not found:
        print("No matching student found.")


# ==================== UPDATE STUDENT ====================

def update_student(students):
    print("\n" + "=" * 55)
    print("                 UPDATE STUDENT")
    print("=" * 55)

    student_id = input("Enter Student ID: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]

    print("\nPress Enter to keep the current value.")

    name = input(f"Name [{student['name']}]: ").strip()
    age = input(f"Age [{student['age']}]: ").strip()
    gender = input(f"Gender [{student['gender']}]: ").strip()
    course = input(f"Course [{student['course']}]: ").strip()
    semester = input(f"Semester [{student['semester']}]: ").strip()
    email = input(f"Email [{student['email']}]: ").strip()
    phone = input(f"Phone [{student['phone']}]: ").strip()

    if name:
        student["name"] = name

    if age:
        student["age"] = age

    if gender:
        student["gender"] = gender

    if course:
        student["course"] = course

    if semester:
        student["semester"] = semester

    if email:
        student["email"] = email

    if phone:
        student["phone"] = phone

    save_students(students)

    print("\nStudent information updated successfully.")


# ==================== DELETE STUDENT ====================

def delete_student(students):
    print("\n" + "=" * 55)
    print("                 DELETE STUDENT")
    print("=" * 55)

    student_id = input("Enter Student ID: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]

    print(f"\nStudent: {student['name']}")

    confirm = input("Are you sure you want to delete? (Y/N): ").strip().upper()

    if confirm == "Y":
        del students[student_id]
        save_students(students)
        print("Student deleted successfully.")
    else:
        print("Deletion cancelled.")


# ==================== COURSE SEARCH ====================

def search_by_course(students):
    print("\n" + "=" * 55)
    print("                 SEARCH BY COURSE")
    print("=" * 55)

    course = input("Enter Course: ").strip().lower()

    found = False

    print("\nStudents enrolled in", course.upper())
    print("-" * 65)

    for student_id, student in students.items():

        if student["course"].lower() == course:

            print(
                f"ID: {student_id} | "
                f"Name: {student['name']} | "
                f"Semester: {student['semester']}"
            )

            found = True

    if not found:
        print("No students found for this course.")


# ==================== STATISTICS ====================

def statistics(students):
    print("\n" + "=" * 55)
    print("                 STUDENT STATISTICS")
    print("=" * 55)

    if not students:
        print("No student records available.")
        return

    total_students = len(students)

    percentages = [
        student["percentage"]
        for student in students.values()
    ]

    average = sum(percentages) / total_students

    highest_id = max(
        students,
        key=lambda x: students[x]["percentage"]
    )

    lowest_id = min(
        students,
        key=lambda x: students[x]["percentage"]
    )

    passed = sum(
        1 for student in students.values()
        if student["percentage"] >= 40
    )

    failed = total_students - passed

    print(f"Total Students : {total_students}")
    print(f"Average Score  : {average:.2f}%")
    print(f"Passed Students: {passed}")
    print(f"Failed Students: {failed}")

    print(
        f"\nHighest Score  : "
        f"{students[highest_id]['name']} "
        f"({students[highest_id]['percentage']:.2f}%)"
    )

    print(
        f"Lowest Score   : "
        f"{students[lowest_id]['name']} "
        f"({students[lowest_id]['percentage']:.2f}%)"
    )


# ==================== MAIN MENU ====================

def main():

    students = load_students()

    while True:

        print("\n")
        print("=" * 60)
        print("           STUDENT MANAGEMENT SYSTEM")
        print("=" * 60)

        print("1.  Add Student")
        print("2.  View All Students")
        print("3.  Search Student")
        print("4.  Update Student")
        print("5.  Delete Student")
        print("6.  Search Students by Course")
        print("7.  Student Statistics")
        print("8.  Exit")

        print("=" * 60)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            search_by_course(students)

        elif choice == "7":
            statistics(students)

        elif choice == "8":
            print("\nThank you for using Student Management System.")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 8.")


# ==================== START PROGRAM ====================

if __name__ == "__main__":
    main()