"""
===============================================================================
File Name    : 114-Encapsulation.py
Description  : Encapsulation in Python
Author       : Shaik Mahaboob Basha
===============================================================================

Definition:
Encapsulation is the process of combining data (variables) and methods
(functions) into a single unit (class). It also helps protect data by
restricting direct access using private variables.

In Python, private variables are created using double underscores (__).

Benefits of Encapsulation:
1. Data Hiding
2. Data Security
3. Better Code Organization
4. Improved Maintainability

Syntax:
class ClassName:

    def __init__(self):
        self.__variable = value

Example:
self.__balance = 5000
"""

# -----------------------------------------------------------------------------
# Creating a class.
# -----------------------------------------------------------------------------
class BankAccount:

    # -------------------------------------------------------------------------
    # Defining the constructor.
    # -------------------------------------------------------------------------
    def __init__(self, account_holder, balance):

        # ---------------------------------------------------------------------
        # Initializing public instance variable.
        # ---------------------------------------------------------------------
        self.account_holder = account_holder

        # ---------------------------------------------------------------------
        # Initializing private instance variable.
        # ---------------------------------------------------------------------
        self.__balance = balance

    # -------------------------------------------------------------------------
    # Creating a method to display account details.
    # -------------------------------------------------------------------------
    def display_details(self):

        # ---------------------------------------------------------------------
        # Displaying account information.
        # ---------------------------------------------------------------------
        print("Account Holder :", self.account_holder)
        print("Balance        :", self.__balance)

    # -------------------------------------------------------------------------
    # Creating a method to deposit money.
    # -------------------------------------------------------------------------
    def deposit(self, amount):

        # ---------------------------------------------------------------------
        # Adding the deposit amount to the balance.
        # ---------------------------------------------------------------------
        self.__balance = self.__balance + amount

        # ---------------------------------------------------------------------
        # Displaying the updated balance.
        # ---------------------------------------------------------------------
        print(amount, "Deposited Successfully")

    # -------------------------------------------------------------------------
    # Creating a method to return the private balance.
    # -------------------------------------------------------------------------
    def get_balance(self):

        # ---------------------------------------------------------------------
        # Returning the private balance.
        # ---------------------------------------------------------------------
        return self.__balance


# -----------------------------------------------------------------------------
# Creating an object of the BankAccount class.
# -----------------------------------------------------------------------------
account = BankAccount("Basha", 5000)

# -----------------------------------------------------------------------------
# Displaying the account details.
# -----------------------------------------------------------------------------
print("Account Details")
account.display_details()
# Output:
# Account Details
# Account Holder : Basha
# Balance        : 5000

print()

# -----------------------------------------------------------------------------
# Depositing an amount.
# -----------------------------------------------------------------------------
account.deposit(2000)
# Output:
# 2000 Deposited Successfully

print()

# -----------------------------------------------------------------------------
# Displaying the updated balance.
# -----------------------------------------------------------------------------
print("Available Balance :", account.get_balance())
# Output:
# Available Balance : 7000

print()

# -----------------------------------------------------------------------------
# The following statement will produce an AttributeError because the private
# variable cannot be accessed directly outside the class.
# Uncomment the line below to observe the error.
# -----------------------------------------------------------------------------
# print(account.__balance)

# Output:
# AttributeError:
# 'BankAccount' object has no attribute '__balance'
