"""
===============================================================================
File Name    : 153-List-Comprehension.py
Description  : List Comprehension in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
List Comprehension is a concise and efficient way to create a new list
from an existing iterable such as a list, tuple, string, or range.

It allows creating a list using a single line of code.

Syntax:

[expression for item in iterable]

Example:
Creating a list of squares using list comprehension.
"""

# -----------------------------------------------------------------------------
# Creating a list of numbers.
# -----------------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5]

# -----------------------------------------------------------------------------
# Creating a new list containing the square of each number.
# -----------------------------------------------------------------------------
square_numbers = [number * number for number in numbers]

# -----------------------------------------------------------------------------
# Displaying the original list.
# -----------------------------------------------------------------------------
print("Original List :", numbers)

# -----------------------------------------------------------------------------
# Displaying the new list.
# -----------------------------------------------------------------------------
print("Square List   :", square_numbers)

# -----------------------------------------------------------------------------
# Creating a list of even numbers using list comprehension.
# -----------------------------------------------------------------------------
even_numbers = [number for number in numbers if number % 2 == 0]

# -----------------------------------------------------------------------------
# Displaying the even numbers.
# -----------------------------------------------------------------------------
print("Even Numbers  :", even_numbers)

# Output:
# Original List : [1, 2, 3, 4, 5]
# Square List   : [1, 4, 9, 16, 25]
# Even Numbers  : [2, 4]
