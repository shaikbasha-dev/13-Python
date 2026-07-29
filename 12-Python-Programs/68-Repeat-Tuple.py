"""
===============================================================================
File Name    : 68-Repeat-Tuple.py
Description  : Repeat a Tuple in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Tuple repetition is the process of repeating the elements of a tuple multiple
times using the (*) operator.

Syntax:
new_tuple = tuple_name * number

Example:
numbers = (10, 20)
result = numbers * 3
"""

# -----------------------------------------------------------------------------
# Creating a tuple of integers.
# -----------------------------------------------------------------------------
numbers = (10, 20, 30)

# -----------------------------------------------------------------------------
# Displaying the original tuple.
# -----------------------------------------------------------------------------
print("Original Tuple :", numbers)
# Output:
# Original Tuple : (10, 20, 30)

print()

# -----------------------------------------------------------------------------
# Repeating the tuple two times.
# -----------------------------------------------------------------------------
repeated_twice = numbers * 2

# -----------------------------------------------------------------------------
# Displaying the repeated tuple.
# -----------------------------------------------------------------------------
print("Tuple Repeated 2 Times :", repeated_twice)
# Output:
# Tuple Repeated 2 Times : (10, 20, 30, 10, 20, 30)

print()

# -----------------------------------------------------------------------------
# Repeating the tuple three times.
# -----------------------------------------------------------------------------
repeated_thrice = numbers * 3

# -----------------------------------------------------------------------------
# Displaying the repeated tuple.
# -----------------------------------------------------------------------------
print("Tuple Repeated 3 Times :", repeated_thrice)
# Output:
# Tuple Repeated 3 Times : (10, 20, 30, 10, 20, 30, 10, 20, 30)

print()

# -----------------------------------------------------------------------------
# Creating a tuple of strings.
# -----------------------------------------------------------------------------
fruits = ("Apple", "Banana")

# -----------------------------------------------------------------------------
# Repeating the string tuple.
# -----------------------------------------------------------------------------
repeated_fruits = fruits * 2

# -----------------------------------------------------------------------------
# Displaying the repeated string tuple.
# -----------------------------------------------------------------------------
print("Repeated Fruit Tuple :", repeated_fruits)
# Output:
# Repeated Fruit Tuple : ('Apple', 'Banana', 'Apple', 'Banana')

print()

# -----------------------------------------------------------------------------
# Displaying the total number of elements in the repeated tuple.
# -----------------------------------------------------------------------------
print("Total Elements :", len(repeated_thrice))
# Output:
# Total Elements : 9
