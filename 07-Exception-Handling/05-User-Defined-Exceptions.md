# User-Defined Exceptions in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What are User-Defined Exceptions?
5. Why are User-Defined Exceptions Required?
6. Creating a Custom Exception
7. Inheriting from the Exception Class
8. Raising User-Defined Exceptions
9. Handling User-Defined Exceptions
10. Internal Working
11. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand User-Defined Exceptions.
- Create custom exception classes.
- Inherit from the built-in Exception class.
- Raise and handle custom exceptions.
- Use custom exceptions in real-world applications.
- Write cleaner and more maintainable programs.

---

# Prerequisites

Before learning this chapter, you should know:

- Exception Handling
- try-except Blocks
- else and finally Blocks
- raise Keyword
- Classes and Inheritance

---

# Introduction

Python provides many built-in exceptions such as:

- ValueError
- TypeError
- IndexError
- KeyError

These exceptions are suitable for common programming errors.

However,

real-world applications often have their own business rules.

For example,

a Banking Application may need to display

```text
Insufficient Balance
```

instead of

```text
ValueError
```

Similarly,

a College Management System may require

```text
Invalid Student ID
```

instead of a generic exception.

To handle such situations,

Python allows developers to create their own exceptions.

These are called **User-Defined Exceptions** or **Custom Exceptions**.

---

# What are User-Defined Exceptions?

## Definition

A **User-Defined Exception** is a custom exception created by the programmer to represent application-specific errors.

It is created by defining a class that inherits from Python's built-in

```python
Exception
```

class.

---

## Simple Definition

> A User-Defined Exception is a custom exception created to handle business-specific or application-specific errors.

---

# Why are User-Defined Exceptions Required?

Suppose we are developing an ATM Application.

If the account balance is

```text
₹5,000
```

and the customer requests

```text
₹10,000
```

Using

```python
ValueError
```

is technically correct,

but it does not clearly describe the business problem.

Instead,

we can create

```text
InsufficientBalanceError
```

which clearly communicates the reason for the failure.

This makes the application easier to understand and maintain.

---

# Real-World Applications

User-Defined Exceptions are commonly used in:

- Banking Applications
- Hospital Management Systems
- Student Management Systems
- E-Commerce Websites
- Airline Reservation Systems
- Inventory Management
- Payment Gateways
- REST APIs

---

# Creating a Custom Exception

A custom exception is created by inheriting from

```python
Exception
```

Syntax

```python
class CustomException(Exception):

    pass
```

Example

```python
class InvalidAgeError(Exception):

    pass
```

---

# Inheriting from the Exception Class

Every custom exception should inherit from

```python
Exception
```

Example

```python
class InsufficientBalanceError(Exception):

    pass
```

This allows Python's exception handling mechanism to recognize the custom exception.

---

# Raising User-Defined Exceptions

A custom exception is raised using the

```python
raise
```

keyword.

Example

```python
raise InvalidAgeError("Age must be at least 18.")
```

---

# Handling User-Defined Exceptions

A custom exception is handled just like any built-in exception.

Example

```python
try:

    raise InvalidAgeError("Age must be at least 18.")

except InvalidAgeError as error:

    print(error)
```

---

# Exception Propagation

When a custom exception is raised,

Python searches for the nearest matching

```python
except
```

block.

If found,

the exception is handled.

Otherwise,

the program terminates and displays a traceback.

---

# Internal Working

```text
Program Starts

↓

Business Rule Checked

↓

Rule Violated?

↓

No

↓

Continue Program

------------------------

Yes

↓

Create Custom Exception Object

↓

raise Statement

↓

Search Matching except Block

↓

Found?

↓

Yes

↓

Handle Exception

↓

Continue Program

------------------------

No

↓

Program Terminates
```

---

# Advantages

- Creates meaningful error types.
- Improves code readability.
- Simplifies debugging.
- Represents business rules clearly.
- Produces maintainable applications.

---

# Best Practices

- Give custom exceptions meaningful names.
- End exception class names with "Error".
- Inherit from `Exception`.
- Provide clear error messages.
- Use custom exceptions only for business-specific problems.

---

# Common Mistakes

## Mistake 1

Not inheriting from

```python
Exception
```

Custom exceptions should always inherit from `Exception` (or one of its subclasses).

---

## Mistake 2

Using generic names.

❌ Bad

```python
class MyException(Exception):
```

