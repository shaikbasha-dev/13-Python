"""
===============================================================================
File Name    : 111-Static-Variables.py
Description  : Static Variables in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A static variable (also called a class variable) is a variable that belongs
to the class rather than individual objects. A single copy of the variable is
shared among all objects of the class.

Purpose of Static Variables:
1. Store common data shared by all objects.
2. Reduce memory usage by avoiding duplicate data.
3. Access common information using the class name.

Syntax:
class ClassName:
    variable_name = value

Example:
Student.college_name
"""

# -----------------------------------------------------------------------------
# Creating a class.
# -----------------------------------------------------------------------------
class Student:

    # -------------------------------------------------------------------------
    # Declaring a static (class) variable.
    # -------------------------------------------------------------------------
    college_name = "ABC Engineering College"

    # -------------------------------------------------------------------------
    # Defining the constructor.
    # -------------------------------------------------------------------------
    def __init__(self, name, age):

        # ---------------------------------------------------------------------
        # Initializing instance variables.
        # ---------------------------------------------------------------------
        self.name = name
        self.age = age

    # -------------------------------------------------------------------------
    # Creating a method to display student details.
    # -------------------------------------------------------------------------
    def display(self):

        # ---------------------------------------------------------------------
        # Displaying instance variables.
        # ---------------------------------------------------------------------
        print("Student Name  :", self.name)
        print("Student Age   :", self.age)

        # ---------------------------------------------------------------------
        # Displaying the static variable.
        # ---------------------------------------------------------------------
        print("College Name  :", Student.college_name)


# -----------------------------------------------------------------------------
# Creating the first object.
# -----------------------------------------------------------------------------
student1 = Student("Basha", 25)

# -----------------------------------------------------------------------------
# Creating the second object.
# -----------------------------------------------------------------------------
student2 = Student("Rahul", 22)

# -----------------------------------------------------------------------------
# Displaying the details of the first student.
# -----------------------------------------------------------------------------
print("First Student")
student1.display()
# Output:
# First Student
# Student Name  : Basha
# Student Age   : 25
# College Name  : ABC Engineering College

print()

# -----------------------------------------------------------------------------
# Displaying the details of the second student.
# -----------------------------------------------------------------------------
print("Second Student")
student2.display()
# Output:
# Second Student
# Student Name  : Rahul
# Student Age   : 22
# College Name  : ABC Engineering College

print()

# -----------------------------------------------------------------------------
# Accessing the static variable using the class name.
# -----------------------------------------------------------------------------
print("College Name :", Student.college_name)
# Output:
# College Name : ABC Engineering College

print()

# -----------------------------------------------------------------------------
# Modifying the static variable using the class name.
# -----------------------------------------------------------------------------
Student.college_name = "XYZ Engineering College"

# -----------------------------------------------------------------------------
# Displaying the updated static variable.
# -----------------------------------------------------------------------------
print("Updated College Name :", Student.college_name)
# Output:
# Updated College Name : XYZ Engineering College

print()

# -----------------------------------------------------------------------------
# Displaying the updated details of both students.
# -----------------------------------------------------------------------------
student1.display()
# Output:
# Student Name  : Basha
# Student Age   : 25
# College Name  : XYZ Engineering College

print()

student2.display()
# Output:
# Student Name  : Rahul
# Student Age   : 22
# College Name  : XYZ Engineering College
