# Built-in Modules in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What are Built-in Modules?
5. Why are Built-in Modules Required?
6. Commonly Used Built-in Modules
7. Advantages of Built-in Modules
8. Internal Working
9. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand built-in modules.
- Learn why built-in modules are useful.
- Use commonly used Python built-in modules.
- Import built-in modules.
- Apply built-in modules in real-world programs.

---

# Prerequisites

Before learning this chapter, you should know:

- Modules
- Import Statements
- Aliasing
- Packages

---

# Introduction

Python comes with a rich collection of pre-written modules called the **Python Standard Library**.

These modules provide ready-to-use functions and classes for common programming tasks.

Instead of writing code from scratch,

developers can simply import the required module and use its functionality.

---

# What are Built-in Modules?

## Definition

A **Built-in Module** is a module that is included with Python and can be imported directly without installing additional packages.

---

## Simple Definition

> Built-in modules are ready-made Python modules provided by the Python Standard Library.

---

# Why are Built-in Modules Required?

Without built-in modules,

developers would have to write common functionality repeatedly.

For example,

- Mathematical calculations
- Random number generation
- Date and time operations
- File system access
- System information

Built-in modules save time and reduce development effort.

---

# Commonly Used Built-in Modules

| Module | Purpose |
|---------|---------|
| `math` | Mathematical functions |
| `random` | Random number generation |
| `datetime` | Date and time operations |
| `time` | Time-related functions |
| `calendar` | Calendar operations |
| `os` | Operating system interaction |
| `sys` | Python runtime information |
| `statistics` | Statistical calculations |
| `string` | String constants and utilities |
| `collections` | Specialized container data types |

---

# Module 1 – math

Used for mathematical operations.

Example

```python
import math

print(math.sqrt(64))

print(math.factorial(5))
```

---

# Module 2 – random

Used for generating random values.

Example

```python
import random

print(random.randint(1, 100))
```

---

# Module 3 – datetime

Used for handling dates and times.

Example

```python
import datetime

print(datetime.datetime.now())
```

---

# Module 4 – time

Used for time-related operations.

Example

```python
import time

print(time.time())
```

---

# Module 5 – calendar

Used to display calendars.

Example

```python
import calendar

print(calendar.month(2026, 7))
```

---

# Module 6 – os

Provides operating system functionality.

Example

```python
import os

print(os.getcwd())
```

---

# Module 7 – sys

Provides access to Python runtime information.

Example

```python
import sys

print(sys.version)
```

---

# Module 8 – statistics

Provides statistical calculations.

Example

```python
import statistics

print(statistics.mean([10, 20, 30]))
```

---

# Module 9 – string

Provides useful string constants.

Example

```python
import string

print(string.ascii_uppercase)
```

---

# Module 10 – collections

Provides specialized container data types.

Example

```python
from collections import Counter

print(Counter("banana"))
```

---

# Internal Working

```text
Program Starts

↓

Import Module

↓

Python Searches Standard Library

↓

Module Loaded

↓

Functions Available

↓

Program Continues
```

---

# Advantages

- Ready-to-use functionality.
- Saves development time.
- Well-tested and reliable.
- Improves productivity.
- Reduces code duplication.

---

# Best Practices

- Import only the required modules.
- Prefer explicit imports.
- Read official documentation.
- Avoid unnecessary imports.
- Use aliases only when needed.

---

# Common Mistakes

## Mistake 1

Trying to install built-in modules using pip.

Example

```bash
pip install math
```

This is incorrect.

---

## Mistake 2

Creating custom modules with names matching built-in modules.

Example

```text
math.py

random.py

os.py
```

---

## Mistake 3

Importing unused modules.

---

## Mistake 4

Using wildcard imports.

---

# Program 1 – Using math Module

```python
import math

print(math.sqrt(144))

print(math.factorial(6))
```

---

## Output

```text
12.0

720
```

---

# Program 2 – Using random Module

```python
import random

print(random.randint(1, 10))
```

---

## Sample Output

```text
8
```

---

# Program 3 – Using datetime Module

```python
import datetime

print(datetime.datetime.now())
```

---

## Sample Output

```text
2026-07-02 15:20:10.123456
```

---

# Program 4 – Using time Module

```python
import time

print(time.time())
```

---

## Sample Output

```text
1782978000.12345
```

---

# Program 5 – Using calendar Module

```python
import calendar

print(calendar.month(2026, 7))
```

---

## Sample Output

```text
     July 2026
Mo Tu We Th Fr Sa Su
...
```

---

# Program 6 – Using os Module

```python
import os

print(os.getcwd())
```

---

## Sample Output

```text
C:\Projects\Python
```

---

# Program 7 – Using sys Module

```python
import sys

print(sys.platform)

print(sys.version)
```

---

## Sample Output

```text
win32

3.14.x
```

---

# Program 8 – Using statistics Module

```python
import statistics

marks = [80, 90, 70, 85, 95]

print(statistics.mean(marks))

print(statistics.median(marks))
```

---

## Output

```text
84

85
```

---

# Program 9 – Using string Module

```python
import string

print(string.ascii_lowercase)

print(string.digits)
```

---

## Output

```text
abcdefghijklmnopqrstuvwxyz

0123456789
```

---

# Program 10 – Using collections Module

```python
from collections import Counter

text = "programming"

print(Counter(text))
```

---

## Sample Output

```text
Counter({'g': 2, 'r': 2, 'm': 2, ...})
```

---

# Dry Run

```text
Program Starts

↓

Import Built-in Module

↓

Python Loads Module

↓

Call Required Function

↓

Function Executes

↓

Display Result

↓

Program Ends
```

---

# Memory Representation

```text
Python Program

│

├── Standard Library

│      ├── math

│      ├── random

│      ├── datetime

│      ├── os

│      ├── sys

│      └── ...

│

└── Main Program
```

---

# Interview Questions

## 1. What are built-in modules?

### Answer

Built-in modules are modules provided by Python's Standard Library.

---

## 2. Which module is used for mathematical operations?

### Answer

```python
math
```

---

## 3. Which module generates random numbers?

### Answer

```python
random
```

---

## 4. Which module is used for date and time operations?

### Answer

```python
datetime
```

---

## 5. Which module interacts with the operating system?

### Answer

```python
os
```

---

## 6. Which module provides Python runtime information?

### Answer

```python
sys
```

---

## 7. Which module performs statistical calculations?

### Answer

```python
statistics
```

---

## 8. Can built-in modules be used without installation?

### Answer

Yes.

They are included with the Python Standard Library.

---

## 9. Should built-in modules be installed using pip?

### Answer

No.

They are already available with Python.

---

## 10. Why are built-in modules important?

### Answer

They provide reusable, reliable, and optimized functionality that reduces development time.

---

# Practice Programs

1. Calculate factorial using `math`.
2. Generate random numbers.
3. Display the current date and time.
4. Print the current working directory.
5. Calculate the average of a list using `statistics`.

---

# Quick Revision

- Built-in Modules → Python Standard Library
- `math` → Mathematics
- `random` → Random numbers
- `datetime` → Date & Time
- `time` → Time functions
- `calendar` → Calendar
- `os` → Operating System
- `sys` → Runtime Information
- `statistics` → Statistical functions
- `collections` → Specialized containers

---

# Chapter Summary

In this chapter, we learned:

- Built-in Modules
- Python Standard Library
- Common Built-in Modules
- Importing Built-in Modules
- Practical Programs
- Advantages
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
