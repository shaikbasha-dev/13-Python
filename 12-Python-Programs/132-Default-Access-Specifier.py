"""
===============================================================================
File Name    : 132-Default-Access-Specifier.py
Description  : Default Access Specifier in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Python does not have a separate Default Access Specifier like some other
programming languages.

If a class variable or method is declared without any underscore prefix,
it is considered a public member by default and can be accessed from
anywhere in the program.

Syntax:

class ClassName:

    def __init__(self):
        self.variable = value

    def method(self):
        pass

Example:
Student class with default (public) members.
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
        # Initializing default (public) instance variables.
        # ---------------------------------------------------------------------
        self.name = "Basha"
        self.course = "Python"

    # -------------------------------------------------------------------------
    # Creating a default (public) method.
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
# Accessing default (public) instance variables.
# -----------------------------------------------------------------------------
print("Student Name   :", student.name)
print("Student Course :", student.course)

# -----------------------------------------------------------------------------
# Calling the default (public) method.
# -----------------------------------------------------------------------------
student.display_details()

# Output:
# Student Name   : Basha
# Student Course : Python
# Name   : Basha
# Course : Python
