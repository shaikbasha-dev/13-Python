"""
===============================================================================
File Name    : 128-Abstraction.py
Description  : Abstraction in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Abstraction is the process of hiding implementation details and showing only
the essential features of an object.

Python supports abstraction using the ABC (Abstract Base Class) module.

An abstract class cannot be instantiated directly. It is meant to be
inherited by other classes that implement its abstract methods.

Syntax:

from abc import ABC, abstractmethod

class Parent(ABC):

    @abstractmethod
    def method(self):
        pass

class Child(Parent):

    def method(self):
        pass

Example:
Shape is an abstract class.
Circle provides the implementation of the abstract method.
"""

# -----------------------------------------------------------------------------
# Importing ABC and abstractmethod from the abc module.
# -----------------------------------------------------------------------------
from abc import ABC, abstractmethod


# -----------------------------------------------------------------------------
# Creating an Abstract class.
# -----------------------------------------------------------------------------
class Shape(ABC):

    # -------------------------------------------------------------------------
    # Creating an abstract method.
    # -------------------------------------------------------------------------
    @abstractmethod
    def draw(self):

        # ---------------------------------------------------------------------
        # This method has no implementation.
        # ---------------------------------------------------------------------
        pass


# -----------------------------------------------------------------------------
# Creating a Child class.
# -----------------------------------------------------------------------------
class Circle(Shape):

    # -------------------------------------------------------------------------
    # Providing the implementation of the abstract method.
    # -------------------------------------------------------------------------
    def draw(self):

        # ---------------------------------------------------------------------
        # Displaying a message.
        # ---------------------------------------------------------------------
        print("Drawing a Circle")


# -----------------------------------------------------------------------------
# Creating an object of the Child class.
# -----------------------------------------------------------------------------
circle = Circle()

# -----------------------------------------------------------------------------
# Calling the implemented method.
# -----------------------------------------------------------------------------
circle.draw()

# Output:
# Drawing a Circle
