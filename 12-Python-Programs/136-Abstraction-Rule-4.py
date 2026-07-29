"""
===============================================================================
File Name    : 136-Abstraction-Rule-4.py
Description  : Abstraction Rule 4 in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Rule 4:
An object cannot be created directly for an abstract class.

Abstract classes are incomplete because they contain one or more abstract
methods. Therefore, they must be inherited by a child class that provides
implementations for all abstract methods.

Syntax:

from abc import ABC, abstractmethod

class Parent(ABC):

    @abstractmethod
    def method(self):
        pass

# Object creation is not allowed.
# object = Parent()

Example:
Animal is an abstract class.
Dog is a concrete class that implements the abstract method.
"""

# -----------------------------------------------------------------------------
# Importing ABC and abstractmethod from the abc module.
# -----------------------------------------------------------------------------
from abc import ABC, abstractmethod


# -----------------------------------------------------------------------------
# Creating an Abstract class.
# -----------------------------------------------------------------------------
class Animal(ABC):

    # -------------------------------------------------------------------------
    # Creating an abstract method.
    # -------------------------------------------------------------------------
    @abstractmethod
    def sound(self):

        # ---------------------------------------------------------------------
        # This method has no implementation.
        # ---------------------------------------------------------------------
        pass


# -----------------------------------------------------------------------------
# Creating a Child class.
# -----------------------------------------------------------------------------
class Dog(Animal):

    # -------------------------------------------------------------------------
    # Providing the implementation of the abstract method.
    # -------------------------------------------------------------------------
    def sound(self):

        # ---------------------------------------------------------------------
        # Displaying the animal sound.
        # ---------------------------------------------------------------------
        print("Dog says: Bark")


# -----------------------------------------------------------------------------
# Creating an object of the Child class.
# -----------------------------------------------------------------------------
dog = Dog()

# -----------------------------------------------------------------------------
# Calling the implemented method.
# -----------------------------------------------------------------------------
dog.sound()

# -----------------------------------------------------------------------------
# The following statement is intentionally commented because an abstract class
# cannot be instantiated directly.
# -----------------------------------------------------------------------------
# animal = Animal()

# Output:
# Dog says: Bark
