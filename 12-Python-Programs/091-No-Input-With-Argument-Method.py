"""
===============================================================================
File Name    : 91-No-Input-With-Argument-Method.py
Description  : No Input With Argument Method in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A No Input With Argument Method does not take input from the user. Instead,
values are passed as arguments when the method is called. The method performs
the required operation using those arguments and does not return any value.

Syntax:
def method_name(argument1, argument2):
    # Statements

method_name(value1, value2)

Example:
def display_student(name, age):
    print(name)
    print(age)

display_student("Rahul", 21)
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
# Calling the method by passing arguments.
# -----------------------------------------------------------------------------
display_student_details("Rahul", 21)

print()

# -----------------------------------------------------------------------------
# Calling the method again with different arguments.
# -----------------------------------------------------------------------------
display_student_details("Anjali", 22)
