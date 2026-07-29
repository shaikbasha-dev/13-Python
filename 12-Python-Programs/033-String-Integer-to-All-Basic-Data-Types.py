"""
===============================================================================
              String Integer to All Basic Data Types
===============================================================================

Program Description:
--------------------
This program demonstrates how to convert a string containing an integer
value into all basic Python data types.

Conversions demonstrated:
1. String to Integer
2. String to Float
3. String to Boolean
4. String to String
5. String to Complex

Example:
"100" → 100
"100" → 100.0
"100" → True
"100" → "100"
"100" → (100+0j)

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 33-String-Integer-to-All-Basic-Data-Types.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating a string variable containing an integer value.
# -----------------------------------------------------------------------------
string_value = "100"
# string_value stores the string "100".

# -----------------------------------------------------------------------------
# Displaying the original string value.
# -----------------------------------------------------------------------------
print("Original String Value :", string_value)
# Output: Original String Value : 100

# -----------------------------------------------------------------------------
# Displaying the original data type.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(string_value))
# Output: Original Data Type : <class 'str'>

# -----------------------------------------------------------------------------
# Converting the string into an integer.
# -----------------------------------------------------------------------------
integer_value = int(string_value)

# -----------------------------------------------------------------------------
# Displaying the integer value and its data type.
# -----------------------------------------------------------------------------
print("\nString to Integer")
print("Converted Value :", integer_value)
# Output: Converted Value : 100

print("Data Type :", type(integer_value))
# Output: Data Type : <class 'int'>

# -----------------------------------------------------------------------------
# Converting the string into a float.
# -----------------------------------------------------------------------------
float_value = float(string_value)

# -----------------------------------------------------------------------------
# Displaying the float value and its data type.
# -----------------------------------------------------------------------------
print("\nString to Float")
print("Converted Value :", float_value)
# Output: Converted Value : 100.0

print("Data Type :", type(float_value))
# Output: Data Type : <class 'float'>

# -----------------------------------------------------------------------------
# Converting the string into a Boolean.
# -----------------------------------------------------------------------------
boolean_value = bool(string_value)

# -----------------------------------------------------------------------------
# Displaying the Boolean value and its data type.
# -----------------------------------------------------------------------------
print("\nString to Boolean")
print("Converted Value :", boolean_value)
# Output: Converted Value : True

print("Data Type :", type(boolean_value))
# Output: Data Type : <class 'bool'>

# -----------------------------------------------------------------------------
# Converting the string into another string.
# -----------------------------------------------------------------------------
new_string_value = str(string_value)

# -----------------------------------------------------------------------------
# Displaying the string value and its data type.
# -----------------------------------------------------------------------------
print("\nString to String")
print("Converted Value :", new_string_value)
# Output: Converted Value : 100

print("Data Type :", type(new_string_value))
# Output: Data Type : <class 'str'>

# -----------------------------------------------------------------------------
# Converting the string into a complex number.
# -----------------------------------------------------------------------------
complex_value = complex(string_value)

# -----------------------------------------------------------------------------
# Displaying the complex value and its data type.
# -----------------------------------------------------------------------------
print("\nString to Complex")
print("Converted Value :", complex_value)
# Output: Converted Value : (100+0j)

print("Data Type :", type(complex_value))
# Output: Data Type : <class 'complex'>

# -----------------------------------------------------------------------------
# Displaying an important note.
# -----------------------------------------------------------------------------
print("\nNote: A string containing a valid integer value can be converted")
print("to all basic Python data types using their respective functions.")
# Output:
# Note: A string containing a valid integer value can be converted
# to all basic Python data types using their respective functions.
