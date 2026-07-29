"""
===============================================================================
File Name    : 61-Remove-Element-from-List.py
Description  : Remove an Element from a List in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
The remove() method is used to remove the first occurrence of a specified
element from a list.

Syntax:
list_name.remove(element)

Example:
numbers.remove(30)
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
# Removing the element 30 from the list.
# -----------------------------------------------------------------------------
numbers.remove(30)

# -----------------------------------------------------------------------------
# Displaying the updated list.
# -----------------------------------------------------------------------------
print("After Removing 30 :", numbers)
# Output:
# After Removing 30 : [10, 20, 40, 50]

print()

# -----------------------------------------------------------------------------
# Removing the first element from the list.
# -----------------------------------------------------------------------------
numbers.remove(10)

# -----------------------------------------------------------------------------
# Displaying the updated list.
# -----------------------------------------------------------------------------
print("After Removing 10 :", numbers)
# Output:
# After Removing 10 : [20, 40, 50]

print()

# -----------------------------------------------------------------------------
# Removing the last element from the list.
# -----------------------------------------------------------------------------
numbers.remove(50)

# -----------------------------------------------------------------------------
# Displaying the updated list.
# -----------------------------------------------------------------------------
print("After Removing 50 :", numbers)
# Output:
# After Removing 50 : [20, 40]

print()

# -----------------------------------------------------------------------------
# Displaying the total number of elements in the list.
# -----------------------------------------------------------------------------
print("Total Elements :", len(numbers))
# Output:
# Total Elements : 2
