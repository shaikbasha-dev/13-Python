# Raising Exceptions in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is Raising an Exception?
5. Why Raise Exceptions?
6. The raise Keyword
7. Syntax
8. Built-in Exceptions
9. Custom Error Messages
10. Internal Working
11. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the `raise` keyword.
- Learn when and why exceptions should be raised.
- Raise built-in exceptions manually.
- Create meaningful exception messages.
- Understand how exception propagation works.
- Write robust and maintainable Python programs.

---

# Prerequisites

Before learning this chapter, you should know:

- Exception Handling
- try Block
- except Block
- else Block
- finally Block

---

# Introduction

In the previous chapters,

we learned how to **handle exceptions** after they occur.

Sometimes,

a program must **detect an invalid condition** and immediately stop normal execution.

For example,

a Banking Application should not allow a withdrawal amount greater than the available balance.

Instead of allowing incorrect operations,

the program should raise an exception.

Python provides the

```python
raise
```

keyword for this purpose.

---

# What is Raising an Exception?

## Definition

**Raising an Exception** means creating an exception intentionally when an invalid condition is detected during program execution.

Instead of waiting for Python to generate an exception automatically,

the programmer explicitly raises the exception.

---

## Simple Definition

> Raising an exception means generating an exception manually using the `raise` keyword.

---

# Why Raise Exceptions?

Suppose we are developing an ATM Application.

Current Balance

```text
₹5,000
```

User Requests

```text
Withdraw ₹10,000
```

Without validation,

the transaction may continue incorrectly.

Instead,

the application should raise an exception such as

```text
Insufficient Balance
```

and stop the transaction.

---

# Real-World Applications

The `raise` keyword is commonly used in:

- Banking Applications
- E-Commerce Websites
- Login Systems
- Payment Gateways
- Hospital Management Systems
- Student Management Systems
- Inventory Applications
- API Development

---

# The raise Keyword

The `raise` keyword is used to generate an exception manually.

Syntax

```python
raise ExceptionType
```

Example

```python
raise ValueError
```

or

```python
raise ValueError("Invalid Input")
```

---

# Syntax

## Raising a Built-in Exception

```python
raise ValueError("Invalid Age")
```

---

## Raising TypeError

```python
raise TypeError("Only Integer Values Allowed")
```

---

## Raising ZeroDivisionError

```python
raise ZeroDivisionError("Cannot Divide by Zero")
```

---

## Raising RuntimeError

```python
raise RuntimeError("Unexpected Runtime Error")
```

---

# Built-in Exceptions Commonly Raised

| Exception | Used When |
|------------|-----------|
| ValueError | Invalid value supplied |
| TypeError | Wrong data type |
| ZeroDivisionError | Division by zero |
| IndexError | Invalid index |
| KeyError | Invalid dictionary key |
| FileNotFoundError | Missing file |
| PermissionError | Permission denied |
| RuntimeError | General runtime issue |

---

# Custom Error Messages

Every exception can include a custom message.

Example

```python
raise ValueError("Age must be greater than 18.")
```

Output

```text
ValueError:
Age must be greater than 18.
```

Meaningful error messages make debugging easier.

---

# Exception Propagation

When an exception is raised,

Python searches for the nearest matching

```python
except
```

block.

If a matching handler exists,

the exception is handled.

Otherwise,

the program terminates and displays a traceback.

---

# Internal Working

