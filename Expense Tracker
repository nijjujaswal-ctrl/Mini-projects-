# Expense Tracker using File Handling and Exception Handling

FILE_NAME = "expenses.txt"

def add_expense():
    try:
        category = input("Enter category (Food, Travel, Shopping, etc.): ")
        amount = float(input("Enter amount: "))

        with open(FILE_NAME, "a") as file:
            file.write(f"{category},{amount}\n")

        print("Expense added successfully!")

    except ValueError:
        print("Invalid amount! Please enter a numeric value.")

def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()

            if not data:
                print("No expenses recorded.")
                return

            print("\nExpenses:")
            for line in data:
                category, amount = line.strip().split(",")
                print(f"Category: {category}, Amount: ₹{amount}")

    except FileNotFoundError:
        print("Expense file not found!")

def summarize_expenses():
    try:
        summary = {}

        with open(FILE_NAME, "r") as file:
            for line in file:
                category, amount = line.strip().split(",")
                amount = float(amount)

                if category in summary:
                    summary[category] += amount
                else:
                    summary[category] = amount

        print("\nExpense Summary:")
        total = 0

        for category, amount in summary.items():
            print(f"{category}: ₹{amount}")
            total += amount

        print(f"\nTotal Expenses: ₹{total}")

    except FileNotFoundError:
        print("Expense file not found!")

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Expense Summary")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        summarize_expenses()

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter 1-4.")
