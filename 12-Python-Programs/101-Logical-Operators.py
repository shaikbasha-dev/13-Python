"""
===============================================================================
File Name    : 101-Logical-Operators.py
Description  : Logical Operators in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Logical operators are used to combine two or more conditions. They return
either True or False based on the evaluation of the conditions.

Logical Operators:
1. and
2. or
3. not

Syntax:
condition1 and condition2
condition1 or condition2
not condition

Example:
10 > 5 and 20 > 15
"""

# -----------------------------------------------------------------------------
# Assigning values to two variables.
# -----------------------------------------------------------------------------
number1 = 20
number2 = 10

# -----------------------------------------------------------------------------
# Displaying the input values.
# -----------------------------------------------------------------------------
print("First Number  :", number1)
# Output:
# First Number  : 20

print("Second Number :", number2)
# Output:
# Second Number : 10

print()

# -----------------------------------------------------------------------------
# Demonstrating the AND logical operator.
# Both conditions must be True for the result to be True.
# -----------------------------------------------------------------------------
print("AND Operator :", number1 > 15 and number2 > 5)
# Output:
# AND Operator : True

# -----------------------------------------------------------------------------
# Demonstrating the OR logical operator.
# At least one condition must be True for the result to be True.
# -----------------------------------------------------------------------------
print("OR Operator :", number1 > 25 or number2 > 5)
# Output:
# OR Operator : True

# -----------------------------------------------------------------------------
# Demonstrating the NOT logical operator.
# It reverses the Boolean result.
# -----------------------------------------------------------------------------
print("NOT Operator :", not (number1 > number2))
# Output:
# NOT Operator : False

print()

# -----------------------------------------------------------------------------
# Additional examples using logical operators.
# -----------------------------------------------------------------------------
print("True and True  :", True and True)
# Output:
# True and True  : True

print("True and False :", True and False)
# Output:
# True and False : False

print("True or False  :", True or False)
# Output:
# True or False  : True

print("not True       :", not True)
# Output:
# not True       : False

print("not False      :", not False)
# Output:
# not False      : True
