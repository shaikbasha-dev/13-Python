"""
===============================================================================
File Name    : 130-Protected-Access-Specifier.py
Description  : Protected Access Specifier in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A Protected Access Specifier is used to indicate that class variables and
methods are intended to be accessed within the class and its child classes.

In Python, protected members are created by prefixing their names with a
single underscore (_). This is a naming convention and not a strict access
restriction.

Syntax:

class ClassName:

    def __init__(self):
        self._variable = value

    def _method(self):
        pass

Example:
Student inherits protected members from Person.
"""

# -----------------------------------------------------------------------------
# Creating the Parent class.
# -----------------------------------------------------------------------------
class Person:

    # -------------------------------------------------------------------------
    # Defining the constructor.
    # -------------------------------------------------------------------------
    def __init__(self):

        # ---------------------------------------------------------------------
        # Initializing protected instance variables.
        # ---------------------------------------------------------------------
        self._name = "Basha"
        self._age = 25

    # -------------------------------------------------------------------------
    # Creating a protected method.
    # -------------------------------------------------------------------------
    def _display_person(self):

        # ---------------------------------------------------------------------
        # Displaying person information.
        # ---------------------------------------------------------------------
        print("Name :", self._name)
        print("Age  :", self._age)


# -----------------------------------------------------------------------------
# Creating the Child class.
# -----------------------------------------------------------------------------
class Student(Person):

    # -------------------------------------------------------------------------
    # Creating a method in the Child class.
    # -------------------------------------------------------------------------
    def display_student(self):

        # ---------------------------------------------------------------------
        # Accessing protected variables inherited from the Parent class.
        # ---------------------------------------------------------------------
        print("Student Name :", self._name)
        print("Student Age  :", self._age)

        # ---------------------------------------------------------------------
        # Calling the protected method of the Parent class.
        # ---------------------------------------------------------------------
        self._display_person()


# -----------------------------------------------------------------------------
# Creating an object of the Child class.
# -----------------------------------------------------------------------------
student = Student()

# -----------------------------------------------------------------------------
# Calling the Child class method.
# -----------------------------------------------------------------------------
student.display_student()

# -----------------------------------------------------------------------------
# Accessing protected members outside the class.
# This is possible in Python but is discouraged by convention.
# -----------------------------------------------------------------------------
print("\nAccessing Protected Members Outside the Class:")
print("Name :", student._name)
print("Age  :", student._age)

# Output:
# Student Name : Basha
# Student Age  : 25
# Name : Basha
# Age  : 25
#
# Accessing Protected Members Outside the Class:
# Name : Basha
# Age  : 25
