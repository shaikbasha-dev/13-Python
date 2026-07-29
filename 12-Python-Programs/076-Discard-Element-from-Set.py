"""
===============================================================================
File Name    : 76-Discard-Element-from-Set.py
Description  : Discard an Element from a Set in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
The discard() method is used to remove a specified element from a set.
If the specified element is not present, no error occurs.

Syntax:
set_name.discard(element)

Example:
numbers.discard(30)
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
# Discarding the element 30 from the set.
# -----------------------------------------------------------------------------
numbers.discard(30)

# -----------------------------------------------------------------------------
# Displaying the updated set.
# -----------------------------------------------------------------------------
print("After Discarding 30 :", numbers)
# Output:
# After Discarding 30 : {10, 20, 40, 50}

print()

# -----------------------------------------------------------------------------
# Discarding another element from the set.
# -----------------------------------------------------------------------------
numbers.discard(50)

# -----------------------------------------------------------------------------
# Displaying the updated set.
# -----------------------------------------------------------------------------
print("After Discarding 50 :", numbers)
# Output:
# After Discarding 50 : {10, 20, 40}

print()

# -----------------------------------------------------------------------------
# Attempting to discard an element that is not present in the set.
# -----------------------------------------------------------------------------
numbers.discard(100)

# -----------------------------------------------------------------------------
# Displaying the set after attempting to discard a non-existing element.
# -----------------------------------------------------------------------------
print("After Discarding 100 :", numbers)
# Output:
# After Discarding 100 : {10, 20, 40}

print()

# -----------------------------------------------------------------------------
# Displaying the total number of elements in the set.
# -----------------------------------------------------------------------------
print("Total Elements :", len(numbers))
# Output:
# Total Elements : 3
