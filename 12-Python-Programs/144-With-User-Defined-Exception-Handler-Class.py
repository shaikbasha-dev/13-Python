"""
===============================================================================
File Name    : 144-With-User-Defined-Exception-Handler-Class.py
Description  : Using a User-Defined Exception Handler Class in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A User-Defined Exception Handler Class is a custom exception class that
contains its own constructor and methods to provide meaningful error
messages.

In this example, the custom exception stores both an error code and an
error message. The exception is raised inside a class method and handled
using a try-except block.

Syntax:

class CustomException(Exception):

    def __init__(self, error_code, message):
        self.error_code = error_code
        self.message = message

Example:
Using a custom exception handler class with student age validation.
"""

# -----------------------------------------------------------------------------
# Creating a User-Defined Exception Handler class.
# -----------------------------------------------------------------------------
class InvalidAgeError(Exception):

    # -------------------------------------------------------------------------
    # Defining the constructor.
    # -------------------------------------------------------------------------
    def __init__(self, error_code, message):

        # ---------------------------------------------------------------------
        # Initializing the error code and message.
        # ---------------------------------------------------------------------
        self.error_code = error_code
        self.message = message

    # -------------------------------------------------------------------------
    # Defining the string representation of the exception.
    # -------------------------------------------------------------------------
    def __str__(self):

        # ---------------------------------------------------------------------
        # Returning the formatted error information.
        # ---------------------------------------------------------------------
        return f"[{self.error_code}] {self.message}"


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
    # Creating a method to validate the student's age.
    # -------------------------------------------------------------------------
    def validate_age(self):

        # ---------------------------------------------------------------------
        # Checking whether the age is valid.
        # ---------------------------------------------------------------------
        if self.age < 18:

            # -----------------------------------------------------------------
            # Raising the custom exception.
            # -----------------------------------------------------------------
            raise InvalidAgeError(
                "AGE001",
                "Student age must be 18 or above."
            )

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
    # Displaying the exception details.
    # -------------------------------------------------------------------------
    print("Exception:", error)

# -----------------------------------------------------------------------------
# Displaying the remaining program.
# -----------------------------------------------------------------------------
print("Program execution completed.")

# Output:
# Exception: [AGE001] Student age must be 18 or above.
# Program execution completed.
