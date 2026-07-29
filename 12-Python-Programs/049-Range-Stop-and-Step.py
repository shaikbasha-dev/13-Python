"""
===============================================================================
                         Range Stop and Step
===============================================================================

Program Description:
--------------------
This program demonstrates the use of the range() function with
stop and step values.

Since Python does not support the syntax range(stop, step),
the start value must be provided explicitly. In this example,
the start value is 0, the stop value is 10, and the step value is 2.

Syntax:

range(start, stop, step)

Example:
range(0, 10, 2)

Output:
0
2
4
6
8

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 49-Range-Stop-and-Step.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Displaying a heading.
# -----------------------------------------------------------------------------
print("Even Numbers from 0 to 8")
# Output: Even Numbers from 0 to 8

# -----------------------------------------------------------------------------
# Using the range() function with start, stop, and step values.
# -----------------------------------------------------------------------------
for number in range(0, 10, 2):
    # The loop variable stores one value at a time.
    print(number)
    # Output:
    # 0
    # 2
    # 4
    # 6
    # 8

# -----------------------------------------------------------------------------
# Displaying a message after the loop.
# -----------------------------------------------------------------------------
print("Program Completed.")
# Output:
# Program Completed.
