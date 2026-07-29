"""
===============================================================================
File Name    : 113-Method-Overloading.py
Description  : Method Overloading in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Method overloading means creating multiple methods with the same name but
different parameter lists.

Python does NOT support method overloading directly because if multiple methods
with the same name are defined, only the last method definition is retained.

Method overloading can be achieved by using default arguments.

Syntax:
def method_name(parameter1=None, parameter2=None):
    pass

Example:
student.details()
student.details("Basha")
student.details("Basha", 25)
"""

# -----------------------------------------------------------------------------
# Creating a class.
# -----------------------------------------------------------------------------
class Student:

    # -------------------------------------------------------------------------
    # Defining a method with default arguments.
    # -------------------------------------------------------------------------
    def details(self, name=None, age=None):

        # ---------------------------------------------------------------------
        # Displaying student details based on the arguments provided.
        # ---------------------------------------------------------------------
        if name is None and age is None:
            print("No Student Details Provided")

        elif age is None:
            print("Student Name :", name)

        else:
            print("Student Name :", name)
            print("Student Age  :", age)


# -----------------------------------------------------------------------------
# Creating an object of the Student class.
# -----------------------------------------------------------------------------
student = Student()

# -----------------------------------------------------------------------------
# Calling the method without any arguments.
# -----------------------------------------------------------------------------
print("Method Call 1")
student.details()
# Output:
# Method Call 1
# No Student Details Provided

print()

# -----------------------------------------------------------------------------
# Calling the method with one argument.
# -----------------------------------------------------------------------------
print("Method Call 2")
student.details("Basha")
# Output:
# Method Call 2
# Student Name : Basha

print()

# -----------------------------------------------------------------------------
# Calling the method with two arguments.
# -----------------------------------------------------------------------------
print("Method Call 3")
student.details("Rahul", 22)
# Output:
# Method Call 3
# Student Name : Rahul
# Student Age  : 22