```text
Program Executes

↓

Condition Checked

↓

Condition Invalid?

↓

No

↓

Continue Program

------------------------

Yes

↓

raise Statement Executes

↓

Exception Object Created

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

- Detects invalid conditions early.
- Prevents incorrect program execution.
- Improves code reliability.
- Produces meaningful error messages.
- Simplifies debugging.
- Helps enforce business rules.

---

# Best Practices

- Raise specific exceptions instead of generic ones.
- Write meaningful exception messages.
- Raise exceptions only for exceptional situations.
- Validate input before processing.
- Keep business rules clear and consistent.

---

# Common Mistakes

## Mistake 1

Raising a generic exception unnecessarily.

Prefer

```python
raise ValueError(...)
```

instead of

```python
raise Exception(...)
```

when a more specific exception applies.

---

## Mistake 2

Using vague error messages.

Poor example

```python
raise ValueError("Error")
```

Better example

```python
raise ValueError("Age must be greater than or equal to 18.")
```

---

## Mistake 3

Using `raise` for normal program flow.

Exceptions should represent exceptional situations,

not ordinary control flow.

---

# Interview Questions

## 1. What is the purpose of the `raise` keyword?

### Answer

The `raise` keyword is used to generate an exception manually.

---

## 2. Why do we raise exceptions?

### Answer

To detect invalid conditions and stop incorrect program execution.

---

## 3. Can we raise built-in exceptions?

### Answer

Yes.

Python allows built-in exceptions such as `ValueError`, `TypeError`, and `RuntimeError` to be raised manually.

---

## 4. Can we provide custom error messages?

### Answer

Yes.

Custom messages can be passed while raising an exception.

---

## 5. What happens after an exception is raised?

### Answer

Python searches for the nearest matching `except` block.

If none is found,

the program terminates with a traceback.

---

# Quick Revision

- `raise` generates an exception manually.
- Use specific exception classes.
- Provide meaningful error messages.
- Exceptions represent abnormal situations.
- Python searches for a matching `except` block after an exception is raised.

---

# Chapter Summary

In this chapter, you learned:

- Raising Exceptions
- `raise` Keyword
- Built-in Exceptions
- Custom Error Messages
- Exception Propagation
- Internal Working
- Advantages
- Best Practices
- Common Mistakes
- Interview Questions
- Quick Revision


# Program 1 – Raising ValueError

## Problem Statement

Write a Python program to raise a `ValueError` when the age is less than 18.

---

## Program

```python
age = int(input("Enter Age : "))

if age < 18:

    raise ValueError("Age must be at least 18.")

print("Eligible")
```

---

## Sample Output

```text
Enter Age : 15

ValueError: Age must be at least 18.
```

---

## Explanation

If the age is less than 18,

the program raises a `ValueError` manually.

---

# Program 2 – Handling Raised Exception

## Program

```python
try:

    age = int(input("Enter Age : "))

    if age < 18:

        raise ValueError("Age must be at least 18.")

    print("Eligible")

except ValueError as error:

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

The exception is raised using `raise`

and handled using the `except` block.

---

# Program 3 – Raising TypeError

## Program

```python
number = "100"

if not isinstance(number, int):

    raise TypeError("Only integer values are allowed.")
```

---

## Output

```text
TypeError: Only integer values are allowed.
```

---

## Explanation

The program validates the data type before processing.

---

# Program 4 – Raising RuntimeError

## Program

```python
server_status = False

if not server_status:

    raise RuntimeError("Server is currently unavailable.")
```

---

## Output

```text
RuntimeError: Server is currently unavailable.
```

---

## Explanation

`RuntimeError` is raised for unexpected runtime conditions.

---

# Program 5 – Banking Application Example

## Program

```python
balance = 5000

withdraw = int(input("Enter Amount : "))

if withdraw > balance:

    raise ValueError("Insufficient Balance.")

balance -= withdraw

print("Remaining Balance :", balance)
```

---

## Sample Output

```text
Enter Amount : 7000

ValueError: Insufficient Balance.
```

---

## Explanation

Business rules are enforced by raising an exception.

---

# Program 6 – Student Marks Validation

## Program

```python
marks = int(input("Enter Marks : "))

if marks < 0 or marks > 100:

    raise ValueError("Marks must be between 0 and 100.")

print("Valid Marks")
```

---

## Sample Output

```text
Enter Marks : 120

ValueError: Marks must be between 0 and 100.
```

---

## Explanation

Input validation ensures only valid marks are accepted.

---

# Program 7 – Salary Validation

## Program

```python
salary = int(input("Enter Salary : "))

if salary < 0:

    raise ValueError("Salary cannot be negative.")

print("Salary Accepted")
```

---

## Sample Output

```text
Enter Salary : -5000

ValueError: Salary cannot be negative.
```

---

