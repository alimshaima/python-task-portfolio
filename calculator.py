# Task 4: Basic Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /, %): ")

if operator == "+":
    result = num1 + num2
    print(f"{num1}+{num2}={result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1}-{num2}={result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1}*{num2}={result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1}/{num2}={result}")
    else:
        print("Error: Cannot be divided by Zero")
elif operator == "%":
    if num2 != 0:
        result = num1 % num2
        print(f"{num1}%{num2}={result}")
    else:
        print("Error: Cannot calculate modulo with Zero")
else:
    print("Invalid operator")
