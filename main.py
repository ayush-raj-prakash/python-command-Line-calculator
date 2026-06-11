while True:
    try:
        num1 = float(input("Enter the first number (or 'q' to quit): "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        continue

    op = input("Enter the operator (+, -, *, /, //, %, **): ")

    if (op in ('/', '//', '%')) and num2 == 0:
        print("Error! Denominator cannot be zero.")
    elif op == '+':
        print(num1 + num2)
    elif op == '-':
        print(num1 - num2)
    elif op == '*':
        print(num1 * num2)
    elif op == '/':
        print(num1 / num2)
    elif op == '//':
        print(num1 // num2)
    elif op == '%':
        print(num1 % num2)
    elif op == '**':
        print(num1 ** num2)
    else:
        print("Invalid operator!")

    again = input("Calculate again? (y/n): ")
    if again.lower() != 'y':
        print("Goodbye!")
        break
