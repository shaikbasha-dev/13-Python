"""
===============================================================================
File Name    : 83-Access-Dictionary-Elements.py
Description  : Access Dictionary Elements in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Dictionary elements can be accessed using their keys. Since dictionaries
store data as key-value pairs, each key is used to retrieve its corresponding
value.

Syntax:
dictionary_name[key]

Example:
student["name"]
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
print("Student Dictionary :", student)
# Output:
# Student Dictionary :
# {'id': 101, 'name': 'Rahul', 'course': 'Python',
#  'marks': 95, 'city': 'Hyderabad'}

print()

# -----------------------------------------------------------------------------
# Accessing the value using the id key.
# -----------------------------------------------------------------------------
print("Student ID :", student["id"])
# Output:
# Student ID : 101

# -----------------------------------------------------------------------------
# Accessing the value using the name key.
# -----------------------------------------------------------------------------
print("Student Name :", student["name"])
# Output:
# Student Name : Rahul

# -----------------------------------------------------------------------------
# Accessing the value using the course key.
# -----------------------------------------------------------------------------
print("Course :", student["course"])
# Output:
# Course : Python

# -----------------------------------------------------------------------------
# Accessing the value using the marks key.
# -----------------------------------------------------------------------------
print("Marks :", student["marks"])
# Output:
# Marks : 95

# -----------------------------------------------------------------------------
# Accessing the value using the city key.
# -----------------------------------------------------------------------------
print("City :", student["city"])
# Output:
# City : Hyderabad

print()

# -----------------------------------------------------------------------------
# Displaying the total number of key-value pairs.
# -----------------------------------------------------------------------------
print("Total Key-Value Pairs :", len(student))
# Output:
# Total Key-Value Pairs : 5
