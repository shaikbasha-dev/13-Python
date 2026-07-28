"""
===============================================================================
                           Continue Statement
===============================================================================

Program Description:
--------------------
This program demonstrates the use of the continue statement in Python.

The continue statement is used to skip the current iteration of a loop
and continue with the next iteration.

Syntax:

continue

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 52-Continue-Statement.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Displaying a heading.
# -----------------------------------------------------------------------------
print("Continue Statement Example")
# Output: Continue Statement Example

# -----------------------------------------------------------------------------
# Using a for loop to display numbers.
# -----------------------------------------------------------------------------
for number in range(1, 11):

    # -------------------------------------------------------------------------
    # Checking whether the current number is equal to 6.
    # -------------------------------------------------------------------------
    if number == 6:

        # ---------------------------------------------------------------------
        # Skipping the current iteration when the condition becomes True.
        # ---------------------------------------------------------------------
        continue

    # -------------------------------------------------------------------------
    # Displaying the current number.
    # -------------------------------------------------------------------------
    print(number)
    # Output:
    # 1
    # 2
    # 3
    # 4
    # 5
    # 7
    # 8
    # 9
    # 10

# -----------------------------------------------------------------------------
# Displaying a message after the loop.
# -----------------------------------------------------------------------------
print("Program Completed.")
# Output:
# Program Completed.
