def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    # Check if the operation is valid
    if operation not in ['+', '-', '*', '/']:
        print("Invalid operation. Please try again.")
        return

    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    if operation == '+':
        print(f'{number1} + {number2} = {number1 + number2}')
    elif operation == '-':
        print(f'{number1} - {number2} = {number1 - number2}')
    elif operation == '*':
        print(f'{number1} * {number2} = {number1 * number2}')
    elif operation == '/':
        if number2 == 0:
            print("Division by zero is not allowed")
        else:
            print(f'{number1} / {number2} = {number1 / number2}')

# Run the calculator
calculate()