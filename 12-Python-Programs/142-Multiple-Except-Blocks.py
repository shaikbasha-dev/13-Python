"""
===============================================================================
File Name    : 142-Multiple-Except-Blocks.py
Description  : Multiple Except Blocks in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Multiple Except Blocks are used to handle different types of exceptions
separately.

When an exception occurs, Python checks each except block in order. The first
matching except block handles the exception, and the remaining except blocks
are skipped.

Syntax:

try:
    # Code that may generate exceptions

except ExceptionType1:
    # Handle first exception

except ExceptionType2:
    # Handle second exception

Example:
Handling ZeroDivisionError and ValueError separately.
"""

# -----------------------------------------------------------------------------
# Displaying the program title.
# -----------------------------------------------------------------------------
print("Multiple Except Blocks Example")

# -----------------------------------------------------------------------------
# Writing the code that may generate exceptions.
# -----------------------------------------------------------------------------
try:

    # -------------------------------------------------------------------------
    # Declaring input values.
    # -------------------------------------------------------------------------
    number1 = 20
    number2 = 0

    # -------------------------------------------------------------------------
    # Performing division.
    # -------------------------------------------------------------------------
    result = number1 / number2

    # -------------------------------------------------------------------------
    # Converting a non-numeric string into an integer.
    # This statement is skipped because the previous statement raises an
    # exception first.
    # -------------------------------------------------------------------------
    value = int("Python")

    # -------------------------------------------------------------------------
    # Displaying the result.
    # -------------------------------------------------------------------------
    print("Result :", result)

# -----------------------------------------------------------------------------
# Handling ZeroDivisionError.
# -----------------------------------------------------------------------------
except ZeroDivisionError:

    # -------------------------------------------------------------------------
    # Displaying the error message.
    # -------------------------------------------------------------------------
    print("Error: Cannot divide a number by zero.")

# -----------------------------------------------------------------------------
# Handling ValueError.
# -----------------------------------------------------------------------------
except ValueError:

    # -------------------------------------------------------------------------
    # Displaying the error message.
    # -------------------------------------------------------------------------
    print("Error: Invalid value for integer conversion.")

# -----------------------------------------------------------------------------
# Displaying the remaining program.
# -----------------------------------------------------------------------------
print("Program execution completed.")

# Output:
# Multiple Except Blocks Example
# Error: Cannot divide a number by zero.
# Program execution completed.
