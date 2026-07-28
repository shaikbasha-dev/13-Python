"""
===============================================================================
                            Break Statement
===============================================================================

Program Description:
--------------------
This program demonstrates the use of the break statement in Python.

The break statement is used to terminate a loop immediately when a
specified condition becomes True. After the break statement is executed,
the control comes out of the loop.

Syntax:

break

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 51-Break-Statement.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Displaying a heading.
# -----------------------------------------------------------------------------
print("Break Statement Example")
# Output: Break Statement Example

# -----------------------------------------------------------------------------
# Using a for loop to display numbers.
# -----------------------------------------------------------------------------
for number in range(1, 11):

    # -------------------------------------------------------------------------
    # Checking whether the current number is equal to 6.
    # -------------------------------------------------------------------------
    if number == 6:

        # ---------------------------------------------------------------------
        # Terminating the loop when the condition becomes True.
        # ---------------------------------------------------------------------
        break

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

# -----------------------------------------------------------------------------
# Displaying a message after the loop.
# -----------------------------------------------------------------------------
print("Program Completed.")
# Output:
# Program Completed.
