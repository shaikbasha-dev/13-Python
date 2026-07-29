"""
===============================================================================
File Name    : 103-Membership-Operators.py
Description  : Membership Operators in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Membership operators are used to check whether a value exists in a sequence
such as a string, list, tuple, set, or dictionary.

Membership Operators:
1. in
2. not in

Syntax:
value in sequence
value not in sequence

Example:
"Python" in languages
"""

# -----------------------------------------------------------------------------
# Creating a list of programming languages.
# -----------------------------------------------------------------------------
languages = ["Python", "Java", "C", "C++", "JavaScript"]

# -----------------------------------------------------------------------------
# Displaying the list.
# -----------------------------------------------------------------------------
print("Programming Languages :", languages)
# Output:
# Programming Languages : ['Python', 'Java', 'C', 'C++', 'JavaScript']

print()

# -----------------------------------------------------------------------------
# Checking whether "Python" is present in the list.
# -----------------------------------------------------------------------------
print("'Python' in languages :", "Python" in languages)
# Output:
# 'Python' in languages : True

# -----------------------------------------------------------------------------
# Checking whether "HTML" is present in the list.
# -----------------------------------------------------------------------------
print("'HTML' in languages :", "HTML" in languages)
# Output:
# 'HTML' in languages : False

print()

# -----------------------------------------------------------------------------
# Checking whether "Java" is not present in the list.
# -----------------------------------------------------------------------------
print("'Java' not in languages :", "Java" not in languages)
# Output:
# 'Java' not in languages : False

# -----------------------------------------------------------------------------
# Checking whether "HTML" is not present in the list.
# -----------------------------------------------------------------------------
print("'HTML' not in languages :", "HTML" not in languages)
# Output:
# 'HTML' not in languages : True

print()

# -----------------------------------------------------------------------------
# Creating a string.
# -----------------------------------------------------------------------------
text = "Python Programming"

# -----------------------------------------------------------------------------
# Displaying the string.
# -----------------------------------------------------------------------------
print("String :", text)
# Output:
# String : Python Programming

print()

# -----------------------------------------------------------------------------
# Checking whether a substring exists in the string.
# -----------------------------------------------------------------------------
print("'Python' in text :", "Python" in text)
# Output:
# 'Python' in text : True

# -----------------------------------------------------------------------------
# Checking whether a substring does not exist in the string.
# -----------------------------------------------------------------------------
print("'Java' not in text :", "Java" not in text)
# Output:
# 'Java' not in text : True
