# Part 2: Multiplication and Division
"""
# Write a Python program to find the multiplication and division of two numbers.
# 
# Ask the user to input two numbers (num1 and num2). 
# Given those two numbers, multiply them together to find the output. 
# Also, divide num1/num2 to find the output.
"""
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

multiplication = num1 * num2
print("Multiplication:", num1, "*", num2, "=", multiplication)

if num2 != 0:
    division = num1 / num2
    print("Division:", num1, "/", num2, "=", division)
else:
    print("Division: Cannot divide by zero!")