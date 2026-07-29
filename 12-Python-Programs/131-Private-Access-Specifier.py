"""
===============================================================================
File Name    : 131-Private-Access-Specifier.py
Description  : Private Access Specifier in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A Private Access Specifier is used to restrict direct access to class
variables and methods from outside the class.

In Python, private members are created by prefixing their names with
double underscores (__). Python performs name mangling to reduce
accidental access from outside the class.

Syntax:

class ClassName:

    def __init__(self):
        self.__variable = value

    def __method(self):
        pass

Example:
Student class with private variables and methods.
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
        # Initializing private instance variables.
        # ---------------------------------------------------------------------
        self.__name = "Basha"
        self.__course = "Python"

    # -------------------------------------------------------------------------
    # Creating a private method.
    # -------------------------------------------------------------------------
    def __display_details(self):

        # ---------------------------------------------------------------------
        # Displaying student information.
        # ---------------------------------------------------------------------
        print("Name   :", self.__name)
        print("Course :", self.__course)

    # -------------------------------------------------------------------------
    # Creating a public method to access private members.
    # -------------------------------------------------------------------------
    def show_details(self):

        # ---------------------------------------------------------------------
        # Calling the private method.
        # ---------------------------------------------------------------------
        self.__display_details()


# -----------------------------------------------------------------------------
# Creating an object of the Student class.
# -----------------------------------------------------------------------------
student = Student()

# -----------------------------------------------------------------------------
# Calling the public method.
# -----------------------------------------------------------------------------
student.show_details()

# -----------------------------------------------------------------------------
# Accessing private members using name mangling.
# This is possible but should generally be avoided.
# -----------------------------------------------------------------------------
print("\nAccessing Private Members Using Name Mangling:")
print("Name   :", student._Student__name)
print("Course :", student._Student__course)

# Output:
# Name   : Basha
# Course : Python
#
# Accessing Private Members Using Name Mangling:
# Name   : Basha
# Course : Python
