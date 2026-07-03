import csv

FILE_NAME = "library.csv"

def add_book():
    book = input("Enter book name to add: ")

    with (openFILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([book])

    print("Book added successfully!")

def remove_book():
    book = input("Enter book name to remove: ")

    try:
        with open(FILE_NAME, "r", newline="") as file:
            books = list(csv.reader(file))

        found = False
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)

            for row in books:
                if row and row[0].lower() != book.lower():
                    writer.writerow(row)
                else:
                    found = True

        if found:
            print("Book removed successfully!")
        else:
            print("Book not found!")

    except FileNotFoundError:
        print("Library file not found!")

def search_book():
    book = input("Enter book name to search: ")

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if row and row[0].lower() == book.lower():
                    print("Book found!")
                    return

            print("Book not found!")

    except FileNotFoundError:
        print("Library file not found!")

def display_books():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)

            print("\nAvailable Books:")
            for row in reader:
                if row:
                    print("-", row[0])

    except FileNotFoundError:
        print("Library file not found!")

# Main Menu
while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        display_books()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
