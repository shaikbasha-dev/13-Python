"""
===============================================================================
File Name    : 133-Abstraction-Rule-1.py
Description  : Abstraction Rule 1 in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Rule 1:
An abstract class can contain one or more abstract methods.

An abstract method is declared using the @abstractmethod decorator and does
not have an implementation. Every child class must provide an implementation
for all abstract methods.

Syntax:

from abc import ABC, abstractmethod

class Parent(ABC):

    @abstractmethod
    def method1(self):
        pass

Example:
Shape is an abstract class containing one abstract method.
Circle implements the abstract method.
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
