"""
===============================================================================
                        If Elif Else Statement
===============================================================================

Program Description:
--------------------
This program demonstrates the use of the if-elif-else statement in Python.

The if-elif-else statement is used to check multiple conditions. Python
evaluates the conditions from top to bottom. As soon as one condition
becomes True, its corresponding block is executed, and the remaining
conditions are skipped.

Syntax:

if condition1:
    statements
elif condition2:
    statements
else:
    statements

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 40-If-Elif-Else-Statement.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Accepting a number from the user.
# -----------------------------------------------------------------------------
number = int(input("Enter a Number: "))
# The entered value is converted into an integer.

# -----------------------------------------------------------------------------
# Checking whether the number is positive, negative, or zero.
# -----------------------------------------------------------------------------
if number > 0:
    # This block executes if the number is greater than zero.
    print("The Number is Positive.")
    # Output (Example 1):
    # Enter a Number: 15
    # The Number is Positive.

elif number < 0:
    # This block executes if the number is less than zero.
    print("The Number is Negative.")
    # Output (Example 2):
    # Enter a Number: -8
    # The Number is Negative.

else:
    # This block executes if none of the above conditions are True.
    print("The Number is Zero.")
    # Output (Example 3):
    # Enter a Number: 0
    # The Number is Zero.

# -----------------------------------------------------------------------------
# Displaying a message after the if-elif-else statement.
# -----------------------------------------------------------------------------
print("Program Completed.")
# Output:
# Program Completed.
