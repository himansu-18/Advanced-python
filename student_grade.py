students = {}

try:
    n = int(input("Enter number of students: "))
except ValueError:
    print("Invalid input! Please enter a number.")
    exit()

for i in range(n):
    try:
        name = input("Enter student name: ")
        id = input("Enter student ID: ")

        marks_p = int(input("Enter marks in Physics: "))
        marks_c = int(input("Enter marks in Chemistry: "))
        marks_m = int(input("Enter marks in Mathematics: "))

        total_marks = marks_p + marks_c + marks_m
        avg = total_marks / 3

        students[name] = {
            "id": id,
            "total_marks": total_marks,
            "avg": avg
        }

    except ValueError:
        print("Invalid marks entered! Please enter numbers only.")
        continue

print("\nStudent Grades:")
for n, d in students.items():
    try:
        print(f"Name: {n}, ID: {d['id']}, Total Marks: {d['total_marks']}, Average: {d['avg']:.2f}")
    except KeyError:
        print("Error displaying student data.")