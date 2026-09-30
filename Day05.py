def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number:"))
            operation = input("Enter the operation (+, -, *, /): ")
            break
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

    if operation == "+":
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}.")
    elif operation == "-":
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}.")
    elif operation == "*":
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}.")
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}.")
        else:
            print("Error! Division by zero is not allowed.")


calculator()
