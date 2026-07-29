"""
===============================================================================
File Name    : 137-Magic-or-Dunder-Methods.py
Description  : Magic (Dunder) Methods in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Magic Methods, also called Dunder (Double Underscore) Methods, are special
methods in Python that begin and end with double underscores (__).

These methods allow Python to automatically perform special operations such
as object creation, string representation, arithmetic operations, comparison,
and more.

Syntax:

class ClassName:

    def __init__(self):
        pass

    def __str__(self):
        pass

Example:
Student class using __init__() and __str__() magic methods.
"""

# -----------------------------------------------------------------------------
# Creating the Student class.
# -----------------------------------------------------------------------------
class Student:

    # -------------------------------------------------------------------------
    # Defining the constructor (__init__) magic method.
    # -------------------------------------------------------------------------
    def __init__(self, name, course):

        # ---------------------------------------------------------------------
        # Initializing instance variables.
        # ---------------------------------------------------------------------
        self.name = name
        self.course = course

    # -------------------------------------------------------------------------
    # Defining the __str__() magic method.
    # -------------------------------------------------------------------------
    def __str__(self):

        # ---------------------------------------------------------------------
        # Returning the object as a readable string.
        # ---------------------------------------------------------------------
        return f"Student(Name: {self.name}, Course: {self.course})"


# -----------------------------------------------------------------------------
# Creating an object of the Student class.
# -----------------------------------------------------------------------------
student = Student("Basha", "Python")

# -----------------------------------------------------------------------------
# Printing the object.
# Python automatically calls the __str__() method.
# -----------------------------------------------------------------------------
print(student)

# -----------------------------------------------------------------------------
# Calling the __str__() method directly.
# -----------------------------------------------------------------------------
print(student.__str__())

# Output:
# Student(Name: Basha, Course: Python)
# Student(Name: Basha, Course: Python)
