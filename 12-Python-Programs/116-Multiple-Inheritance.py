"""
===============================================================================
File Name    : 116-Multiple-Inheritance.py
Description  : Multiple Inheritance in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Multiple Inheritance is a type of inheritance in which one child class
inherits the properties and methods of more than one parent class.

Syntax:

class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass

Example:
Student inherits from Person and College.
"""

# -----------------------------------------------------------------------------
# Creating the first Parent class.
# -----------------------------------------------------------------------------
class Person:

    # -------------------------------------------------------------------------
    # Defining the constructor of the first Parent class.
    # -------------------------------------------------------------------------
    def __init__(self):

        # ---------------------------------------------------------------------
        # Initializing instance variables.
        # ---------------------------------------------------------------------
        self.name = "Basha"
        self.age = 25

    # -------------------------------------------------------------------------
    # Creating a method to display person details.
    # -------------------------------------------------------------------------
    def display_person(self):

        # ---------------------------------------------------------------------
        # Displaying person information.
        # ---------------------------------------------------------------------
        print("Name    :", self.name)
        print("Age     :", self.age)


# -----------------------------------------------------------------------------
# Creating the second Parent class.
# -----------------------------------------------------------------------------
class College:

    # -------------------------------------------------------------------------
    # Defining the constructor of the second Parent class.
    # -------------------------------------------------------------------------
    def __init__(self):

        # ---------------------------------------------------------------------
        # Initializing instance variables.
        # ---------------------------------------------------------------------
        self.college_name = "ABC College"

    # -------------------------------------------------------------------------
    # Creating a method to display college details.
    # -------------------------------------------------------------------------
    def display_college(self):

        # ---------------------------------------------------------------------
        # Displaying college information.
        # ---------------------------------------------------------------------
        print("College :", self.college_name)


# -----------------------------------------------------------------------------
# Creating the Child class that inherits both Parent classes.
# -----------------------------------------------------------------------------
class Student(Person, College):

    # -------------------------------------------------------------------------
    # Defining the constructor of the Child class.
    # -------------------------------------------------------------------------
    def __init__(self):

        # ---------------------------------------------------------------------
        # Calling the constructor of the first Parent class.
        # ---------------------------------------------------------------------
        Person.__init__(self)

        # ---------------------------------------------------------------------
        # Calling the constructor of the second Parent class.
        # ---------------------------------------------------------------------
        College.__init__(self)

        # ---------------------------------------------------------------------
        # Initializing child class instance variable.
        # ---------------------------------------------------------------------
        self.course = "Python"

    # -------------------------------------------------------------------------
    # Creating a method to display student details.
    # -------------------------------------------------------------------------
    def display_student(self):

        # ---------------------------------------------------------------------
        # Calling methods of both Parent classes.
        # ---------------------------------------------------------------------
        self.display_person()
        self.display_college()

        # ---------------------------------------------------------------------
        # Displaying child class information.
        # ---------------------------------------------------------------------
        print("Course  :", self.course)


# -----------------------------------------------------------------------------
# Creating an object of the Child class.
# -----------------------------------------------------------------------------
student = Student()

# -----------------------------------------------------------------------------
# Calling the Child class method.
# -----------------------------------------------------------------------------
student.display_student()

# Output:
# Name    : Basha
# Age     : 25
# College : ABC College
# Course  : Python
