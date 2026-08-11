# Shopping Cart System

cart = []
categories = set()
item_prices = {}

def add_item():
    item = input("Enter item name: ")
    price = float(input("Enter item price: "))
    category = input("Enter item category: ")

    cart.append(item)
    item_prices[item] = price
    categories.add(category)

    print(f"{item} added to cart.")

def remove_item():
    item = input("Enter item name to remove: ")

    if item in cart:
        cart.remove(item)
        del item_prices[item]
        print(f"{item} removed from cart.")
    else:
        print("Item not found in cart.")

def display_cart():
    if not cart:
        print("Cart is empty.")
        return

    print("\n--- Shopping Cart ---")
    for item in cart:
        print(f"{item} - ₹{item_prices[item]}")

    print("\nUnique Categories:")
    for category in categories:
        print(category)

def calculate_bill():
    total = sum(item_prices.values())
    print(f"\nTotal Bill = ₹{total:.2f}")

while True:
    print("\n----SHOPPING CART SYSTEM ----")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Display Cart")
    print("4. Calculate Total Bill")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_item()

    elif choice == "2":
        remove_item()

    elif choice == "3":
        display_cart()

    elif choice == "4":
        calculate_bill()

    elif choice == "5":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice. Try again.")
