def calculator():

    print("Welcome to the Python Calculator!")
    print("Type 'exit' at any time to quit.")

    while True:
        # 1. User Input for operation
        operation = input("Enter an operation (+, -, *, /): ").lower().strip()

        if operation == "exit":
            print("Exiting calculator. Goodbye!")
            break

        # 4. Error Handling for invalid operation
        if operation not in ["+", "-", "*", "/"]:
            print("Invalid operation. Please enter +, -, *, or /.")
            continue

        try:
            # 1. User Input for numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

        except ValueError:
            # 4. Error Handling for non-numeric input
            print("Invalid input. Please enter valid numbers.")
            continue

        # 2. Conditional Logic to perform the correct calculation
        # 3. Perform Calculation inside each conditional block
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            # 4. Error Handling for division by zero
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
        
        # 5. Output the result
        print(f"Result: {num1} {operation} {num2} = {result}")
        print("-" * 20) # Separator for readability

# Run the calculator program
calculator()
