"""
===============================================================================
                  Complex to Float Type Casting
===============================================================================

Program Description:
--------------------
This program demonstrates Complex to Float Type Casting in Python.

Python does not allow direct conversion of a complex number into a
floating-point number using the float() function.

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 20-Complex-to-Float-Type-Casting.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating a complex variable.
# -----------------------------------------------------------------------------
complex_number = 25 + 10j
# complex_number stores the complex value (25+10j).

# -----------------------------------------------------------------------------
# Displaying the original complex value.
# -----------------------------------------------------------------------------
print("Original Complex Value :", complex_number)
# Output: Original Complex Value : (25+10j)

# -----------------------------------------------------------------------------
# Displaying the data type of the variable.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(complex_number))
# Output: Original Data Type : <class 'complex'>

# -----------------------------------------------------------------------------
# Attempting to convert the complex number into a float.
# Python does not support this conversion because a complex number
# contains both real and imaginary parts.
# -----------------------------------------------------------------------------
float_number = float(complex_number)

# Output:
# TypeError:
# float() argument must be a string or a real number, not 'complex'
