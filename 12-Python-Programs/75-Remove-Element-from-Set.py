"""
===============================================================================
File Name    : 75-Remove-Element-from-Set.py
Description  : Remove an Element from a Set in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
The remove() method is used to remove a specified element from a set.
If the specified element is not present in the set, a KeyError occurs.

Syntax:
set_name.remove(element)

Example:
numbers.remove(30)
"""

# -----------------------------------------------------------------------------
# Creating a set of integers.
# -----------------------------------------------------------------------------
numbers = {10, 20, 30, 40, 50}

# -----------------------------------------------------------------------------
# Displaying the original set.
# -----------------------------------------------------------------------------
print("Original Set :", numbers)
# Output:
# Original Set : {10, 20, 30, 40, 50}

print()

# -----------------------------------------------------------------------------
# Removing the element 30 from the set.
# -----------------------------------------------------------------------------
numbers.remove(30)

# -----------------------------------------------------------------------------
# Displaying the updated set.
# -----------------------------------------------------------------------------
print("After Removing 30 :", numbers)
# Output:
# After Removing 30 : {10, 20, 40, 50}

print()

# -----------------------------------------------------------------------------
# Removing another element from the set.
# -----------------------------------------------------------------------------
numbers.remove(50)

# -----------------------------------------------------------------------------
# Displaying the updated set.
# -----------------------------------------------------------------------------
print("After Removing 50 :", numbers)
# Output:
# After Removing 50 : {10, 20, 40}

print()

# -----------------------------------------------------------------------------
# Displaying the total number of elements in the set.
# -----------------------------------------------------------------------------
print("Total Elements :", len(numbers))
# Output:
# Total Elements : 3

print()

# -----------------------------------------------------------------------------
# Attempting to remove an element that is not present in the set.
# -----------------------------------------------------------------------------
numbers.remove(100)

# Output:
# KeyError: 100
