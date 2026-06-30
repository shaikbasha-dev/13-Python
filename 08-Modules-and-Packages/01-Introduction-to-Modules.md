# Introduction to Modules in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is a Module?
5. Why are Modules Required?
6. Advantages of Modules
7. Types of Modules
8. Built-in Modules
9. User-Defined Modules
10. Module Execution
11. Internal Working
12. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what a module is.
- Learn why modules are used.
- Differentiate built-in and user-defined modules.
- Understand how modules improve code organization.
- Learn how Python executes modules.

---

# Prerequisites

Before learning this chapter, you should know:

- Functions
- Classes
- File Handling Basics
- Python Program Structure

---

# Introduction

As Python programs grow larger,

writing all the code in a single file becomes difficult to manage.

To improve readability, maintainability, and code reuse,

Python allows programs to be divided into smaller files called **modules**.

A module groups related functions, classes, and variables into a single file, making programs easier to organize and maintain.

---

# What is a Module?

## Definition

A **module** is a Python file (`.py`) that contains reusable code such as functions, classes, variables, and executable statements.

---

## Simple Definition

> A module is a Python file that contains reusable code.

---

# Why are Modules Required?

Without modules:

- Programs become large and difficult to maintain.
- Code duplication increases.
- Reusability decreases.
- Collaboration becomes harder.

Using modules:

- Code is organized.
- Reusability improves.
- Maintenance becomes easier.
- Team development becomes simpler.

---

# Real-World Example

Consider an online shopping application.

Instead of writing everything in one file, the application can be divided into modules:

- `login.py`
- `payment.py`
- `orders.py`
- `products.py`
- `notifications.py`

Each module handles a specific responsibility.

---

# Advantages of Modules

- Improves code organization.
- Encourages code reuse.
- Simplifies maintenance.
- Supports team development.
- Makes debugging easier.
- Reduces code duplication.

---

# Types of Modules

Python supports two main types of modules:

## 1. Built-in Modules

Modules provided by Python.

Examples:

- `math`
- `random`
- `datetime`
- `os`
- `sys`

---

## 2. User-Defined Modules

Modules created by the programmer.

Example:

```text
calculator.py
```

---

# Built-in Modules

Python provides many ready-to-use modules.

Examples include:

| Module | Purpose |
|---------|---------|
| `math` | Mathematical operations |
| `random` | Random number generation |
| `datetime` | Date and time handling |
| `os` | Operating system interaction |
| `sys` | Access to Python runtime information |

---

# User-Defined Modules

A user-defined module is simply a `.py` file created by the programmer.

It can contain:

- Variables
- Functions
- Classes
- Executable statements

These modules can be imported and reused in other Python programs.

---

# Module Execution

When a module is imported:

1. Python locates the module.
2. The module is loaded into memory.
3. The module code is executed once.
4. The module object becomes available for use.

---

# Internal Working

```text
Python Program

↓

import Module

↓

Python Searches Module

↓

Module Loaded

↓

Module Executed

↓

Functions and Classes Available

↓

Program Continues
```

---

# Advantages

- Code Reusability
- Better Organization
- Easier Maintenance
- Improved Readability
- Modular Design

---

# Best Practices

- Give modules meaningful names.
- Keep each module focused on a single responsibility.
- Avoid writing unnecessary executable code at the module level.
- Group related functions and classes together.
- Reuse existing modules instead of duplicating code.

---

# Common Mistakes

## Mistake 1

Creating very large modules containing unrelated functionality.

---

## Mistake 2

Using unclear module names.

---

## Mistake 3

Duplicating code instead of importing reusable modules.

---

# Interview Questions

## 1. What is a module?

### Answer

A module is a Python file containing reusable code such as functions, classes, variables, and executable statements.

---

## 2. Why are modules used?

### Answer

Modules improve code organization, reusability, readability, and maintainability.

---

## 3. What are the two types of modules?

### Answer

- Built-in modules
- User-defined modules

---

## 4. Give examples of built-in modules.

### Answer

- `math`
- `random`
- `datetime`
- `os`
- `sys`

---

## 5. What is a user-defined module?

### Answer

A Python module created by the programmer for reusable application-specific functionality.

---

# Quick Revision

- Module → Reusable Python file.
- Built-in Module → Provided by Python.
- User-Defined Module → Created by the programmer.
- Modules improve organization and code reuse.

---

# Chapter Summary

In this chapter, we learned:

- Modules
- Types of Modules
- Built-in Modules
- User-Defined Modules
- Module Execution
- Advantages
- Best Practices
- Interview Questions
- Quick Revision


# Program 1 – Importing a Built-in Module

## Problem Statement

Write a Python program to import the `math` module and calculate the square root of a number.

---

## Program

```python
import math

number = 64

result = math.sqrt(number)

print("Square Root :", result)
```

---

## Output

```text
Square Root : 8.0
```

---

## Explanation

The built-in `math` module provides mathematical functions.

The `sqrt()` function calculates the square root of a number.

---

# Program 2 – Using the random Module

## Program

```python
import random

number = random.randint(1, 100)

print("Random Number :", number)
```

---

## Sample Output

```text
Random Number : 57
```

---

## Explanation

