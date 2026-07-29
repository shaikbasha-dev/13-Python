"""
===============================================================================
File Name    : 57-Append-Element-to-List.py
Description  : Append an Element to a List in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
The append() method is used to add a single element to the end of a list.

Syntax:
list_name.append(element)

Example:
numbers.append(60)
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
# Appending a new integer element to the list.
# -----------------------------------------------------------------------------
numbers.append(60)

# -----------------------------------------------------------------------------
# Displaying the updated list.
# -----------------------------------------------------------------------------
print("After Appending 60 :", numbers)
# Output:
# After Appending 60 : [10, 20, 30, 40, 50, 60]

print()

# -----------------------------------------------------------------------------
# Appending a string element to the list.
# -----------------------------------------------------------------------------
numbers.append("Python")

# -----------------------------------------------------------------------------
# Displaying the updated list.
# -----------------------------------------------------------------------------
print("After Appending 'Python' :", numbers)
# Output:
# After Appending 'Python' : [10, 20, 30, 40, 50, 60, 'Python']

print()

# -----------------------------------------------------------------------------
# Appending a Boolean value to the list.
# -----------------------------------------------------------------------------
numbers.append(True)

# -----------------------------------------------------------------------------
# Displaying the final list.
# -----------------------------------------------------------------------------
print("Final List :", numbers)
# Output:
# Final List : [10, 20, 30, 40, 50, 60, 'Python', True]

print()

# -----------------------------------------------------------------------------
# Displaying the total number of elements in the list.
# -----------------------------------------------------------------------------
print("Total Elements :", len(numbers))
# Output:
# Total Elements : 8
