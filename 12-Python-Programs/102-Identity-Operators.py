"""
===============================================================================
File Name    : 102-Identity-Operators.py
Description  : Identity Operators in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Identity operators are used to check whether two variables refer to the same
object in memory. They compare the memory locations (object identities) rather
than the values.

Identity Operators:
1. is
2. is not

Syntax:
variable1 is variable2
variable1 is not variable2

Example:
a is b
a is not b
"""

# -----------------------------------------------------------------------------
# Creating the first list.
# -----------------------------------------------------------------------------
list1 = [10, 20, 30]

# -----------------------------------------------------------------------------
# Assigning the reference of list1 to list2.
# Both variables refer to the same object.
# -----------------------------------------------------------------------------
list2 = list1

# -----------------------------------------------------------------------------
# Creating another list with the same values.
# This is a different object in memory.
# -----------------------------------------------------------------------------
list3 = [10, 20, 30]

# -----------------------------------------------------------------------------
# Displaying the list values.
# -----------------------------------------------------------------------------
print("List 1 :", list1)
# Output:
# List 1 : [10, 20, 30]

print("List 2 :", list2)
# Output:
# List 2 : [10, 20, 30]

print("List 3 :", list3)
# Output:
# List 3 : [10, 20, 30]

print()

# -----------------------------------------------------------------------------
# Comparing whether list1 and list2 refer to the same object.
# -----------------------------------------------------------------------------
print("list1 is list2 :", list1 is list2)
# Output:
# list1 is list2 : True

# -----------------------------------------------------------------------------
# Comparing whether list1 and list3 refer to the same object.
# -----------------------------------------------------------------------------
print("list1 is list3 :", list1 is list3)
# Output:
# list1 is list3 : False

print()

# -----------------------------------------------------------------------------
# Comparing whether list1 and list2 are different objects.
# -----------------------------------------------------------------------------
print("list1 is not list2 :", list1 is not list2)
# Output:
# list1 is not list2 : False

# -----------------------------------------------------------------------------
# Comparing whether list1 and list3 are different objects.
# -----------------------------------------------------------------------------
print("list1 is not list3 :", list1 is not list3)
# Output:
# list1 is not list3 : True

print()

# -----------------------------------------------------------------------------
# Displaying the memory addresses of all three lists.
# -----------------------------------------------------------------------------
print("Address of list1 :", id(list1))
# Output:
# Address of list1 : (Memory Address)

print("Address of list2 :", id(list2))
# Output:
# Address of list2 : (Memory Address)

print("Address of list3 :", id(list3))
# Output:
# Address of list3 : (Memory Address)