The `random` module generates random values.

`randint()` returns a random integer within the specified range.

---

# Program 3 – Using the datetime Module

## Program

```python
import datetime

today = datetime.datetime.now()

print(today)
```

---

## Sample Output

```text
2026-07-01 10:30:15.245678
```

---

## Explanation

The `datetime` module is used to work with dates and times.

`now()` returns the current date and time.

---

# Program 4 – Using the os Module

## Program

```python
import os

print(os.getcwd())
```

---

## Sample Output

```text
C:\PythonProjects
```

---

## Explanation

The `os` module provides operating system related functionality.

`getcwd()` returns the current working directory.

---

# Program 5 – Creating a User-Defined Module

## File : calculator.py

```python
def add(a, b):

    return a + b
```

---

## File : main.py

```python
import calculator

result = calculator.add(10, 20)

print(result)
```

---

## Output

```text
30
```

---

## Explanation

The `calculator.py` file acts as a user-defined module.

It can be imported and reused in other programs.

---

# Program 6 – Module with Multiple Functions

## File : calculator.py

```python
def add(a, b):

    return a + b

def sub(a, b):

    return a - b
```

---

## File : main.py

```python
import calculator

print(calculator.add(15, 5))

print(calculator.sub(15, 5))
```

---

## Output

```text
20

10
```

---

## Explanation

A module can contain multiple related functions.

---

# Program 7 – Module with Variables

## File : company.py

```python
company_name = "OpenAI"
```

---

## File : main.py

```python
import company

print(company.company_name)
```

---

## Output

```text
OpenAI
```

---

## Explanation

Modules can also store reusable variables.

---

# Program 8 – Module with a Class

## File : student.py

```python
class Student:

    def display(self):

        print("Student Class")
```

---

## File : main.py

```python
import student

obj = student.Student()

obj.display()
```

---

## Output

```text
Student Class
```

---

## Explanation

Modules can contain classes in addition to functions and variables.

---

# Program 9 – Multiple Module Imports

## Program

```python
import math
import random

print(math.factorial(5))

print(random.randint(1, 10))
```

---

## Sample Output

```text
120

7
```

---

## Explanation

A single program can import multiple modules.

Each module provides different functionality.

---

# Program 10 – Reusing a Module

## File : calculator.py

```python
def multiply(a, b):

    return a * b
```

---

## File : program1.py

```python
import calculator

print(calculator.multiply(5, 6))
```

---

## File : program2.py

```python
import calculator

print(calculator.multiply(10, 20))
```

---

## Output

```text
30

200
```

---

## Explanation

One module can be reused across multiple Python programs.

This is one of the biggest advantages of modular programming.

---

# Dry Run

```text
Program Starts

↓

import Module

↓

Python Searches Module

↓

Module Loaded

↓

Module Executed

↓

Required Function Called

↓

Result Returned

↓

Program Ends
```

---

# Memory Representation

```text
Program

│

├── Main Module

│

└── Imported Module

      │

      ├── Variables

      ├── Functions

      └── Classes

↓

Program Ends
```

---

# Advantages

- Improves code reusability.
- Simplifies maintenance.
- Organizes related code.
- Reduces duplication.
- Makes large applications easier to manage.

---

# Best Practices

- Keep modules focused on a single responsibility.
- Use meaningful module names.
- Group related functions and classes together.
- Import only the modules you need.
- Reuse existing modules whenever possible.

---

# Common Mistakes

## Mistake 1

Creating modules with unrelated functionality.

---

## Mistake 2

Giving modules confusing names.

---

## Mistake 3

Duplicating code instead of importing reusable modules.

---

## Mistake 4

Forgetting to keep user-defined modules in the correct project directory.

---

# Interview Questions

## 1. What is a module?

### Answer

A module is a Python file containing reusable functions, classes, variables, and executable statements.

---

## 2. What are the two types of modules?

### Answer

- Built-in modules
- User-defined modules

---

## 3. Why are modules important?

### Answer

Modules improve code organization, reusability, readability, and maintainability.

---

## 4. Can a module contain classes and variables?

### Answer

Yes.

A module can contain functions, classes, variables, and executable code.

---

## 5. Can one module be reused in multiple programs?

### Answer

Yes.

One module can be imported and reused by multiple Python programs.

---

## 6. Name some commonly used built-in modules.

### Answer

- `math`
- `random`
- `datetime`
- `os`
- `sys`

---

## 7. What happens when a module is imported?

### Answer

Python locates the module, loads it into memory, executes it once, and makes its contents available to the importing program.

---

# Practice Programs

1. Import the `math` module and calculate a square root.
2. Generate random numbers using the `random` module.
3. Create a user-defined module with arithmetic functions.
4. Create a module containing a class.
5. Import multiple modules into the same program.

---

# Quick Revision

- Module → Reusable Python file.
- Built-in Module → Provided by Python.
- User-Defined Module → Created by the programmer.
- A module can contain functions, classes, variables, and executable statements.
- Modules improve code organization and reusability.

---

# Chapter Summary

In this chapter, we learned:

- Introduction to Modules
- Built-in Modules
- User-Defined Modules
- Creating Modules
- Importing Modules
- Module Reusability
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
