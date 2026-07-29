"""
===============================================================================
File Name    : 138-Exception-Handling.py
Description  : Exception Handling in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Exception Handling is the process of handling runtime errors so that a program
does not terminate unexpectedly.

Python provides the following keywords for exception handling:
- try
- except
- else
- finally
- raise

In this introductory example, only the try and except blocks are used.

Syntax:

try:
    # Code that may generate an exception
except ExceptionType:
    # Code to handle the exception

Example:
Handling division by zero.
"""

# -----------------------------------------------------------------------------
# Displaying the program title.
# -----------------------------------------------------------------------------
print("Exception Handling Example")

# -----------------------------------------------------------------------------
# Declaring two numbers.
# -----------------------------------------------------------------------------
number1 = 10
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
# Handling the ZeroDivisionError exception.
# -----------------------------------------------------------------------------
except ZeroDivisionError:

    # -------------------------------------------------------------------------
    # Displaying an error message.
    # -------------------------------------------------------------------------
    print("Error: Division by zero is not allowed.")

# -----------------------------------------------------------------------------
# Displaying the remaining program.
# -----------------------------------------------------------------------------
print("Program execution completed.")

# Output:
# Exception Handling Example
# Error: Division by zero is not allowed.
# Program execution completed.
