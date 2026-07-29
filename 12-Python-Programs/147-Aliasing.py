"""
===============================================================================
File Name    : 147-Aliasing.py
Description  : Aliasing in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Aliasing is the process of giving another name (alias) to an existing module,
function, class, or object.

The 'as' keyword is used to create an alias. Aliasing makes long names shorter
and improves code readability.

Syntax:

import module_name as alias_name

from module_name import function_name as alias_name

Example:
Importing the math module using an alias.
"""

# -----------------------------------------------------------------------------
# Importing the built-in math module using an alias.
# -----------------------------------------------------------------------------
import math as m

# -----------------------------------------------------------------------------
# Declaring a number.
# -----------------------------------------------------------------------------
number = 36

# -----------------------------------------------------------------------------
# Finding the square root using the alias.
# -----------------------------------------------------------------------------
square_root = m.sqrt(number)

# -----------------------------------------------------------------------------
# Displaying the square root.
# -----------------------------------------------------------------------------
print("Square Root :", square_root)

# -----------------------------------------------------------------------------
# Displaying the value of PI using the alias.
# -----------------------------------------------------------------------------
print("Value of PI :", m.pi)

# -----------------------------------------------------------------------------
# Calculating the factorial using the alias.
# -----------------------------------------------------------------------------
print("Factorial   :", m.factorial(5))

# Output:
# Square Root : 6.0
# Value of PI : 3.141592653589793
# Factorial   : 120
