# Part 1: Addition and Subtraction
"""
# Write a Python program to find the addition and subtraction of two numbers.
#
# Ask the user to input two numbers (num1 and num2). 
# Given those two numbers, add them together to find the output. 
# Also, subtract the two numbers to find the output.
"""

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2

print("Addition:", num1, "+", num2, "=", addition)
print("Subtraction:", num1, "-", num2, "=", subtraction)
