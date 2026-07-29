"""
===============================================================================
File Name    : 93-Types-of-String-Creation.py
Description  : Types of String Creation in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A string is a sequence of characters enclosed within single quotes, double
quotes, or triple quotes. Python provides multiple ways to create strings
depending on the requirement.

Types of String Creation:
1. Single Quotes
2. Double Quotes
3. Triple Single Quotes
4. Triple Double Quotes
5. Using the str() Function

Syntax:
string_name = 'Hello'
string_name = "Hello"
string_name = '''Hello'''
string_name = """Hello"""
string_name = str(value)

Example:
name = "Rahul"
"""

# -----------------------------------------------------------------------------
# Creating a string using single quotes.
# -----------------------------------------------------------------------------
single_quote_string = 'Python'

# -----------------------------------------------------------------------------
# Displaying the single quote string.
# -----------------------------------------------------------------------------
print("Single Quote String :", single_quote_string)
# Output:
# Single Quote String : Python

print()

# -----------------------------------------------------------------------------
# Creating a string using double quotes.
# -----------------------------------------------------------------------------
double_quote_string = "Programming"

# -----------------------------------------------------------------------------
# Displaying the double quote string.
# -----------------------------------------------------------------------------
print("Double Quote String :", double_quote_string)
# Output:
# Double Quote String : Programming

print()

# -----------------------------------------------------------------------------
# Creating a string using triple single quotes.
# -----------------------------------------------------------------------------
triple_single_quote_string = '''Welcome to
Python Programming'''

# -----------------------------------------------------------------------------
# Displaying the triple single quote string.
# -----------------------------------------------------------------------------
print("Triple Single Quote String :")
print(triple_single_quote_string)
# Output:
# Triple Single Quote String :
# Welcome to
# Python Programming

print()

# -----------------------------------------------------------------------------
# Creating a string using triple double quotes.
# -----------------------------------------------------------------------------
triple_double_quote_string = """Learning
Python Strings"""

# -----------------------------------------------------------------------------
# Displaying the triple double quote string.
# -----------------------------------------------------------------------------
print("Triple Double Quote String :")
print(triple_double_quote_string)
# Output:
# Triple Double Quote String :
# Learning
# Python Strings

print()

# -----------------------------------------------------------------------------
# Creating a string using the str() function.
# -----------------------------------------------------------------------------
number = 100
string_from_number = str(number)

# -----------------------------------------------------------------------------
# Displaying the string created using the str() function.
# -----------------------------------------------------------------------------
print("String Using str() Function :", string_from_number)
# Output:
# String Using str() Function : 100

print()

# -----------------------------------------------------------------------------
# Displaying the data type of the converted value.
# -----------------------------------------------------------------------------
print("Type :", type(string_from_number))
# Output:
# Type : <class 'str'>
