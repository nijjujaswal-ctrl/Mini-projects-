# Student Result Management System

students = {
    "Nishant": 85,
    "Nijju": 92,
    "Babbu": 78,
    "Prince": 88,
    "Deepu": 95
}

grades = []

total_marks = sum(students.values())
average = total_marks / len(students)

topper = max(students, key=students.get)
top_marks = students[topper]

for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    elif marks >= 60:
        grade = "D"
    else:
        grade = "F"

    grades.append((name, grade))

print("Student Marks:")
for name, marks in students.items():
    print(f"{name}: {marks}")

print("\nAverage Marks:", average)

print(f"\nTopper: {topper} ({top_marks} marks)")

print("\nGrades:")
for name, grade in grades:
    print(f"{name}: Grade {grade}")

