"""
===============================================================================
File Name    : 69-Convert-Tuple-to-List.py
Description  : Convert a Tuple to a List in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A tuple can be converted into a list using the list() function. This is useful
when you want to modify the elements because tuples are immutable, whereas
lists are mutable.

Syntax:
list_name = list(tuple_name)

Example:
numbers = (10, 20, 30)
number_list = list(numbers)
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
# Converting the tuple into a list.
# -----------------------------------------------------------------------------
number_list = list(numbers)

# -----------------------------------------------------------------------------
# Displaying the converted list.
# -----------------------------------------------------------------------------
print("Converted List :", number_list)
# Output:
# Converted List : [10, 20, 30, 40, 50]

print()

# -----------------------------------------------------------------------------
# Adding a new element to the list.
# -----------------------------------------------------------------------------
number_list.append(60)

# -----------------------------------------------------------------------------
# Displaying the updated list.
# -----------------------------------------------------------------------------
print("List After Adding 60 :", number_list)
# Output:
# List After Adding 60 : [10, 20, 30, 40, 50, 60]

print()

# -----------------------------------------------------------------------------
# Displaying the type of the original tuple.
# -----------------------------------------------------------------------------
print("Type of Tuple :", type(numbers))
# Output:
# Type of Tuple : <class 'tuple'>

# -----------------------------------------------------------------------------
# Displaying the type of the converted list.
# -----------------------------------------------------------------------------
print("Type of List :", type(number_list))
# Output:
# Type of List : <class 'list'>
