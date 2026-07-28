"""
===============================================================================
                                For Loop
===============================================================================

Program Description:
--------------------
This program demonstrates the use of the for loop in Python.

The for loop is used to execute a block of code repeatedly for each item
in a sequence. In this example, the range() function is used to generate
numbers from 1 to 5.

Syntax:

for variable in sequence:
    statements

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 42-For-Loop.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Displaying a heading.
# -----------------------------------------------------------------------------
print("Numbers from 1 to 5")
# Output: Numbers from 1 to 5

# -----------------------------------------------------------------------------
# Using the for loop to display numbers from 1 to 5.
# -----------------------------------------------------------------------------
for number in range(1, 6):
    # The loop variable stores one value at a time.
    print(number)
    # Output:
    # 1
    # 2
    # 3
    # 4
    # 5

# -----------------------------------------------------------------------------
# Displaying a message after the for loop.
# -----------------------------------------------------------------------------
print("Program Completed.")
# Output:
# Program Completed.
