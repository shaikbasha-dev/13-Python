"""
===============================================================================
File Name    : 146-Modules.py
Description  : Modules in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A Module is a Python file that contains variables, functions, and classes
which can be reused in other Python programs.

Python provides:
1. Built-in Modules
2. User-Defined Modules

In this example, a built-in module is used.

Syntax:

import module_name

module_name.function()

Example:
Using the built-in math module.
"""

# -----------------------------------------------------------------------------
# Importing the built-in math module.
# -----------------------------------------------------------------------------
import math

# -----------------------------------------------------------------------------
# Declaring a number.
# -----------------------------------------------------------------------------
number = 25

# -----------------------------------------------------------------------------
# Finding the square root of the number.
# -----------------------------------------------------------------------------
square_root = math.sqrt(number)

# -----------------------------------------------------------------------------
# Displaying the square root.
# -----------------------------------------------------------------------------
print("Square Root :", square_root)

# -----------------------------------------------------------------------------
# Finding the value of pi.
# -----------------------------------------------------------------------------
print("Value of PI :", math.pi)

# -----------------------------------------------------------------------------
# Finding the factorial of a number.
# -----------------------------------------------------------------------------
print("Factorial   :", math.factorial(5))

# Output:
# Square Root : 5.0
# Value of PI : 3.141592653589793
# Factorial   : 120
