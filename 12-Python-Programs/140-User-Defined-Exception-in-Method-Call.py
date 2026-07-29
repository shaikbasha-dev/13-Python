"""
===============================================================================
File Name    : 140-User-Defined-Exception-in-Method-Call.py
Description  : User-Defined Exception in Method Call in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A User-Defined Exception can also be raised inside a method.

The calling code can handle the exception using the try and except blocks.
This approach helps keep validation logic inside the class methods.

Syntax:

class CustomException(Exception):
    pass

class ClassName:

    def method(self):

        raise CustomException("Error Message")

Example:
Raise a custom exception when the student's age is less than 18.
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
# Creating the Student class.
# -----------------------------------------------------------------------------
class Student:

    # -------------------------------------------------------------------------
    # Defining the constructor.
    # -------------------------------------------------------------------------
    def __init__(self, age):

        # ---------------------------------------------------------------------
        # Initializing the age.
        # ---------------------------------------------------------------------
        self.age = age

    # -------------------------------------------------------------------------
    # Creating a method to validate the age.
    # -------------------------------------------------------------------------
    def validate_age(self):

        # ---------------------------------------------------------------------
        # Checking the student's age.
        # ---------------------------------------------------------------------
        if self.age < 18:

            # -----------------------------------------------------------------
            # Raising the user-defined exception.
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
# Exception: Student age must be 18 or above.
# Program execution completed.
