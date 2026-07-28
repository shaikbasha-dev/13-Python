"""
===============================================================================
                  String to Boolean Type Casting
===============================================================================

Program Description:
--------------------
This program demonstrates how to convert a String data type into a
Boolean data type using the bool() function.

In Python:
- An empty string ("") is converted to False.
- Any non-empty string is converted to True.

Examples:
""        ---> False
"Python" ---> True
"100"     ---> True
"False"   ---> True

Note:
The string "False" is a non-empty string, so it is converted to True.

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 23-String-to-Boolean-Type-Casting.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating a non-empty string variable.
# -----------------------------------------------------------------------------
string_value1 = "Python"
# string_value1 stores the string "Python".

# -----------------------------------------------------------------------------
# Displaying the original string value.
# -----------------------------------------------------------------------------
print("Original String Value :", string_value1)
# Output: Original String Value : Python

# -----------------------------------------------------------------------------
# Displaying the data type of the original variable.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(string_value1))
# Output: Original Data Type : <class 'str'>

# -----------------------------------------------------------------------------
# Converting the non-empty string into a Boolean using bool().
# Any non-empty string is converted to True.
# -----------------------------------------------------------------------------
boolean_value1 = bool(string_value1)
# boolean_value1 stores the Boolean value True.

# -----------------------------------------------------------------------------
# Displaying the converted Boolean value.
# -----------------------------------------------------------------------------
print("Converted Boolean Value :", boolean_value1)
# Output: Converted Boolean Value : True

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Converted Data Type :", type(boolean_value1))
# Output: Converted Data Type : <class 'bool'>

# -----------------------------------------------------------------------------
# Creating an empty string variable.
# -----------------------------------------------------------------------------
string_value2 = ""
# string_value2 stores an empty string.

# -----------------------------------------------------------------------------
# Displaying the original string value.
# -----------------------------------------------------------------------------
print("Original String Value :", string_value2)
# Output: Original String Value :

# -----------------------------------------------------------------------------
# Displaying the data type of the original variable.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(string_value2))
# Output: Original Data Type : <class 'str'>

# -----------------------------------------------------------------------------
# Converting the empty string into a Boolean using bool().
# An empty string is converted to False.
# -----------------------------------------------------------------------------
boolean_value2 = bool(string_value2)
# boolean_value2 stores the Boolean value False.

# -----------------------------------------------------------------------------
# Displaying the converted Boolean value.
# -----------------------------------------------------------------------------
print("Converted Boolean Value :", boolean_value2)
# Output: Converted Boolean Value : False

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Converted Data Type :", type(boolean_value2))
# Output: Converted Data Type : <class 'bool'>

# -----------------------------------------------------------------------------
# Displaying an important note about String-to-Boolean conversion.
# -----------------------------------------------------------------------------
print("Note: An empty string converts to False, and any non-empty string converts to True.")
# Output: Note: An empty string converts to False, and any non-empty string converts to True.

# -----------------------------------------------------------------------------
# Displaying another important note.
# -----------------------------------------------------------------------------
print("Note: The string 'False' is still converted to True because it is a non-empty string.")
# Output: Note: The string 'False' is still converted to True because it is a non-empty string.
