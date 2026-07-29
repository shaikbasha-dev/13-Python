"""
===============================================================================
                        Implicit Type Casting
===============================================================================

Program Description:
--------------------
This program demonstrates Implicit Type Casting (Automatic Type Conversion)
in Python.

Implicit Type Casting is performed automatically by the Python interpreter
when two compatible data types are involved in an operation.

Generally, Python converts a smaller data type into a larger data type
to prevent data loss.

Example:
Integer (int) + Float (float) = Float (float)

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 11-Implicit-Type-Casting.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating an integer variable.
# -----------------------------------------------------------------------------
number1 = 10
# number1 stores the integer value 10.

# -----------------------------------------------------------------------------
# Creating a float variable.
# -----------------------------------------------------------------------------
number2 = 20.5
# number2 stores the float value 20.5.

# -----------------------------------------------------------------------------
# Displaying the value of number1.
# -----------------------------------------------------------------------------
print("Value of number1 :", number1)
# Output: Value of number1 : 10

# -----------------------------------------------------------------------------
# Displaying the data type of number1.
# -----------------------------------------------------------------------------
print("Data Type of number1 :", type(number1))
# Output: Data Type of number1 : <class 'int'>

# -----------------------------------------------------------------------------
# Displaying the value of number2.
# -----------------------------------------------------------------------------
print("Value of number2 :", number2)
# Output: Value of number2 : 20.5

# -----------------------------------------------------------------------------
# Displaying the data type of number2.
# -----------------------------------------------------------------------------
print("Data Type of number2 :", type(number2))
# Output: Data Type of number2 : <class 'float'>

# -----------------------------------------------------------------------------
# Adding an integer and a float.
# Python automatically converts the integer into a float before addition.
# This process is known as Implicit Type Casting.
# -----------------------------------------------------------------------------
result = number1 + number2
# result stores the float value 30.5.

# -----------------------------------------------------------------------------
# Displaying the result after addition.
# -----------------------------------------------------------------------------
print("Result :", result)
# Output: Result : 30.5

# -----------------------------------------------------------------------------
# Displaying the data type of the result.
# Since one operand is float, the result is also float.
# -----------------------------------------------------------------------------
print("Data Type of result :", type(result))
# Output: Data Type of result : <class 'float'>
