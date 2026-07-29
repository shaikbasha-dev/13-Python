"""
===============================================================================
File Name    : 152-Decorators.py
Description  : Decorators in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A Decorator is a special function in Python that adds extra functionality
to another function without modifying its original code.

Decorators are represented using the @ symbol.

Syntax:

def decorator(function):

    def wrapper():
        # Additional functionality
        function()

    return wrapper

@decorator
def function_name():
    pass

Example:
Using a decorator to display messages before and after a function call.
"""

# -----------------------------------------------------------------------------
# Creating a decorator function.
# -----------------------------------------------------------------------------
def decorator(function):

    # -------------------------------------------------------------------------
    # Creating a wrapper function.
    # -------------------------------------------------------------------------
    def wrapper():

        # ---------------------------------------------------------------------
        # Displaying a message before calling the original function.
        # ---------------------------------------------------------------------
        print("Before calling the function.")

        # ---------------------------------------------------------------------
        # Calling the original function.
        # ---------------------------------------------------------------------
        function()

        # ---------------------------------------------------------------------
        # Displaying a message after calling the original function.
        # ---------------------------------------------------------------------
        print("After calling the function.")

    # -------------------------------------------------------------------------
    # Returning the wrapper function.
    # -------------------------------------------------------------------------
    return wrapper


# -----------------------------------------------------------------------------
# Applying the decorator to the display() function.
# -----------------------------------------------------------------------------
@decorator
def display():

    # -------------------------------------------------------------------------
    # Displaying the original function message.
    # -------------------------------------------------------------------------
    print("Welcome to Python Decorators.")


# -----------------------------------------------------------------------------
# Calling the decorated function.
# -----------------------------------------------------------------------------
display()

# Output:
# Before calling the function.
# Welcome to Python Decorators.
# After calling the function.
