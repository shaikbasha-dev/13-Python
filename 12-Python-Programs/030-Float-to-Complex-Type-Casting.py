"""
===============================================================================
                   Float to Complex Type Casting
===============================================================================

Program Description:
--------------------
This program demonstrates how to convert a Float data type into a
Complex data type using the complex() function.

During this conversion, Python converts the float into a complex number
by assigning the float as the real part and 0 as the imaginary part.

Example:
99.99 ---> (99.99+0j)

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 30-Float-to-Complex-Type-Casting.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating a float variable.
# -----------------------------------------------------------------------------
float_number = 99.99
# float_number stores the float value 99.99.

# -----------------------------------------------------------------------------
# Displaying the original float value.
# -----------------------------------------------------------------------------
print("Original Float Value :", float_number)
# Output: Original Float Value : 99.99

# -----------------------------------------------------------------------------
# Displaying the data type of the original variable.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(float_number))
# Output: Original Data Type : <class 'float'>

# -----------------------------------------------------------------------------
# Converting the float into a complex number using complex().
# The float becomes the real part, and the imaginary part is 0.
# -----------------------------------------------------------------------------
complex_number = complex(float_number)
# complex_number stores the complex value (99.99+0j).

# -----------------------------------------------------------------------------
# Displaying the converted complex value.
# -----------------------------------------------------------------------------
print("Converted Complex Value :", complex_number)
# Output: Converted Complex Value : (99.99+0j)

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Converted Data Type :", type(complex_number))
# Output: Converted Data Type : <class 'complex'>

# -----------------------------------------------------------------------------
# Displaying the real part of the complex number.
# -----------------------------------------------------------------------------
print("Real Part :", complex_number.real)
# Output: Real Part : 99.99

# -----------------------------------------------------------------------------
# Displaying the imaginary part of the complex number.
# -----------------------------------------------------------------------------
print("Imaginary Part :", complex_number.imag)
# Output: Imaginary Part : 0.0

# -----------------------------------------------------------------------------
# Displaying an important note about Float-to-Complex conversion.
# -----------------------------------------------------------------------------
print("Note: complex() converts a float into a complex number with an imaginary part of 0.")
# Output: Note: complex() converts a float into a complex number with an imaginary part of 0.
