"""
===============================================================================
                           Complex Data Type
===============================================================================

Program Description:
--------------------
This program demonstrates the Complex (complex) data type in Python.

A complex number consists of two parts:
1. Real Part
2. Imaginary Part

The imaginary part is represented using the letter 'j'.

General Syntax:
complex_number = real_part + imaginary_partj

Example:
10 + 5j

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 09-Complex-Data-Type.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating a complex variable named number1.
# The variable stores a complex number having both real and imaginary parts.
# -----------------------------------------------------------------------------
number1 = 10 + 5j
# number1 contains the complex value 10+5j.

# -----------------------------------------------------------------------------
# Creating another complex variable named number2.
# The variable stores a negative real part and a positive imaginary part.
# -----------------------------------------------------------------------------
number2 = -8 + 3j
# number2 contains the complex value -8+3j.

# -----------------------------------------------------------------------------
# Creating another complex variable named number3.
# The variable stores a positive real part and a negative imaginary part.
# -----------------------------------------------------------------------------
number3 = 15 - 7j
# number3 contains the complex value 15-7j.

# -----------------------------------------------------------------------------
# Displaying the value stored in number1.
# -----------------------------------------------------------------------------
print("Value of number1 :", number1)
# Output: Value of number1 : (10+5j)

# -----------------------------------------------------------------------------
# Displaying the value stored in number2.
# -----------------------------------------------------------------------------
print("Value of number2 :", number2)
# Output: Value of number2 : (-8+3j)

# -----------------------------------------------------------------------------
# Displaying the value stored in number3.
# -----------------------------------------------------------------------------
print("Value of number3 :", number3)
# Output: Value of number3 : (15-7j)

# -----------------------------------------------------------------------------
# Displaying the data type of number1.
# type() is a built-in function used to identify the data type of a variable.
# -----------------------------------------------------------------------------
print("Data Type of number1 :", type(number1))
# Output: Data Type of number1 : <class 'complex'>

# -----------------------------------------------------------------------------
# Displaying the real part of number1.
# The real attribute returns the real part of a complex number.
# -----------------------------------------------------------------------------
print("Real Part of number1 :", number1.real)
# Output: Real Part of number1 : 10.0

# -----------------------------------------------------------------------------
# Displaying the imaginary part of number1.
# The imag attribute returns the imaginary part of a complex number.
# -----------------------------------------------------------------------------
print("Imaginary Part of number1 :", number1.imag)
# Output: Imaginary Part of number1 : 5.0
