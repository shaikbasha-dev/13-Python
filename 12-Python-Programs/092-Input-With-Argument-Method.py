"""
===============================================================================
File Name    : 92-Input-With-Argument-Method.py
Description  : Input With Argument Method in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
An Input With Argument Method takes input from the user outside the method.
The input values are passed as arguments when calling the method. The method
uses those arguments and does not return any value.

Syntax:
def method_name(argument1, argument2):
    # Statements

value1 = input("Enter First Value: ")
value2 = input("Enter Second Value: ")

method_name(value1, value2)

Example:
def display_student(name, age):
    print(name)
    print(age)

student_name = input("Enter Student Name: ")
student_age = input("Enter Student Age: ")

display_student(student_name, student_age)
"""

# -----------------------------------------------------------------------------
# Defining a method with arguments.
# -----------------------------------------------------------------------------
def display_student_details(student_name, student_age):

    # -------------------------------------------------------------------------
    # Displaying the student name.
    # -------------------------------------------------------------------------
    print("Student Name :", student_name)
    # Output:
    # Student Name : Rahul

    # -------------------------------------------------------------------------
    # Displaying the student age.
    # -------------------------------------------------------------------------
    print("Student Age :", student_age)
    # Output:
    # Student Age : 21


# -----------------------------------------------------------------------------
# Taking student name as input from the user.
# -----------------------------------------------------------------------------
student_name = input("Enter Student Name : ")

# -----------------------------------------------------------------------------
# Taking student age as input from the user.
# -----------------------------------------------------------------------------
student_age = input("Enter Student Age : ")

print()

# -----------------------------------------------------------------------------
# Calling the method by passing user input as arguments.
# -----------------------------------------------------------------------------
display_student_details(student_name, student_age)
