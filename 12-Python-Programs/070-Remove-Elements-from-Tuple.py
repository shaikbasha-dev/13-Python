"""
===============================================================================
File Name    : 70-Remove-Elements-from-Tuple.py
Description  : Remove Elements from a Tuple in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A tuple is immutable, which means its elements cannot be removed directly.
To remove elements from a tuple, first convert it into a list, remove the
required elements, and then convert it back into a tuple.

Syntax:
list_name = list(tuple_name)
list_name.remove(element)
tuple_name = tuple(list_name)

Example:
numbers = (10, 20, 30)
number_list = list(numbers)
number_list.remove(20)
numbers = tuple(number_list)
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
# Removing the element 30 from the list.
# -----------------------------------------------------------------------------
number_list.remove(30)

# -----------------------------------------------------------------------------
# Removing the element 50 from the list.
# -----------------------------------------------------------------------------
number_list.remove(50)

# -----------------------------------------------------------------------------
# Converting the modified list back into a tuple.
# -----------------------------------------------------------------------------
numbers = tuple(number_list)

# -----------------------------------------------------------------------------
# Displaying the updated tuple.
# -----------------------------------------------------------------------------
print("Tuple After Removing Elements :", numbers)
# Output:
# Tuple After Removing Elements : (10, 20, 40)

print()

# -----------------------------------------------------------------------------
# Displaying the total number of elements in the updated tuple.
# -----------------------------------------------------------------------------
print("Total Elements :", len(numbers))
# Output:
# Total Elements : 3

print()

# -----------------------------------------------------------------------------
# Displaying the type of the updated tuple.
# -----------------------------------------------------------------------------
print("Type of Tuple :", type(numbers))
# Output:
# Type of Tuple : <class 'tuple'>
