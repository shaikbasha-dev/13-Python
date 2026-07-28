"""
===============================================================================
                        Explicit Type Casting
===============================================================================

Program Description:
--------------------
This program demonstrates Explicit Type Casting (Manual Type Conversion)
in Python.

Explicit Type Casting is performed manually by the programmer using
Python's built-in type conversion functions such as:

1. int()
2. float()
3. str()
4. bool()
5. complex()

It is used when the programmer wants to convert one data type into
another explicitly.

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 12-Explicit-Type-Casting.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating a float variable.
# -----------------------------------------------------------------------------
number = 25.75
# number stores the float value 25.75.

# -----------------------------------------------------------------------------
# Displaying the original value.
# -----------------------------------------------------------------------------
print("Original Value :", number)
# Output: Original Value : 25.75

# -----------------------------------------------------------------------------
# Displaying the original data type.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(number))
# Output: Original Data Type : <class 'float'>

# -----------------------------------------------------------------------------
# Converting the float value into an integer.
# int() removes the decimal part of the float value.
# -----------------------------------------------------------------------------
integer_number = int(number)
# integer_number stores the integer value 25.

# -----------------------------------------------------------------------------
# Displaying the converted integer value.
# -----------------------------------------------------------------------------
print("Integer Value :", integer_number)
# Output: Integer Value : 25

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Data Type :", type(integer_number))
# Output: Data Type : <class 'int'>

# -----------------------------------------------------------------------------
# Converting the integer value into a string.
# str() converts the integer into a string.
# -----------------------------------------------------------------------------
string_value = str(integer_number)
# string_value stores the string "25".

# -----------------------------------------------------------------------------
# Displaying the converted string value.
# -----------------------------------------------------------------------------
print("String Value :", string_value)
# Output: String Value : 25

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Data Type :", type(string_value))
# Output: Data Type : <class 'str'>

# -----------------------------------------------------------------------------
# Converting the integer value into a float.
# float() converts the integer into a floating-point number.
# -----------------------------------------------------------------------------
float_value = float(integer_number)
# float_value stores the float value 25.0.

# -----------------------------------------------------------------------------
# Displaying the converted float value.
# -----------------------------------------------------------------------------
print("Float Value :", float_value)
# Output: Float Value : 25.0

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Data Type :", type(float_value))
# Output: Data Type : <class 'float'>

# -----------------------------------------------------------------------------
# Converting the integer value into a complex number.
# complex() converts the integer into a complex number.
# -----------------------------------------------------------------------------
complex_value = complex(integer_number)
# complex_value stores the complex value (25+0j).

# -----------------------------------------------------------------------------
# Displaying the converted complex value.
# -----------------------------------------------------------------------------
print("Complex Value :", complex_value)
# Output: Complex Value : (25+0j)

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Data Type :", type(complex_value))
# Output: Data Type : <class 'complex'>

# -----------------------------------------------------------------------------
# Converting the integer value into a Boolean value.
# Any non-zero number becomes True.
# -----------------------------------------------------------------------------
boolean_value = bool(integer_number)
# boolean_value stores the Boolean value True.

# -----------------------------------------------------------------------------
# Displaying the converted Boolean value.
# -----------------------------------------------------------------------------
print("Boolean Value :", boolean_value)
# Output: Boolean Value : True

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Data Type :", type(boolean_value))
# Output: Data Type : <class 'bool'>