✅ Better

```python
class InvalidAgeError(Exception):
```

---

## Mistake 3

Using custom exceptions for ordinary programming mistakes.

Reserve custom exceptions for business rules and domain-specific errors.

---

# Interview Questions

## 1. What is a User-Defined Exception?

### Answer

A User-Defined Exception is a custom exception created by the programmer for application-specific errors.

---

## 2. How do you create a custom exception?

### Answer

By creating a class that inherits from `Exception`.

---

## 3. Why should custom exceptions inherit from `Exception`?

### Answer

So that Python recognizes them as exceptions and they work correctly with `try-except`.

---

## 4. How do you raise a custom exception?

### Answer

Using the `raise` keyword.

---

## 5. Can custom exceptions include error messages?

### Answer

Yes.

They can include custom messages just like built-in exceptions.

---

# Quick Revision

- User-Defined Exceptions are custom exceptions.
- Inherit from `Exception`.
- Raise using `raise`.
- Handle using `try-except`.
- Use for business-specific validation.

---

# Chapter Summary

In this chapter, we learned:

- User-Defined Exceptions
- Creating Custom Exception Classes
- Inheriting from `Exception`
- Raising Custom Exceptions
- Handling Custom Exceptions
- Internal Working
- Best Practices
- Common Mistakes
- Interview Questions
- Quick Revision


# Program 1 – Creating a Simple User-Defined Exception

## Problem Statement

Write a Python program to create and raise a custom exception.

---

## Program

```python
class InvalidAgeError(Exception):

    pass


raise InvalidAgeError("Age must be at least 18.")
```

---

## Output

```text
InvalidAgeError: Age must be at least 18.
```

---

## Explanation

A custom exception named

```python
InvalidAgeError
```

is created by inheriting from

```python
Exception
```

The exception is raised using the

```python
raise
```

statement.

---

# Program 2 – Handling a User-Defined Exception

## Program

```python
class InvalidAgeError(Exception):

    pass


try:

    age = int(input("Enter Age : "))

    if age < 18:

        raise InvalidAgeError("Age must be at least 18.")

    print("Eligible")

except InvalidAgeError as error:

    print(error)
```

---

## Sample Output

```text
Enter Age : 16

Age must be at least 18.
```

---

## Explanation

The custom exception is raised when the condition fails

and handled using

```python
except InvalidAgeError
```

---

# Program 3 – Insufficient Balance Exception

## Program

```python
class InsufficientBalanceError(Exception):

    pass


balance = 5000

withdraw = int(input("Enter Amount : "))

if withdraw > balance:

    raise InsufficientBalanceError("Insufficient Balance.")

balance -= withdraw

print("Remaining Balance :", balance)
```

---

## Sample Output

```text
Enter Amount : 7000

InsufficientBalanceError: Insufficient Balance.
```

---

## Explanation

Instead of raising a generic

```python
ValueError
```

the program raises a business-specific exception.

---

# Program 4 – Invalid Marks Exception

## Program

```python
class InvalidMarksError(Exception):

    pass


marks = int(input("Enter Marks : "))

if marks < 0 or marks > 100:

    raise InvalidMarksError("Marks must be between 0 and 100.")

print("Marks Accepted")
```

---

## Sample Output

```text
Enter Marks : 120

InvalidMarksError: Marks must be between 0 and 100.
```

---

# Program 5 – Invalid Salary Exception

## Program

```python
class InvalidSalaryError(Exception):

    pass


salary = int(input("Enter Salary : "))

if salary < 0:

    raise InvalidSalaryError("Salary cannot be negative.")

print("Salary Accepted")
```

---

## Sample Output

```text
Enter Salary : -5000

InvalidSalaryError: Salary cannot be negative.
```

---

# Program 6 – Password Validation Exception

## Program

```python
class WeakPasswordError(Exception):

    pass


password = input("Enter Password : ")

if len(password) < 8:

    raise WeakPasswordError(
        "Password must contain at least 8 characters."
    )

print("Password Accepted")
```

---

## Sample Output

```text
Enter Password : admin

WeakPasswordError: Password must contain at least 8 characters.
```

---

## Explanation

The custom exception clearly indicates the business rule.

---

# Program 7 – Student Admission Example

## Program

```python
class AdmissionError(Exception):

    pass


percentage = float(input("Enter Percentage : "))

if percentage < 60:

    raise AdmissionError(
        "Minimum 60% is required for admission."
    )

print("Admission Approved")
```

