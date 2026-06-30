# Encapsulation in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is Encapsulation?
5. Why is Encapsulation Required?
6. Real-World Example
7. Data and Methods
8. Data Hiding
9. Encapsulation vs Data Hiding
10. Achieving Encapsulation in Python
11. Getters and Setters
12. Python Properties
13. Internal Working
14. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand Encapsulation.
- Explain the need for Encapsulation.
- Differentiate Encapsulation and Data Hiding.
- Create encapsulated classes.
- Use Getters and Setters.
- Use Python Properties.
- Apply Encapsulation in real-world applications.

---

# Prerequisites

Before learning this chapter, you should know:

- Classes
- Objects
- Instance Variables
- Methods
- self Keyword

---

# Introduction

Object-Oriented Programming is built on four fundamental pillars.

They are:

- Encapsulation
- Abstraction
- Inheritance
- Polymorphism

The first pillar is **Encapsulation**.

Encapsulation helps us organize data and methods into a single unit while controlling how the data is accessed and modified.

It improves security, maintainability, and code organization.

---

# What is Encapsulation?

## Definition

**Encapsulation** is the process of combining **data (variables)** and **methods (functions)** into a single unit called a **class**.

The methods provide a controlled way to access and modify the data.

---

# Simple Definition

> Wrapping data and methods together inside a class is called **Encapsulation**.

---

# Why is Encapsulation Required?

Suppose we are developing a Banking Application.

Every customer has:

- Account Number
- Account Holder Name
- Balance
- ATM PIN

Should every user be able to modify the balance directly?

**No.**

Instead,

the balance should only be modified using methods such as:

- Deposit()
- Withdraw()

This prevents accidental or unauthorized modifications.

Encapsulation provides this controlled access.

---

# Real-World Example

Consider an ATM Machine.

You can:

- Deposit Money
- Withdraw Money
- Check Balance

But you cannot directly access or change the bank's internal database.

The ATM provides controlled access through specific operations.

Similarly,

a class provides controlled access to its data using methods.

---

# Components of Encapsulation

Encapsulation consists of two components.

## 1. Data (Attributes)

Stores the state of an object.

Example

```text
Name

Age

Salary

Balance
```

---

## 2. Methods (Functions)

Perform operations on the data.

Example

```text
Deposit()

Withdraw()

Display()

Update()
```

---

# Encapsulation Diagram

```text
+--------------------------------+

        Student Class

----------------------------------

Data

• Name

• Age

• Marks

----------------------------------

Methods

• display()

• updateMarks()

----------------------------------

+--------------------------------+
```

---

# Data Hiding

Data Hiding means restricting direct access to sensitive data.

Instead of accessing variables directly,

users interact with the object through methods.

Example

```text
Balance

↓

Deposit()

Withdraw()
```

---

# Is Encapsulation the Same as Data Hiding?

**No.**

Many beginners think both terms are the same, but they are different.

### Encapsulation

- Wraps data and methods into one unit.
- Focuses on organization and controlled access.

### Data Hiding

- Restricts direct access to data.
- Focuses on protecting sensitive information.

Data Hiding is **one benefit of Encapsulation**, but they are not identical concepts.

---

# Encapsulation vs Data Hiding

| Encapsulation | Data Hiding |
|---------------|-------------|
| Combines data and methods into a class | Restricts direct access to data |
| Focuses on code organization | Focuses on security |
| Achieved using classes | Achieved using access control and naming conventions |
| Improves maintainability | Protects sensitive information |

---

# Achieving Encapsulation in Python

Encapsulation is achieved by:

- Creating a class.
- Defining instance variables.
- Providing methods to access or modify the data.
- Using public, protected, or private members where appropriate.

---

# Getters and Setters

Instead of accessing variables directly,

we use methods.

### Getter

A Getter method returns the value of a variable.

Example

```python
def get_name(self):
    return self.__name
```

---

### Setter

A Setter method updates the value of a variable.

Example

```python
def set_name(self, name):
    self.__name = name
```

