# Creating Custom Modules in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is a Custom Module?
5. Why Create Custom Modules?
6. Creating Your First Module
7. Importing Custom Modules
8. Module Search Path
9. Organizing Project Files
10. Internal Working
11. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Create your own Python modules.
- Import custom modules into other programs.
- Organize Python projects using modules.
- Understand how Python locates modules.
- Reuse code efficiently.

---

# Prerequisites

Before learning this chapter, you should know:

- Functions
- Classes
- Variables
- Introduction to Modules

---

# Introduction

As applications become larger,

keeping all the code inside one Python file makes the program difficult to read and maintain.

To solve this problem,

Python allows developers to divide applications into multiple reusable modules.

Each module is responsible for a specific task.

---

# What is a Custom Module?

## Definition

A **Custom Module** is a Python file (`.py`) created by the programmer to store reusable functions, classes, variables, and other program logic.

---

## Simple Definition

> A custom module is a Python file created by the developer for code reuse.

---

# Why Create Custom Modules?

Custom modules help developers:

- Reuse code.
- Improve readability.
- Reduce duplication.
- Organize projects.
- Simplify maintenance.
- Enable teamwork.

---

# Creating Your First Module

Example project structure:

```text
Project

│

├── calculator.py

└── main.py
```

The reusable code is written inside

```text
calculator.py
```

and imported into

```text
main.py
```

---

# Example Module

```python
# calculator.py

def add(a, b):

    return a + b
```

---

# Using the Module

```python
# main.py

import calculator

print(calculator.add(10, 20))
```

---

# Output

```text
30
```

---

# Importing Custom Modules

Once a module is created,

it can be imported using

```python
import module_name
```

Example

```python
import calculator
```

Python searches for

```text
calculator.py
```

and loads it into memory.

---

# Module Search Path

When Python imports a module,

it searches in the following locations:

1. Current project directory.
2. Directories listed in `PYTHONPATH`.
3. Standard library directories.
4. Installed third-party packages.

---

# Organizing Project Files

Example

```text
StudentManagement

│

├── student.py

├── marks.py

├── attendance.py

└── main.py
```

Each file performs one specific responsibility.

This makes projects easier to understand and maintain.

---

# Internal Working

```text
Program Starts

↓

import calculator

↓

Python Searches calculator.py

↓

Module Loaded

↓

Module Executed

↓

Functions Available

↓

Program Continues
```

---

# Advantages

- Improves code reuse.
- Reduces duplication.
- Organizes projects.
- Simplifies debugging.
- Makes maintenance easier.

---

# Best Practices

- Keep one responsibility per module.
- Use meaningful module names.
- Avoid unnecessary executable code.
- Group related functions together.
- Reuse existing modules whenever possible.

---

# Common Mistakes

## Mistake 1

Creating very large modules.

---

## Mistake 2

Giving modules meaningless names.

---

## Mistake 3

Copying code instead of importing modules.

---

## Mistake 4

Saving modules outside the project search path.

---

# Interview Questions

## 1. What is a custom module?

### Answer

A Python file created by the programmer to store reusable code.

---

## 2. Why are custom modules used?

### Answer

To improve code organization, reusability, readability, and maintainability.

---

## 3. Which extension does a Python module have?

### Answer

```text
.py
```

---

## 4. How is a custom module imported?

### Answer

```python
import module_name
```

---

## 5. Where does Python search for modules?

### Answer

- Current directory
- PYTHONPATH
- Standard library
- Installed packages

---

# Quick Revision

- Custom Module → Programmer-created Python file.
- `.py` extension.
- Imported using `import`.
- Supports code reuse.
- Improves project organization.

---

# Chapter Summary

In this chapter, you learned:

- Custom Modules
- Creating Modules
- Importing Modules
- Module Search Path
- Project Organization
- Advantages
- Best Practices
- Interview Questions
- Quick Revision


# Program 1 – Creating a Simple Custom Module

## Problem Statement

Create a custom module that contains a function to add two numbers.

---

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

print("Sum :", result)
```

---

## Output

```text
Sum : 30
```

---

## Explanation

The function `add()` is defined in `calculator.py`.

The `main.py` program imports the module and calls the function.

---

# Program 2 – Module with Multiple Functions

## File : calculator.py

```python
def add(a, b):

    return a + b

def subtract(a, b):

    return a - b

def multiply(a, b):

    return a * b
```

---

## File : main.py

```python
import calculator

print(calculator.add(20, 10))

print(calculator.subtract(20, 10))

print(calculator.multiply(20, 10))
```

---

## Output

```text
30

10

200
```

---

## Explanation

A single module can contain multiple related functions.

---

# Program 3 – Module with Variables

## File : company.py

```python
company_name = "OpenAI"

location = "San Francisco"
```

---

## File : main.py

```python
import company

print(company.company_name)

print(company.location)
```

---

## Output

```text
OpenAI

