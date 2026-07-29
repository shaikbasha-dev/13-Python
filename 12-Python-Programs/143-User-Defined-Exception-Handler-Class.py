"""
===============================================================================
File Name    : 143-User-Defined-Exception-Handler-Class.py
Description  : User-Defined Exception Handler Class in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A User-Defined Exception Handler Class is a custom exception class that
contains its own constructor and methods to provide meaningful error
messages.

Instead of using the default Exception behavior, the custom exception class
can define how the error information is stored and displayed.

Syntax:

class CustomException(Exception):

    def __init__(self, message):
        self.message = message

Example:
Creating a custom exception handler class for age validation.
"""

# -----------------------------------------------------------------------------
# Creating a User-Defined Exception Handler class.
# -----------------------------------------------------------------------------
class InvalidAgeError(Exception):

    # -------------------------------------------------------------------------
    # Defining the constructor.
    # -------------------------------------------------------------------------
    def __init__(self, message):

        # ---------------------------------------------------------------------
        # Initializing the error message.
        # ---------------------------------------------------------------------
        self.message = message

    # -------------------------------------------------------------------------
    # Defining the string representation of the exception.
    # -------------------------------------------------------------------------
    def __str__(self):

        # ---------------------------------------------------------------------
        # Returning the error message.
        # ---------------------------------------------------------------------
        return self.message


# -----------------------------------------------------------------------------
# Creating the Student class.
# -----------------------------------------------------------------------------
class Student:

    # -------------------------------------------------------------------------
    # Defining the constructor.
    # -------------------------------------------------------------------------
    def __init__(self, age):

        # ---------------------------------------------------------------------
        # Initializing the student's age.
        # ---------------------------------------------------------------------
        self.age = age

    # -------------------------------------------------------------------------
    # Creating a method to validate the age.
    # -------------------------------------------------------------------------
    def validate_age(self):

        # ---------------------------------------------------------------------
        # Checking whether the age is valid.
        # ---------------------------------------------------------------------
        if self.age < 18:

            # -----------------------------------------------------------------
            # Raising the custom exception.
            # -----------------------------------------------------------------
            raise InvalidAgeError("Student age must be 18 or above.")

        # ---------------------------------------------------------------------
        # Displaying the success message.
        # ---------------------------------------------------------------------
        print("Student is eligible.")


# -----------------------------------------------------------------------------
# Creating an object of the Student class.
# -----------------------------------------------------------------------------
student = Student(16)

# -----------------------------------------------------------------------------
# Writing the code that may generate an exception.
# -----------------------------------------------------------------------------
try:

    # -------------------------------------------------------------------------
    # Calling the validation method.
    # -------------------------------------------------------------------------
    student.validate_age()

# -----------------------------------------------------------------------------
# Handling the custom exception.
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
# Exception: Student age must be 18 or above.
# Program execution completed.
