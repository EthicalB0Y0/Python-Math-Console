import os
import math

def print_header():
    print("\t+=================================================================+")
    print("\t\t\tWelcome to the Basic Calculator Program")
    print("\t+=================================================================+")

print_header()

s = input("\n\t\t\tType 'y' if you want to see the menu: ")

if s == 'y':
    os.system('clear')
else:
    print("Invalid choice. Exiting the calc.")
    exit()

history = []

while s == 'y':
    print_header()
    print("\n\t\t\tOperations You Can Perform")
    print("\t\t\t1. Addition")
    print("\t\t\t2. Subtraction")
    print("\t\t\t3. Multiplication")
    print("\t\t\t4. Division")
    print("\t\t\t5. Cubes")
    print("\t\t\t6. Squares")
    print("\t\t\t7. Square root")
    print("\t\t\t8. Exponents")
    print("\t\t\t9. History")
    print("\t\t\t10. Exit")

    choice = input("\t\t\tEnter the number of operation (1-10): ")

    if choice == '9':
        if not history:
            print("\t\t\tNo past calculations to show")
        else:
            print("\t\t\tCalculation History:")
            for entry in history:
                print(entry)
        continue

    num1 = float(input("\t\t\tEnter the first number: "))
    num2 = float(input("\t\t\tEnter the second number: "))

    def add(x, y):
        result = x + y
        print(f"\n\tSum Result: {result}")
        history.append(f"\t\t\tAddition: {num1} + {num2} = {result}")

    def subtract(x, y):
        result = x - y
        print(f"\n\tSubtraction Result: {result}")
        history.append(f"\t\t\tSubtraction: {num1} - {num2} = {result}")

    def multiply(x, y):
        result = x * y
        print(f"\n\tMultiplication Result: {result}")
        history.append(f"\t\t\tMultiplication: {num1} * {num2} = {result}")

    def divide(x, y):
        if y == 0:
            print("\n\tError: Cannot divide by zero")
        else:
            result = x / y
            print(f"\n\tDivision Result: {result}")
            history.append(f"\t\t\tDivision: {num1} / {num2} = {result}")

    def cube(x, y):
        cube_x = x ** 3
        cube_y = y ** 3
        print(f"\n\tThe cube of {num1} is: {cube_x}")
        print(f"\tThe cube of {num2} is: {cube_y}")
        history.append(f"\t\t\tCubes: {num1}^3 = {cube_x}, {num2}^3 = {cube_y}")

    def square(x, y):
        square_x = x ** 2
        square_y = y ** 2
        print(f"\n\tThe square of {num1} is: {square_x}")
        print(f"\tThe square of {num2} is: {square_y}")
        history.append(f"\t\t\tSquares: {num1}^2 = {square_x}, {num2}^2 = {square_y}")

    def square_root(x, y):
        sqrt_x = math.sqrt(x)
        sqrt_y = math.sqrt(y)
        print(f"\n\tThe square root of {num1} is: {sqrt_x}")
        print(f"\tThe square root of {num2} is: {sqrt_y}")
        history.append(f"\t\t\tSquare Root: sqrt({num1}) = {sqrt_x}, sqrt({num2}) = {sqrt_y}")

    def exponentiate(x, y):
        result = x ** y
        print(f"\n\t{num1} raised to the power of {num2} is: {result}")
        history.append(f"\t\t\tExponentiate: {num1}^{num2} = {result}")

    if choice == '1':
        add(num1, num2)
    elif choice == '2':
        subtract(num1, num2)
    elif choice == '3':
        multiply(num1, num2)
    elif choice == '4':
        divide(num1, num2)
    elif choice == '5':
        cube(num1, num2)
    elif choice == '6':
        square(num1, num2)
    elif choice == '7':
        square_root(num1, num2)
    elif choice == '8':
        exponentiate(num1, num2)
    elif choice == '10':
        print("\n\tExiting the calculator. Thank you for using it!")
        break
    else:
        print("\n\tInvalid choice. Please enter a number between 1 and 10.")
    
    s = input("\n\tDo you want to perform another operation? Type 'y' for yes: ")
    
    if s == 'y':
        os.system('clear')
    
    if s != 'y':
        print("\n\tExiting the calculator. Thank you for using it!")
        break

