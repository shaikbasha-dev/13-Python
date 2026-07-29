"""
===============================================================================
File Name    : 120-Inherited-Overridden-Specialized-Methods.py
Description  : Inherited, Overridden, and Specialized Methods in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
In object-oriented programming, methods in a child class can be classified
into three categories:

1. Inherited Method
   - A method that is inherited from the parent class without any changes.

2. Overridden Method
   - A method that is redefined in the child class with a new implementation.

3. Specialized Method
   - A new method that exists only in the child class.

Example:
Person -> Student
"""

# -----------------------------------------------------------------------------
# Creating the Parent class.
# -----------------------------------------------------------------------------
class Person:

    # -------------------------------------------------------------------------
    # Creating an inherited method.
    # -------------------------------------------------------------------------
    def show_name(self):

        # ---------------------------------------------------------------------
        # Displaying the name.
        # ---------------------------------------------------------------------
        print("Name : Basha")

    # -------------------------------------------------------------------------
    # Creating a method that will be overridden.
    # -------------------------------------------------------------------------
    def show_role(self):

        # ---------------------------------------------------------------------
        # Displaying the parent role.
        # ---------------------------------------------------------------------
        print("Role : Person")


# -----------------------------------------------------------------------------
# Creating the Child class.
# -----------------------------------------------------------------------------
class Student(Person):

    # -------------------------------------------------------------------------
    # Overriding the Parent class method.
    # -------------------------------------------------------------------------
    def show_role(self):

        # ---------------------------------------------------------------------
        # Displaying the child role.
        # ---------------------------------------------------------------------
        print("Role : Student")

    # -------------------------------------------------------------------------
    # Creating a specialized method.
    # -------------------------------------------------------------------------
    def show_course(self):

        # ---------------------------------------------------------------------
        # Displaying the course.
        # ---------------------------------------------------------------------
        print("Course : Python")


# -----------------------------------------------------------------------------
# Creating an object of the Child class.
# -----------------------------------------------------------------------------
student = Student()

# -----------------------------------------------------------------------------
# Calling the inherited method.
# -----------------------------------------------------------------------------
student.show_name()

# -----------------------------------------------------------------------------
# Calling the overridden method.
# -----------------------------------------------------------------------------
student.show_role()

# -----------------------------------------------------------------------------
# Calling the specialized method.
# -----------------------------------------------------------------------------
student.show_course()

# Output:
# Name : Basha
# Role : Student
# Course : Python
