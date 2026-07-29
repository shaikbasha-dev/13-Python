"""
===============================================================================
File Name    : 118-Diamond-Shape-Problem.py
Description  : Diamond Shape Problem in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
The Diamond Shape Problem occurs when a class inherits from two parent
classes that both inherit from the same grandparent class.

Python solves this problem automatically using the Method Resolution
Order (MRO), which determines the order in which methods are searched.

Syntax:

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

Example:
A common method exists in both B and C.
Python calls the method according to the MRO.
"""

# -----------------------------------------------------------------------------
# Creating the Grandparent class.
# -----------------------------------------------------------------------------
class A:

    # -------------------------------------------------------------------------
    # Creating a method in the Grandparent class.
    # -------------------------------------------------------------------------
    def display(self):

        # ---------------------------------------------------------------------
        # Displaying a message.
        # ---------------------------------------------------------------------
        print("Display method from Class A")


# -----------------------------------------------------------------------------
# Creating the first Parent class.
# -----------------------------------------------------------------------------
class B(A):

    # -------------------------------------------------------------------------
    # Overriding the display() method.
    # -------------------------------------------------------------------------
    def display(self):

        # ---------------------------------------------------------------------
        # Displaying a message.
        # ---------------------------------------------------------------------
        print("Display method from Class B")


# -----------------------------------------------------------------------------
# Creating the second Parent class.
# -----------------------------------------------------------------------------
class C(A):

    # -------------------------------------------------------------------------
    # Overriding the display() method.
    # -------------------------------------------------------------------------
    def display(self):

        # ---------------------------------------------------------------------
        # Displaying a message.
        # ---------------------------------------------------------------------
        print("Display method from Class C")


# -----------------------------------------------------------------------------
# Creating the Child class.
# -----------------------------------------------------------------------------
class D(B, C):
    pass


# -----------------------------------------------------------------------------
# Creating an object of the Child class.
# -----------------------------------------------------------------------------
obj = D()

# -----------------------------------------------------------------------------
# Calling the display() method.
# According to the MRO, Python searches:
# D → B → C → A
# Therefore, B's method is executed.
# -----------------------------------------------------------------------------
obj.display()

# -----------------------------------------------------------------------------
# Displaying the Method Resolution Order.
# -----------------------------------------------------------------------------
print("\nMethod Resolution Order (MRO):")
print(D.__mro__)

# Output:
# Display method from Class B
#
# Method Resolution Order (MRO):
# (<class '__main__.D'>,
#  <class '__main__.B'>,
#  <class '__main__.C'>,
#  <class '__main__.A'>,
#  <class 'object'>)
