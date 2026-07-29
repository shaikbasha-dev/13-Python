"""
===============================================================================
                               While Loop
===============================================================================

Program Description:
--------------------
This program demonstrates the use of the while loop in Python.

The while loop is used to execute a block of code repeatedly as long as
the given condition is True.

Syntax:

while condition:
    statements

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 43-While-Loop.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating a variable with the starting value.
# -----------------------------------------------------------------------------
number = 1
# number stores the starting value 1.

# -----------------------------------------------------------------------------
# Displaying a heading.
# -----------------------------------------------------------------------------
print("Numbers from 1 to 5")
# Output: Numbers from 1 to 5

# -----------------------------------------------------------------------------
# Using the while loop to display numbers from 1 to 5.
# -----------------------------------------------------------------------------
while number <= 5:
    # Displaying the current value of the variable.
    print(number)
    # Output:
    # 1
    # 2
    # 3
    # 4
    # 5

    # -------------------------------------------------------------------------
    # Increasing the value of the variable by 1.
    # -------------------------------------------------------------------------
    number = number + 1
    # The value of number increases after each iteration.

# -----------------------------------------------------------------------------
# Displaying a message after the while loop.
# -----------------------------------------------------------------------------
print("Program Completed.")
# Output:
# Program Completed.
