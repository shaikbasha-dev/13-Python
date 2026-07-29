"""
===============================================================================
File Name    : 108-Single-Object.py
Description  : Single Object in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A single object is an object created from a class. Multiple variables can
refer to the same object.

In Python, assigning one object reference to another variable does not create
a new object. Instead, both variables point to the same object in memory.

Syntax:
object2 = object1

Example:
student2 = student1
"""

# -----------------------------------------------------------------------------
# Creating a class.
# -----------------------------------------------------------------------------
class Student:

    # -------------------------------------------------------------------------
    # Initializing the object.
    # -------------------------------------------------------------------------
    def __init__(self, name, age):

        # ---------------------------------------------------------------------
        # Assigning values to instance variables.
        # ---------------------------------------------------------------------
        self.name = name
        self.age = age

    # -------------------------------------------------------------------------
    # Creating a method to display object details.
    # -------------------------------------------------------------------------
    def display(self):

        # ---------------------------------------------------------------------
        # Displaying object information.
        # ---------------------------------------------------------------------
        print("Student Name :", self.name)
        print("Student Age  :", self.age)


# -----------------------------------------------------------------------------
# Creating a single object.
# -----------------------------------------------------------------------------
student1 = Student("Basha", 25)

# -----------------------------------------------------------------------------
# Assigning the same object reference to another variable.
# -----------------------------------------------------------------------------
student2 = student1

# -----------------------------------------------------------------------------
# Displaying the details using the first reference.
# -----------------------------------------------------------------------------
print("Using student1")
student1.display()
# Output:
# Using student1
# Student Name : Basha
# Student Age  : 25

print()

# -----------------------------------------------------------------------------
# Displaying the details using the second reference.
# -----------------------------------------------------------------------------
print("Using student2")
student2.display()
# Output:
# Using student2
# Student Name : Basha
# Student Age  : 25

print()

# -----------------------------------------------------------------------------
# Displaying the memory addresses of both variables.
# -----------------------------------------------------------------------------
print("Address of student1 :", id(student1))
# Output:
# Address of student1 : (Memory Address)

print("Address of student2 :", id(student2))
# Output:
# Address of student2 : (Memory Address)

print()

# -----------------------------------------------------------------------------
# Checking whether both variables refer to the same object.
# -----------------------------------------------------------------------------
print("student1 is student2 :", student1 is student2)
# Output:
# student1 is student2 : True
