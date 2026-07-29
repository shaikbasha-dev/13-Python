"""
===============================================================================
File Name    : 64-Delete-List.py
Description  : Delete a List in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
The del keyword is used to delete an entire list from memory. After deleting
the list, it can no longer be accessed.

Syntax:
del list_name

Example:
del numbers
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
# Displaying the number of elements in the list.
# -----------------------------------------------------------------------------
print("Total Elements :", len(numbers))
# Output:
# Total Elements : 5

print()

# -----------------------------------------------------------------------------
# Deleting the entire list.
# -----------------------------------------------------------------------------
del numbers

# -----------------------------------------------------------------------------
# Displaying a confirmation message.
# -----------------------------------------------------------------------------
print("The list has been deleted successfully.")
# Output:
# The list has been deleted successfully.

print()

# -----------------------------------------------------------------------------
# Attempting to access the deleted list.
# -----------------------------------------------------------------------------
print(numbers)
# Output:
# NameError: name 'numbers' is not defined
