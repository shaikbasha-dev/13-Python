"""
===============================================================================
                  Boolean to String Type Casting
===============================================================================

Program Description:
--------------------
This program demonstrates how to convert a Boolean data type into a
String data type using the str() function.

After conversion, the Boolean value becomes a string and can be used
in string operations such as concatenation.

Examples:
True  ---> "True"
False ---> "False"

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 27-Boolean-to-String-Type-Casting.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating a Boolean variable with the value True.
# -----------------------------------------------------------------------------
boolean_value = True
# boolean_value stores the Boolean value True.

# -----------------------------------------------------------------------------
# Displaying the original Boolean value.
# -----------------------------------------------------------------------------
print("Original Boolean Value :", boolean_value)
# Output: Original Boolean Value : True

# -----------------------------------------------------------------------------
# Displaying the data type of the original variable.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(boolean_value))
# Output: Original Data Type : <class 'bool'>

# -----------------------------------------------------------------------------
# Converting the Boolean value into a string using str().
# -----------------------------------------------------------------------------
string_value = str(boolean_value)
# string_value stores the string "True".

# -----------------------------------------------------------------------------
# Displaying the converted string value.
# -----------------------------------------------------------------------------
print("Converted String Value :", string_value)
# Output: Converted String Value : True

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Converted Data Type :", type(string_value))
# Output: Converted Data Type : <class 'str'>

# -----------------------------------------------------------------------------
# Concatenating the converted string with another string.
# -----------------------------------------------------------------------------
message = "Boolean Value: " + string_value
# message stores the concatenated string.

# -----------------------------------------------------------------------------
# Displaying the concatenated string.
# -----------------------------------------------------------------------------
print(message)
# Output: Boolean Value: True

# -----------------------------------------------------------------------------
# Displaying an important note about Boolean-to-String conversion.
# -----------------------------------------------------------------------------
print("Note: str() converts a Boolean value into its string representation.")
# Output: Note: str() converts a Boolean value into its string representation.
