"""
===============================================================================
File Name    : 104-Bitwise-Operators.py
Description  : Bitwise Operators in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Bitwise operators perform operations directly on the binary (bit)
representation of integer values.

Bitwise Operators:
1. &   (Bitwise AND)
2. |   (Bitwise OR)
3. ^   (Bitwise XOR)
4. ~   (Bitwise NOT)
5. <<  (Left Shift)
6. >>  (Right Shift)

Syntax:
operand1 operator operand2

Example:
5 & 3
"""

# -----------------------------------------------------------------------------
# Assigning values to two variables.
# -----------------------------------------------------------------------------
number1 = 10
number2 = 6

# -----------------------------------------------------------------------------
# Displaying the input values.
# -----------------------------------------------------------------------------
print("First Number  :", number1)
# Output:
# First Number  : 10

print("Second Number :", number2)
# Output:
# Second Number : 6

print()

# -----------------------------------------------------------------------------
# Displaying the binary representation of both numbers.
# -----------------------------------------------------------------------------
print("Binary of", number1, ":", bin(number1))
# Output:
# Binary of 10 : 0b1010

print("Binary of", number2, ":", bin(number2))
# Output:
# Binary of 6 : 0b110

print()

# -----------------------------------------------------------------------------
# Performing Bitwise AND operation.
# -----------------------------------------------------------------------------
print("Bitwise AND (&) :", number1 & number2)
# Output:
# Bitwise AND (&) : 2

# -----------------------------------------------------------------------------
# Performing Bitwise OR operation.
# -----------------------------------------------------------------------------
print("Bitwise OR (|) :", number1 | number2)
# Output:
# Bitwise OR (|) : 14

# -----------------------------------------------------------------------------
# Performing Bitwise XOR operation.
# -----------------------------------------------------------------------------
print("Bitwise XOR (^) :", number1 ^ number2)
# Output:
# Bitwise XOR (^) : 12

# -----------------------------------------------------------------------------
# Performing Bitwise NOT operation.
# -----------------------------------------------------------------------------
print("Bitwise NOT (~) :", ~number1)
# Output:
# Bitwise NOT (~) : -11

print()

# -----------------------------------------------------------------------------
# Performing Left Shift operation.
# -----------------------------------------------------------------------------
print("Left Shift (<< 1) :", number1 << 1)
# Output:
# Left Shift (<< 1) : 20

# -----------------------------------------------------------------------------
# Performing Right Shift operation.
# -----------------------------------------------------------------------------
print("Right Shift (>> 1) :", number1 >> 1)
# Output:
# Right Shift (>> 1) : 5
