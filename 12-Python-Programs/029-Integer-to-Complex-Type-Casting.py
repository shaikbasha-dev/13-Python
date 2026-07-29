"""
===============================================================================
                  Integer to Complex Type Casting
===============================================================================

Program Description:
--------------------
This program demonstrates how to convert an Integer data type into a
Complex data type using the complex() function.

During this conversion, Python converts the integer into a complex number
by assigning the integer as the real part and 0 as the imaginary part.

Example:
100 ---> (100+0j)

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 29-Integer-to-Complex-Type-Casting.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating an integer variable.
# -----------------------------------------------------------------------------
integer_number = 100
# integer_number stores the integer value 100.

# -----------------------------------------------------------------------------
# Displaying the original integer value.
# -----------------------------------------------------------------------------
print("Original Integer Value :", integer_number)
# Output: Original Integer Value : 100

# -----------------------------------------------------------------------------
# Displaying the data type of the original variable.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(integer_number))
# Output: Original Data Type : <class 'int'>

# -----------------------------------------------------------------------------
# Converting the integer into a complex number using complex().
# The integer becomes the real part, and the imaginary part is 0.
# -----------------------------------------------------------------------------
complex_number = complex(integer_number)
# complex_number stores the complex value (100+0j).

# -----------------------------------------------------------------------------
# Displaying the converted complex value.
# -----------------------------------------------------------------------------
print("Converted Complex Value :", complex_number)
# Output: Converted Complex Value : (100+0j)

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Converted Data Type :", type(complex_number))
# Output: Converted Data Type : <class 'complex'>

# -----------------------------------------------------------------------------
# Displaying the real part of the complex number.
# -----------------------------------------------------------------------------
print("Real Part :", complex_number.real)
# Output: Real Part : 100.0

# -----------------------------------------------------------------------------
# Displaying the imaginary part of the complex number.
# -----------------------------------------------------------------------------
print("Imaginary Part :", complex_number.imag)
# Output: Imaginary Part : 0.0

# -----------------------------------------------------------------------------
# Displaying an important note about Integer-to-Complex conversion.
# -----------------------------------------------------------------------------
print("Note: complex() converts an integer into a complex number with an imaginary part of 0.")
# Output: Note: complex() converts an integer into a complex number with an imaginary part of 0.
