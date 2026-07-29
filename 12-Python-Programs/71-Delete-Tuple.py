"""
===============================================================================
File Name    : 71-Delete-Tuple.py
Description  : Delete a Tuple in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
The del keyword is used to delete an entire tuple from memory. After deleting
the tuple, it can no longer be accessed.

Syntax:
del tuple_name

Example:
del numbers
"""

# -----------------------------------------------------------------------------
# Creating a tuple of integers.
# -----------------------------------------------------------------------------
numbers = (10, 20, 30, 40, 50)

# -----------------------------------------------------------------------------
# Displaying the original tuple.
# -----------------------------------------------------------------------------
print("Original Tuple :", numbers)
# Output:
# Original Tuple : (10, 20, 30, 40, 50)

print()

# -----------------------------------------------------------------------------
# Displaying the total number of elements in the tuple.
# -----------------------------------------------------------------------------
print("Total Elements :", len(numbers))
# Output:
# Total Elements : 5

print()

# -----------------------------------------------------------------------------
# Deleting the entire tuple.
# -----------------------------------------------------------------------------
del numbers

# -----------------------------------------------------------------------------
# Displaying a confirmation message.
# -----------------------------------------------------------------------------
print("The tuple has been deleted successfully.")
# Output:
# The tuple has been deleted successfully.

print()

# -----------------------------------------------------------------------------
# Attempting to access the deleted tuple.
# -----------------------------------------------------------------------------
print(numbers)
# Output:
# NameError: name 'numbers' is not defined
