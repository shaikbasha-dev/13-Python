"""
===============================================================================
File Name    : 59-Insert-Element-into-List.py
Description  : Insert an Element into a List in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
The insert() method is used to insert an element at a specified position
(index) in a list.

Syntax:
list_name.insert(index, element)

Example:
numbers.insert(2, 30)
"""

# -----------------------------------------------------------------------------
# Creating a list of integers.
# -----------------------------------------------------------------------------
numbers = [10, 20, 40, 50]

# -----------------------------------------------------------------------------
# Displaying the original list.
# -----------------------------------------------------------------------------
print("Original List :", numbers)
# Output:
# Original List : [10, 20, 40, 50]

print()

# -----------------------------------------------------------------------------
# Inserting an element at index 2.
# -----------------------------------------------------------------------------
numbers.insert(2, 30)

# -----------------------------------------------------------------------------
# Displaying the updated list.
# -----------------------------------------------------------------------------
print("After Inserting 30 at Index 2 :", numbers)
# Output:
# After Inserting 30 at Index 2 : [10, 20, 30, 40, 50]

print()

# -----------------------------------------------------------------------------
# Inserting an element at the beginning of the list.
# -----------------------------------------------------------------------------
numbers.insert(0, 5)

# -----------------------------------------------------------------------------
# Displaying the updated list.
# -----------------------------------------------------------------------------
print("After Inserting 5 at Index 0 :", numbers)
# Output:
# After Inserting 5 at Index 0 : [5, 10, 20, 30, 40, 50]

print()

# -----------------------------------------------------------------------------
# Inserting a string element into the list.
# -----------------------------------------------------------------------------
numbers.insert(3, "Python")

# -----------------------------------------------------------------------------
# Displaying the updated list.
# -----------------------------------------------------------------------------
print("After Inserting 'Python' at Index 3 :", numbers)
# Output:
# After Inserting 'Python' at Index 3 : [5, 10, 20, 'Python', 30, 40, 50]

print()

# -----------------------------------------------------------------------------
# Displaying the total number of elements in the list.
# -----------------------------------------------------------------------------
print("Total Elements :", len(numbers))
# Output:
# Total Elements : 7
