# Import Statement in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is an Import Statement?
5. Why is the Import Statement Required?
6. Different Ways to Import Modules
7. Importing Multiple Modules
8. Module Search Process
9. Internal Working
10. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the purpose of the import statement.
- Import built-in modules.
- Import user-defined modules.
- Import specific members from a module.
- Import multiple modules.
- Understand Python's module search process.
- Follow best practices for importing modules.

---

# Prerequisites

Before learning this chapter, you should know:

- Modules
- Custom Modules
- Functions
- Classes

---

# Introduction

Python provides thousands of reusable functions and classes through modules.

To use the contents of a module,

the module must first be imported into the current program.

The **import statement** tells Python to load a module so that its functions, classes, and variables can be used.

---

# What is an Import Statement?

## Definition

An **import statement** is used to load a module into the current Python program.

After importing,

the module's contents become available for use.

---

## Simple Definition

> The import statement allows one Python program to use code written in another module.

---

# Why is the Import Statement Required?

Without importing a module,

its functions, classes, and variables cannot be accessed.

Importing modules allows:

- Code reuse
- Better organization
- Reduced duplication
- Easier maintenance
- Faster development

---

# Different Ways to Import Modules

Python provides several ways to import modules.

---

# 1. Import Entire Module

Syntax

```python
import math
```

Usage

```python
import math

print(math.sqrt(25))
```

Every member is accessed using the module name.

---

# 2. Import Specific Members

Syntax

```python
from math import sqrt
```

Usage

```python
from math import sqrt

print(sqrt(25))
```

Only the required member is imported.

---

# 3. Import Multiple Members

Syntax

```python
from math import sqrt, factorial
```

Example

```python
from math import sqrt, factorial

print(sqrt(36))

print(factorial(5))
```

---

# 4. Import Everything (Wildcard Import)

Syntax

```python
from math import *
```

Example

```python
from math import *

print(sqrt(49))
```

> **Note:** Wildcard imports are generally discouraged because they can make code harder to read and may cause name conflicts.

---

# 5. Import Multiple Modules

Syntax

```python
import math

import random
```

or

```python
import math, random
```

---

# User-Defined Module Import

Example

```python
import calculator
```

Python searches for

```text
calculator.py
```

and imports it.

---

# Module Search Process

When Python encounters an import statement,

it searches in the following order:

1. Current project directory
2. Directories listed in `PYTHONPATH`
3. Python standard library
4. Installed third-party packages

If the module is not found,

Python raises

```python
ModuleNotFoundError
```

---

# Internal Working

```text
Program Starts

↓

Import Statement

↓

Python Searches Module

↓

Module Found?

↓

Yes

↓

Load Module

↓

Execute Module Once

↓

Module Object Created

↓

Program Continues

-------------------------

No

↓

ModuleNotFoundError
```

---

# Advantages

- Encourages code reuse.
- Improves readability.
- Makes applications modular.
- Simplifies maintenance.
- Reduces duplicate code.

---

# Best Practices

- Import only what is needed.
- Place import statements at the top of the file.
- Prefer explicit imports over wildcard imports.
- Use meaningful module names.
- Organize imports logically.

---

# Common Mistakes

## Mistake 1

Using a module without importing it.

---

## Mistake 2

Using wildcard imports unnecessarily.

---

## Mistake 3

Misspelling module names.

---

## Mistake 4

Creating custom modules with names that conflict with built-in modules.

Example

```text
random.py
math.py
```

Avoid such names.

---

# Interview Questions

## 1. What is the purpose of the import statement?

### Answer

The import statement loads a module so that its functions, classes, variables, and other members can be used in the current program.

---

## 2. What are the different ways to import a module?

### Answer

- `import module`
- `from module import member`
- `from module import member1, member2`
- `from module import *`

---

## 3. Which import style is generally recommended?

### Answer

Using explicit imports such as

```python
import math
```

or

```python
from math import sqrt
```

because they improve readability and avoid namespace conflicts.

---

## 4. What happens if Python cannot find a module?

### Answer

Python raises

```python
ModuleNotFoundError
```

---

## 5. Why should wildcard imports usually be avoided?

### Answer

Because they can introduce namespace conflicts and make code more difficult to understand and maintain.

---

# Quick Revision

- `import module`
- `from module import member`
- `from module import member1, member2`
- `from module import *` (use sparingly)
- Import statements should usually be placed at the top of the file.
- Python searches predefined locations to find modules.

---

# Chapter Summary

In this chapter, we learned:

- Import Statement
- Different Import Methods
- Importing Built-in Modules
- Importing User-Defined Modules
- Module Search Process
- Best Practices
- Common Mistakes
- Interview Questions
- Quick Revision


# Program 1 – Importing an Entire Module

## Problem Statement

Write a Python program to import the `math` module and calculate the square root of a number.

---

## Program

```python
import math

number = 81

result = math.sqrt(number)

print("Square Root :", result)
```

---

## Output

```text
Square Root : 9.0
```

---

## Explanation

The entire `math` module is imported.

The required function is accessed using

```python
math.sqrt()
```

---

# Program 2 – Importing a Specific Function

## Program

```python
from math import sqrt

print(sqrt(100))
```

---

## Output

```text
10.0
```

---

## Explanation

Only the `sqrt()` function is imported.

