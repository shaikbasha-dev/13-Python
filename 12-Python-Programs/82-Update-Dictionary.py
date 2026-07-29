"""
===============================================================================
File Name    : 82-Update-Dictionary.py
Description  : Update a Dictionary in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A dictionary can be updated by changing the value of an existing key or by
using the update() method to add or modify multiple key-value pairs.

Syntax:
dictionary_name[key] = new_value

or

dictionary_name.update({key: value})

Example:
student["marks"] = 98
student.update({"course": "Java"})
"""

# -----------------------------------------------------------------------------
# Creating a student dictionary.
# -----------------------------------------------------------------------------
student = {
    "id": 101,
    "name": "Rahul",
    "course": "Python",
    "marks": 95
}

# -----------------------------------------------------------------------------
# Displaying the original dictionary.
# -----------------------------------------------------------------------------
print("Original Dictionary :", student)
# Output:
# Original Dictionary :
# {'id': 101, 'name': 'Rahul', 'course': 'Python', 'marks': 95}

print()

# -----------------------------------------------------------------------------
# Updating the value of the course key.
# -----------------------------------------------------------------------------
student["course"] = "Java"

# -----------------------------------------------------------------------------
# Displaying the updated dictionary.
# -----------------------------------------------------------------------------
print("After Updating Course :", student)
# Output:
# After Updating Course :
# {'id': 101, 'name': 'Rahul', 'course': 'Java', 'marks': 95}

print()

# -----------------------------------------------------------------------------
# Updating the value of the marks key.
# -----------------------------------------------------------------------------
student["marks"] = 98

# -----------------------------------------------------------------------------
# Displaying the updated dictionary.
# -----------------------------------------------------------------------------
print("After Updating Marks :", student)
# Output:
# After Updating Marks :
# {'id': 101, 'name': 'Rahul', 'course': 'Java', 'marks': 98}

print()

# -----------------------------------------------------------------------------
# Updating multiple key-value pairs using the update() method.
# -----------------------------------------------------------------------------
student.update({
    "city": "Hyderabad",
    "mobile": "9876543210"
})

# -----------------------------------------------------------------------------
# Displaying the final dictionary.
# -----------------------------------------------------------------------------
print("After update() Method :", student)
# Output:
# After update() Method :
# {'id': 101, 'name': 'Rahul', 'course': 'Java',
#  'marks': 98, 'city': 'Hyderabad', 'mobile': '9876543210'}

print()

# -----------------------------------------------------------------------------
# Displaying the total number of key-value pairs.
# -----------------------------------------------------------------------------
print("Total Key-Value Pairs :", len(student))
# Output:
# Total Key-Value Pairs : 6
