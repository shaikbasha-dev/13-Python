"""
===============================================================================
File Name    : 96-Split-Method.py
Description  : Split Method in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
The split() method is used to split a string into a list of substrings based
on a specified separator. If no separator is provided, the string is split
using whitespace.

Syntax:
string_name.split(separator)

Example:
text.split()
text.split(",")
"""

# -----------------------------------------------------------------------------
# Creating a string with spaces.
# -----------------------------------------------------------------------------
text = "Python is easy to learn"

# -----------------------------------------------------------------------------
# Displaying the original string.
# -----------------------------------------------------------------------------
print("Original String :", text)
# Output:
# Original String : Python is easy to learn

print()

# -----------------------------------------------------------------------------
# Splitting the string using whitespace.
# -----------------------------------------------------------------------------
words = text.split()

# -----------------------------------------------------------------------------
# Displaying the list of words.
# -----------------------------------------------------------------------------
print("After split() :", words)
# Output:
# After split() : ['Python', 'is', 'easy', 'to', 'learn']

print()

# -----------------------------------------------------------------------------
# Creating a comma-separated string.
# -----------------------------------------------------------------------------
fruits = "Apple,Banana,Mango,Orange"

# -----------------------------------------------------------------------------
# Displaying the comma-separated string.
# -----------------------------------------------------------------------------
print("Fruit String :", fruits)
# Output:
# Fruit String : Apple,Banana,Mango,Orange

print()

# -----------------------------------------------------------------------------
# Splitting the string using a comma as the separator.
# -----------------------------------------------------------------------------
fruit_list = fruits.split(",")

# -----------------------------------------------------------------------------
# Displaying the list of fruits.
# -----------------------------------------------------------------------------
print("After split(',') :", fruit_list)
# Output:
# After split(',') : ['Apple', 'Banana', 'Mango', 'Orange']

print()

# -----------------------------------------------------------------------------
# Displaying the total number of words.
# -----------------------------------------------------------------------------
print("Total Words :", len(words))
# Output:
# Total Words : 5

# -----------------------------------------------------------------------------
# Displaying the total number of fruits.
# -----------------------------------------------------------------------------
print("Total Fruits :", len(fruit_list))
# Output:
# Total Fruits : 4
