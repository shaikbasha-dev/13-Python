"""
===============================================================================
File Name    : 94-String-Inbuilt-Methods.py
Description  : String Inbuilt Methods in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Python provides many built-in methods to perform different operations on
strings such as changing case, searching, replacing, counting, splitting,
joining, and checking string properties.

Some Common String Methods:
1. upper()
2. lower()
3. title()
4. capitalize()
5. swapcase()
6. replace()
7. find()
8. count()
9. startswith()
10. endswith()

Syntax:
string_name.method_name()

Example:
text.upper()
"""

# -----------------------------------------------------------------------------
# Creating a string.
# -----------------------------------------------------------------------------
text = "welcome to python programming"

# -----------------------------------------------------------------------------
# Displaying the original string.
# -----------------------------------------------------------------------------
print("Original String :", text)
# Output:
# Original String : welcome to python programming

print()

# -----------------------------------------------------------------------------
# Converting the string into uppercase.
# -----------------------------------------------------------------------------
print("upper() :", text.upper())
# Output:
# upper() : WELCOME TO PYTHON PROGRAMMING

# -----------------------------------------------------------------------------
# Converting the string into lowercase.
# -----------------------------------------------------------------------------
print("lower() :", text.lower())
# Output:
# lower() : welcome to python programming

# -----------------------------------------------------------------------------
# Converting the first letter of each word into uppercase.
# -----------------------------------------------------------------------------
print("title() :", text.title())
# Output:
# title() : Welcome To Python Programming

# -----------------------------------------------------------------------------
# Converting the first letter of the string into uppercase.
# -----------------------------------------------------------------------------
print("capitalize() :", text.capitalize())
# Output:
# capitalize() : Welcome to python programming

# -----------------------------------------------------------------------------
# Swapping uppercase letters to lowercase and vice versa.
# -----------------------------------------------------------------------------
print("swapcase() :", text.swapcase())
# Output:
# swapcase() : WELCOME TO PYTHON PROGRAMMING

print()

# -----------------------------------------------------------------------------
# Replacing a word in the string.
# -----------------------------------------------------------------------------
print("replace() :", text.replace("python", "Java"))
# Output:
# replace() : welcome to Java programming

print()

# -----------------------------------------------------------------------------
# Finding the position of a word.
# -----------------------------------------------------------------------------
print("find('python') :", text.find("python"))
# Output:
# find('python') : 11

# -----------------------------------------------------------------------------
# Counting the occurrence of a character.
# -----------------------------------------------------------------------------
print("count('o') :", text.count("o"))
# Output:
# count('o') : 5

print()

# -----------------------------------------------------------------------------
# Checking whether the string starts with a word.
# -----------------------------------------------------------------------------
print("startswith('welcome') :", text.startswith("welcome"))
# Output:
# startswith('welcome') : True

# -----------------------------------------------------------------------------
# Checking whether the string ends with a word.
# -----------------------------------------------------------------------------
print("endswith('programming') :", text.endswith("programming"))
# Output:
# endswith('programming') : True
