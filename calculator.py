# Simple Calculator Program with Intentional Bugs

# Display a welcome message
print("Welcome to the Simple Calculator!")
print("You can perform addition, subtraction, multiplication, and division.")

# Loop to allow multiple calculations
while True:
    # Display the operation menu
    print("\nSelect an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    # Get the user's choice
    choice = input("Enter your choice (1/2/3/4/5): ")

    # Selection: Check if the user wants to exit
    if choice == 5:
        print("Thank you for using the calculator. Goodbye!")
        break  # Exit the loop

    # Validate the user's choice
    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid choice! Please select a valid option.")
        continue  # Restart the loop

    # Get two numbers from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue  # Restart the loop

    # Perform the selected operation using arithmetic and variables
    if choice == "1":  # Addition
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}.")
    elif choice == "2":  # Subtraction
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}.")
    elif choice == "3":  # Multiplication
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}.")
    elif choice == "4":  # Division
        if num2 == "0":
            print("Error! Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}.")
    
    result = None


print("Program ended.") 