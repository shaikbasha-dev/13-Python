"""
===============================================================================
File Name    : 123-Method-Chaining.py
Description  : Method Chaining in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Method Chaining is a technique in which multiple methods are called one after
another using a single object. Each method returns the current object
(self), allowing the next method to be called immediately.

Syntax:

class ClassName:

    def method1(self):
        return self

    def method2(self):
        return self

object.method1().method2()

Example:
A Student object calls multiple methods in a single statement.
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
        # Initializing instance variables.
        # ---------------------------------------------------------------------
        self.name = ""
        self.course = ""

    # -------------------------------------------------------------------------
    # Creating a method to set the student name.
    # -------------------------------------------------------------------------
    def set_name(self, name):

        # ---------------------------------------------------------------------
        # Assigning the name.
        # ---------------------------------------------------------------------
        self.name = name

        # ---------------------------------------------------------------------
        # Returning the current object for method chaining.
        # ---------------------------------------------------------------------
        return self

    # -------------------------------------------------------------------------
    # Creating a method to set the course.
    # -------------------------------------------------------------------------
    def set_course(self, course):

        # ---------------------------------------------------------------------
        # Assigning the course.
        # ---------------------------------------------------------------------
        self.course = course

        # ---------------------------------------------------------------------
        # Returning the current object for method chaining.
        # ---------------------------------------------------------------------
        return self

    # -------------------------------------------------------------------------
    # Creating a method to display student details.
    # -------------------------------------------------------------------------
    def display(self):

        # ---------------------------------------------------------------------
        # Displaying student information.
        # ---------------------------------------------------------------------
        print("Name   :", self.name)
        print("Course :", self.course)

        # ---------------------------------------------------------------------
        # Returning the current object for method chaining.
        # ---------------------------------------------------------------------
        return self


# -----------------------------------------------------------------------------
# Creating an object of the Student class.
# -----------------------------------------------------------------------------
student = Student()

# -----------------------------------------------------------------------------
# Calling multiple methods using method chaining.
# -----------------------------------------------------------------------------
student.set_name("Basha").set_course("Python").display()

# Output:
# Name   : Basha
# Course : Python
