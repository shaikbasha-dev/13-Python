"""
===============================================================================
File Name    : 109-Multiple-Objects.py
Description  : Multiple Objects in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Multiple objects are separate instances created from the same class. Each
object has its own memory location and can store different values.

Unlike assigning one object reference to another variable, creating multiple
objects allocates separate memory for each object.

Syntax:
object1 = ClassName()
object2 = ClassName()

Example:
student1 = Student("Basha", 25)
student2 = Student("Rahul", 22)
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
        # Displaying the object information.
        # ---------------------------------------------------------------------
        print("Student Name :", self.name)
        print("Student Age  :", self.age)


# -----------------------------------------------------------------------------
# Creating the first object.
# -----------------------------------------------------------------------------
student1 = Student("Basha", 25)

# -----------------------------------------------------------------------------
# Creating the second object.
# -----------------------------------------------------------------------------
student2 = Student("Rahul", 22)

# -----------------------------------------------------------------------------
# Displaying details of the first object.
# -----------------------------------------------------------------------------
print("First Object")
student1.display()
# Output:
# First Object
# Student Name : Basha
# Student Age  : 25

print()

# -----------------------------------------------------------------------------
# Displaying details of the second object.
# -----------------------------------------------------------------------------
print("Second Object")
student2.display()
# Output:
# Second Object
# Student Name : Rahul
# Student Age  : 22

print()

# -----------------------------------------------------------------------------
# Displaying the memory addresses of both objects.
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
# student1 is student2 : False
