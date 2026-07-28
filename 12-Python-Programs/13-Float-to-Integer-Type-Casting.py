"""
===============================================================================
                   Float to Integer Type Casting
===============================================================================

Program Description:
--------------------
This program demonstrates how to convert a Float data type into an
Integer data type using the int() function.

During this conversion, Python removes the decimal part of the float
value instead of rounding it.

Example:
25.99  --->  25

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 13-Float-to-Integer-Type-Casting.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating a float variable.
# -----------------------------------------------------------------------------
float_number = 45.89
# float_number stores the float value 45.89.

# -----------------------------------------------------------------------------
# Displaying the original float value.
# -----------------------------------------------------------------------------
print("Original Float Value :", float_number)
# Output: Original Float Value : 45.89

# -----------------------------------------------------------------------------
# Displaying the data type of the original variable.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(float_number))
# Output: Original Data Type : <class 'float'>

# -----------------------------------------------------------------------------
# Converting the float value into an integer using the int() function.
# The decimal part (.89) is removed during conversion.
# -----------------------------------------------------------------------------
integer_number = int(float_number)
# integer_number stores the integer value 45.

# -----------------------------------------------------------------------------
# Displaying the converted integer value.
# -----------------------------------------------------------------------------
print("Converted Integer Value :", integer_number)
# Output: Converted Integer Value : 45

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Converted Data Type :", type(integer_number))
# Output: Converted Data Type : <class 'int'>

# -----------------------------------------------------------------------------
# Displaying an important note about float-to-integer conversion.
# -----------------------------------------------------------------------------
print("Note: int() removes the decimal part instead of rounding the value.")
# Output: Note: int() removes the decimal part instead of rounding the value.
