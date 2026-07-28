"""
===============================================================================
                            Range Only Stop
===============================================================================

Program Description:
--------------------
This program demonstrates the use of the range() function with only the
stop value.

When only the stop value is provided, the sequence starts from 0 by
default and ends before the specified stop value.

Syntax:

range(stop)

Example:
range(5)

Output:
0
1
2
3
4

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 45-Range-Only-Stop.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Displaying a heading.
# -----------------------------------------------------------------------------
print("Numbers from 0 to 4")
# Output: Numbers from 0 to 4

# -----------------------------------------------------------------------------
# Using the range() function with only the stop value.
# -----------------------------------------------------------------------------
for number in range(5):
    # The loop variable stores one value at a time.
    print(number)
    # Output:
    # 0
    # 1
    # 2
    # 3
    # 4

# -----------------------------------------------------------------------------
# Displaying a message after the loop.
# -----------------------------------------------------------------------------
print("Program Completed.")
# Output:
# Program Completed.
