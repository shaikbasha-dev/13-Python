"""
===============================================================================
File Name    : 60-Change-List-Element.py
Description  : Change a List Element in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
List elements can be changed by assigning a new value to an existing index.
Since lists are mutable, their elements can be modified after creation.

Syntax:
list_name[index] = new_value

Example:
numbers[2] = 30
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
# Changing the first element.
# -----------------------------------------------------------------------------
numbers[0] = 100

# -----------------------------------------------------------------------------
# Displaying the updated list.
# -----------------------------------------------------------------------------
print("After Changing First Element :", numbers)
# Output:
# After Changing First Element : [100, 20, 30, 40, 50]

print()

# -----------------------------------------------------------------------------
# Changing the third element.
# -----------------------------------------------------------------------------
numbers[2] = 300

# -----------------------------------------------------------------------------
# Displaying the updated list.
# -----------------------------------------------------------------------------
print("After Changing Third Element :", numbers)
# Output:
# After Changing Third Element : [100, 20, 300, 40, 50]

print()

# -----------------------------------------------------------------------------
# Changing the last element.
# -----------------------------------------------------------------------------
numbers[4] = 500

# -----------------------------------------------------------------------------
# Displaying the updated list.
# -----------------------------------------------------------------------------
print("After Changing Last Element :", numbers)
# Output:
# After Changing Last Element : [100, 20, 300, 40, 500]

print()

# -----------------------------------------------------------------------------
# Displaying the total number of elements in the list.
# -----------------------------------------------------------------------------
print("Total Elements :", len(numbers))
# Output:
# Total Elements : 5
