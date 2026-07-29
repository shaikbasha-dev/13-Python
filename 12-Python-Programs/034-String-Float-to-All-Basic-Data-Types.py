"""
===============================================================================
               String Float to All Basic Data Types
===============================================================================

Program Description:
--------------------
This program demonstrates how to convert a string containing a float
value into all basic Python data types.

Conversions demonstrated:
1. String to Integer (Not Possible)
2. String to Float
3. String to Boolean
4. String to String
5. String to Complex

Example:
"99.99" → int()      ✗ Not Possible
"99.99" → 99.99
"99.99" → True
"99.99" → "99.99"
"99.99" → (99.99+0j)

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 34-String-Float-to-All-Basic-Data-Types.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating a string variable containing a float value.
# -----------------------------------------------------------------------------
string_value = "99.99"
# string_value stores the string "99.99".

# -----------------------------------------------------------------------------
# Displaying the original string value.
# -----------------------------------------------------------------------------
print("Original String Value :", string_value)
# Output: Original String Value : 99.99

# -----------------------------------------------------------------------------
# Displaying the original data type.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(string_value))
# Output: Original Data Type : <class 'str'>

# -----------------------------------------------------------------------------
# Converting the string into an integer.
# This conversion is not possible because the string contains a float value.
# -----------------------------------------------------------------------------
integer_value = int(string_value)

# Output:
# ValueError:
# invalid literal for int() with base 10: '99.99'

# -----------------------------------------------------------------------------
# The remaining statements are not executed because the program stops
# when the above ValueError occurs.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Converting the string into a float.
# -----------------------------------------------------------------------------
float_value = float(string_value)

print("\nString to Float")
print("Converted Value :", float_value)
# Output: Converted Value : 99.99

print("Data Type :", type(float_value))
# Output: Data Type : <class 'float'>

# -----------------------------------------------------------------------------
# Converting the string into a Boolean.
# -----------------------------------------------------------------------------
boolean_value = bool(string_value)

print("\nString to Boolean")
print("Converted Value :", boolean_value)
# Output: Converted Value : True

print("Data Type :", type(boolean_value))
# Output: Data Type : <class 'bool'>

# -----------------------------------------------------------------------------
# Converting the string into another string.
# -----------------------------------------------------------------------------
new_string_value = str(string_value)

print("\nString to String")
print("Converted Value :", new_string_value)
# Output: Converted Value : 99.99

print("Data Type :", type(new_string_value))
# Output: Data Type : <class 'str'>

# -----------------------------------------------------------------------------
# Converting the string into a complex number.
# -----------------------------------------------------------------------------
complex_value = complex(string_value)

print("\nString to Complex")
print("Converted Value :", complex_value)
# Output: Converted Value : (99.99+0j)

print("Data Type :", type(complex_value))
# Output: Data Type : <class 'complex'>

# -----------------------------------------------------------------------------
# Displaying an important note.
# -----------------------------------------------------------------------------
print("\nNote: A string containing a float value cannot be directly")
print("converted into an integer using int().")
# Output:
# Note: A string containing a float value cannot be directly
# converted into an integer using int().
