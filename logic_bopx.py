# Project: Logic Box
# Description: Pattern Generator and Number Analyzer
def display_welcome():
    """Display welcome message and program instructions."""
    print("\n" + "=" * 55)
    print("              WELCOME TO LOGIC BOX")
    print("=" * 55)
    print("Pattern Generator and Number Analyzer")
    print("\nFeatures:")
    print("1. Generate a Right-Angled Triangle")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    print("=" * 55)
# PATTERN GENERATOR
def pattern_generator():
    """Generate a right-angled triangle using nested loops."""

    print("\n--- PATTERN GENERATOR ---")
    print("Available Pattern: Right-Angled Triangle")

    # Input validation using while loop
    while True:
        try:
            rows = int(input("Enter the number of rows: "))

            if rows <= 0:
                print("Error: Number of rows must be greater than 0.")
                print("Pattern generation stopped.")
                
                # break is used as required in the project
                break

            # Generate pattern using nested loops
            print("\nGenerated Pattern:")

            for i in range(1, rows + 1):

                # Demonstrating break
                if i > rows:
                    break

                for j in range(1, i + 1):
                    print("*", end=" ")

                print()

            print("\nPattern generated successfully.")
            break

        except ValueError:
            print("Error: Please enter a valid integer.")
            continue
# NUMBER ANALYZER
def number_analyzer():
    """Analyze numbers within a user-defined range."""

    print("\n--- NUMBER ANALYZER ---")

    while True:
        try:
            start = int(input("Enter the start number: "))
            end = int(input("Enter the end number: "))

            # Validate range
            if end <= start:
                print("Error: End number must be greater than start number.")
                print("Please enter the values again.\n")
                continue

            break

        except ValueError:
            print("Error: Please enter valid integer values.")
            continue

    print("\nNumbers in the range:")
    print("-" * 40)

    total = 0

    print("\nOdd and Even Analysis:")

    # for loop with range()
    for number in range(start, end + 1):

        # Demonstrating continue
        # Zero is skipped without performing odd/even operation
        if number == 0:
            print("0 -> Skipped")
            continue

        # Demonstrating pass
        if number > 0:
            pass

        # Check odd or even
        if number % 2 == 0:
            print(number, "-> Even")
        else:
            print(number, "-> Odd")

        # Calculate sum
        total += number

    print("-" * 40)
    print("Sum of all numbers from", start, "to", end, "=", total)

# MENU

def display_menu():
    """Display the main menu."""

    print("\n" + "=" * 40)
    print("              MAIN MENU")
    print("=" * 40)
    print("1. Pattern Generation")
    print("2. Number Analysis")
    print("3. Exit")
    print("=" * 40)

# MAIN PROGRAM

def main():

    display_welcome()

    while True:

        display_menu()

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            pattern_generator()

        elif choice == "2":
            number_analyzer()

        elif choice == "3":
            print("\n" + "=" * 40)
            print("Thank you for using Logic Box!")
            print("Program ended successfully.")
            print("=" * 40)
            break

        else:
            print("\nInvalid choice!")
            print("Please select an option between 1 and 3.")
            continue


# PROGRAM START

if __name__ == "__main__":
    main()