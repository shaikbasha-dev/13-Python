"""
===============================================================================
File Name    : 139-User-Defined-Exception.py
Description  : User-Defined Exception in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A User-Defined Exception is a custom exception created by the programmer.

It is created by inheriting from the built-in Exception class. User-defined
exceptions are useful when the built-in exceptions do not meet the program's
requirements.

Syntax:

class CustomException(Exception):
    pass

raise CustomException("Error Message")

Example:
Raise an exception when the user's age is less than 18.
"""

# -----------------------------------------------------------------------------
# Creating a User-Defined Exception class.
# -----------------------------------------------------------------------------
class InvalidAgeError(Exception):

    # -------------------------------------------------------------------------
    # This class inherits from the built-in Exception class.
    # -------------------------------------------------------------------------
    pass


# -----------------------------------------------------------------------------
# Declaring the age.
# -----------------------------------------------------------------------------
age = 16

# -----------------------------------------------------------------------------
# Writing the code that may generate an exception.
# -----------------------------------------------------------------------------
try:

    # -------------------------------------------------------------------------
    # Checking the age.
    # -------------------------------------------------------------------------
    if age < 18:

        # ---------------------------------------------------------------------
        # Raising the user-defined exception.
        # ---------------------------------------------------------------------
        raise InvalidAgeError("Age must be 18 or above.")

    # -------------------------------------------------------------------------
    # Displaying the success message.
    # -------------------------------------------------------------------------
    print("You are eligible.")

# -----------------------------------------------------------------------------
# Handling the user-defined exception.
# -----------------------------------------------------------------------------
except InvalidAgeError as error:

    # -------------------------------------------------------------------------
    # Displaying the exception message.
    # -------------------------------------------------------------------------
    print("Exception:", error)

# -----------------------------------------------------------------------------
# Displaying the remaining program.
# -----------------------------------------------------------------------------
print("Program execution completed.")

# Output:
# Exception: Age must be 18 or above.
# Program execution completed.
