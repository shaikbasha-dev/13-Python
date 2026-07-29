"""
===============================================================================
                        Range Start and Stop
===============================================================================

Program Description:
--------------------
This program demonstrates the use of the range() function with
start and stop values.

The sequence starts from the specified start value and ends before
the specified stop value.

Syntax:

range(start, stop)

Example:
range(1, 6)

Output:
1
2
3
4
5

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 47-Range-Start-and-Stop.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Displaying a heading.
# -----------------------------------------------------------------------------
print("Numbers from 1 to 5")
# Output: Numbers from 1 to 5

# -----------------------------------------------------------------------------
# Using the range() function with start and stop values.
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
# Displaying a message after the loop.
# -----------------------------------------------------------------------------
print("Program Completed.")
# Output:
# Program Completed.
