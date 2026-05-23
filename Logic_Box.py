# Keep showing the menu until the user chooses to exit
while True:
    print("Welcome to Pattern Generator and Number Analyzer!\n")

    # Display menu options
    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    # Get the user's choice
    choice = input("Enter your choice: ").strip()

    # Option 1: Generate a star pattern
    if choice == "1":
        # Ask for the number of rows
        rows = int(input("Enter the number of rows for the pattern: "))

        # Print the pattern row by row
        for i in range(1, rows + 1):
            for j in range(1, i + 1):
                print("* ", end="")
            print()  # Move to the next line

    # Option 2: Analyze numbers in a range
    elif choice == "2":
        # Get the starting and ending numbers
        first = int(input("Enter the start of the range: "))
        second = int(input("Enter the end of the range: "))

        total = 0  # Variable to store the sum

        # Check each number in the range
        for i in range(first, second + 1):
            # Determine if the number is even or odd
            parity = "Even" if i % 2 == 0 else "Odd"
            print(f"The number {i} is {parity}.")

            # Add the number to the total sum
            total += i

        # Display the final sum
        print(f"The sum of all numbers from {first} to {second} is: {total}")

    # Option 3: Exit the program
    elif choice == "3":
        print("Thank you for using this program. Goodbye!")
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
