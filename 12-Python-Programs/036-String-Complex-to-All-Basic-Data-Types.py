"""
===============================================================================
              String Complex to All Basic Data Types
===============================================================================

Program Description:
--------------------
This program demonstrates how to convert a string containing a complex
value into all basic Python data types.

Conversions demonstrated:
1. String to Integer (Not Possible)
2. String to Float (Not Possible)
3. String to Boolean
4. String to String
5. String to Complex

Example:
"10+5j" → int()      ✗ Not Possible
"10+5j" → float()    ✗ Not Possible
"10+5j" → True
"10+5j" → "10+5j"
"10+5j" → (10+5j)

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 36-String-Complex-to-All-Basic-Data-Types.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating a string variable containing a complex value.
# -----------------------------------------------------------------------------
string_value = "10+5j"
# string_value stores the string "10+5j".

# -----------------------------------------------------------------------------
# Displaying the original string value.
# -----------------------------------------------------------------------------
print("Original String Value :", string_value)
# Output: Original String Value : 10+5j

# -----------------------------------------------------------------------------
# Displaying the original data type.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(string_value))
# Output: Original Data Type : <class 'str'>

# -----------------------------------------------------------------------------
# Converting the string into an integer.
# This conversion is not possible because the string contains
# a complex value.
# -----------------------------------------------------------------------------
integer_value = int(string_value)

# Output:
# ValueError:
# invalid literal for int() with base 10: '10+5j'

# -----------------------------------------------------------------------------
# The remaining statements are not executed because the program stops
# when the above ValueError occurs.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Converting the string into a float.
# This conversion is not possible because the string contains
# a complex value.
# -----------------------------------------------------------------------------
float_value = float(string_value)

# Output:
# ValueError:
# could not convert string to float: '10+5j'

# -----------------------------------------------------------------------------
# Converting the string into a Boolean.
# Any non-empty string converts to True.
# -----------------------------------------------------------------------------
boolean_value = bool(string_value)

print("\nString to Boolean")
# Output:

print("Converted Value :", boolean_value)
# Output: Converted Value : True

print("Data Type :", type(boolean_value))
# Output: Data Type : <class 'bool'>

# -----------------------------------------------------------------------------
# Converting the string into another string.
# -----------------------------------------------------------------------------
new_string_value = str(string_value)

print("\nString to String")
# Output:

print("Converted Value :", new_string_value)
# Output: Converted Value : 10+5j

print("Data Type :", type(new_string_value))
# Output: Data Type : <class 'str'>

# -----------------------------------------------------------------------------
# Converting the string into a complex number.
# -----------------------------------------------------------------------------
complex_value = complex(string_value)

print("\nString to Complex")
# Output:

print("Converted Value :", complex_value)
# Output: Converted Value : (10+5j)

print("Data Type :", type(complex_value))
# Output: Data Type : <class 'complex'>

# -----------------------------------------------------------------------------
# Displaying an important note.
# -----------------------------------------------------------------------------
print("\nNote: A string containing a valid complex value can be")
print("converted only to complex, Boolean, and string.")
# Output:
# Note: A string containing a valid complex value can be
# converted only to complex, Boolean, and string.
