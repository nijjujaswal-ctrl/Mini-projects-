import pandas as pd

# Empty DataFrame
columns = ["Name", "Math", "Science", "English"]
df = pd.DataFrame(columns=columns)


# Grade Function
def calculate_grade(percentage):
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
    else:
        return "Fail"


# Add Student
def add_student():
    global df

    name = input("Enter Student Name: ")
    math = int(input("Math Marks: "))
    science = int(input("Science Marks: "))
    english = int(input("English Marks: "))

    new_data = pd.DataFrame({
        "Name": [name],
        "Math": [math],
        "Science": [science],
        "English": [english]
    })

    df = pd.concat([df, new_data], ignore_index=True)
    print("Student Added Successfully!\n")


# Analyze Marks
def analyze():
    global df

    if df.empty:
        print("No student data available.\n")
        return

    result = df.copy()

    result["Total"] = result[["Math", "Science", "English"]].sum(axis=1)
    result["Percentage"] = result["Total"] / 3
    result["Grade"] = result["Percentage"].apply(calculate_grade)

    print("\nStudent Report")
    print(result)

    topper = result.loc[result["Percentage"].idxmax()]
    print("\nTopper:", topper["Name"])
    print("Percentage:", round(topper["Percentage"], 2))

    print("\nClass Statistics")
    print("Average Percentage:", round(result["Percentage"].mean(), 2))
    print("Highest Percentage:", round(result["Percentage"].max(), 2))
    print("Lowest Percentage:", round(result["Percentage"].min(), 2))

    result.to_csv("student_report.csv", index=False)
    print("\nReport saved as student_report.csv\n")


# Display Students
def display():
    if df.empty:
        print("No Records Found.\n")
    else:
        print(df)
        print()


# Main Menu
while True:
    print("===== Student Marks Analyzer =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Analyze Marks")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display()

    elif choice == "3":
        analyze()

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!\n")
