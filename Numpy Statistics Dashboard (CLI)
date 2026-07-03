import numpy as np
from collections import Counter

# Function to find mode
def find_mode(data):
    count = Counter(data)
    max_count = max(count.values())
    mode = [k for k, v in count.items() if v == max_count]

    if max_count == 1:
        return "No Mode"
    return mode


# Function to display statistics
def statistics_dashboard(arr):
    print("\n========== NUMPY STATISTICS DASHBOARD ==========")

    print(f"Data                : {arr}")
    print(f"Mean                : {np.mean(arr):.2f}")
    print(f"Median              : {np.median(arr):.2f}")
    print(f"Mode                : {find_mode(arr)}")
    print(f"Minimum             : {np.min(arr)}")
    print(f"Maximum             : {np.max(arr)}")
    print(f"Sum                 : {np.sum(arr)}")
    print(f"Variance            : {np.var(arr):.2f}")
    print(f"Standard Deviation  : {np.std(arr):.2f}")

    print("\nPercentiles")
    print(f"25th Percentile     : {np.percentile(arr, 25):.2f}")
    print(f"50th Percentile     : {np.percentile(arr, 50):.2f}")
    print(f"75th Percentile     : {np.percentile(arr, 75):.2f}")

    print("===============================================\n")


# Main Program
while True:
    print("===== NumPy Statistics Dashboard =====")
    print("1. Enter Data")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            numbers = list(map(float, input("\nEnter numbers separated by space: ").split()))

            if len(numbers) == 0:
                print("No data entered!\n")
                continue

            arr = np.array(numbers)

            statistics_dashboard(arr)

        except ValueError:
            print("Invalid Input! Please enter only numbers.\n")

    elif choice == "2":
        print("Thank you for using NumPy Statistics Dashboard!")
        break

    else:
        print("Invalid Choice! Try Again.\n")
