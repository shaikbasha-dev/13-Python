"""
===============================================================================
                  Integer to Float Type Casting
===============================================================================

Program Description:
--------------------
This program demonstrates how to convert an Integer data type into a
Float data type using the float() function.

During this conversion, Python adds a decimal point (.0) to the integer
value and converts it into a floating-point number.

Example:
100  --->  100.0

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 17-Integer-to-Float-Type-Casting.py

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
# Converting the integer into a float using the float() function.
# -----------------------------------------------------------------------------
float_number = float(integer_number)
# float_number stores the float value 100.0.

# -----------------------------------------------------------------------------
# Displaying the converted float value.
# -----------------------------------------------------------------------------
print("Converted Float Value :", float_number)
# Output: Converted Float Value : 100.0

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Converted Data Type :", type(float_number))
# Output: Converted Data Type : <class 'float'>

# -----------------------------------------------------------------------------
# Displaying an important note about integer-to-float conversion.
# -----------------------------------------------------------------------------
print("Note: float() converts an integer into a floating-point number.")
# Output: Note: float() converts an integer into a floating-point number.

# -----------------------------------------------------------------------------
# Displaying another important note.
# -----------------------------------------------------------------------------
print("Example: 50 becomes 50.0 after conversion.")
# Output: Example: 50 becomes 50.0 after conversion.
