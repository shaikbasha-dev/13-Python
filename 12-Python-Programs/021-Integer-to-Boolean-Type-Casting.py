"""
===============================================================================
                 Integer to Boolean Type Casting
===============================================================================

Program Description:
--------------------
This program demonstrates how to convert an Integer data type into a
Boolean data type using the bool() function.

In Python:
0 is converted to False.
Any non-zero integer is converted to True.

Examples:
0   ---> False
10  ---> True
-25 ---> True

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 21-Integer-to-Boolean-Type-Casting.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating an integer variable with a non-zero value.
# -----------------------------------------------------------------------------
integer_number1 = 100
# integer_number1 stores the integer value 100.

# -----------------------------------------------------------------------------
# Displaying the original integer value.
# -----------------------------------------------------------------------------
print("Original Integer Value :", integer_number1)
# Output: Original Integer Value : 100

# -----------------------------------------------------------------------------
# Displaying the data type of the original variable.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(integer_number1))
# Output: Original Data Type : <class 'int'>

# -----------------------------------------------------------------------------
# Converting the non-zero integer into a Boolean using bool().
# Any non-zero integer is converted to True.
# -----------------------------------------------------------------------------
boolean_value1 = bool(integer_number1)
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
# Creating another integer variable with the value 0.
# -----------------------------------------------------------------------------
integer_number2 = 0
# integer_number2 stores the integer value 0.

# -----------------------------------------------------------------------------
# Displaying the original integer value.
# -----------------------------------------------------------------------------
print("Original Integer Value :", integer_number2)
# Output: Original Integer Value : 0

# -----------------------------------------------------------------------------
# Displaying the data type of the original variable.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(integer_number2))
# Output: Original Data Type : <class 'int'>

# -----------------------------------------------------------------------------
# Converting the integer value 0 into a Boolean using bool().
# Zero is converted to False.
# -----------------------------------------------------------------------------
boolean_value2 = bool(integer_number2)
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
# Displaying an important note about Integer-to-Boolean conversion.
# -----------------------------------------------------------------------------
print("Note: Zero converts to False, and any non-zero integer converts to True.")
# Output: Note: Zero converts to False, and any non-zero integer converts to True.
