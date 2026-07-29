"""
===============================================================================
File Name    : 134-Abstraction-Rule-2.py
Description  : Abstraction Rule 2 in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Rule 2:
If a class contains one or more abstract methods, the class itself must
inherit from the ABC (Abstract Base Class).

Syntax:

from abc import ABC, abstractmethod

class Parent(ABC):

    @abstractmethod
    def method(self):
        pass

Example:
Vehicle is an abstract class because it inherits from ABC.
Car provides the implementation of the abstract method.
"""

# -----------------------------------------------------------------------------
# Importing ABC and abstractmethod from the abc module.
# -----------------------------------------------------------------------------
from abc import ABC, abstractmethod


# -----------------------------------------------------------------------------
# Creating an Abstract class.
# -----------------------------------------------------------------------------
class Vehicle(ABC):

    # -------------------------------------------------------------------------
    # Creating an abstract method.
    # -------------------------------------------------------------------------
    @abstractmethod
    def start(self):

        # ---------------------------------------------------------------------
        # This method has no implementation.
        # ---------------------------------------------------------------------
        pass


# -----------------------------------------------------------------------------
# Creating a Child class.
# -----------------------------------------------------------------------------
class Car(Vehicle):

    # -------------------------------------------------------------------------
    # Providing the implementation of the abstract method.
    # -------------------------------------------------------------------------
    def start(self):

        # ---------------------------------------------------------------------
        # Displaying a message.
        # ---------------------------------------------------------------------
        print("Car engine started.")


# -----------------------------------------------------------------------------
# Creating an object of the Child class.
# -----------------------------------------------------------------------------
car = Car()

# -----------------------------------------------------------------------------
# Calling the implemented method.
# -----------------------------------------------------------------------------
car.start()

# Output:
# Car engine started.
