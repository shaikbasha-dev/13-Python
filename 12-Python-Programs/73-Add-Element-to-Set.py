"""
===============================================================================
File Name    : 73-Add-Element-to-Set.py
Description  : Add an Element to a Set in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
The add() method is used to add a single element to a set. If the element
already exists, it will not be added again because sets store only unique
values.

Syntax:
set_name.add(element)

Example:
numbers.add(60)
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
# Adding a new element to the set.
# -----------------------------------------------------------------------------
numbers.add(60)

# -----------------------------------------------------------------------------
# Displaying the set after adding the new element.
# -----------------------------------------------------------------------------
print("After Adding 60 :", numbers)
# Output:
# After Adding 60 : {10, 20, 30, 40, 50, 60}

print()

# -----------------------------------------------------------------------------
# Adding another element to the set.
# -----------------------------------------------------------------------------
numbers.add(70)

# -----------------------------------------------------------------------------
# Displaying the updated set.
# -----------------------------------------------------------------------------
print("After Adding 70 :", numbers)
# Output:
# After Adding 70 : {10, 20, 30, 40, 50, 60, 70}

print()

# -----------------------------------------------------------------------------
# Attempting to add a duplicate element.
# -----------------------------------------------------------------------------
numbers.add(30)

# -----------------------------------------------------------------------------
# Displaying the set after attempting to add a duplicate element.
# -----------------------------------------------------------------------------
print("After Adding Duplicate 30 :", numbers)
# Output:
# After Adding Duplicate 30 : {10, 20, 30, 40, 50, 60, 70}

print()

# -----------------------------------------------------------------------------
# Displaying the total number of elements in the set.
# -----------------------------------------------------------------------------
print("Total Elements :", len(numbers))
# Output:
# Total Elements : 7
