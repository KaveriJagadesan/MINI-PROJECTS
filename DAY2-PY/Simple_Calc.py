# Enter the first number and convert it to a float
num1 = float(input('Enter the first number: '))

#Enter the second number and convert it to a float
num2 = float(input('Enter the second number: '))

# The user to choose an operation
operator = input('Enter an operator (+, -, *, /): ')

# Use if/elif/else to perform the selected operation
if operator == '+':
    result = num1 + num2
    print(f'{num1} + {num2} = {result}')
elif operator == '-':
    result = num1 - num2
    print(f'{num1} - {num2} = {result}')
elif operator == '*':
    result = num1 * num2
    print(f'{num1} * {num2} = {result}')
elif operator == '/':
    # Check for division by zero to prevent an error
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f'{num1} / {num2} = {result}')
else:
    print('Invalid operator. Please enter +, -, *, or /.')

