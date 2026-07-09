# Packages in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is a Package?
5. Why are Packages Required?
6. Package Structure
7. Creating a Package
8. __init__.py File
9. Importing Packages
10. Sub-Packages
11. Package vs Module
12. Internal Working
13. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand packages in Python.
- Differentiate modules and packages.
- Create your own packages.
- Understand the purpose of the `__init__.py` file.
- Import modules from packages.
- Organize large Python projects using packages.
- Work with sub-packages.

---

# Prerequisites

Before learning this chapter, you should know:

- Modules
- Custom Modules
- Import Statements
- Aliasing

---

# Introduction

As applications become larger,

creating hundreds of modules in a single folder becomes difficult to manage.

Python solves this problem using **Packages**.

Packages allow developers to organize related modules inside folders, making projects easier to understand, maintain, and reuse.

---

# What is a Package?

## Definition

A **Package** is a directory (folder) that contains one or more Python modules and is used to organize related code.

Traditionally, packages include an `__init__.py` file to indicate that the directory is a package.

---

## Simple Definition

> A package is a folder that contains related Python modules.

---

# Why are Packages Required?

Without packages,

large projects become difficult to organize.

Example:

```text
Project

calculator.py
employee.py
student.py
salary.py
database.py
payment.py
inventory.py
products.py
orders.py
reports.py
notifications.py
```

Finding a specific module becomes difficult.

Using packages,

the same project becomes

```text
Project

├── employee
│     ├── employee.py
│     ├── salary.py
│     └── attendance.py
│
├── sales
│     ├── orders.py
│     ├── products.py
│     └── reports.py
│
└── database
      └── connection.py
```

This structure is easier to understand and maintain.

---

# Advantages of Packages

- Organize large projects.
- Reduce module name conflicts.
- Improve readability.
- Improve maintainability.
- Encourage modular programming.
- Support code reuse.

---

# Package Structure

Example

```text
Project

│

├── calculator

│     ├── __init__.py

│     ├── addition.py

│     ├── subtraction.py

│     └── multiplication.py

│

└── main.py
```

---

# Creating a Package

Step 1

Create a folder

```text
calculator
```

Step 2

Create

```text
__init__.py
```

Step 3

Add modules

```text
addition.py

subtraction.py

multiplication.py
```

The folder now behaves as a package.

---

# What is __init__.py?

## Definition

`__init__.py` is a special Python file placed inside a package.

Traditionally, it marks the directory as a Python package.

It can also contain initialization code that runs when the package is imported.

---

## Simple Definition

> `__init__.py` is the initialization file of a package.

---

# Importing Modules from Packages

Suppose

```text
calculator

│

├── __init__.py

└── addition.py
```

contains

```python
def add(a, b):

    return a + b
```

Import statement

```python
from calculator import addition

print(addition.add(10, 20))
```

---

# Importing Specific Members

```python
from calculator.addition import add

print(add(15, 25))
```

---

# Sub-Packages

A package can contain another package.

Example

```text
Company

│

├── HR

│      ├── employee.py

│      └── payroll.py

│

└── Sales

       ├── products.py

       └── orders.py
```

These are called **sub-packages**.

---

# Package vs Module

| Module | Package |
|---------|----------|
| Single `.py` file | Folder containing modules |
| Stores reusable code | Organizes multiple modules |
| Smaller unit | Larger organizational unit |
| Example: `math.py` | Example: `calculator/` |

---

# Internal Working

```text
Program Starts

↓

Import Package

↓

Python Searches Package

↓

__init__.py Executed

↓

Required Module Loaded

↓

Functions Available

↓

Program Continues
```

---

# Advantages

- Better project organization.
- Supports modular programming.
- Easier maintenance.
- Reduces naming conflicts.
- Encourages code reuse.

---

# Best Practices

- Group related modules into packages.
- Use meaningful package names.
- Keep package hierarchy simple.
- Avoid circular imports.
- Organize packages based on functionality.

---

# Common Mistakes

## Mistake 1

Putting unrelated modules inside the same package.

---

## Mistake 2

Creating very deep package hierarchies.

---

## Mistake 3

Using confusing package names.

---

## Mistake 4

