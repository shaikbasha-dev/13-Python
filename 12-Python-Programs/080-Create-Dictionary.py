"""
===============================================================================
File Name    : 80-Create-Dictionary.py
Description  : Create a Dictionary in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A dictionary is a built-in collection data type used to store data as
key-value pairs. Dictionaries are mutable, unordered, and keys must be unique.

Syntax:
dictionary_name = {
    key1: value1,
    key2: value2
}

Example:
student = {
    "id": 101,
    "name": "Rahul"
}
"""

# -----------------------------------------------------------------------------
# Creating a dictionary with integer values.
# -----------------------------------------------------------------------------
numbers = {
    1: 10,
    2: 20,
    3: 30
}

# -----------------------------------------------------------------------------
# Displaying the integer dictionary.
# -----------------------------------------------------------------------------
print("Integer Dictionary :", numbers)
# Output:
# Integer Dictionary : {1: 10, 2: 20, 3: 30}

print()

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
# Displaying the student dictionary.
# -----------------------------------------------------------------------------
print("Student Dictionary :", student)
# Output:
# Student Dictionary :
# {'id': 101, 'name': 'Rahul', 'course': 'Python', 'marks': 95}

print()

# -----------------------------------------------------------------------------
# Creating a mixed data type dictionary.
# -----------------------------------------------------------------------------
employee = {
    "id": 1001,
    "name": "Amit",
    "salary": 45000.50,
    "is_permanent": True
}

# -----------------------------------------------------------------------------
# Displaying the mixed dictionary.
# -----------------------------------------------------------------------------
print("Employee Dictionary :", employee)
# Output:
# Employee Dictionary :
# {'id': 1001, 'name': 'Amit', 'salary': 45000.5, 'is_permanent': True}

print()

# -----------------------------------------------------------------------------
# Creating an empty dictionary.
# -----------------------------------------------------------------------------
empty_dictionary = {}

# -----------------------------------------------------------------------------
# Displaying the empty dictionary.
# -----------------------------------------------------------------------------
print("Empty Dictionary :", empty_dictionary)
# Output:
# Empty Dictionary : {}

print()

# -----------------------------------------------------------------------------
# Displaying the type of the dictionary.
# -----------------------------------------------------------------------------
print("Type of student :", type(student))
# Output:
# Type of student : <class 'dict'>
