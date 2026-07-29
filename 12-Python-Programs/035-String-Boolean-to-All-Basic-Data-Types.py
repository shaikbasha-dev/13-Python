"""
===============================================================================
              String Boolean to All Basic Data Types
===============================================================================

Program Description:
--------------------
This program demonstrates how to convert a string containing a Boolean
value into all basic Python data types.

Conversions demonstrated:
1. String to Integer (Not Possible)
2. String to Float (Not Possible)
3. String to Boolean
4. String to String
5. String to Complex (Not Possible)

Example:
"True"  → int()      ✗ Not Possible
"True"  → float()    ✗ Not Possible
"True"  → True
"True"  → "True"
"True"  → complex()  ✗ Not Possible

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 35-String-Boolean-to-All-Basic-Data-Types.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating a string variable containing a Boolean value.
# -----------------------------------------------------------------------------
string_value = "True"
# string_value stores the string "True".

# -----------------------------------------------------------------------------
# Displaying the original string value.
# -----------------------------------------------------------------------------
print("Original String Value :", string_value)
# Output: Original String Value : True

# -----------------------------------------------------------------------------
# Displaying the original data type.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(string_value))
# Output: Original Data Type : <class 'str'>

# -----------------------------------------------------------------------------
# Converting the string into an integer.
# This conversion is not possible because the string does not contain
# a valid integer value.
# -----------------------------------------------------------------------------
integer_value = int(string_value)

# Output:
# ValueError:
# invalid literal for int() with base 10: 'True'

# -----------------------------------------------------------------------------
# The remaining statements are not executed because the program stops
# when the above ValueError occurs.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Converting the string into a float.
# This conversion is also not possible because the string does not
# contain a valid float value.
# -----------------------------------------------------------------------------
float_value = float(string_value)

# Output:
# ValueError:
# could not convert string to float: 'True'

# -----------------------------------------------------------------------------
# Converting the string into a Boolean.
# Any non-empty string converts to True.
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
# Output: Converted Value : True

print("Data Type :", type(new_string_value))
# Output: Data Type : <class 'str'>

# -----------------------------------------------------------------------------
# Converting the string into a complex number.
# This conversion is not possible because "True" is not a valid
# numeric string.
# -----------------------------------------------------------------------------
complex_value = complex(string_value)

# Output:
# ValueError:
# complex() arg is a malformed string

# -----------------------------------------------------------------------------
# Displaying an important note.
# -----------------------------------------------------------------------------
print("\nNote: The string 'True' is not a numeric string.")
print("Only bool() and str() conversions are successful.")
# Output:
# Note: The string 'True' is not a numeric string.
# Only bool() and str() conversions are successful.
