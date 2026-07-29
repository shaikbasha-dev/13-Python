"""
===============================================================================
File Name    : 149-Lambda-Addition.py
Description  : Lambda Function for Addition in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A Lambda Function is an anonymous function created using the lambda keyword.

This program demonstrates how to perform the addition of two numbers
using a lambda function.

Syntax:

lambda arguments : expression

Example:
Adding two numbers using a lambda function.
"""

# -----------------------------------------------------------------------------
# Creating a lambda function to add two numbers.
# -----------------------------------------------------------------------------
addition = lambda first_number, second_number: first_number + second_number

# -----------------------------------------------------------------------------
# Declaring two numbers.
# -----------------------------------------------------------------------------
number1 = 25
number2 = 15

# -----------------------------------------------------------------------------
# Calling the lambda function.
# -----------------------------------------------------------------------------
result = addition(number1, number2)

# -----------------------------------------------------------------------------
# Displaying the input values.
# -----------------------------------------------------------------------------
print("First Number  :", number1)

# -----------------------------------------------------------------------------
# Displaying the second input value.
# -----------------------------------------------------------------------------
print("Second Number :", number2)

# -----------------------------------------------------------------------------
# Displaying the addition result.
# -----------------------------------------------------------------------------
print("Sum           :", result)

# Output:
# First Number  : 25
# Second Number : 15
# Sum           : 40