---

# Python Properties

Python provides the `@property` decorator to create getter methods in a more Pythonic way.

Example

```python
@property
def name(self):
    return self.__name
```

A setter can also be created using:

```python
@name.setter
```

Properties allow controlled access while keeping the syntax simple for users of the class.

---

# Internal Working

```text
User

↓

Calls Method

↓

Method Validates Data

↓

Updates Variable

↓

Returns Result
```

Instead of modifying variables directly,

methods control the entire process.

---

# Advantages of Encapsulation

- Improves security.
- Protects sensitive data.
- Makes code reusable.
- Improves maintainability.
- Supports modular programming.
- Reduces coupling between components.

---

# Disadvantages of Encapsulation

- Slightly increases code size.
- Requires additional methods for data access.
- May add complexity for very small programs.

---

# Real-Time Applications

Encapsulation is used in:

- Banking Systems
- Hospital Management Systems
- ATM Software
- Student Management Systems
- Employee Payroll Systems
- E-Commerce Applications
- Inventory Management Systems

---

# Summary

In this part, we learned:

- Encapsulation
- Need for Encapsulation
- Data Hiding
- Components of Encapsulation
- Getters
- Setters
- Python Properties
- Internal Working
- Advantages
- Real-Time Applications


# Program 1 – Basic Encapsulation

## Problem Statement

Write a Python program to demonstrate Encapsulation.

---

## Program

```python
class Student:

    def __init__(self):
        self.name = "Rahul"
        self.age = 21

    def display(self):
        print("Name :", self.name)
        print("Age  :", self.age)

student = Student()

student.display()
```

---

## Output

```text
Name : Rahul
Age  : 21
```

---

## Explanation

In this program,

- The data (`name` and `age`) and
- The method (`display()`)

are combined inside a single class.

This is Encapsulation.

---

# Program 2 – Encapsulation using Private Variables

## Problem Statement

Write a Python program to demonstrate Encapsulation using private variables.

---

## Program

```python
class BankAccount:

    def __init__(self):

        self.__balance = 10000

    def display_balance(self):

        print("Balance :", self.__balance)

account = BankAccount()

account.display_balance()
```

---

## Output

```text
Balance : 10000
```

---

## Explanation

The variable

```python
__balance
```

is private.

It cannot be accessed directly from outside the class.

The balance is accessed through the method

```python
display_balance()
```

This provides controlled access to the data.

---

# Program 3 – Using Getter Method

## Problem Statement

Write a Python program to retrieve a private variable using a Getter method.

---

## Program

```python
class Student:

    def __init__(self):

        self.__name = "Rahul"

    def get_name(self):

        return self.__name

student = Student()

print(student.get_name())
```

---

## Output

```text
Rahul
```

---

## Explanation

The Getter method returns the value of the private variable without allowing direct access.

---

# Program 4 – Using Setter Method

## Problem Statement

Write a Python program to update a private variable using a Setter method.

---

## Program

```python
class Student:

    def __init__(self):

        self.__name = ""

    def set_name(self, name):

        self.__name = name

    def get_name(self):

        return self.__name

student = Student()

student.set_name("Priya")

print(student.get_name())
```

---

## Output

```text
Priya
```

---

## Explanation

Instead of modifying the variable directly,

the Setter method updates the value.

This allows validation before assigning new values.

---

# Program 5 – Getter and Setter with Validation

## Problem Statement

Write a Python program to validate student age before storing it.

---

## Program

```python
class Student:

    def __init__(self):

        self.__age = 0

    def set_age(self, age):

        if age >= 18:
            self.__age = age
        else:
            print("Invalid Age")

    def get_age(self):

        return self.__age

student = Student()

student.set_age(21)

print(student.get_age())
```

---

## Output

```text
21
```

---

## Explanation

Before storing the value,

the Setter validates the input.

Invalid values are rejected.

This is one of the biggest advantages of Encapsulation.

---

# Program 6 – Using Python Property

## Problem Statement

Write a Python program using the `@property` decorator.

