
PIN = "1008"
balance = 1000

entered_pin = input("Enter your PIN: ")

if entered_pin == PIN:
    print("Login Successful!")

    while True:
        print("\n---- ATM MENU ----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print(f"Current Balance: ₹{balance}")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹"))
            balance += amount
            print(f"₹{amount} deposited successfully.")
            print(f"New Balance: ₹{balance}")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))

            if amount <= balance:
                balance -= amount
                print(f"₹{amount} withdrawn successfully.")
                print(f"Remaining Balance: ₹{balance}")
            else:
                print("Insufficient Balance!")

        elif choice == "4":
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Incorrect PIN. Access Denied!")
