"""
===============================================================================
File Name    : 58-Extend-List.py
Description  : Extend a List in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
The extend() method is used to add multiple elements from another iterable
(such as a list, tuple, or set) to the end of an existing list.

Syntax:
list_name.extend(iterable)

Example:
numbers.extend([40, 50, 60])
"""

# -----------------------------------------------------------------------------
# Creating the first list.
# -----------------------------------------------------------------------------
numbers = [10, 20, 30]

# -----------------------------------------------------------------------------
# Displaying the original list.
# -----------------------------------------------------------------------------
print("Original List :", numbers)
# Output:
# Original List : [10, 20, 30]

print()

# -----------------------------------------------------------------------------
# Creating another list.
# -----------------------------------------------------------------------------
new_numbers = [40, 50, 60]

# -----------------------------------------------------------------------------
# Displaying the second list.
# -----------------------------------------------------------------------------
print("New List :", new_numbers)
# Output:
# New List : [40, 50, 60]

print()

# -----------------------------------------------------------------------------
# Extending the first list with the second list.
# -----------------------------------------------------------------------------
numbers.extend(new_numbers)

# -----------------------------------------------------------------------------
# Displaying the updated list.
# -----------------------------------------------------------------------------
print("After Extending :", numbers)
# Output:
# After Extending : [10, 20, 30, 40, 50, 60]

print()

# -----------------------------------------------------------------------------
# Extending the list with another list of strings.
# -----------------------------------------------------------------------------
numbers.extend(["Python", "Java"])

# -----------------------------------------------------------------------------
# Displaying the updated list.
# -----------------------------------------------------------------------------
print("After Adding Strings :", numbers)
# Output:
# After Adding Strings : [10, 20, 30, 40, 50, 60, 'Python', 'Java']

print()

# -----------------------------------------------------------------------------
# Displaying the total number of elements.
# -----------------------------------------------------------------------------
print("Total Elements :", len(numbers))
# Output:
# Total Elements : 8
