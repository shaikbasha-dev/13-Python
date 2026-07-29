"""
===============================================================================
File Name    : 90-Input-No-Argument-Method.py
Description  : Input No Argument Method in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
An Input No Argument Method is a method that takes input from the user inside
the method body and does not accept any arguments during the method call.
It also does not return any value.

Syntax:
def method_name():
    variable = input("Enter Value: ")
    # Statements

method_name()

Example:
def display_name():
    name = input("Enter Your Name: ")
    print("Name :", name)

display_name()
"""

# -----------------------------------------------------------------------------
# Defining a method that takes input inside the method.
# -----------------------------------------------------------------------------
def display_student_details():

    # -------------------------------------------------------------------------
    # Taking student name as input from the user.
    # -------------------------------------------------------------------------
    student_name = input("Enter Student Name : ")

    # -------------------------------------------------------------------------
    # Taking student age as input from the user.
    # -------------------------------------------------------------------------
    student_age = input("Enter Student Age : ")

    print()

    # -------------------------------------------------------------------------
    # Displaying the student details.
    # -------------------------------------------------------------------------
    print("Student Name :", student_name)
    # Output:
    # Student Name : Rahul

    print("Student Age :", student_age)
    # Output:
    # Student Age : 21


# -----------------------------------------------------------------------------
# Calling the method.
# -----------------------------------------------------------------------------
display_student_details()
