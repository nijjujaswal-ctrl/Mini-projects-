contacts = {}          #
phone_numbers = set()


def add_contact():
    name = input("Enter contact name: ")
    number = input("Enter phone number: ")

    if number in phone_numbers:
        print("Duplicate phone number! Contact not added.")
    else:
        contacts[name] = number
        phone_numbers.add(number)
        print("Contact added successfully.")


def search_contact():
    name = input("Enter contact name to search: ")

    if name in contacts:
        print(f"{name} : {contacts[name]}")
    else:
        print("Contact not found.")


def update_contact():
    name = input("Enter contact name to update: ")

    if name in contacts:
        new_number = input("Enter new phone number: ")

        if new_number in phone_numbers and new_number != contacts[name]:
            print("Duplicate phone number! Update failed.")
        else:
            old_number = contacts[name]
            phone_numbers.remove(old_number)

            contacts[name] = new_number
            phone_numbers.add(new_number)

            print("Contact updated successfully.")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter contact name to delete: ")

    if name in contacts:
        phone_numbers.remove(contacts[name])
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        search_contact()

    elif choice == "3":
        update_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        if contacts:
            print("\nContacts:")
            for name, number in contacts.items():
                print(f"{name} : {number}")
        else:
            print("No contacts available.")

    elif choice == "6":
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice. Please try again.")
