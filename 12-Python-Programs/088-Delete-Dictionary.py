"""
===============================================================================
File Name    : 88-Delete-Dictionary.py
Description  : Delete a Dictionary in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
The del keyword is used to delete an entire dictionary from memory. After
deleting the dictionary, it can no longer be accessed.

Syntax:
del dictionary_name

Example:
del student
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
# Displaying the total number of key-value pairs.
# -----------------------------------------------------------------------------
print("Total Key-Value Pairs :", len(student))
# Output:
# Total Key-Value Pairs : 5

print()

# -----------------------------------------------------------------------------
# Deleting the entire dictionary.
# -----------------------------------------------------------------------------
del student

# -----------------------------------------------------------------------------
# Displaying a confirmation message.
# -----------------------------------------------------------------------------
print("The dictionary has been deleted successfully.")
# Output:
# The dictionary has been deleted successfully.

print()

# -----------------------------------------------------------------------------
# Attempting to access the deleted dictionary.
# -----------------------------------------------------------------------------
print(student)

# Output:
# NameError: name 'student' is not defined
