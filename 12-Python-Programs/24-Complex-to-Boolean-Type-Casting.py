"""
===============================================================================
                 Complex to Boolean Type Casting
===============================================================================

Program Description:
--------------------
This program demonstrates how to convert a Complex data type into a
Boolean data type using the bool() function.

In Python:
- A complex number with both real and imaginary parts equal to zero
  is converted to False.
- Any non-zero complex number is converted to True.

Examples:
0 + 0j   ---> False
5 + 2j   ---> True
0 + 3j   ---> True
7 + 0j   ---> True

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 24-Complex-to-Boolean-Type-Casting.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating a non-zero complex variable.
# -----------------------------------------------------------------------------
complex_number1 = 10 + 5j
# complex_number1 stores the complex value (10+5j).

# -----------------------------------------------------------------------------
# Displaying the original complex value.
# -----------------------------------------------------------------------------
print("Original Complex Value :", complex_number1)
# Output: Original Complex Value : (10+5j)

# -----------------------------------------------------------------------------
# Displaying the data type of the original variable.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(complex_number1))
# Output: Original Data Type : <class 'complex'>

# -----------------------------------------------------------------------------
# Converting the non-zero complex number into a Boolean using bool().
# Any non-zero complex number is converted to True.
# -----------------------------------------------------------------------------
boolean_value1 = bool(complex_number1)
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
# Creating a zero complex variable.
# -----------------------------------------------------------------------------
complex_number2 = 0 + 0j
# complex_number2 stores the complex value 0j.

# -----------------------------------------------------------------------------
# Displaying the original complex value.
# -----------------------------------------------------------------------------
print("Original Complex Value :", complex_number2)
# Output: Original Complex Value : 0j

# -----------------------------------------------------------------------------
# Displaying the data type of the original variable.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(complex_number2))
# Output: Original Data Type : <class 'complex'>

# -----------------------------------------------------------------------------
# Converting the zero complex number into a Boolean using bool().
# A complex number with both real and imaginary parts equal to zero
# is converted to False.
# -----------------------------------------------------------------------------
boolean_value2 = bool(complex_number2)
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
# Displaying an important note about Complex-to-Boolean conversion.
# -----------------------------------------------------------------------------
print("Note: A non-zero complex number converts to True, while 0j converts to False.")
# Output: Note: A non-zero complex number converts to True, while 0j converts to False.
