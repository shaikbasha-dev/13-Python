"""
===============================================================================
File Name    : 150-Lambda-Subtraction.py
Description  : Lambda Function for Subtraction in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A Lambda Function is an anonymous function created using the lambda keyword.

This program demonstrates how to perform the subtraction of two numbers
using a lambda function.

Syntax:

lambda arguments : expression

Example:
Subtracting two numbers using a lambda function.
"""

# -----------------------------------------------------------------------------
# Creating a lambda function to subtract two numbers.
# -----------------------------------------------------------------------------
subtraction = lambda first_number, second_number: first_number - second_number

# -----------------------------------------------------------------------------
# Declaring two numbers.
# -----------------------------------------------------------------------------
number1 = 50
number2 = 20

# -----------------------------------------------------------------------------
# Calling the lambda function.
# -----------------------------------------------------------------------------
result = subtraction(number1, number2)

# -----------------------------------------------------------------------------
# Displaying the first input value.
# -----------------------------------------------------------------------------
print("First Number  :", number1)

# -----------------------------------------------------------------------------
# Displaying the second input value.
# -----------------------------------------------------------------------------
print("Second Number :", number2)

# -----------------------------------------------------------------------------
# Displaying the subtraction result.
# -----------------------------------------------------------------------------
print("Difference    :", result)

# Output:
# First Number  : 50
# Second Number : 20
# Difference    : 30