---

## Sample Output

```text
Enter Percentage : 52

AdmissionError: Minimum 60% is required for admission.
```

---

# Program 8 – Product Stock Validation

## Program

```python
class OutOfStockError(Exception):

    pass


stock = 5

required = int(input("Required Quantity : "))

if required > stock:

    raise OutOfStockError("Product is out of stock.")

print("Order Confirmed")
```

---

## Sample Output

```text
Required Quantity : 10

OutOfStockError: Product is out of stock.
```

---

# Program 9 – Library Book Issue System

## Program

```python
class BookNotAvailableError(Exception):

    pass


available = False

if not available:

    raise BookNotAvailableError(
        "Requested book is not available."
    )

print("Book Issued")
```

---

## Output

```text
BookNotAvailableError:
Requested book is not available.
```

---

# Program 10 – Complete Example using try-except

## Program

```python
class InvalidAgeError(Exception):

    pass


try:

    age = int(input("Enter Age : "))

    if age < 18:

        raise InvalidAgeError(
            "Age must be at least 18."
        )

    print("Registration Successful")

except InvalidAgeError as error:

    print(error)
```

---

## Sample Output

```text
Enter Age : 15

Age must be at least 18.
```

---

## Explanation

The exception is

- Created
- Raised
- Handled

using Python's exception handling mechanism.

---

# Dry Run

```text
Program Starts

↓

Input Accepted

↓

Business Rule Checked

↓

Rule Violated?

↓

No

↓

Continue Program

------------------------

Yes

↓

raise

↓

Custom Exception Object Created

↓

Matching except Found

↓

Handle Exception

↓

Program Continues
```

---

# Memory Representation

```text
Program

↓

Input

↓

Business Validation

↓

Condition Failed

↓

Custom Exception Object

↓

raise

↓

except Block

↓

Program Continues
```

---

# Advantages

- Represents business rules clearly.
- Improves readability.
- Produces meaningful error messages.
- Simplifies debugging.
- Makes enterprise applications easier to maintain.

---

# Best Practices

- Inherit custom exceptions from `Exception`.
- Use descriptive class names ending with `Error`.
- Provide meaningful exception messages.
- Raise exceptions only for exceptional conditions.
- Handle exceptions appropriately.

---

# Common Mistakes

## Mistake 1

Creating a custom exception without inheriting from `Exception`.

❌ Incorrect

```python
class InvalidAgeError:

    pass
```

---

## Mistake 2

Using unclear exception names.

❌ Incorrect

```python
class MyError(Exception):
```

✅ Better

```python
class InvalidAgeError(Exception):
```

---

## Mistake 3

Using custom exceptions for syntax or programming mistakes.

Custom exceptions should represent application-specific rules.

---

## Mistake 4

Raising custom exceptions without meaningful messages.

Always explain why the exception occurred.

---

# Interview Questions

## 1. What is a User-Defined Exception?

### Answer

A User-Defined Exception is a custom exception created by the programmer for application-specific or business-specific errors.

---

## 2. Which class should custom exceptions inherit from?

### Answer

```python
Exception
```

---

## 3. Why do we create custom exceptions?

### Answer

To represent business rules clearly and improve code readability.

---

## 4. How do you raise a custom exception?

### Answer

Using the `raise` keyword.

---

## 5. Can custom exceptions contain error messages?

### Answer

Yes.

They can contain meaningful messages just like built-in exceptions.

---

## 6. How are custom exceptions handled?

### Answer

Using `try-except`, just like built-in exceptions.

---

## 7. When should custom exceptions be used?

### Answer

When built-in exceptions do not clearly describe an application's business rules.

---

# Practice Programs

1. Create an `InvalidAgeError`.
2. Create an `InsufficientBalanceError`.
3. Create a `WeakPasswordError`.
4. Create an `InvalidMarksError`.
5. Create a `BookNotAvailableError`.

---

# Quick Revision

- Custom Exception → Programmer-created exception.
- Inherit from `Exception`.
- Raise using `raise`.
- Handle using `try-except`.
- Use meaningful class names and messages.

---

# Chapter Summary

In this chapter, we learned:

- User-Defined Exceptions
- Creating Custom Exception Classes
- Raising Custom Exceptions
- Handling Custom Exceptions
- Business Rule Validation
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
