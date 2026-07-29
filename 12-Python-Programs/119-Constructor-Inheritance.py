"""
===============================================================================
File Name    : 119-Constructor-Inheritance.py
Description  : Constructor Inheritance in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Constructor Inheritance is the process of calling the constructor of the
parent class from the child class. This allows the child class to inherit
and initialize the parent class properties before initializing its own
properties.

Syntax:

class Parent:

    def __init__(self):
        pass

class Child(Parent):

    def __init__(self):
        super().__init__()

Example:
Student inherits the constructor of Person.
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
        print("Person constructor is called.")

    # -------------------------------------------------------------------------
    # Creating a method to display person details.
    # -------------------------------------------------------------------------
    def display_person(self):

        # ---------------------------------------------------------------------
        # Displaying Parent class information.
        # ---------------------------------------------------------------------
        print("Name   :", self.name)
        print("Age    :", self.age)


# -----------------------------------------------------------------------------
# Creating the Child class.
# -----------------------------------------------------------------------------
class Student(Person):

    # -------------------------------------------------------------------------
    # Defining the constructor of the Child class.
    # -------------------------------------------------------------------------
    def __init__(self):

        # ---------------------------------------------------------------------
        # Calling the Parent class constructor.
        # ---------------------------------------------------------------------
        super().__init__()

        # ---------------------------------------------------------------------
        # Initializing Child class instance variable.
        # ---------------------------------------------------------------------
        self.course = "Python"

        # ---------------------------------------------------------------------
        # Displaying a message.
        # ---------------------------------------------------------------------
        print("Student constructor is called.")

    # -------------------------------------------------------------------------
    # Creating a method to display student details.
    # -------------------------------------------------------------------------
    def display_student(self):

        # ---------------------------------------------------------------------
        # Calling the Parent class method.
        # ---------------------------------------------------------------------
        self.display_person()

        # ---------------------------------------------------------------------
        # Displaying Child class information.
        # ---------------------------------------------------------------------
        print("Course :", self.course)


# -----------------------------------------------------------------------------
# Creating an object of the Child class.
# -----------------------------------------------------------------------------
student = Student()

# -----------------------------------------------------------------------------
# Calling the Child class method.
# -----------------------------------------------------------------------------
student.display_student()

# Output:
# Person constructor is called.
# Student constructor is called.
# Name   : Basha
# Age    : 25
# Course : Python
