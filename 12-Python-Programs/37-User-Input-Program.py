"""
===============================================================================
                           User Input Program
===============================================================================

Program Description:
--------------------
This program demonstrates how to accept input from the user using the
input() function in Python.

The input() function waits for the user to enter a value from the
keyboard. By default, the entered value is stored as a string.

Author      : Shaik Mahaboob Basha
Repository  : 13-Python
File Name   : 37-User-Input-Program.py

===============================================================================
"""

# -----------------------------------------------------------------------------
# Displaying a message to the user.
# -----------------------------------------------------------------------------
print("Python User Input Program")
# Output: Python User Input Program

# -----------------------------------------------------------------------------
# Accepting the user's name using the input() function.
# -----------------------------------------------------------------------------
name = input("Enter Your Name: ")
# The entered value is stored as a string.

# -----------------------------------------------------------------------------
# Displaying the entered name.
# -----------------------------------------------------------------------------
print("Your Name is :", name)
# Output:
# Enter Your Name: Mahaboob
# Your Name is : Mahaboob

# -----------------------------------------------------------------------------
# Displaying the data type of the entered value.
# -----------------------------------------------------------------------------
print("Data Type :", type(name))
# Output: Data Type : <class 'str'>

# -----------------------------------------------------------------------------
# Displaying an important note.
# -----------------------------------------------------------------------------
print("Note: The input() function always returns a string by default.")
# Output: Note: The input() function always returns a string by default.