San Francisco
```

---

## Explanation

Modules can contain variables in addition to functions.

---

# Program 4 – Module with Constants

## File : constants.py

```python
PI = 3.14159

GRAVITY = 9.8
```

---

## File : main.py

```python
import constants

print(constants.PI)

print(constants.GRAVITY)
```

---

## Output

```text
3.14159

9.8
```

---

## Explanation

Modules are commonly used to store application-wide constants.

---

# Program 5 – Module with a Class

## File : student.py

```python
class Student:

    def display(self):

        print("Student Details")
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
Student Details
```

---

## Explanation

A module can contain classes and objects.

---

# Program 6 – Multiple Custom Modules

## File : addition.py

```python
def add(a, b):

    return a + b
```

---

## File : multiplication.py

```python
def multiply(a, b):

    return a * b
```

---

## File : main.py

```python
import addition

import multiplication

print(addition.add(5, 6))

print(multiplication.multiply(5, 6))
```

---

## Output

```text
11

30
```

---

## Explanation

A project can contain multiple modules,

each handling a specific responsibility.

---

# Program 7 – Reusing the Same Module

## File : calculator.py

```python
def square(number):

    return number * number
```

---

## File : program1.py

```python
import calculator

print(calculator.square(5))
```

---

## File : program2.py

```python
import calculator

print(calculator.square(10))
```

---

## Output

```text
25

100
```

---

## Explanation

The same module can be reused by multiple Python programs.

---

# Program 8 – Organizing Project Files

## Project Structure

```text
EmployeeManagement

│

├── employee.py

├── salary.py

├── department.py

└── main.py
```

---

## Explanation

Each module is responsible for one specific task.

This improves readability and maintenance.

---

# Program 9 – Importing Multiple Modules

## Program

```python
import calculator

import constants

print(calculator.add(15, 25))

print(constants.PI)
```

---

## Output

```text
40

3.14159
```

---

## Explanation

A single Python program can import multiple custom modules.

---

# Program 10 – Complete Custom Module Example

## File : employee.py

```python
class Employee:

    def __init__(self, name):

        self.name = name

    def display(self):

        print("Employee :", self.name)
```

---

## File : main.py

```python
import employee

emp = employee.Employee("Rahul")

emp.display()
```

---

## Output

```text
Employee : Rahul
```

---

## Explanation

This example demonstrates a complete custom module containing a class that is imported and used by another program.

---

# Dry Run

```text
Program Starts

↓

Import Module

↓

Python Searches Module

↓

Module Loaded

↓

Functions / Variables / Classes Available

↓

Required Method Called

↓

Result Displayed

↓

Program Ends
```

---

# Memory Representation

```text
Project

│

├── main.py

│

└── calculator.py

      │

      ├── Variables

      ├── Functions

      └── Classes

↓

Program Ends
```

---

# Advantages

- Promotes code reuse.
- Improves project organization.
- Reduces duplicate code.
- Simplifies debugging.
- Makes maintenance easier.

---

# Best Practices

- Keep one responsibility per module.
- Use meaningful module names.
- Group related functions together.
- Avoid unnecessary executable statements in modules.
- Reuse modules instead of copying code.

---

# Common Mistakes

## Mistake 1

Creating very large modules containing unrelated functionality.

---

## Mistake 2

Saving modules outside the project directory.

---

## Mistake 3

Using unclear or confusing module names.

---

## Mistake 4

Duplicating code instead of importing reusable modules.

---

# Interview Questions

## 1. What is a custom module?

### Answer

A custom module is a Python file created by the programmer to store reusable code.

---

## 2. Can a module contain classes?

### Answer

Yes.

A module can contain functions, classes, variables, and executable statements.

---

## 3. Can multiple programs use the same module?

### Answer

Yes.

Modules are designed for code reuse.

---

## 4. Why should modules have a single responsibility?

### Answer

It improves readability, maintenance, and reusability.

---

## 5. Where should custom modules be stored?

### Answer

Inside the project directory or another location included in Python's module search path.

---

## 6. Can a program import multiple modules?

### Answer

Yes.

A Python program can import multiple built-in and user-defined modules.

---

## 7. What are the advantages of custom modules?

### Answer

- Code reuse
- Better organization
- Easier maintenance
- Reduced duplication
- Improved readability

---

# Practice Programs

1. Create a calculator module.
2. Create a module containing constants.
3. Create a module containing a class.
4. Import multiple custom modules into one program.
5. Reuse the same module in multiple Python programs.

---

# Quick Revision

- Custom Module → Programmer-created `.py` file.
- Can contain functions, variables, classes, and executable statements.
- Imported using `import`.
- Supports code reuse.
- Improves project organization.

---

# Chapter Summary

In this chapter, you learned:

- Creating Custom Modules
- Importing Custom Modules
- Modules with Functions
- Modules with Variables
- Modules with Classes
- Multiple Module Projects
- Module Reusability
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
