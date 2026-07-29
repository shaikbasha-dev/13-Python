"""
===============================================================================
File Name    : 79-Delete-Set.py
Description  : Delete a Set in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
The del keyword is used to delete an entire set from memory. After deleting
the set, it can no longer be accessed.

Syntax:
del set_name

Example:
del numbers
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
# Displaying the total number of elements in the set.
# -----------------------------------------------------------------------------
print("Total Elements :", len(numbers))
# Output:
# Total Elements : 5

print()

# -----------------------------------------------------------------------------
# Deleting the entire set.
# -----------------------------------------------------------------------------
del numbers

# -----------------------------------------------------------------------------
# Displaying a confirmation message.
# -----------------------------------------------------------------------------
print("The set has been deleted successfully.")
# Output:
# The set has been deleted successfully.

print()

# -----------------------------------------------------------------------------
# Attempting to access the deleted set.
# -----------------------------------------------------------------------------
print(numbers)
# Output:
# NameError: name 'numbers' is not defined
