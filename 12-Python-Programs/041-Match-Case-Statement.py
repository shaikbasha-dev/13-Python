"""
===============================================================================
                         Match Case Statement
===============================================================================

Program Description:
--------------------
This program demonstrates the use of the match-case statement in Python.

The match-case statement is used to compare a value against multiple
cases. When a matching case is found, the corresponding block of code
is executed.

Note:
The match-case statement is available in Python 3.10 and later versions.

Syntax:

match expression:
    case value1:
        statements
    case value2:
        statements
    case _:
        statements

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 41-Match-Case-Statement.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Accepting a number from the user.
# -----------------------------------------------------------------------------
number = int(input("Enter a Number (1-3): "))
# The entered value is converted into an integer.

# -----------------------------------------------------------------------------
# Checking the entered number using the match-case statement.
# -----------------------------------------------------------------------------
match number:

    # -------------------------------------------------------------------------
    # Executed when the entered number is 1.
    # -------------------------------------------------------------------------
    case 1:
        print("You Entered One.")
        # Output (Example):
        # Enter a Number (1-3): 1
        # You Entered One.

    # -------------------------------------------------------------------------
    # Executed when the entered number is 2.
    # -------------------------------------------------------------------------
    case 2:
        print("You Entered Two.")
        # Output (Example):
        # Enter a Number (1-3): 2
        # You Entered Two.

    # -------------------------------------------------------------------------
    # Executed when the entered number is 3.
    # -------------------------------------------------------------------------
    case 3:
        print("You Entered Three.")
        # Output (Example):
        # Enter a Number (1-3): 3
        # You Entered Three.

    # -------------------------------------------------------------------------
    # Executed when no case matches.
    # -------------------------------------------------------------------------
    case _:
        print("Invalid Input.")
        # Output (Example):
        # Enter a Number (1-3): 5
        # Invalid Input.

# -----------------------------------------------------------------------------
# Displaying a message after the match-case statement.
# -----------------------------------------------------------------------------
print("Program Completed.")
# Output:
# Program Completed.
