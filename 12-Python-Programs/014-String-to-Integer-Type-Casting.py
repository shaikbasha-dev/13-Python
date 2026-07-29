"""
===============================================================================
                  String to Integer Type Casting
===============================================================================

Program Description:
--------------------
This program demonstrates how to convert a String data type into an
Integer data type using the int() function.

The string must contain only numeric characters.
Otherwise, Python raises a ValueError.

Example:
"100"  --->  100

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 14-String-to-Integer-Type-Casting.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating a string variable.
# The string contains a numeric value.
# -----------------------------------------------------------------------------
string_number = "100"
# string_number stores the string "100".

# -----------------------------------------------------------------------------
# Displaying the original string value.
# -----------------------------------------------------------------------------
print("Original String Value :", string_number)
# Output: Original String Value : 100

# -----------------------------------------------------------------------------
# Displaying the data type of the original variable.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(string_number))
# Output: Original Data Type : <class 'str'>

# -----------------------------------------------------------------------------
# Converting the string into an integer using the int() function.
# Since the string contains only numeric characters, the conversion succeeds.
# -----------------------------------------------------------------------------
integer_number = int(string_number)
# integer_number stores the integer value 100.

# -----------------------------------------------------------------------------
# Displaying the converted integer value.
# -----------------------------------------------------------------------------
print("Converted Integer Value :", integer_number)
# Output: Converted Integer Value : 100

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Converted Data Type :", type(integer_number))
# Output: Converted Data Type : <class 'int'>

# -----------------------------------------------------------------------------
# Displaying an important note about string-to-integer conversion.
# -----------------------------------------------------------------------------
print("Note: int() converts only numeric strings into integers.")
# Output: Note: int() converts only numeric strings into integers.

# -----------------------------------------------------------------------------
# Displaying another important note.
# A non-numeric string cannot be converted into an integer.
# -----------------------------------------------------------------------------
print("Example: int('ABC') raises ValueError.")
# Output: Example: int('ABC') raises ValueError.
