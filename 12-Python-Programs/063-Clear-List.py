"""
===============================================================================
File Name    : 63-Clear-List.py
Description  : Clear a List in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
The clear() method is used to remove all elements from a list. After calling
this method, the list becomes empty, but the list object still exists.

Syntax:
list_name.clear()

Example:
numbers.clear()
"""

# -----------------------------------------------------------------------------
# Creating a list of integers.
# -----------------------------------------------------------------------------
numbers = [10, 20, 30, 40, 50]

# -----------------------------------------------------------------------------
# Displaying the original list.
# -----------------------------------------------------------------------------
print("Original List :", numbers)
# Output:
# Original List : [10, 20, 30, 40, 50]

print()

# -----------------------------------------------------------------------------
# Displaying the number of elements before clearing the list.
# -----------------------------------------------------------------------------
print("Elements Before Clear :", len(numbers))
# Output:
# Elements Before Clear : 5

print()

# -----------------------------------------------------------------------------
# Removing all elements from the list.
# -----------------------------------------------------------------------------
numbers.clear()

# -----------------------------------------------------------------------------
# Displaying the list after clearing.
# -----------------------------------------------------------------------------
print("List After clear() :", numbers)
# Output:
# List After clear() : []

print()

# -----------------------------------------------------------------------------
# Displaying the number of elements after clearing the list.
# -----------------------------------------------------------------------------
print("Elements After Clear :", len(numbers))
# Output:
# Elements After Clear : 0

print()

# -----------------------------------------------------------------------------
# Displaying the type of the list.
# -----------------------------------------------------------------------------
print("Type of List :", type(numbers))
# Output:
# Type of List : <class 'list'>
