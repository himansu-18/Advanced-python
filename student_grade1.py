n = int(input("Enter number of students: "))

students = {}

class InvalidStudentIDException(Exception):
    pass



while True:
    print("1.Add Student")
    print("2.View Grades")
    print("3.Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        try:
            id = input("Enter student ID: ")
            if not id:
                raise InvalidStudentIDException("Student ID cannot be empty.")
        except InvalidStudentIDException as e:
            print(e)
            continue
        marks_p = int(input("Enter marks in Physics: "))
        marks_c = int(input("Enter marks in Chemistry: "))
        marks_m = int(input("Enter marks in Mathematics: "))
        total_marks = marks_p + marks_c + marks_m
        avg = total_marks / 3
        students[name] = {"id": id, "total_marks": total_marks, "avg": avg}
    elif choice == 2:
        print("\nStudent Grades:")
        for n, d in students.items():
            print(f"Name: {n}, ID: {d['id']}, Total Marks: {d['total_marks']}, Average: {d['avg']:.2f}")
    elif choice == 3:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")