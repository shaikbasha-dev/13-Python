"""
===============================================================================
File Name    : 84-Remove-Key-Using-Pop.py
Description  : Remove a Key Using pop() in Python Dictionary
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
The pop() method is used to remove a specified key from a dictionary and
returns the corresponding value.

Syntax:
dictionary_name.pop(key)

Example:
student.pop("marks")
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
# Removing the "marks" key using the pop() method.
# -----------------------------------------------------------------------------
removed_value = student.pop("marks")

# -----------------------------------------------------------------------------
# Displaying the removed value.
# -----------------------------------------------------------------------------
print("Removed Value :", removed_value)
# Output:
# Removed Value : 95

# -----------------------------------------------------------------------------
# Displaying the updated dictionary.
# -----------------------------------------------------------------------------
print("Dictionary After Removing 'marks' :", student)
# Output:
# Dictionary After Removing 'marks' :
# {'id': 101, 'name': 'Rahul', 'course': 'Python', 'city': 'Hyderabad'}

print()

# -----------------------------------------------------------------------------
# Removing another key using the pop() method.
# -----------------------------------------------------------------------------
removed_value = student.pop("city")

# -----------------------------------------------------------------------------
# Displaying the removed value.
# -----------------------------------------------------------------------------
print("Removed Value :", removed_value)
# Output:
# Removed Value : Hyderabad

# -----------------------------------------------------------------------------
# Displaying the updated dictionary.
# -----------------------------------------------------------------------------
print("Dictionary After Removing 'city' :", student)
# Output:
# Dictionary After Removing 'city' :
# {'id': 101, 'name': 'Rahul', 'course': 'Python'}

print()

# -----------------------------------------------------------------------------
# Displaying the total number of key-value pairs.
# -----------------------------------------------------------------------------
print("Total Key-Value Pairs :", len(student))
# Output:
# Total Key-Value Pairs : 3