Creating duplicate modules in multiple packages.

---

# Program 1 – Creating a Package

## Project Structure

```text
Project

├── calculator

│     ├── __init__.py

│     └── addition.py

└── main.py
```

---

## File : addition.py

```python
def add(a, b):

    return a + b
```

---

## File : main.py

```python
from calculator import addition

print(addition.add(10, 20))
```

---

## Output

```text
30
```

---

# Program 2 – Importing a Function from a Package

```python
from calculator.addition import add

print(add(50, 40))
```

---

## Output

```text
90
```

---

# Program 3 – Package with Multiple Modules

```text
calculator

├── addition.py

├── subtraction.py

└── multiplication.py
```

```python
from calculator import addition

from calculator import subtraction

print(addition.add(5, 5))

print(subtraction.subtract(10, 3))
```

---

## Output

```text
10

7
```

---

# Program 4 – Package Containing Classes

## File : student.py

```python
class Student:

    def display(self):

        print("Student Package")
```

---

## File : main.py

```python
from school.student import Student

obj = Student()

obj.display()
```

---

## Output

```text
Student Package
```

---

# Program 5 – Sub-Package Example

```text
Company

├── HR

│      └── employee.py

└── Sales

       └── orders.py
```

```python
from Company.HR import employee
```

---

# Program 6 – Import Entire Package Module

```python
import calculator.addition

print(calculator.addition.add(7, 8))
```

---

## Output

```text
15
```

---

# Program 7 – Multiple Package Imports

```python
from calculator import addition

from calculator import multiplication

print(addition.add(2, 3))

print(multiplication.multiply(4, 5))
```

---

## Output

```text
5

20
```

---

# Program 8 – Package Alias

```python
import calculator.addition as add_module

print(add_module.add(100, 200))
```

---

## Output

```text
300
```

---

# Program 9 – Using __init__.py

## File : __init__.py

```python
print("Calculator Package Loaded")
```

---

## File : main.py

```python
import calculator
```

---

## Output

```text
Calculator Package Loaded
```

---

# Program 10 – Complete Package Example

```text
Project

calculator

│

├── __init__.py

├── addition.py

├── subtraction.py

└── multiplication.py

main.py
```

```python
from calculator.addition import add

print(add(25, 75))
```

---

## Output

```text
100
```

---

# Dry Run

```text
Program Starts

↓

Import Package

↓

Python Finds Package Folder

↓

Execute __init__.py

↓

Load Required Module

↓

Execute Function

↓

Display Output

↓

Program Ends
```

---

# Memory Representation

```text
Project

│

├── Package

│      │

│      ├── __init__.py

│      ├── Module 1

│      ├── Module 2

│      └── Module 3

│

└── Main Program
```

---

# Interview Questions

## 1. What is a package?

### Answer

A package is a directory containing related Python modules.

---

## 2. What is the purpose of `__init__.py`?

### Answer

It initializes a package and traditionally identifies the directory as a Python package.

---

## 3. What is the difference between a module and a package?

### Answer

A module is a single `.py` file, whereas a package is a directory containing one or more modules.

---

## 4. Can a package contain another package?

### Answer

Yes.

Such packages are called sub-packages.

---

## 5. Why are packages used?

### Answer

Packages improve project organization, readability, maintainability, and code reuse.

---

## 6. Can packages contain classes and functions?

### Answer

Yes.

Packages contain modules, and modules can contain classes, functions, variables, and executable statements.

---

## 7. Is `__init__.py` always empty?

### Answer

No.

It can contain initialization code, variables, or package-level imports if required.

---

# Practice Programs

1. Create a calculator package.
2. Create a student package.
3. Create a package with multiple modules.
4. Create a sub-package.
5. Import modules using different techniques.

---

# Quick Revision

- Package → Folder containing modules.
- Module → Python file.
- `__init__.py` → Package initialization file.
- Packages organize large projects.
- Packages can contain sub-packages.
- Import using package.module syntax.

---

# Chapter Summary

In this chapter, we learned:

- Packages
- Package Structure
- Creating Packages
- `__init__.py`
- Importing Packages
- Sub-Packages
- Module vs Package
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision


