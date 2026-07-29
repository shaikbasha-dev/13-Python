"""
===============================================================================
File Name    : 62-Pop-Element-from-List.py
Description  : Pop an Element from a List in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
The pop() method is used to remove and return an element from a specified
index in a list. If no index is specified, it removes and returns the last
element.

Syntax:
list_name.pop(index)
or
list_name.pop()

Example:
numbers.pop(2)
numbers.pop()
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
# Removing the last element from the list.
# -----------------------------------------------------------------------------
removed_element = numbers.pop()

# -----------------------------------------------------------------------------
# Displaying the removed element.
# -----------------------------------------------------------------------------
print("Removed Last Element :", removed_element)
# Output:
# Removed Last Element : 50

# -----------------------------------------------------------------------------
# Displaying the updated list.
# -----------------------------------------------------------------------------
print("List After pop() :", numbers)
# Output:
# List After pop() : [10, 20, 30, 40]

print()

# -----------------------------------------------------------------------------
# Removing the element at index 1.
# -----------------------------------------------------------------------------
removed_element = numbers.pop(1)

# -----------------------------------------------------------------------------
# Displaying the removed element.
# -----------------------------------------------------------------------------
print("Removed Element at Index 1 :", removed_element)
# Output:
# Removed Element at Index 1 : 20

# -----------------------------------------------------------------------------
# Displaying the updated list.
# -----------------------------------------------------------------------------
print("List After pop(1) :", numbers)
# Output:
# List After pop(1) : [10, 30, 40]

print()

# -----------------------------------------------------------------------------
# Displaying the total number of elements in the list.
# -----------------------------------------------------------------------------
print("Total Elements :", len(numbers))
# Output:
# Total Elements : 3
