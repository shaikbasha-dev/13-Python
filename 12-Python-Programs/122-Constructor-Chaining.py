"""
===============================================================================
File Name    : 122-Constructor-Chaining.py
Description  : Constructor Chaining in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Constructor Chaining is the process of calling one constructor from another
constructor in an inheritance hierarchy. In Python, constructor chaining is
commonly achieved using the super() function.

Syntax:

class Parent:

    def __init__(self):
        pass

class Child(Parent):

    def __init__(self):
        super().__init__()

Example:
Person -> Student -> Employee
"""

# -----------------------------------------------------------------------------
# Creating the Grandparent class.
# -----------------------------------------------------------------------------
class Person:

    # -------------------------------------------------------------------------
    # Defining the constructor of the Grandparent class.
    # -------------------------------------------------------------------------
    def __init__(self):

        # ---------------------------------------------------------------------
        # Displaying a message.
        # ---------------------------------------------------------------------
        print("Person constructor executed.")


# -----------------------------------------------------------------------------
# Creating the Parent class.
# -----------------------------------------------------------------------------
class Student(Person):

    # -------------------------------------------------------------------------
    # Defining the constructor of the Parent class.
    # -------------------------------------------------------------------------
    def __init__(self):

        # ---------------------------------------------------------------------
        # Calling the Grandparent class constructor.
        # ---------------------------------------------------------------------
        super().__init__()

        # ---------------------------------------------------------------------
        # Displaying a message.
        # ---------------------------------------------------------------------
        print("Student constructor executed.")


# -----------------------------------------------------------------------------
# Creating the Child class.
# -----------------------------------------------------------------------------
class Employee(Student):

    # -------------------------------------------------------------------------
    # Defining the constructor of the Child class.
    # -------------------------------------------------------------------------
    def __init__(self):

        # ---------------------------------------------------------------------
        # Calling the Parent class constructor.
        # ---------------------------------------------------------------------
        super().__init__()

        # ---------------------------------------------------------------------
        # Displaying a message.
        # ---------------------------------------------------------------------
        print("Employee constructor executed.")


# -----------------------------------------------------------------------------
# Creating an object of the Child class.
# -----------------------------------------------------------------------------
employee = Employee()

# Output:
# Person constructor executed.
# Student constructor executed.
# Employee constructor executed.
