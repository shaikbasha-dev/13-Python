"""
===============================================================================
                        Range Start and Step
===============================================================================

Program Description:
--------------------
This program demonstrates the use of the range() function with
start, stop, and step values.

The sequence starts from the specified start value and increases
by the specified step value until it reaches the stop value.
The stop value is not included in the sequence.

Syntax:

range(start, stop, step)

Example:
range(2, 11, 2)

Output:
2
4
6
8
10

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 48-Range-Start-and-Step.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Displaying a heading.
# -----------------------------------------------------------------------------
print("Even Numbers from 2 to 10")
# Output: Even Numbers from 2 to 10

# -----------------------------------------------------------------------------
# Using the range() function with start, stop, and step values.
# -----------------------------------------------------------------------------
for number in range(2, 11, 2):
    # The loop variable stores one value at a time.
    print(number)
    # Output:
    # 2
    # 4
    # 6
    # 8
    # 10

# -----------------------------------------------------------------------------
# Displaying a message after the loop.
# -----------------------------------------------------------------------------
print("Program Completed.")
# Output:
# Program Completed.
