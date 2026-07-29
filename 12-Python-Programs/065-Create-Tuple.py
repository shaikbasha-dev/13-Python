"""
===============================================================================
File Name    : 65-Create-Tuple.py
Description  : Create a Tuple in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A tuple is a collection data type used to store multiple values in a single
variable. Tuples are ordered, immutable, and allow duplicate values.

Syntax:
tuple_name = (value1, value2, value3)

Example:
numbers = (10, 20, 30)
"""

# -----------------------------------------------------------------------------
# Creating a tuple of integers.
# -----------------------------------------------------------------------------
numbers = (10, 20, 30, 40, 50)

# -----------------------------------------------------------------------------
# Displaying the integer tuple.
# -----------------------------------------------------------------------------
print("Integer Tuple :", numbers)
# Output:
# Integer Tuple : (10, 20, 30, 40, 50)

print()

# -----------------------------------------------------------------------------
# Creating a tuple of strings.
# -----------------------------------------------------------------------------
fruits = ("Apple", "Banana", "Mango", "Orange")

# -----------------------------------------------------------------------------
# Displaying the string tuple.
# -----------------------------------------------------------------------------
print("Fruit Tuple :", fruits)
# Output:
# Fruit Tuple : ('Apple', 'Banana', 'Mango', 'Orange')

print()

# -----------------------------------------------------------------------------
# Creating a mixed data type tuple.
# -----------------------------------------------------------------------------
student = (101, "Rahul", 92.5, True)

# -----------------------------------------------------------------------------
# Displaying the mixed tuple.
# -----------------------------------------------------------------------------
print("Mixed Tuple :", student)
# Output:
# Mixed Tuple : (101, 'Rahul', 92.5, True)

print()

# -----------------------------------------------------------------------------
# Creating an empty tuple.
# -----------------------------------------------------------------------------
empty_tuple = ()

# -----------------------------------------------------------------------------
# Displaying the empty tuple.
# -----------------------------------------------------------------------------
print("Empty Tuple :", empty_tuple)
# Output:
# Empty Tuple : ()

print()

# -----------------------------------------------------------------------------
# Displaying the type of the tuple.
# -----------------------------------------------------------------------------
print("Type of numbers :", type(numbers))
# Output:
# Type of numbers : <class 'tuple'>
