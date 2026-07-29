"""
===============================================================================
File Name    : 81-Add-Key-Value-Pair-to-Dictionary.py
Description  : Add a Key-Value Pair to a Dictionary in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A new key-value pair can be added to a dictionary by assigning a value to a
new key. If the key already exists, its value will be updated.

Syntax:
dictionary_name[key] = value

Example:
student["course"] = "Python"
"""

# -----------------------------------------------------------------------------
# Creating a student dictionary.
# -----------------------------------------------------------------------------
student = {
    "id": 101,
    "name": "Rahul"
}

# -----------------------------------------------------------------------------
# Displaying the original dictionary.
# -----------------------------------------------------------------------------
print("Original Dictionary :", student)
# Output:
# Original Dictionary : {'id': 101, 'name': 'Rahul'}

print()

# -----------------------------------------------------------------------------
# Adding a new key-value pair for course.
# -----------------------------------------------------------------------------
student["course"] = "Python"

# -----------------------------------------------------------------------------
# Displaying the updated dictionary.
# -----------------------------------------------------------------------------
print("After Adding Course :", student)
# Output:
# After Adding Course :
# {'id': 101, 'name': 'Rahul', 'course': 'Python'}

print()

# -----------------------------------------------------------------------------
# Adding a new key-value pair for marks.
# -----------------------------------------------------------------------------
student["marks"] = 95

# -----------------------------------------------------------------------------
# Displaying the updated dictionary.
# -----------------------------------------------------------------------------
print("After Adding Marks :", student)
# Output:
# After Adding Marks :
# {'id': 101, 'name': 'Rahul', 'course': 'Python', 'marks': 95}

print()

# -----------------------------------------------------------------------------
# Adding a new key-value pair for city.
# -----------------------------------------------------------------------------
student["city"] = "Hyderabad"

# -----------------------------------------------------------------------------
# Displaying the final dictionary.
# -----------------------------------------------------------------------------
print("Final Dictionary :", student)
# Output:
# Final Dictionary :
# {'id': 101, 'name': 'Rahul', 'course': 'Python',
#  'marks': 95, 'city': 'Hyderabad'}

print()

# -----------------------------------------------------------------------------
# Displaying the total number of key-value pairs.
# -----------------------------------------------------------------------------
print("Total Key-Value Pairs :", len(student))
# Output:
# Total Key-Value Pairs : 5
