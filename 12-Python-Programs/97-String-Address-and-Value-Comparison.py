"""
===============================================================================
File Name    : 97-String-Address-and-Value-Comparison.py
Description  : String Address and Value Comparison in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Strings can be compared in two different ways:
1. Value Comparison using (==)
2. Address Comparison using (is)

== Operator:
Checks whether the values (contents) of two strings are equal.

is Operator:
Checks whether both variables refer to the same object in memory.

Syntax:
string1 == string2
string1 is string2

Example:
name1 = "Python"
name2 = "Python"

print(name1 == name2)
print(name1 is name2)
"""

# -----------------------------------------------------------------------------
# Creating the first string.
# -----------------------------------------------------------------------------
string1 = "Python"

# -----------------------------------------------------------------------------
# Creating the second string with the same value.
# -----------------------------------------------------------------------------
string2 = "Python"

# -----------------------------------------------------------------------------
# Creating the third string with a different value.
# -----------------------------------------------------------------------------
string3 = "Java"

# -----------------------------------------------------------------------------
# Displaying the string values.
# -----------------------------------------------------------------------------
print("String 1 :", string1)
# Output:
# String 1 : Python

print("String 2 :", string2)
# Output:
# String 2 : Python

print("String 3 :", string3)
# Output:
# String 3 : Java

print()

# -----------------------------------------------------------------------------
# Comparing the values of string1 and string2.
# -----------------------------------------------------------------------------
print("string1 == string2 :", string1 == string2)
# Output:
# string1 == string2 : True

# -----------------------------------------------------------------------------
# Comparing the memory addresses of string1 and string2.
# -----------------------------------------------------------------------------
print("string1 is string2 :", string1 is string2)
# Output:
# string1 is string2 : True

print()

# -----------------------------------------------------------------------------
# Comparing the values of string1 and string3.
# -----------------------------------------------------------------------------
print("string1 == string3 :", string1 == string3)
# Output:
# string1 == string3 : False

# -----------------------------------------------------------------------------
# Comparing the memory addresses of string1 and string3.
# -----------------------------------------------------------------------------
print("string1 is string3 :", string1 is string3)
# Output:
# string1 is string3 : False

print()

# -----------------------------------------------------------------------------
# Displaying the memory address of each string.
# -----------------------------------------------------------------------------
print("Address of string1 :", id(string1))
# Output:
# Address of string1 : (Memory Address)

print("Address of string2 :", id(string2))
# Output:
# Address of string2 : (Memory Address)

print("Address of string3 :", id(string3))
# Output:
# Address of string3 : (Memory Address)
