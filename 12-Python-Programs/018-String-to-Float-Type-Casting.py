"""
===============================================================================
                  String to Float Type Casting
===============================================================================

Program Description:
--------------------
This program demonstrates how to convert a String data type into a
Float data type using the float() function.

The string must contain a valid floating-point number.
Otherwise, Python raises a ValueError.

Example:
"99.99"  --->  99.99

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 18-String-to-Float-Type-Casting.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating a string variable.
# The string contains a floating-point value.
# -----------------------------------------------------------------------------
string_number = "99.99"
# string_number stores the string "99.99".

# -----------------------------------------------------------------------------
# Displaying the original string value.
# -----------------------------------------------------------------------------
print("Original String Value :", string_number)
# Output: Original String Value : 99.99

# -----------------------------------------------------------------------------
# Displaying the data type of the original variable.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(string_number))
# Output: Original Data Type : <class 'str'>

# -----------------------------------------------------------------------------
# Converting the string into a float using the float() function.
# Since the string contains a valid floating-point number,
# the conversion succeeds.
# -----------------------------------------------------------------------------
float_number = float(string_number)
# float_number stores the float value 99.99.

# -----------------------------------------------------------------------------
# Displaying the converted float value.
# -----------------------------------------------------------------------------
print("Converted Float Value :", float_number)
# Output: Converted Float Value : 99.99

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Converted Data Type :", type(float_number))
# Output: Converted Data Type : <class 'float'>

# -----------------------------------------------------------------------------
# Displaying an important note about string-to-float conversion.
# -----------------------------------------------------------------------------
print("Note: float() converts numeric strings containing decimal values into floating-point numbers.")
# Output: Note: float() converts numeric strings containing decimal values into floating-point numbers.

# -----------------------------------------------------------------------------
# Displaying another important note.
# A non-numeric string cannot be converted into a float.
# -----------------------------------------------------------------------------
print("Example: float('Python') raises ValueError.")
# Output: Example: float('Python') raises ValueError.
