"""
===============================================================================
                            Range Only Step
===============================================================================

Program Description:
--------------------
This program demonstrates the use of the range() function with
start, stop, and step values.

The step value specifies how much the value increases after each
iteration.

Syntax:

range(start, stop, step)

Example:
range(1, 10, 2)

Output:
1
3
5
7
9

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 46-Range-Only-Step.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Displaying a heading.
# -----------------------------------------------------------------------------
print("Odd Numbers from 1 to 9")
# Output: Odd Numbers from 1 to 9

# -----------------------------------------------------------------------------
# Using the range() function with start, stop, and step values.
# -----------------------------------------------------------------------------
for number in range(1, 10, 2):
    # The loop variable stores one value at a time.
    print(number)
    # Output:
    # 1
    # 3
    # 5
    # 7
    # 9

# -----------------------------------------------------------------------------
# Displaying a message after the loop.
# -----------------------------------------------------------------------------
print("Program Completed.")
# Output:
# Program Completed.
