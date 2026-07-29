"""
===============================================================================
File Name    : 67-Concatenate-Tuples.py
Description  : Concatenate Tuples in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Tuple concatenation is the process of joining two or more tuples into a single
tuple using the (+) operator.

Syntax:
new_tuple = tuple1 + tuple2

Example:
numbers = (10, 20)
letters = ("A", "B")
result = numbers + letters
"""

# -----------------------------------------------------------------------------
# Creating the first tuple.
# -----------------------------------------------------------------------------
tuple1 = (10, 20, 30)

# -----------------------------------------------------------------------------
# Creating the second tuple.
# -----------------------------------------------------------------------------
tuple2 = (40, 50, 60)

# -----------------------------------------------------------------------------
# Displaying the first tuple.
# -----------------------------------------------------------------------------
print("First Tuple :", tuple1)
# Output:
# First Tuple : (10, 20, 30)

# -----------------------------------------------------------------------------
# Displaying the second tuple.
# -----------------------------------------------------------------------------
print("Second Tuple :", tuple2)
# Output:
# Second Tuple : (40, 50, 60)

print()

# -----------------------------------------------------------------------------
# Concatenating the two tuples.
# -----------------------------------------------------------------------------
combined_tuple = tuple1 + tuple2

# -----------------------------------------------------------------------------
# Displaying the concatenated tuple.
# -----------------------------------------------------------------------------
print("Concatenated Tuple :", combined_tuple)
# Output:
# Concatenated Tuple : (10, 20, 30, 40, 50, 60)

print()

# -----------------------------------------------------------------------------
# Creating two string tuples.
# -----------------------------------------------------------------------------
fruits = ("Apple", "Banana")
colors = ("Red", "Green")

# -----------------------------------------------------------------------------
# Concatenating the string tuples.
# -----------------------------------------------------------------------------
fruit_colors = fruits + colors

# -----------------------------------------------------------------------------
# Displaying the concatenated string tuple.
# -----------------------------------------------------------------------------
print("Fruit and Color Tuple :", fruit_colors)
# Output:
# Fruit and Color Tuple : ('Apple', 'Banana', 'Red', 'Green')

print()

# -----------------------------------------------------------------------------
# Displaying the total number of elements in the concatenated tuple.
# -----------------------------------------------------------------------------
print("Total Elements :", len(combined_tuple))
# Output:
# Total Elements : 6
