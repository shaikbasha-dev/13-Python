"""
===============================================================================
                  Integer to String Type Casting
===============================================================================

Program Description:
--------------------
This program demonstrates how to convert an Integer data type into a
String data type using the str() function.

After conversion, the integer becomes a string and can be used in
string operations such as concatenation.

Example:
100 ---> "100"

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 25-Integer-to-String-Type-Casting.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating an integer variable.
# -----------------------------------------------------------------------------
integer_number = 100
# integer_number stores the integer value 100.

# -----------------------------------------------------------------------------
# Displaying the original integer value.
# -----------------------------------------------------------------------------
print("Original Integer Value :", integer_number)
# Output: Original Integer Value : 100

# -----------------------------------------------------------------------------
# Displaying the data type of the original variable.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(integer_number))
# Output: Original Data Type : <class 'int'>

# -----------------------------------------------------------------------------
# Converting the integer into a string using str().
# -----------------------------------------------------------------------------
string_value = str(integer_number)
# string_value stores the string "100".

# -----------------------------------------------------------------------------
# Displaying the converted string value.
# -----------------------------------------------------------------------------
print("Converted String Value :", string_value)
# Output: Converted String Value : 100

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Converted Data Type :", type(string_value))
# Output: Converted Data Type : <class 'str'>

# -----------------------------------------------------------------------------
# Concatenating the converted string with another string.
# -----------------------------------------------------------------------------
message = "Student ID: " + string_value
# message stores the concatenated string.

# -----------------------------------------------------------------------------
# Displaying the concatenated string.
# -----------------------------------------------------------------------------
print(message)
# Output: Student ID: 100

# -----------------------------------------------------------------------------
# Displaying an important note about Integer-to-String conversion.
# -----------------------------------------------------------------------------
print("Note: str() converts an integer into its string representation.")
# Output: Note: str() converts an integer into its string representation.
