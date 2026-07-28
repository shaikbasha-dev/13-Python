"""
===============================================================================
                              If Statement
===============================================================================

Program Description:
--------------------
This program demonstrates the use of the if statement in Python.

The if statement is used to execute a block of code only when a given
condition is True.

Syntax:

if condition:
    statements

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 38-If-Statement.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Accepting a number from the user.
# -----------------------------------------------------------------------------
number = int(input("Enter a Number: "))
# The entered value is converted into an integer.

# -----------------------------------------------------------------------------
# Checking whether the number is greater than zero.
# -----------------------------------------------------------------------------
if number > 0:
    # This block executes only if the condition is True.
    print("The Number is Positive.")
    # Output (Example):
    # Enter a Number: 15
    # The Number is Positive.

# -----------------------------------------------------------------------------
# Displaying a message after the if statement.
# -----------------------------------------------------------------------------
print("Program Completed.")
# Output:
# Program Completed.
