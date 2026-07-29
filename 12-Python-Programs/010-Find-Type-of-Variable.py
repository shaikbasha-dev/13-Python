"""
===============================================================================
                        Find Type of Variable
===============================================================================

Program Description:
--------------------
This program demonstrates how to determine the data type of a variable
using the built-in type() function in Python.

The type() function returns the class (data type) of the specified object.

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 10-Find-Type-of-Variable.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating an integer variable.
# -----------------------------------------------------------------------------
integer_number = 100
# integer_number stores the integer value 100.

# -----------------------------------------------------------------------------
# Creating a float variable.
# -----------------------------------------------------------------------------
float_number = 99.99
# float_number stores the float value 99.99.

# -----------------------------------------------------------------------------
# Creating a Boolean variable.
# -----------------------------------------------------------------------------
boolean_value = True
# boolean_value stores the Boolean value True.

# -----------------------------------------------------------------------------
# Creating a string variable.
# -----------------------------------------------------------------------------
student_name = "Shaik Mahaboob Basha"
# student_name stores the string "Shaik Mahaboob Basha".

# -----------------------------------------------------------------------------
# Creating a complex variable.
# -----------------------------------------------------------------------------
complex_number = 20 + 10j
# complex_number stores the complex value 20+10j.

# -----------------------------------------------------------------------------
# Displaying the data type of the integer variable.
# type() returns the data type of integer_number.
# -----------------------------------------------------------------------------
print("Data Type of integer_number :", type(integer_number))
# Output: Data Type of integer_number : <class 'int'>

# -----------------------------------------------------------------------------
# Displaying the data type of the float variable.
# type() returns the data type of float_number.
# -----------------------------------------------------------------------------
print("Data Type of float_number :", type(float_number))
# Output: Data Type of float_number : <class 'float'>

# -----------------------------------------------------------------------------
# Displaying the data type of the Boolean variable.
# type() returns the data type of boolean_value.
# -----------------------------------------------------------------------------
print("Data Type of boolean_value :", type(boolean_value))
# Output: Data Type of boolean_value : <class 'bool'>

# -----------------------------------------------------------------------------
# Displaying the data type of the string variable.
# type() returns the data type of student_name.
# -----------------------------------------------------------------------------
print("Data Type of student_name :", type(student_name))
# Output: Data Type of student_name : <class 'str'>

# -----------------------------------------------------------------------------
# Displaying the data type of the complex variable.
# type() returns the data type of complex_number.
# -----------------------------------------------------------------------------
print("Data Type of complex_number :", type(complex_number))
# Output: Data Type of complex_number : <class 'complex'>
