"""
===============================================================================
File Name    : 148-Lambda-Function.py
Description  : Lambda Function in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A Lambda Function is a small anonymous function that can have any number
of arguments but only one expression.

The lambda keyword is used to create a function without defining it using
the def keyword.

Syntax:

lambda arguments : expression

Example:
Creating a lambda function to find the sum of two numbers.
"""

# -----------------------------------------------------------------------------
# Creating a lambda function to add two numbers.
# -----------------------------------------------------------------------------
addition = lambda number1, number2: number1 + number2

# -----------------------------------------------------------------------------
# Calling the lambda function.
# -----------------------------------------------------------------------------
result = addition(10, 20)

# -----------------------------------------------------------------------------
# Displaying the result.
# -----------------------------------------------------------------------------
print("Sum :", result)

# -----------------------------------------------------------------------------
# Creating a lambda function to find the square of a number.
# -----------------------------------------------------------------------------
square = lambda number: number * number

# -----------------------------------------------------------------------------
# Calling the lambda function.
# -----------------------------------------------------------------------------
result = square(5)

# -----------------------------------------------------------------------------
# Displaying the result.
# -----------------------------------------------------------------------------
print("Square :", result)

# -----------------------------------------------------------------------------
# Creating a lambda function to find the maximum of two numbers.
# -----------------------------------------------------------------------------
maximum = lambda number1, number2: number1 if number1 > number2 else number2

# -----------------------------------------------------------------------------
# Calling the lambda function.
# -----------------------------------------------------------------------------
result = maximum(25, 40)

# -----------------------------------------------------------------------------
# Displaying the result.
# -----------------------------------------------------------------------------
print("Maximum :", result)

# Output:
# Sum : 30
# Square : 25
# Maximum : 40
