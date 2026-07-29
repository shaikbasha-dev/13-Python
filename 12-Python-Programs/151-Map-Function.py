"""
===============================================================================
File Name    : 151-Map-Function.py
Description  : Map Function in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
The map() function is a built-in Python function used to apply a function
to every item in an iterable such as a list, tuple, or set.

The map() function returns a map object, which can be converted into a
list, tuple, or other iterable.

Syntax:

map(function_name, iterable)

Example:
Using the map() function to find the square of each number in a list.
"""

# -----------------------------------------------------------------------------
# Creating a function to calculate the square of a number.
# -----------------------------------------------------------------------------
def square(number):

    # -------------------------------------------------------------------------
    # Returning the square of the number.
    # -------------------------------------------------------------------------
    return number * number


# -----------------------------------------------------------------------------
# Creating a list of numbers.
# -----------------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5]

# -----------------------------------------------------------------------------
# Applying the square() function to each element using map().
# -----------------------------------------------------------------------------
result = map(square, numbers)

# -----------------------------------------------------------------------------
# Converting the map object into a list.
# -----------------------------------------------------------------------------
square_numbers = list(result)

# -----------------------------------------------------------------------------
# Displaying the original list.
# -----------------------------------------------------------------------------
print("Original List :", numbers)

# -----------------------------------------------------------------------------
# Displaying the squared values.
# -----------------------------------------------------------------------------
print("Square List   :", square_numbers)

# Output:
# Original List : [1, 2, 3, 4, 5]
# Square List   : [1, 4, 9, 16, 25]
