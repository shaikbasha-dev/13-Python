"""
===============================================================================
File Name    : 85-Remove-Last-Key-Using-Popitem.py
Description  : Remove the Last Key Using popitem() in Python Dictionary
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
The popitem() method is used to remove and return the last inserted key-value
pair from a dictionary.

Syntax:
dictionary_name.popitem()

Example:
student.popitem()
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
# Removing the last inserted key-value pair.
# -----------------------------------------------------------------------------
removed_item = student.popitem()

# -----------------------------------------------------------------------------
# Displaying the removed key-value pair.
# -----------------------------------------------------------------------------
print("Removed Key-Value Pair :", removed_item)
# Output:
# Removed Key-Value Pair : ('city', 'Hyderabad')

# -----------------------------------------------------------------------------
# Displaying the updated dictionary.
# -----------------------------------------------------------------------------
print("Dictionary After First popitem() :", student)
# Output:
# Dictionary After First popitem() :
# {'id': 101, 'name': 'Rahul', 'course': 'Python', 'marks': 95}

print()

# -----------------------------------------------------------------------------
# Removing another last inserted key-value pair.
# -----------------------------------------------------------------------------
removed_item = student.popitem()

# -----------------------------------------------------------------------------
# Displaying the removed key-value pair.
# -----------------------------------------------------------------------------
print("Removed Key-Value Pair :", removed_item)
# Output:
# Removed Key-Value Pair : ('marks', 95)

# -----------------------------------------------------------------------------
# Displaying the updated dictionary.
# -----------------------------------------------------------------------------
print("Dictionary After Second popitem() :", student)
# Output:
# Dictionary After Second popitem() :
# {'id': 101, 'name': 'Rahul', 'course': 'Python'}

print()

# -----------------------------------------------------------------------------
# Displaying the total number of key-value pairs.
# -----------------------------------------------------------------------------
print("Total Key-Value Pairs :", len(student))
# Output:
# Total Key-Value Pairs : 3
