"""
===============================================================================
                     Range Start, Stop and Step
===============================================================================

Program Description:
--------------------
This program demonstrates the use of the range() function with
start, stop, and step values.

The sequence starts from the specified start value, increases by the
specified step value, and stops before the specified stop value.

Syntax:

range(start, stop, step)

Example:
range(5, 16, 2)

Output:
5
7
9
11
13
15

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 50-Range-Start-Stop-and-Step.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Displaying a heading.
# -----------------------------------------------------------------------------
print("Odd Numbers from 5 to 15")
# Output: Odd Numbers from 5 to 15

# -----------------------------------------------------------------------------
# Using the range() function with start, stop, and step values.
# -----------------------------------------------------------------------------
for number in range(5, 16, 2):
    # The loop variable stores one value at a time.
    print(number)
    # Output:
    # 5
    # 7
    # 9
    # 11
    # 13
    # 15

# -----------------------------------------------------------------------------
# Displaying a message after the loop.
# -----------------------------------------------------------------------------
print("Program Completed.")
# Output:
# Program Completed.
