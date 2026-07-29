"""
===============================================================================
                  Object-Oriented Style Example
===============================================================================

Program Description:
--------------------
This program demonstrates the Object-Oriented Programming (OOP) style in Python.

Object-Oriented Programming is a programming paradigm that organizes a
program using classes and objects. A class acts as a blueprint, while
an object is a real-world entity created from that class.

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 04-Object-Oriented-Style-Example.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Defining a class named Student.
# A class is a blueprint used to create objects.
# -----------------------------------------------------------------------------
class Student:

    # -------------------------------------------------------------------------
    # Defining a method inside the class.
    # This method displays the student information.
    # -------------------------------------------------------------------------
    def display(self):
        # Displaying the student's name.
        print("Student Name : Shaik Mahaboob Basha")
        # Output: Student Name : Shaik Mahaboob Basha

        # Displaying the student's course.
        print("Course       : Python Programming")
        # Output: Course       : Python Programming

        # Displaying the student's role.
        print("Role         : Learner")
        # Output: Role         : Learner


# -----------------------------------------------------------------------------
# Creating an object of the Student class.
# The object is used to access the class members.
# -----------------------------------------------------------------------------
student = Student()
# A Student object is created and stored in the variable 'student'.

# -----------------------------------------------------------------------------
# Calling the display() method using the object.
# This executes the statements inside the display() method.
# -----------------------------------------------------------------------------
student.display()
# Output:
# Student Name : Shaik Mahaboob Basha
# Course       : Python Programming
# Role         : Learner
