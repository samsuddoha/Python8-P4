# Take inputs from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

# Perform the operation based on the operator
if operator == '+':
    result = num1 + num2
    print(f"Sum of {num1} and {num2} is: {result}")
elif operator == '-':
    result = num1 - num2
    print(f"Difference of {num1} and {num2} is: {result}")
elif operator == '*':
    result = num1 * num2
    print(f"Product of {num1} and {num2} is: {result}")
elif operator == '/':
    # Check if the second number is zero to avoid division by zero
    if num2 != 0:
        result = num1 / num2
        print(f"Division of {num1} by {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator! Please enter one of +, -, *, /")
