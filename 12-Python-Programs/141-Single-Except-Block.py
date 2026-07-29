"""
===============================================================================
File Name    : 141-Single-Except-Block.py
Description  : Single Except Block in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A Single Except Block is used to handle one specific type of exception.

If the exception raised inside the try block matches the except block,
the exception is handled and the program continues executing normally.

Syntax:

try:
    # Code that may generate an exception
except ExceptionType:
    # Code to handle the exception

Example:
Handling a ZeroDivisionError using a single except block.
"""

# -----------------------------------------------------------------------------
# Displaying the program title.
# -----------------------------------------------------------------------------
print("Single Except Block Example")

# -----------------------------------------------------------------------------
# Declaring two numbers.
# -----------------------------------------------------------------------------
number1 = 20
number2 = 0

# -----------------------------------------------------------------------------
# Writing the code that may generate an exception.
# -----------------------------------------------------------------------------
try:

    # -------------------------------------------------------------------------
    # Performing division.
    # -------------------------------------------------------------------------
    result = number1 / number2

    # -------------------------------------------------------------------------
    # Displaying the result.
    # -------------------------------------------------------------------------
    print("Result :", result)

# -----------------------------------------------------------------------------
# Handling only the ZeroDivisionError exception.
# -----------------------------------------------------------------------------
except ZeroDivisionError:

    # -------------------------------------------------------------------------
    # Displaying an error message.
    # -------------------------------------------------------------------------
    print("Error: Cannot divide a number by zero.")

# -----------------------------------------------------------------------------
# Displaying the remaining program.
# -----------------------------------------------------------------------------
print("Program execution completed.")

# Output:
# Single Except Block Example
# Error: Cannot divide a number by zero.
# Program execution completed.
