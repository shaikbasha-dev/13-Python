"""
===============================================================================
                 Basic Calculator Using User Input
===============================================================================

Program Description:
--------------------
This program demonstrates a basic calculator using user input.

The user enters two numbers, and the program performs basic arithmetic
operations such as addition, subtraction, multiplication, division,
modulus, floor division, and exponentiation.

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 54-Basic-Calculator-Using-User-Input.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Reading the first number from the user.
# -----------------------------------------------------------------------------
number1 = float(input("Enter the First Number: "))
# Example Input: 20

# -----------------------------------------------------------------------------
# Reading the second number from the user.
# -----------------------------------------------------------------------------
number2 = float(input("Enter the Second Number: "))
# Example Input: 5

# -----------------------------------------------------------------------------
# Displaying the entered values.
# -----------------------------------------------------------------------------
print("First Number  :", number1)
print("Second Number :", number2)
# Example Output:
# First Number  : 20.0
# Second Number : 5.0

# -----------------------------------------------------------------------------
# Performing addition.
# -----------------------------------------------------------------------------
print("Addition        :", number1 + number2)
# Example Output: Addition        : 25.0

# -----------------------------------------------------------------------------
# Performing subtraction.
# -----------------------------------------------------------------------------
print("Subtraction     :", number1 - number2)
# Example Output: Subtraction     : 15.0

# -----------------------------------------------------------------------------
# Performing multiplication.
# -----------------------------------------------------------------------------
print("Multiplication  :", number1 * number2)
# Example Output: Multiplication  : 100.0

# -----------------------------------------------------------------------------
# Performing division.
# -----------------------------------------------------------------------------
print("Division        :", number1 / number2)
# Example Output: Division        : 4.0

# -----------------------------------------------------------------------------
# Performing modulus operation.
# -----------------------------------------------------------------------------
print("Modulus         :", number1 % number2)
# Example Output: Modulus         : 0.0

# -----------------------------------------------------------------------------
# Performing floor division.
# -----------------------------------------------------------------------------
print("Floor Division  :", number1 // number2)
# Example Output: Floor Division  : 4.0

# -----------------------------------------------------------------------------
# Performing exponentiation.
# -----------------------------------------------------------------------------
print("Exponentiation  :", number1 ** number2)
# Example Output: Exponentiation  : 3200000.0

# -----------------------------------------------------------------------------
# Displaying a completion message.
# -----------------------------------------------------------------------------
print("Program Completed.")
# Output:
# Program Completed.
