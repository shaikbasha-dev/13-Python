"""
===============================================================================
File Name    : 86-Delete-Key-Using-Del.py
Description  : Delete a Key Using del in Python Dictionary
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
The del keyword is used to delete a specified key-value pair from a dictionary.
If the specified key does not exist, a KeyError occurs.

Syntax:
del dictionary_name[key]

Example:
del student["marks"]
"""

# -----------------------------------------------------------------------------
# Creating a student dictionary.
# -----------------------------------------------------------------------------
student = {
    "id": 101,
    "name": "Rahul",
    "course": "Python",
    "marks": 95,
    "city": "Hyderabad"
}

# -----------------------------------------------------------------------------
# Displaying the original dictionary.
# -----------------------------------------------------------------------------
print("Original Dictionary :", student)
# Output:
# Original Dictionary :
# {'id': 101, 'name': 'Rahul', 'course': 'Python',
#  'marks': 95, 'city': 'Hyderabad'}

print()

# -----------------------------------------------------------------------------
# Deleting the "marks" key from the dictionary.
# -----------------------------------------------------------------------------
del student["marks"]

# -----------------------------------------------------------------------------
# Displaying the updated dictionary.
# -----------------------------------------------------------------------------
print("After Deleting 'marks' :", student)
# Output:
# After Deleting 'marks' :
# {'id': 101, 'name': 'Rahul', 'course': 'Python', 'city': 'Hyderabad'}

print()

# -----------------------------------------------------------------------------
# Deleting the "city" key from the dictionary.
# -----------------------------------------------------------------------------
del student["city"]

# -----------------------------------------------------------------------------
# Displaying the updated dictionary.
# -----------------------------------------------------------------------------
print("After Deleting 'city' :", student)
# Output:
# After Deleting 'city' :
# {'id': 101, 'name': 'Rahul', 'course': 'Python'}

print()

# -----------------------------------------------------------------------------
# Displaying the total number of key-value pairs.
# -----------------------------------------------------------------------------
print("Total Key-Value Pairs :", len(student))
# Output:
# Total Key-Value Pairs : 3

print()

# -----------------------------------------------------------------------------
# Attempting to delete a key that does not exist.
# -----------------------------------------------------------------------------
del student["age"]

# Output:
# KeyError: 'age'
