"""
===============================================================================
File Name    : 87-Clear-Dictionary.py
Description  : Clear a Dictionary in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
The clear() method is used to remove all key-value pairs from a dictionary.
After calling this method, the dictionary becomes empty, but the dictionary
object still exists.

Syntax:
dictionary_name.clear()

Example:
student.clear()
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
# Displaying the total number of key-value pairs before clearing.
# -----------------------------------------------------------------------------
print("Key-Value Pairs Before Clear :", len(student))
# Output:
# Key-Value Pairs Before Clear : 5

print()

# -----------------------------------------------------------------------------
# Removing all key-value pairs from the dictionary.
# -----------------------------------------------------------------------------
student.clear()

# -----------------------------------------------------------------------------
# Displaying the dictionary after clearing.
# -----------------------------------------------------------------------------
print("Dictionary After clear() :", student)
# Output:
# Dictionary After clear() : {}

print()

# -----------------------------------------------------------------------------
# Displaying the total number of key-value pairs after clearing.
# -----------------------------------------------------------------------------
print("Key-Value Pairs After Clear :", len(student))
# Output:
# Key-Value Pairs After Clear : 0

print()

# -----------------------------------------------------------------------------
# Displaying the type of the dictionary.
# -----------------------------------------------------------------------------
print("Type of Dictionary :", type(student))
# Output:
# Type of Dictionary : <class 'dict'>
