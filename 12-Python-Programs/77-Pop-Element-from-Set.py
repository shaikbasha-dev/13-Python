"""
===============================================================================
File Name    : 77-Pop-Element-from-Set.py
Description  : Pop an Element from a Set in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
The pop() method is used to remove and return an arbitrary element from a set.
Since sets are unordered collections, the element removed is not guaranteed
to be the first or last element.

Syntax:
set_name.pop()

Example:
removed_element = numbers.pop()
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
# Removing an arbitrary element from the set.
# -----------------------------------------------------------------------------
removed_element = numbers.pop()

# -----------------------------------------------------------------------------
# Displaying the removed element.
# -----------------------------------------------------------------------------
print("Removed Element :", removed_element)
# Output:
# Removed Element : (Any one element from the set)

# -----------------------------------------------------------------------------
# Displaying the updated set.
# -----------------------------------------------------------------------------
print("Set After pop() :", numbers)
# Output:
# Set After pop() : Remaining elements after removing one element

print()

# -----------------------------------------------------------------------------
# Removing another arbitrary element from the set.
# -----------------------------------------------------------------------------
removed_element = numbers.pop()

# -----------------------------------------------------------------------------
# Displaying the removed element.
# -----------------------------------------------------------------------------
print("Removed Element :", removed_element)
# Output:
# Removed Element : (Any one remaining element)

# -----------------------------------------------------------------------------
# Displaying the updated set.
# -----------------------------------------------------------------------------
print("Set After Second pop() :", numbers)
# Output:
# Set After Second pop() : Remaining elements after removing another element

print()

# -----------------------------------------------------------------------------
# Displaying the total number of elements in the set.
# -----------------------------------------------------------------------------
print("Total Elements :", len(numbers))
# Output:
# Total Elements : 3
