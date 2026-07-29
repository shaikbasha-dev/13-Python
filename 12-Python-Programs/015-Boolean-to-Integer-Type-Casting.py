"""
===============================================================================
                 Boolean to Integer Type Casting
===============================================================================

Program Description:
--------------------
This program demonstrates how to convert a Boolean data type into an
Integer data type using the int() function.

In Python:
True  is converted to 1
False is converted to 0

Example:
True   --->  1
False  --->  0

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 15-Boolean-to-Integer-Type-Casting.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating a Boolean variable with the value True.
# -----------------------------------------------------------------------------
boolean_value_true = True
# boolean_value_true stores the Boolean value True.

# -----------------------------------------------------------------------------
# Displaying the original Boolean value.
# -----------------------------------------------------------------------------
print("Original Boolean Value :", boolean_value_true)
# Output: Original Boolean Value : True

# -----------------------------------------------------------------------------
# Displaying the data type of the original variable.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(boolean_value_true))
# Output: Original Data Type : <class 'bool'>

# -----------------------------------------------------------------------------
# Converting the Boolean value True into an integer using int().
# True is converted to 1.
# -----------------------------------------------------------------------------
integer_value_true = int(boolean_value_true)
# integer_value_true stores the integer value 1.

# -----------------------------------------------------------------------------
# Displaying the converted integer value.
# -----------------------------------------------------------------------------
print("Converted Integer Value :", integer_value_true)
# Output: Converted Integer Value : 1

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Converted Data Type :", type(integer_value_true))
# Output: Converted Data Type : <class 'int'>

# -----------------------------------------------------------------------------
# Creating another Boolean variable with the value False.
# -----------------------------------------------------------------------------
boolean_value_false = False
# boolean_value_false stores the Boolean value False.

# -----------------------------------------------------------------------------
# Displaying the original Boolean value.
# -----------------------------------------------------------------------------
print("Original Boolean Value :", boolean_value_false)
# Output: Original Boolean Value : False

# -----------------------------------------------------------------------------
# Displaying the data type of the original variable.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(boolean_value_false))
# Output: Original Data Type : <class 'bool'>

# -----------------------------------------------------------------------------
# Converting the Boolean value False into an integer using int().
# False is converted to 0.
# -----------------------------------------------------------------------------
integer_value_false = int(boolean_value_false)
# integer_value_false stores the integer value 0.

# -----------------------------------------------------------------------------
# Displaying the converted integer value.
# -----------------------------------------------------------------------------
print("Converted Integer Value :", integer_value_false)
# Output: Converted Integer Value : 0

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Converted Data Type :", type(integer_value_false))
# Output: Converted Data Type : <class 'int'>

# -----------------------------------------------------------------------------
# Displaying an important note about Boolean-to-Integer conversion.
# -----------------------------------------------------------------------------
print("Note: True converts to 1 and False converts to 0.")
# Output: Note: True converts to 1 and False converts to 0.
