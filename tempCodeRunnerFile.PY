# Student Enrollment & Attendance System

students = {}      # rollno: {name, sec}
courses = {}       # course_id: course_name
enrollments = {}   # (rollno, course_id): {attendance, grade}

COURSE_LIMIT = 3

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    sec = input("Enter Section: ")
    students[roll] = {"name": name, "sec": sec}
    print("Student added successfully!")

def add_course():
    cid = input("Enter Course ID: ")
    cname = input("Enter Course Name: ")
    courses[cid] = cname
    print("Course added successfully!")

def enroll_student():
    roll = input("Enter Roll No: ")
    cid = input("Enter Course ID: ")

    count = sum(1 for (r, _) in enrollments if r == roll)
    if count >= COURSE_LIMIT:
        print("Course limit exceeded!")
        return

    enrollments[(roll, cid)] = {"attendance": 0, "grade": None}
    print("Student enrolled successfully!")

def mark_attendance():
    roll = input("Enter Roll No: ")
    cid = input("Enter Course ID: ")
    att = int(input("Enter Attendance %: "))
    enrollments[(roll, cid)]["attendance"] = att

    if att < 75:
        print("⚠ Student is a defaulter!")

def assign_grade():
    roll = input("Enter Roll No: ")
    cid = input("Enter Course ID: ")
    grade = input("Enter Grade: ")
    enrollments[(roll, cid)]["grade"] = grade
    print("Grade assigned!")

def student_report():
    roll = input("Enter Roll No: ")
    print("\nStudent Report")
    for (r, c), data in enrollments.items():
        if r == roll:
            print(f"Course: {courses[c]}, Attendance: {data['attendance']}%, Grade: {data['grade']}")

def course_report():
    cid = input("Enter Course ID: ")
    print("\nCourse Wise Report")
    for (r, c), data in enrollments.items():
        if c == cid:
            print(f"Roll No: {r}, Attendance: {data['attendance']}%, Grade: {data['grade']}")

while True:
    print("""
1. Add Student
2. Add Course
3. Enroll Student
4. Mark Attendance
5. Assign Grade
6. View Student Report
7. Course Wise Report
8. Exit
""")
    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        add_course()
    elif choice == "3":
        enroll_student()
    elif choice == "4":
        mark_attendance()
    elif choice == "5":
        assign_grade()
    elif choice == "6":
        student_report()
    elif choice == "7":
        course_report()
    elif choice == "8":
        print("Exiting system...")
        break
    else:
        print("Invalid choice!")
