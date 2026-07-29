"""
===============================================================================
File Name    : 56-Create-List.py
Description  : Create a List in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A list is a collection data type used to store multiple values in a single
variable. Lists are ordered, mutable, and allow duplicate values.

Syntax:
list_name = [value1, value2, value3]

Example:
numbers = [10, 20, 30]
"""

# -----------------------------------------------------------------------------
# Creating a list of integers.
# -----------------------------------------------------------------------------
numbers = [10, 20, 30, 40, 50]

# -----------------------------------------------------------------------------
# Displaying the complete list.
# -----------------------------------------------------------------------------
print("Integer List :", numbers)
# Output:
# Integer List : [10, 20, 30, 40, 50]

print()

# -----------------------------------------------------------------------------
# Creating a list of strings.
# -----------------------------------------------------------------------------
fruits = ["Apple", "Banana", "Mango", "Orange"]

# -----------------------------------------------------------------------------
# Displaying the complete list.
# -----------------------------------------------------------------------------
print("Fruit List :", fruits)
# Output:
# Fruit List : ['Apple', 'Banana', 'Mango', 'Orange']

print()

# -----------------------------------------------------------------------------
# Creating a mixed data type list.
# -----------------------------------------------------------------------------
student = [101, "Rahul", 92.5, True]

# -----------------------------------------------------------------------------
# Displaying the complete list.
# -----------------------------------------------------------------------------
print("Mixed List :", student)
# Output:
# Mixed List : [101, 'Rahul', 92.5, True]

print()

# -----------------------------------------------------------------------------
# Creating an empty list.
# -----------------------------------------------------------------------------
empty_list = []

# -----------------------------------------------------------------------------
# Displaying the empty list.
# -----------------------------------------------------------------------------
print("Empty List :", empty_list)
# Output:
# Empty List : []

print()

# -----------------------------------------------------------------------------
# Displaying the type of a list.
# -----------------------------------------------------------------------------
print("Type of numbers :", type(numbers))
# Output:
# Type of numbers : <class 'list'>
