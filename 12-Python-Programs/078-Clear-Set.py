"""
===============================================================================
File Name    : 78-Clear-Set.py
Description  : Clear a Set in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
The clear() method is used to remove all elements from a set. After calling
this method, the set becomes empty, but the set object still exists.

Syntax:
set_name.clear()

Example:
numbers.clear()
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
# Displaying the number of elements before clearing the set.
# -----------------------------------------------------------------------------
print("Elements Before Clear :", len(numbers))
# Output:
# Elements Before Clear : 5

print()

# -----------------------------------------------------------------------------
# Removing all elements from the set.
# -----------------------------------------------------------------------------
numbers.clear()

# -----------------------------------------------------------------------------
# Displaying the set after clearing.
# -----------------------------------------------------------------------------
print("Set After clear() :", numbers)
# Output:
# Set After clear() : set()

print()

# -----------------------------------------------------------------------------
# Displaying the number of elements after clearing the set.
# -----------------------------------------------------------------------------
print("Elements After Clear :", len(numbers))
# Output:
# Elements After Clear : 0

print()

# -----------------------------------------------------------------------------
# Displaying the type of the set.
# -----------------------------------------------------------------------------
print("Type of Set :", type(numbers))
# Output:
# Type of Set : <class 'set'>
