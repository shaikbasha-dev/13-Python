"""
===============================================================================
                           If Else Statement
===============================================================================

Program Description:
--------------------
This program demonstrates the use of the if-else statement in Python.

The if-else statement is used to execute one block of code when the
condition is True and another block of code when the condition is False.

Syntax:

if condition:
    statements
else:
    statements

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 39-If-Else-Statement.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Accepting a number from the user.
# -----------------------------------------------------------------------------
number = int(input("Enter a Number: "))
# The entered value is converted into an integer.

# -----------------------------------------------------------------------------
# Checking whether the number is positive or not.
# -----------------------------------------------------------------------------
if number > 0:
    # This block executes if the condition is True.
    print("The Number is Positive.")
    # Output (Example 1):
    # Enter a Number: 25
    # The Number is Positive.
else:
    # This block executes if the condition is False.
    print("The Number is Zero or Negative.")
    # Output (Example 2):
    # Enter a Number: -10
    # The Number is Zero or Negative.

# -----------------------------------------------------------------------------
# Displaying a message after the if-else statement.
# -----------------------------------------------------------------------------
print("Program Completed.")
# Output:
# Program Completed.
