"""
===============================================================================
                  Boolean to Float Type Casting
===============================================================================

Program Description:
--------------------
This program demonstrates how to convert a Boolean data type into a
Float data type using the float() function.

In Python:
True  is converted to 1.0
False is converted to 0.0

Example:
True   --->  1.0
False  --->  0.0

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 19-Boolean-to-Float-Type-Casting.py

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
# Converting the Boolean value True into a float using float().
# True is converted to 1.0.
# -----------------------------------------------------------------------------
float_value_true = float(boolean_value_true)
# float_value_true stores the float value 1.0.

# -----------------------------------------------------------------------------
# Displaying the converted float value.
# -----------------------------------------------------------------------------
print("Converted Float Value :", float_value_true)
# Output: Converted Float Value : 1.0

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Converted Data Type :", type(float_value_true))
# Output: Converted Data Type : <class 'float'>

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
# Converting the Boolean value False into a float using float().
# False is converted to 0.0.
# -----------------------------------------------------------------------------
float_value_false = float(boolean_value_false)
# float_value_false stores the float value 0.0.

# -----------------------------------------------------------------------------
# Displaying the converted float value.
# -----------------------------------------------------------------------------
print("Converted Float Value :", float_value_false)
# Output: Converted Float Value : 0.0

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Converted Data Type :", type(float_value_false))
# Output: Converted Data Type : <class 'float'>

# -----------------------------------------------------------------------------
# Displaying an important note about Boolean-to-Float conversion.
# -----------------------------------------------------------------------------
print("Note: True converts to 1.0 and False converts to 0.0.")
# Output: Note: True converts to 1.0 and False converts to 0.0.
