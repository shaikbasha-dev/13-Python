"""
===============================================================================
                  Complex to String Type Casting
===============================================================================

Program Description:
--------------------
This program demonstrates how to convert a Complex data type into a
String data type using the str() function.

After conversion, the complex number becomes a string and can be used
in string operations such as concatenation.

Example:
10 + 5j ---> "10+5j"

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 28-Complex-to-String-Type-Casting.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating a complex variable.
# -----------------------------------------------------------------------------
complex_number = 10 + 5j
# complex_number stores the complex value (10+5j).

# -----------------------------------------------------------------------------
# Displaying the original complex value.
# -----------------------------------------------------------------------------
print("Original Complex Value :", complex_number)
# Output: Original Complex Value : (10+5j)

# -----------------------------------------------------------------------------
# Displaying the data type of the original variable.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(complex_number))
# Output: Original Data Type : <class 'complex'>

# -----------------------------------------------------------------------------
# Converting the complex number into a string using str().
# -----------------------------------------------------------------------------
string_value = str(complex_number)
# string_value stores the string "(10+5j)".

# -----------------------------------------------------------------------------
# Displaying the converted string value.
# -----------------------------------------------------------------------------
print("Converted String Value :", string_value)
# Output: Converted String Value : (10+5j)

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Converted Data Type :", type(string_value))
# Output: Converted Data Type : <class 'str'>

# -----------------------------------------------------------------------------
# Concatenating the converted string with another string.
# -----------------------------------------------------------------------------
message = "Complex Number: " + string_value
# message stores the concatenated string.

# -----------------------------------------------------------------------------
# Displaying the concatenated string.
# -----------------------------------------------------------------------------
print(message)
# Output: Complex Number: (10+5j)

# -----------------------------------------------------------------------------
# Displaying an important note about Complex-to-String conversion.
# -----------------------------------------------------------------------------
print("Note: str() converts a complex number into its string representation.")
# Output: Note: str() converts a complex number into its string representation.
