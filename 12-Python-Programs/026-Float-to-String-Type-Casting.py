"""
===============================================================================
                   Float to String Type Casting
===============================================================================

Program Description:
--------------------
This program demonstrates how to convert a Float data type into a
String data type using the str() function.

After conversion, the float becomes a string and can be used in
string operations such as concatenation.

Example:
99.99 ---> "99.99"

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 26-Float-to-String-Type-Casting.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating a float variable.
# -----------------------------------------------------------------------------
float_number = 99.99
# float_number stores the float value 99.99.

# -----------------------------------------------------------------------------
# Displaying the original float value.
# -----------------------------------------------------------------------------
print("Original Float Value :", float_number)
# Output: Original Float Value : 99.99

# -----------------------------------------------------------------------------
# Displaying the data type of the original variable.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(float_number))
# Output: Original Data Type : <class 'float'>

# -----------------------------------------------------------------------------
# Converting the float into a string using str().
# -----------------------------------------------------------------------------
string_value = str(float_number)
# string_value stores the string "99.99".

# -----------------------------------------------------------------------------
# Displaying the converted string value.
# -----------------------------------------------------------------------------
print("Converted String Value :", string_value)
# Output: Converted String Value : 99.99

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Converted Data Type :", type(string_value))
# Output: Converted Data Type : <class 'str'>

# -----------------------------------------------------------------------------
# Concatenating the converted string with another string.
# -----------------------------------------------------------------------------
message = "Price: ₹" + string_value
# message stores the concatenated string.

# -----------------------------------------------------------------------------
# Displaying the concatenated string.
# -----------------------------------------------------------------------------
print(message)
# Output: Price: ₹99.99

# -----------------------------------------------------------------------------
# Displaying an important note about Float-to-String conversion.
# -----------------------------------------------------------------------------
print("Note: str() converts a float into its string representation.")
# Output: Note: str() converts a float into its string representation.
