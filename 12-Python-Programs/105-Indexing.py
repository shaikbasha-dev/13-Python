"""
===============================================================================
File Name    : 105-Indexing.py
Description  : Indexing in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Indexing is used to access individual characters or elements from a sequence
such as a string, list, or tuple by using their index positions.

Types of Indexing:
1. Positive Indexing
2. Negative Indexing

Positive Indexing:
Starts from 0 and moves from left to right.

Negative Indexing:
Starts from -1 and moves from right to left.

Syntax:
sequence[index]

Example:
text[0]
text[-1]
"""

# -----------------------------------------------------------------------------
# Creating a string.
# -----------------------------------------------------------------------------
text = "Python"

# -----------------------------------------------------------------------------
# Displaying the original string.
# -----------------------------------------------------------------------------
print("String :", text)
# Output:
# String : Python

print()

# -----------------------------------------------------------------------------
# Accessing characters using positive indexing.
# -----------------------------------------------------------------------------
print("First Character (Index 0) :", text[0])
# Output:
# First Character (Index 0) : P

print("Second Character (Index 1) :", text[1])
# Output:
# Second Character (Index 1) : y

print("Third Character (Index 2) :", text[2])
# Output:
# Third Character (Index 2) : t

print("Last Character Using Positive Index (Index 5) :", text[5])
# Output:
# Last Character Using Positive Index (Index 5) : n

print()

# -----------------------------------------------------------------------------
# Accessing characters using negative indexing.
# -----------------------------------------------------------------------------
print("Last Character (Index -1) :", text[-1])
# Output:
# Last Character (Index -1) : n

print("Second Last Character (Index -2) :", text[-2])
# Output:
# Second Last Character (Index -2) : o

print("Third Last Character (Index -3) :", text[-3])
# Output:
# Third Last Character (Index -3) : h

print()

# -----------------------------------------------------------------------------
# Displaying all index positions.
# -----------------------------------------------------------------------------
print("Positive Index Positions")
print("P -> 0")
print("y -> 1")
print("t -> 2")
print("h -> 3")
print("o -> 4")
print("n -> 5")

print()

print("Negative Index Positions")
print("P -> -6")
print("y -> -5")
print("t -> -4")
print("h -> -3")
print("o -> -2")
print("n -> -1")
