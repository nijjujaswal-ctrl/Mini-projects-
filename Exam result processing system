def calculate_grade(percentage):
    """Module-style grading logic."""
    if percentage >= 90: return 'A+'
    elif percentage >= 80: return 'A'
    elif percentage >= 70: return 'B'
    elif percentage >= 60: return 'C'
    else: return 'D'

class ExamSystem:
    def __init__(self):
        self.records = []  # List to maintain records

    def add_student(self, name, roll_no, marks_dict):
        student_details = (name, roll_no)
        total = sum(marks_dict.values())
        percentage = total / len(marks_dict) if marks_dict else 0
        grade = calculate_grade(percentage)

        record = {
            "details": student_details,
            "marks": marks_dict,
            "total": total,
            "grade": grade
        }
        self.records.append(record)

    def save_results(self, filename="exam_results.txt"):
        try:
            with open(filename, "w") as f:
                for r in self.records:
                    name, roll = r['details']
                    f.write(f"Roll: {roll} | Name: {name} | Total: {r['total']} | Grade: {r['grade']}\n")
            print(f"\n[v] Results saved to {filename}")
        except IOError as e:
            print(f"\n[x] File Error: {e}")

    def generate_rank_list(self):
        if not self.records:
            print("\nNo records found.")
            return
        ranked = sorted(self.records, key=lambda x: x['total'], reverse=True)
        print("\n--- RANK LIST ---")
        for i, r in enumerate(ranked, 1):
            name, roll = r['details']
            print(f"{i}. {name} (Roll: {roll}) - Total: {r['total']}")

    def show_grade_report(self):
        if not self.records:
            print("\nNo records found.")
            return
        print("\n--- GRADE REPORT ---")
        for r in self.records:
            name, _ = r['details']
            print(f"Student: {name.ljust(15)} | Grade: {r['grade']}")

system = ExamSystem()

while True:
    print("\n==== EXAM RESULT SYSTEM ====")
    print("1. Add Student & Marks")
    print("2. View Rank List")
    print("3. View Grade Report")
    print("4. Save to File")
    print("5. Exit")

    choice = input("Select Option: ").strip()

    if choice == '1':
        name = input("Enter Student Name: ")
        roll = input("Enter Roll Number: ")
        subjects = ["Math", "Science", "English"]
        marks_dict = {}
        try:
            for sub in subjects:
                marks = int(input(f"Enter marks for {sub}: "))
                marks_dict[sub] = marks
            system.add_student(name, roll, marks_dict)
            print("Student record added.")
        except ValueError:
            print("Error: Please enter numeric marks.")

    elif choice == '2':
        system.generate_rank_list()

    elif choice == '3':
        system.show_grade_report()

    elif choice == '4':
        system.save_results()

    elif choice == '5':
        print("Exiting system.")
        break
    else:
        print("Invalid choice. Try again.")
