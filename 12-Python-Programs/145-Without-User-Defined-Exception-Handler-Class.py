"""
===============================================================================
File Name    : 145-Without-User-Defined-Exception-Handler-Class.py
Description  : Without User-Defined Exception Handler Class in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
A program can raise and handle a user-defined exception without creating
a separate exception handler class.

In this approach, the built-in Exception class is used directly to raise
custom error messages.

Syntax:

raise Exception("Error Message")

Example:
Using the built-in Exception class for student age validation.
"""

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
            # Raising the built-in Exception with a custom message.
            # -----------------------------------------------------------------
            raise Exception("Student age must be 18 or above.")

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
# Handling the exception.
# -----------------------------------------------------------------------------
except Exception as error:

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
