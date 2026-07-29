"""

===============================================================================

File Name    : 126-Calculator-Using-Polymorphism.py

Description  : Calculator Using Polymorphism in Python

Author       : Shaik Mahaboob Basha

===============================================================================



Definition:

Polymorphism allows the same method name to perform different operations

depending on the object that calls it.



In this example, different calculator classes implement the same calculate()

method to perform different arithmetic operations.



Syntax:



class ClassName:



    def calculate(self):

        pass



Example:

Addition, Subtraction, Multiplication, and Division calculators implement

the same calculate() method in different ways.

"""



# -----------------------------------------------------------------------------

# Creating the Addition class.

# -----------------------------------------------------------------------------

class Addition:



    # -------------------------------------------------------------------------

    # Creating the calculate method.

    # -------------------------------------------------------------------------

    def calculate(self, num1, num2):



        # ---------------------------------------------------------------------

        # Returning the addition result.

        # ---------------------------------------------------------------------

        return num1 + num2





# -----------------------------------------------------------------------------

# Creating the Subtraction class.

# -----------------------------------------------------------------------------

class Subtraction:



    # -------------------------------------------------------------------------

    # Creating the calculate method.

    # -------------------------------------------------------------------------

    def calculate(self, num1, num2):



        # ---------------------------------------------------------------------

        # Returning the subtraction result.

        # ---------------------------------------------------------------------

        return num1 - num2





# -----------------------------------------------------------------------------

# Creating the Multiplication class.

# -----------------------------------------------------------------------------

class Multiplication:



    # -------------------------------------------------------------------------

    # Creating the calculate method.

    # -------------------------------------------------------------------------

    def calculate(self, num1, num2):



        # ---------------------------------------------------------------------

        # Returning the multiplication result.

        # ---------------------------------------------------------------------

        return num1 * num2





# -----------------------------------------------------------------------------

# Creating the Division class.

# -----------------------------------------------------------------------------

class Division:



    # -------------------------------------------------------------------------

    # Creating the calculate method.

    # -------------------------------------------------------------------------

    def calculate(self, num1, num2):



        # ---------------------------------------------------------------------

        # Returning the division result.

        # ---------------------------------------------------------------------

        return num1 / num2





# -----------------------------------------------------------------------------

# Creating a function that accepts any calculator object.

# -----------------------------------------------------------------------------

def perform_operation(calculator, num1, num2):



    # -------------------------------------------------------------------------

    # Calling the calculate method.

    # -------------------------------------------------------------------------

    result = calculator.calculate(num1, num2)



    # -------------------------------------------------------------------------

    # Returning the result.

    # -------------------------------------------------------------------------

    return result





# -----------------------------------------------------------------------------

# Creating objects of different calculator classes.

# -----------------------------------------------------------------------------

addition = Addition()

subtraction = Subtraction()

multiplication = Multiplication()

division = Division()



# -----------------------------------------------------------------------------

# Declaring input values.

# -----------------------------------------------------------------------------

number1 = 20

number2 = 10



# -----------------------------------------------------------------------------

# Performing addition.

# -----------------------------------------------------------------------------

print("Addition       :", perform_operation(addition, number1, number2))



# -----------------------------------------------------------------------------

# Performing subtraction.

# -----------------------------------------------------------------------------

print("Subtraction    :", perform_operation(subtraction, number1, number2))



# -----------------------------------------------------------------------------

# Performing multiplication.

# -----------------------------------------------------------------------------

print("Multiplication :", perform_operation(multiplication, number1, number2))



# -----------------------------------------------------------------------------

# Performing division.

# -----------------------------------------------------------------------------

print("Division       :", perform_operation(division, number1, number2))



# Output:

# Addition       : 30

# Subtraction    : 10

# Multiplication : 200

# Division       : 2.0
