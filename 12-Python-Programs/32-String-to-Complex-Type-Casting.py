"""
===============================================================================
                  String to Complex Type Casting
===============================================================================

Program Description:
--------------------
This program demonstrates how to convert a String data type into a
Complex data type using the complex() function.

The string must represent a valid integer, floating-point number,
or complex number.

Examples:
"100"    ---> (100+0j)
"99.99"  ---> (99.99+0j)
"5+3j"   ---> (5+3j)

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 32-String-to-Complex-Type-Casting.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating a string variable.
# -----------------------------------------------------------------------------
string_value = "25+10j"
# string_value stores the string "25+10j".

# -----------------------------------------------------------------------------
# Displaying the original string value.
# -----------------------------------------------------------------------------
print("Original String Value :", string_value)
# Output: Original String Value : 25+10j

# -----------------------------------------------------------------------------
# Displaying the data type of the original variable.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(string_value))
# Output: Original Data Type : <class 'str'>

# -----------------------------------------------------------------------------
# Converting the string into a complex number using complex().
# -----------------------------------------------------------------------------
complex_number = complex(string_value)
# complex_number stores the complex value (25+10j).

# -----------------------------------------------------------------------------
# Displaying the converted complex value.
# -----------------------------------------------------------------------------
print("Converted Complex Value :", complex_number)
# Output: Converted Complex Value : (25+10j)

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Converted Data Type :", type(complex_number))
# Output: Converted Data Type : <class 'complex'>

# -----------------------------------------------------------------------------
# Displaying the real part of the complex number.
# -----------------------------------------------------------------------------
print("Real Part :", complex_number.real)
# Output: Real Part : 25.0

# -----------------------------------------------------------------------------
# Displaying the imaginary part of the complex number.
# -----------------------------------------------------------------------------
print("Imaginary Part :", complex_number.imag)
# Output: Imaginary Part : 10.0

# -----------------------------------------------------------------------------
# Displaying an important note about String-to-Complex conversion.
# -----------------------------------------------------------------------------
print("Note: complex() converts a valid numeric string into a complex number.")
# Output: Note: complex() converts a valid numeric string into a complex number.
