"""
===============================================================================
File Name    : 110-Constructor.py
Description  : Constructor in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A constructor is a special method that is automatically executed when an
object is created. In Python, the constructor is written using the __init__()
method.

Purpose of Constructor:
1. Initialize object data.
2. Assign values to instance variables.
3. Perform initialization tasks during object creation.

Syntax:
class ClassName:

    def __init__(self, parameters):
        # Initialization code

Example:
student = Student("Basha", 25)
"""

# -----------------------------------------------------------------------------
# Creating a class.
# -----------------------------------------------------------------------------
class Student:

    # -------------------------------------------------------------------------
    # Defining the constructor.
    # -------------------------------------------------------------------------
    def __init__(self, name, age):

        # ---------------------------------------------------------------------
        # Initializing instance variables.
        # ---------------------------------------------------------------------
        self.name = name
        self.age = age

        # ---------------------------------------------------------------------
        # Displaying a message when the constructor is executed.
        # ---------------------------------------------------------------------
        print("Constructor Executed")

    # -------------------------------------------------------------------------
    # Creating a method to display student details.
    # -------------------------------------------------------------------------
    def display(self):

        # ---------------------------------------------------------------------
        # Displaying the object data.
        # ---------------------------------------------------------------------
        print("Student Name :", self.name)
        print("Student Age  :", self.age)


# -----------------------------------------------------------------------------
# Creating the first object.
# -----------------------------------------------------------------------------
student1 = Student("Basha", 25)
# Output:
# Constructor Executed

print()

# -----------------------------------------------------------------------------
# Displaying the details of the first object.
# -----------------------------------------------------------------------------
student1.display()
# Output:
# Student Name : Basha
# Student Age  : 25

print()

# -----------------------------------------------------------------------------
# Creating the second object.
# -----------------------------------------------------------------------------
student2 = Student("Rahul", 22)
# Output:
# Constructor Executed

print()

# -----------------------------------------------------------------------------
# Displaying the details of the second object.
# -----------------------------------------------------------------------------
student2.display()
# Output:
# Student Name : Rahul
# Student Age  : 22
