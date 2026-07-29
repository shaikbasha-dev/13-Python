"""
===============================================================================
                           Range Only Start
===============================================================================

Program Description:
--------------------
This program demonstrates the use of the range() function with only the
start value.

When only one value is provided to range(), Python treats it as the
stop value. The sequence starts from 0 by default and ends before the
specified value.

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
File Name   : 44-Range-Only-Start.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Displaying a heading.
# -----------------------------------------------------------------------------
print("Numbers Generated Using range(5)")
# Output: Numbers Generated Using range(5)

# -----------------------------------------------------------------------------
# Using the range() function with only one value.
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
