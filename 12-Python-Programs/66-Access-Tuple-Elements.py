"""
===============================================================================
File Name    : 66-Access-Tuple-Elements.py
Description  : Access Tuple Elements in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Tuple elements can be accessed using their index values. The index starts
from 0 for the first element and -1 for the last element.

Syntax:
tuple_name[index]

Example:
numbers[0]
numbers[-1]
"""

# -----------------------------------------------------------------------------
# Creating a tuple of integers.
# -----------------------------------------------------------------------------
numbers = (10, 20, 30, 40, 50)

# -----------------------------------------------------------------------------
# Displaying the original tuple.
# -----------------------------------------------------------------------------
print("Original Tuple :", numbers)
# Output:
# Original Tuple : (10, 20, 30, 40, 50)

print()

# -----------------------------------------------------------------------------
# Accessing the first element.
# -----------------------------------------------------------------------------
print("First Element :", numbers[0])
# Output:
# First Element : 10

# -----------------------------------------------------------------------------
# Accessing the second element.
# -----------------------------------------------------------------------------
print("Second Element :", numbers[1])
# Output:
# Second Element : 20

# -----------------------------------------------------------------------------
# Accessing the third element.
# -----------------------------------------------------------------------------
print("Third Element :", numbers[2])
# Output:
# Third Element : 30

print()

# -----------------------------------------------------------------------------
# Accessing the last element using a negative index.
# -----------------------------------------------------------------------------
print("Last Element :", numbers[-1])
# Output:
# Last Element : 50

# -----------------------------------------------------------------------------
# Accessing the second last element using a negative index.
# -----------------------------------------------------------------------------
print("Second Last Element :", numbers[-2])
# Output:
# Second Last Element : 40

print()

# -----------------------------------------------------------------------------
# Displaying the total number of elements in the tuple.
# -----------------------------------------------------------------------------
print("Total Elements :", len(numbers))
# Output:
# Total Elements : 5