The module name is not required while calling the function.

---

# Program 3 – Importing Multiple Functions

## Program

```python
from math import sqrt, factorial

print(sqrt(64))

print(factorial(5))
```

---

## Output

```text
8.0

120
```

---

## Explanation

Multiple functions can be imported from the same module.

---

# Program 4 – Wildcard Import

## Program

```python
from math import *

print(sqrt(49))

print(pow(2, 5))
```

---

## Output

```text
7.0

32.0
```

---

## Explanation

The wildcard (`*`) imports all public members from the module.

Although supported,

this approach is generally **not recommended** because it may cause naming conflicts.

---

# Program 5 – Importing Multiple Modules

## Program

```python
import math
import random

print(math.factorial(6))

print(random.randint(1, 10))
```

---

## Sample Output

```text
720

4
```

---

## Explanation

Multiple modules can be imported into the same Python program.

---

# Program 6 – Importing a User-Defined Module

## File : calculator.py

```python
def add(a, b):

    return a + b
```

---

## File : main.py

```python
import calculator

print(calculator.add(20, 30))
```

---

## Output

```text
50
```

---

## Explanation

Python imports the user-defined module

```text
calculator.py
```

and makes its functions available.

---

# Program 7 – Importing Multiple Members from a User-Defined Module

## File : calculator.py

```python
def add(a, b):

    return a + b

def subtract(a, b):

    return a - b
```

---

## File : main.py

```python
from calculator import add, subtract

print(add(15, 5))

print(subtract(15, 5))
```

---

## Output

```text
20

10
```

---

## Explanation

Only the required functions are imported.

This keeps the namespace cleaner.

---

# Program 8 – ModuleNotFoundError

## Program

```python
import samplemodule
```

---

## Output

```text
ModuleNotFoundError:
No module named 'samplemodule'
```

---

## Explanation

Python raises

```python
ModuleNotFoundError
```

when it cannot locate the specified module.

---

# Program 9 – Importing datetime Module

## Program

```python
import datetime

current = datetime.datetime.now()

print(current)
```

---

## Sample Output

```text
2026-07-01 14:45:10.123456
```

---

## Explanation

The `datetime` module provides classes for working with dates and times.

---

# Program 10 – Importing os Module

## Program

```python
import os

print(os.getcwd())

print(os.name)
```

---

## Sample Output

```text
C:\Users\Student\Python

nt
```

---

## Explanation

The `os` module provides operating system related functionality.

- `getcwd()` returns the current working directory.
- `name` identifies the operating system.

---

# Dry Run

```text
Program Starts

↓

Import Statement

↓

Python Searches Module

↓

Module Found

↓

Module Loaded

↓

Functions Available

↓

Required Function Executed

↓

Output Displayed

↓

Program Ends
```

---

# Memory Representation

```text
Python Program

│

├── Main Module

│

├── math Module

│

├── random Module

│

└── calculator Module

      │

      ├── Variables

      ├── Functions

      └── Classes

↓

Program Ends
```

---

# Advantages

- Encourages code reuse.
- Makes applications modular.
- Reduces duplicate code.
- Improves readability.
- Simplifies maintenance.

---

# Best Practices

- Place import statements at the beginning of the file.
- Import only the required modules or members.
- Prefer explicit imports over wildcard imports.
- Use meaningful names for custom modules.
- Avoid naming custom modules after built-in modules.

---

# Common Mistakes

## Mistake 1

Using a function without importing its module.

---

## Mistake 2

Using wildcard imports unnecessarily.

---

## Mistake 3

Misspelling the module name.

---

## Mistake 4

Naming custom modules after built-in modules such as:

```text
math.py

random.py

os.py
```

This can prevent the intended built-in module from being imported.

---

# Interview Questions

## 1. What is the purpose of the `import` statement?

### Answer

It loads a module into the current program so that its members can be used.

---

## 2. What is the difference between

```python
import math
```

and

```python
from math import sqrt
```

### Answer

`import math` imports the entire module.

`from math import sqrt` imports only the `sqrt()` function.

---

## 3. Can multiple modules be imported in one program?

### Answer

Yes.

A Python program can import multiple built-in and user-defined modules.

---

## 4. What happens if Python cannot find a module?

### Answer

Python raises

```python
ModuleNotFoundError
```

---

## 5. Why are wildcard imports discouraged?

### Answer

Because they can cause namespace conflicts and reduce code readability.

---

## 6. Where should import statements usually be placed?

### Answer

At the beginning of the Python file, following any module-level documentation and before executable code.

---

## 7. Can user-defined modules be imported like built-in modules?

### Answer

Yes.

As long as they are located in Python's module search path.

---

# Practice Programs

1. Import the `math` module and calculate a square root.
2. Import only the `factorial()` function.
3. Import multiple functions from the same module.
4. Create and import a custom module.
5. Demonstrate `ModuleNotFoundError`.

---

# Quick Revision

- `import module`
- `from module import member`
- `from module import member1, member2`
- `from module import *` (avoid in production code)
- Import statements should be placed at the top of the file.
- Python searches the module search path before importing.

---

# Chapter Summary

In this chapter, you learned:

- Import Statement
- Importing Entire Modules
- Importing Specific Members
- Importing Multiple Members
- Wildcard Imports
- User-Defined Module Imports
- Module Search Process
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision

