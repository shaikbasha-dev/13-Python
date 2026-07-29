"""
===============================================================================
File Name    : 124-Method-Chaining-in-Multiple-Inheritance.py
Description  : Method Chaining in Multiple Inheritance in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Method Chaining in Multiple Inheritance is a technique where methods from
multiple parent classes are executed in sequence using the super() function.

Python follows the Method Resolution Order (MRO) to determine the order in
which methods are executed.

Syntax:

class A:

    def display(self):
        pass

class B(A):

    def display(self):
        super().display()

class C(B):

    def display(self):
        super().display()

Example:
A -> B -> C
"""

# -----------------------------------------------------------------------------
# Creating the first Parent class.
# -----------------------------------------------------------------------------
class A:

    # -------------------------------------------------------------------------
    # Creating a display method.
    # -------------------------------------------------------------------------
    def display(self):

        # ---------------------------------------------------------------------
        # Displaying a message.
        # ---------------------------------------------------------------------
        print("Display method from Class A")


# -----------------------------------------------------------------------------
# Creating the second Parent class.
# -----------------------------------------------------------------------------
class B(A):

    # -------------------------------------------------------------------------
    # Overriding the display method.
    # -------------------------------------------------------------------------
    def display(self):

        # ---------------------------------------------------------------------
        # Displaying a message.
        # ---------------------------------------------------------------------
        print("Display method from Class B")

        # ---------------------------------------------------------------------
        # Calling the next method according to the MRO.
        # ---------------------------------------------------------------------
        super().display()


# -----------------------------------------------------------------------------
# Creating the third Parent class.
# -----------------------------------------------------------------------------
class C(B):

    # -------------------------------------------------------------------------
    # Overriding the display method.
    # -------------------------------------------------------------------------
    def display(self):

        # ---------------------------------------------------------------------
        # Displaying a message.
        # ---------------------------------------------------------------------
        print("Display method from Class C")

        # ---------------------------------------------------------------------
        # Calling the next method according to the MRO.
        # ---------------------------------------------------------------------
        super().display()


# -----------------------------------------------------------------------------
# Creating the Child class.
# -----------------------------------------------------------------------------
class D(C):

    # -------------------------------------------------------------------------
    # Overriding the display method.
    # -------------------------------------------------------------------------
    def display(self):

        # ---------------------------------------------------------------------
        # Displaying a message.
        # ---------------------------------------------------------------------
        print("Display method from Class D")

        # ---------------------------------------------------------------------
        # Calling the next method according to the MRO.
        # ---------------------------------------------------------------------
        super().display()


# -----------------------------------------------------------------------------
# Creating an object of the Child class.
# -----------------------------------------------------------------------------
obj = D()

# -----------------------------------------------------------------------------
# Calling the display method.
# -----------------------------------------------------------------------------
obj.display()

# -----------------------------------------------------------------------------
# Displaying the Method Resolution Order.
# -----------------------------------------------------------------------------
print("\nMethod Resolution Order (MRO):")
print(D.__mro__)

# Output:
# Display method from Class D
# Display method from Class C
# Display method from Class B
# Display method from Class A
#
# Method Resolution Order (MRO):
# (<class '__main__.D'>,
#  <class '__main__.C'>,
#  <class '__main__.B'>,
#  <class '__main__.A'>,
#  <class 'object'>)
