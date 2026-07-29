"""
===============================================================================
File Name    : 135-Abstraction-Rule-3.py
Description  : Abstraction Rule 3 in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Rule 3:
A Child class must implement all abstract methods of its Parent abstract
class. Only then can an object of the Child class be created.

Syntax:

from abc import ABC, abstractmethod

class Parent(ABC):

    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass

class Child(Parent):

    def method1(self):
        pass

    def method2(self):
        pass

Example:
Employee implements all abstract methods of Person.
"""

# -----------------------------------------------------------------------------
# Importing ABC and abstractmethod from the abc module.
# -----------------------------------------------------------------------------
from abc import ABC, abstractmethod


# -----------------------------------------------------------------------------
# Creating an Abstract class.
# -----------------------------------------------------------------------------
class Person(ABC):

    # -------------------------------------------------------------------------
    # Creating the first abstract method.
    # -------------------------------------------------------------------------
    @abstractmethod
    def get_name(self):

        # ---------------------------------------------------------------------
        # This method has no implementation.
        # ---------------------------------------------------------------------
        pass

    # -------------------------------------------------------------------------
    # Creating the second abstract method.
    # -------------------------------------------------------------------------
    @abstractmethod
    def get_role(self):

        # ---------------------------------------------------------------------
        # This method has no implementation.
        # ---------------------------------------------------------------------
        pass


# -----------------------------------------------------------------------------
# Creating the Child class.
# -----------------------------------------------------------------------------
class Employee(Person):

    # -------------------------------------------------------------------------
    # Implementing the first abstract method.
    # -------------------------------------------------------------------------
    def get_name(self):

        # ---------------------------------------------------------------------
        # Displaying the employee name.
        # ---------------------------------------------------------------------
        print("Name : Basha")

    # -------------------------------------------------------------------------
    # Implementing the second abstract method.
    # -------------------------------------------------------------------------
    def get_role(self):

        # ---------------------------------------------------------------------
        # Displaying the employee role.
        # ---------------------------------------------------------------------
        print("Role : Python Developer")


# -----------------------------------------------------------------------------
# Creating an object of the Child class.
# -----------------------------------------------------------------------------
employee = Employee()

# -----------------------------------------------------------------------------
# Calling the implemented methods.
# -----------------------------------------------------------------------------
employee.get_name()
employee.get_role()

# Output:
# Name : Basha
# Role : Python Developer