---

## Program

```python
class Student:

    def __init__(self):

        self.__name = "Rahul"

    @property
    def name(self):

        return self.__name

student = Student()

print(student.name)
```

---

## Output

```text
Rahul
```

---

## Explanation

The `@property` decorator allows us to access a method like an attribute.

Instead of writing

```python
student.get_name()
```

we simply write

```python
student.name
```

This is the recommended Pythonic approach.

---

# Program 7 – Property with Setter

## Program

```python
class Student:

    def __init__(self):

        self.__marks = 0

    @property
    def marks(self):

        return self.__marks

    @marks.setter
    def marks(self, value):

        if value >= 0:
            self.__marks = value

student = Student()

student.marks = 95

print(student.marks)
```

---

## Output

```text
95
```

---

## Explanation

The setter validates the data before storing it.

The user interacts with the object as if `marks` were a normal attribute, while the validation logic remains hidden.

---

# Internal Working

```text
User

↓

Setter Method

↓

Validation

↓

Private Variable Updated

↓

Getter Method

↓

Value Returned
```

---

# Memory Representation

```text
Student Object

        │

        ▼

+------------------------------+

__name

↓

Rahul

------------------------------

get_name()

set_name()

display()

+------------------------------+
```

---

# Advantages

- Protects sensitive data.
- Prevents unauthorized modification.
- Improves maintainability.
- Supports validation.
- Promotes code reuse.
- Makes programs modular.

---

# Best Practices

- Use private variables for sensitive data.
- Validate input inside Setter methods.
- Prefer `@property` for cleaner code.
- Avoid exposing private data directly.
- Keep Getter and Setter methods simple.

---

# Common Mistakes

## Mistake 1

Accessing private variables directly.

❌ Incorrect

```python
student.__name
```

Produces

```text
AttributeError
```

---

## Mistake 2

Not validating data.

```python
self.__age = age
```

Always validate user input before storing it.

---

## Mistake 3

Making every variable private unnecessarily.

Not every variable needs to be private.

Use private members only for sensitive or controlled data.

---

# Real-Time Applications

Encapsulation is widely used in:

- Banking Systems
- ATM Applications
- Hospital Management Systems
- Payroll Systems
- Student Management Systems
- E-Commerce Applications
- Library Management Systems

---

# Interview Questions

## 1. What is Encapsulation?

### Answer

Encapsulation is the process of combining data and methods into a single unit called a class.

---

## 2. Why is Encapsulation used?

### Answer

Encapsulation protects data, improves security, and provides controlled access through methods.

---

## 3. What is Data Hiding?

### Answer

Data Hiding is the process of restricting direct access to sensitive data.

It is one of the benefits of Encapsulation.

---

## 4. What is the difference between Encapsulation and Data Hiding?

### Answer

Encapsulation combines data and methods into a class.

Data Hiding restricts direct access to data.

---

## 5. What is a Getter Method?

### Answer

A Getter method returns the value of a private variable.

---

## 6. What is a Setter Method?

### Answer

A Setter method updates the value of a private variable, often after validating the input.

---

## 7. What is the advantage of using `@property`?

### Answer

It provides controlled access to data while allowing attributes to be accessed using simple dot notation.

---

# Practice Programs

1. Create an Employee class with private salary and Getter/Setter methods.
2. Create a BankAccount class that validates withdrawals.
3. Create a Product class using `@property`.
4. Create a Student class that validates marks.
5. Create a Customer class with private mobile number and update it using a Setter.

---

# Quick Revision

- Encapsulation combines data and methods into one unit.
- Data Hiding protects sensitive data.
- Private variables use `__`.
- Getter methods retrieve values.
- Setter methods update values.
- `@property` is the Pythonic way to implement controlled access.
- Validation should be performed inside Setter methods.

---

# Chapter Summary

In this chapter, you learned:

- Encapsulation
- Data Hiding
- Encapsulation vs Data Hiding
- Getters
- Setters
- Python Properties
- Internal Working
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
