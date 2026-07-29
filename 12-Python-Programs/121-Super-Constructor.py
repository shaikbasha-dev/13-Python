"""
===============================================================================
File Name    : 121-Super-Constructor.py
Description  : super() Constructor in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
The super() constructor is used to call the constructor of the parent class
from the child class. It helps initialize the parent class before executing
the child class constructor.

Syntax:

class Parent:

    def __init__(self):
        pass

class Child(Parent):

    def __init__(self):
        super().__init__()

Example:
Student calls the constructor of Person using super().
"""

# -----------------------------------------------------------------------------
# Creating the Parent class.
# -----------------------------------------------------------------------------
class Person:

    # -------------------------------------------------------------------------
    # Defining the constructor of the Parent class.
    # -------------------------------------------------------------------------
    def __init__(self):

        # ---------------------------------------------------------------------
        # Initializing Parent class instance variables.
        # ---------------------------------------------------------------------
        self.name = "Basha"
        self.age = 25

        # ---------------------------------------------------------------------
        # Displaying a message.
        # ---------------------------------------------------------------------
        print("Person constructor executed.")


# -----------------------------------------------------------------------------
# Creating the Child class.
# -----------------------------------------------------------------------------
class Student(Person):

    # -------------------------------------------------------------------------
    # Defining the constructor of the Child class.
    # -------------------------------------------------------------------------
    def __init__(self):

        # ---------------------------------------------------------------------
        # Calling the Parent class constructor using super().
        # ---------------------------------------------------------------------
        super().__init__()

        # ---------------------------------------------------------------------
        # Initializing Child class instance variable.
        # ---------------------------------------------------------------------
        self.course = "Python"

        # ---------------------------------------------------------------------
        # Displaying a message.
        # ---------------------------------------------------------------------
        print("Student constructor executed.")

    # -------------------------------------------------------------------------
    # Creating a method to display all details.
    # -------------------------------------------------------------------------
    def display_details(self):

        # ---------------------------------------------------------------------
        # Displaying Parent class data.
        # ---------------------------------------------------------------------
        print("Name   :", self.name)
        print("Age    :", self.age)

        # ---------------------------------------------------------------------
        # Displaying Child class data.
        # ---------------------------------------------------------------------
        print("Course :", self.course)


# -----------------------------------------------------------------------------
# Creating an object of the Child class.
# -----------------------------------------------------------------------------
student = Student()

# -----------------------------------------------------------------------------
# Calling the display method.
# -----------------------------------------------------------------------------
student.display_details()

# Output:
# Person constructor executed.
# Student constructor executed.
# Name   : Basha
# Age    : 25
# Course : Python
