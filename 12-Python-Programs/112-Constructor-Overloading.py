"""
===============================================================================
File Name    : 112-Constructor-Overloading.py
Description  : Constructor Overloading in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Constructor overloading means creating multiple constructors with different
parameter lists.

Python does NOT support constructor overloading directly because a class can
have only one __init__() method. However, constructor overloading can be
achieved by using default arguments.

Syntax:
def __init__(self, parameter1=None, parameter2=None):
    pass

Example:
student1 = Student()
student2 = Student("Basha")
student3 = Student("Basha", 25)
"""

# -----------------------------------------------------------------------------
# Creating a class.
# -----------------------------------------------------------------------------
class Student:

    # -------------------------------------------------------------------------
    # Defining a constructor with default arguments.
    # -------------------------------------------------------------------------
    def __init__(self, name=None, age=None):

        # ---------------------------------------------------------------------
        # Initializing instance variables.
        # ---------------------------------------------------------------------
        self.name = name
        self.age = age

    # -------------------------------------------------------------------------
    # Creating a method to display object details.
    # -------------------------------------------------------------------------
    def display(self):

        # ---------------------------------------------------------------------
        # Displaying the object data.
        # ---------------------------------------------------------------------
        print("Student Name :", self.name)
        print("Student Age  :", self.age)


# -----------------------------------------------------------------------------
# Creating an object without passing any arguments.
# -----------------------------------------------------------------------------
student1 = Student()

# -----------------------------------------------------------------------------
# Displaying the details of the first object.
# -----------------------------------------------------------------------------
print("Student 1")
student1.display()
# Output:
# Student 1
# Student Name : None
# Student Age  : None

print()

# -----------------------------------------------------------------------------
# Creating an object by passing only the name.
# -----------------------------------------------------------------------------
student2 = Student("Basha")

# -----------------------------------------------------------------------------
# Displaying the details of the second object.
# -----------------------------------------------------------------------------
print("Student 2")
student2.display()
# Output:
# Student 2
# Student Name : Basha
# Student Age  : None

print()

# -----------------------------------------------------------------------------
# Creating an object by passing both name and age.
# -----------------------------------------------------------------------------
student3 = Student("Rahul", 22)

# -----------------------------------------------------------------------------
# Displaying the details of the third object.
# -----------------------------------------------------------------------------
print("Student 3")
student3.display()
# Output:
# Student 3
# Student Name : Rahul
# Student Age  : 22
