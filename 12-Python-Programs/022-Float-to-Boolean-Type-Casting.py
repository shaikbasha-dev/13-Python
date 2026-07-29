"""
===============================================================================
                  Float to Boolean Type Casting
===============================================================================

Program Description:
--------------------
This program demonstrates how to convert a Float data type into a
Boolean data type using the bool() function.

In Python:
0.0 is converted to False.
Any non-zero float is converted to True.

Examples:
0.0    ---> False
15.75  ---> True
-8.25  ---> True

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 22-Float-to-Boolean-Type-Casting.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating a float variable with a non-zero value.
# -----------------------------------------------------------------------------
float_number1 = 45.75
# float_number1 stores the float value 45.75.

# -----------------------------------------------------------------------------
# Displaying the original float value.
# -----------------------------------------------------------------------------
print("Original Float Value :", float_number1)
# Output: Original Float Value : 45.75

# -----------------------------------------------------------------------------
# Displaying the data type of the original variable.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(float_number1))
# Output: Original Data Type : <class 'float'>

# -----------------------------------------------------------------------------
# Converting the non-zero float into a Boolean using bool().
# Any non-zero float is converted to True.
# -----------------------------------------------------------------------------
boolean_value1 = bool(float_number1)
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
# Creating another float variable with the value 0.0.
# -----------------------------------------------------------------------------
float_number2 = 0.0
# float_number2 stores the float value 0.0.

# -----------------------------------------------------------------------------
# Displaying the original float value.
# -----------------------------------------------------------------------------
print("Original Float Value :", float_number2)
# Output: Original Float Value : 0.0

# -----------------------------------------------------------------------------
# Displaying the data type of the original variable.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(float_number2))
# Output: Original Data Type : <class 'float'>

# -----------------------------------------------------------------------------
# Converting the float value 0.0 into a Boolean using bool().
# Zero is converted to False.
# -----------------------------------------------------------------------------
boolean_value2 = bool(float_number2)
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
# Displaying an important note about Float-to-Boolean conversion.
# -----------------------------------------------------------------------------
print("Note: 0.0 converts to False, and any non-zero float converts to True.")
# Output: Note: 0.0 converts to False, and any non-zero float converts to True.
