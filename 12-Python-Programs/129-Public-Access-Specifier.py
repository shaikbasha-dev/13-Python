"""
===============================================================================
File Name    : 129-Public-Access-Specifier.py
Description  : Public Access Specifier in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A Public Access Specifier allows class variables and methods to be accessed
from anywhere in the program.

In Python, members are public by default. They can be accessed both inside
and outside the class.

Syntax:

class ClassName:

    def __init__(self):
        self.variable = value

    def method(self):
        pass

Example:
Student class with public variables and methods.
"""

# -----------------------------------------------------------------------------
# Creating the Student class.
# -----------------------------------------------------------------------------
class Student:

    # -------------------------------------------------------------------------
    # Defining the constructor.
    # -------------------------------------------------------------------------
    def __init__(self):

        # ---------------------------------------------------------------------
        # Initializing public instance variables.
        # ---------------------------------------------------------------------
        self.name = "Basha"
        self.course = "Python"

    # -------------------------------------------------------------------------
    # Creating a public method.
    # -------------------------------------------------------------------------
    def display_details(self):

        # ---------------------------------------------------------------------
        # Displaying student information.
        # ---------------------------------------------------------------------
        print("Name   :", self.name)
        print("Course :", self.course)


# -----------------------------------------------------------------------------
# Creating an object of the Student class.
# -----------------------------------------------------------------------------
student = Student()

# -----------------------------------------------------------------------------
# Accessing public variables outside the class.
# -----------------------------------------------------------------------------
print("Student Name   :", student.name)
print("Student Course :", student.course)

# -----------------------------------------------------------------------------
# Calling the public method outside the class.
# -----------------------------------------------------------------------------
student.display_details()

# -----------------------------------------------------------------------------
# Modifying public variables outside the class.
# -----------------------------------------------------------------------------
student.name = "Mahaboob Basha"
student.course = "Java Full Stack"

# -----------------------------------------------------------------------------
# Displaying the updated values.
# -----------------------------------------------------------------------------
print("\nAfter Modifying Public Variables:")

# -----------------------------------------------------------------------------
# Calling the public method again.
# -----------------------------------------------------------------------------
student.display_details()

# Output:
# Student Name   : Basha
# Student Course : Python
# Name   : Basha
# Course : Python
#
# After Modifying Public Variables:
# Name   : Mahaboob Basha
# Course : Java Full Stack