# Program 8 – Password Length Validation

## Program

```python
password = input("Enter Password : ")

if len(password) < 8:

    raise ValueError("Password must contain at least 8 characters.")

print("Password Accepted")
```

---

## Sample Output

```text
Enter Password : admin

ValueError: Password must contain at least 8 characters.
```

---

## Explanation

The program validates password length before accepting it.

---

# Program 9 – Product Quantity Validation

## Program

```python
quantity = int(input("Enter Quantity : "))

if quantity <= 0:

    raise ValueError("Quantity must be greater than zero.")

print("Order Accepted")
```

---

## Sample Output

```text
Enter Quantity : 0

ValueError: Quantity must be greater than zero.
```

---

## Explanation

Invalid order quantities are rejected using an exception.

---

# Program 10 – Raising and Handling Custom Business Rule

## Program

```python
try:

    amount = int(input("Enter Amount : "))

    if amount > 100000:

        raise ValueError("Transaction limit exceeded.")

    print("Transaction Successful")

except ValueError as error:

    print(error)
```

---

## Sample Output

```text
Enter Amount : 150000

Transaction limit exceeded.
```

---

## Explanation

The business rule is enforced using `raise`

and handled gracefully using `try-except`.

---

# Dry Run

```text
Program Starts

↓

Input Accepted

↓

Condition Checked

↓

Condition Valid?

↓

Yes

↓

Continue Program

------------------------

No

↓

raise Statement

↓

Exception Object Created

↓

Matching except Block

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

Input Value

↓

Validation

↓

Valid?

↓

Yes

↓

Continue

------------------------

No

↓

raise

↓

Exception Object

↓

except Block

↓

Program Continues
```

---

# Advantages

- Detects invalid input early.
- Prevents incorrect program execution.
- Improves software reliability.
- Enforces business rules.
- Produces meaningful error messages.

---

# Best Practices

- Raise specific exceptions.
- Write meaningful error messages.
- Validate data before processing.
- Handle raised exceptions where appropriate.
- Avoid raising exceptions for normal program flow.

---

# Common Mistakes

## Mistake 1

Using generic exceptions unnecessarily.

❌ Incorrect

```python
raise Exception("Invalid Input")
```

✅ Better

```python
raise ValueError("Age must be at least 18.")
```

---

## Mistake 2

Raising exceptions without meaningful messages.

Always explain why the exception occurred.

---

## Mistake 3

Using exceptions instead of proper validation logic.

Validate inputs first and raise exceptions only when validation fails.

---

## Mistake 4

Ignoring raised exceptions.

If an exception is expected,

handle it appropriately using `try-except`.

---

# Interview Questions

## 1. What is the `raise` keyword?

### Answer

The `raise` keyword is used to generate an exception manually.

---

## 2. Why do we raise exceptions?

### Answer

To indicate invalid conditions and prevent incorrect program execution.

---

## 3. Can built-in exceptions be raised manually?

### Answer

Yes.

Exceptions such as `ValueError`, `TypeError`, and `RuntimeError` can be raised manually.

---

## 4. Can we provide a custom error message?

### Answer

Yes.

A custom message can be passed while raising the exception.

---

## 5. What happens after an exception is raised?

### Answer

Python searches for the nearest matching `except` block.

If none is found,

the program terminates with a traceback.

---

## 6. Should `raise` be used for normal program flow?

### Answer

No.

It should only be used for exceptional situations.

---

## 7. Which exception is commonly raised for invalid user input?

### Answer

`ValueError`.

---

# Practice Programs

1. Raise a `ValueError` for invalid age.
2. Raise a `TypeError` for invalid data types.
3. Validate student marks using `raise`.
4. Validate password length.
5. Create a banking withdrawal validation program.

---

# Quick Revision

- `raise` manually generates exceptions.
- Use specific exception classes.
- Write meaningful error messages.
- Validate data before processing.
- Handle exceptions using `try-except`.

---

# Chapter Summary

In this chapter, we learned:

- `raise` Keyword
- Raising Built-in Exceptions
- Custom Error Messages
- Business Rule Validation
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
