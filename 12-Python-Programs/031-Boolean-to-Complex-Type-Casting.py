"""
===============================================================================
                  Boolean to Complex Type Casting
===============================================================================

Program Description:
--------------------
This program demonstrates how to convert a Boolean data type into a
Complex data type using the complex() function.

During this conversion:
- True is converted to (1+0j)
- False is converted to 0j

Examples:
True  ---> (1+0j)
False ---> 0j

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 31-Boolean-to-Complex-Type-Casting.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Creating a Boolean variable with the value True.
# -----------------------------------------------------------------------------
boolean_value1 = True
# boolean_value1 stores the Boolean value True.

# -----------------------------------------------------------------------------
# Displaying the original Boolean value.
# -----------------------------------------------------------------------------
print("Original Boolean Value :", boolean_value1)
# Output: Original Boolean Value : True

# -----------------------------------------------------------------------------
# Displaying the data type of the original variable.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(boolean_value1))
# Output: Original Data Type : <class 'bool'>

# -----------------------------------------------------------------------------
# Converting the Boolean value True into a complex number using complex().
# True becomes the real part, and the imaginary part is 0.
# -----------------------------------------------------------------------------
complex_number1 = complex(boolean_value1)
# complex_number1 stores the complex value (1+0j).

# -----------------------------------------------------------------------------
# Displaying the converted complex value.
# -----------------------------------------------------------------------------
print("Converted Complex Value :", complex_number1)
# Output: Converted Complex Value : (1+0j)

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Converted Data Type :", type(complex_number1))
# Output: Converted Data Type : <class 'complex'>

# -----------------------------------------------------------------------------
# Displaying the real part of the complex number.
# -----------------------------------------------------------------------------
print("Real Part :", complex_number1.real)
# Output: Real Part : 1.0

# -----------------------------------------------------------------------------
# Displaying the imaginary part of the complex number.
# -----------------------------------------------------------------------------
print("Imaginary Part :", complex_number1.imag)
# Output: Imaginary Part : 0.0

# -----------------------------------------------------------------------------
# Creating another Boolean variable with the value False.
# -----------------------------------------------------------------------------
boolean_value2 = False
# boolean_value2 stores the Boolean value False.

# -----------------------------------------------------------------------------
# Displaying the original Boolean value.
# -----------------------------------------------------------------------------
print("Original Boolean Value :", boolean_value2)
# Output: Original Boolean Value : False

# -----------------------------------------------------------------------------
# Displaying the data type of the original variable.
# -----------------------------------------------------------------------------
print("Original Data Type :", type(boolean_value2))
# Output: Original Data Type : <class 'bool'>

# -----------------------------------------------------------------------------
# Converting the Boolean value False into a complex number using complex().
# False becomes the real part, and the imaginary part is 0.
# -----------------------------------------------------------------------------
complex_number2 = complex(boolean_value2)
# complex_number2 stores the complex value 0j.

# -----------------------------------------------------------------------------
# Displaying the converted complex value.
# -----------------------------------------------------------------------------
print("Converted Complex Value :", complex_number2)
# Output: Converted Complex Value : 0j

# -----------------------------------------------------------------------------
# Displaying the data type after conversion.
# -----------------------------------------------------------------------------
print("Converted Data Type :", type(complex_number2))
# Output: Converted Data Type : <class 'complex'>

# -----------------------------------------------------------------------------
# Displaying the real part of the complex number.
# -----------------------------------------------------------------------------
print("Real Part :", complex_number2.real)
# Output: Real Part : 0.0

# -----------------------------------------------------------------------------
# Displaying the imaginary part of the complex number.
# -----------------------------------------------------------------------------
print("Imaginary Part :", complex_number2.imag)
# Output: Imaginary Part : 0.0

# -----------------------------------------------------------------------------
# Displaying an important note about Boolean-to-Complex conversion.
# -----------------------------------------------------------------------------
print("Note: True converts to (1+0j) and False converts to 0j.")
# Output: Note: True converts to (1+0j) and False converts to 0j.
