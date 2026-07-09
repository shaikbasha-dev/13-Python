# Decorators in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is a Decorator?
5. Why are Decorators Required?
6. Real-World Analogy
7. How Decorators Work
8. Syntax of Decorators
9. Components of a Decorator
10. Nested Functions
11. Wrapper Functions
12. @ Symbol
13. Multiple Decorators
14. Advantages
15. Internal Working
16. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand decorators.
- Understand higher-order functions.
- Create custom decorators.
- Use wrapper functions.
- Use the @ syntax.
- Create multiple decorators.
- Apply decorators in real-world applications.

---

# Prerequisites

Before learning this chapter, you should know:

- Functions
- Lambda Functions
- Nested Functions
- Returning Functions
- Functional Programming Basics

---

# Introduction

In software development,

developers often need to perform some common tasks before or after executing a function.

Examples include:

- Logging
- Authentication
- Authorization
- Performance measurement
- Input validation
- Exception handling

Writing the same code repeatedly inside every function leads to duplicate code.

Python solves this problem using **Decorators**.

---

# What is a Decorator?

## Definition

A **Decorator** is a function that receives another function as an argument, adds additional functionality, and returns a new function without modifying the original function.

---

## Simple Definition

> A decorator adds extra functionality to an existing function without changing its original code.

---

# Why are Decorators Required?

Suppose you have 100 functions.

Each function must:

- Log execution
- Check authentication
- Measure execution time

Without decorators,

the same code must be written 100 times.

Decorators allow writing that logic once and applying it wherever needed.

---

# Real-World Analogy

Imagine a birthday gift.

Original Item

```text
Book
```

Decorator

```text
Gift Wrapper
```

Final Product

```text
Gift Wrapped Book
```

The book remains the same.

Only additional decoration is added.

Similarly,

a decorator keeps the original function unchanged while adding extra behavior.

---

# Higher-Order Functions

A higher-order function is a function that:

- Accepts another function as an argument.
- Returns another function.

Decorators are built using higher-order functions.

Example

```python
def display():

    print("Hello")
```

A decorator receives

```python
display
```

as an argument.

---

# How Decorators Work

```text
Original Function

↓

Decorator

↓

Wrapper Function

↓

Additional Functionality

↓

Original Function Executes

↓

Additional Functionality

↓

Output
```

---

# Syntax of Decorators

Without @ Symbol

```python
def decorator(func):

    def wrapper():

        print("Before Function")

        func()

        print("After Function")

    return wrapper
```

Applying Decorator

```python
decorated = decorator(display)

decorated()
```

---

Using @ Symbol

```python
@decorator

def display():

    print("Hello")
```

Python automatically executes

```python
display = decorator(display)
```

---

# Components of a Decorator

A decorator consists of three functions.

### Original Function

```python
def display():

    print("Hello")
```

---

### Decorator Function

```python
def decorator(func):
```

Receives another function.

---

### Wrapper Function

```python
def wrapper():
```

Executes

- Before logic
- Original function
- After logic

---

# Nested Functions

A function defined inside another function is called a nested function.

Example

```python
def outer():

    def inner():

        print("Inner Function")

    inner()
```

Nested functions are the foundation of decorators.

---

# Wrapper Function

The wrapper function controls the execution of the original function.

Example

```text
Wrapper

↓

Before Code

↓

Original Function

↓

After Code
```

---

# @ Symbol

Python provides

```python
@
```

for applying decorators.

Instead of writing

```python
display = decorator(display)
```

we simply write

```python
@decorator
```

This makes the code cleaner and easier to read.

---

# Multiple Decorators

A function can have multiple decorators.

Example

```python
@decorator1

@decorator2

def display():

    pass
```

Execution Order

```text
decorator1

↓

decorator2

↓

Original Function
```

---

# Real-World Uses

Decorators are commonly used for:

- Authentication
- Authorization
- Logging
- Performance Measurement
- Caching
- Retry Mechanisms
- Validation
- Exception Handling
- API Development
- Web Frameworks

---

# Advantages

- Promotes code reuse.
- Eliminates duplicate code.
- Improves readability.
- Keeps business logic clean.
- Easy maintenance.
- Widely used in professional projects.

---

# Best Practices

- Keep decorators focused on one responsibility.
- Use meaningful decorator names.
- Keep wrapper functions simple.
- Preserve function metadata using `functools.wraps`.
- Avoid excessive nesting of decorators.

---

# Common Mistakes

## Mistake 1

Forgetting to return the wrapper function.

Incorrect

```python
return
```

Correct

```python
return wrapper
```

---

## Mistake 2

Calling the function instead of passing it.

Incorrect

```python
decorator(display())
```

Correct

```python
decorator(display)
```

---

## Mistake 3

Not accepting arguments in the wrapper when decorating functions that require parameters.

---

## Mistake 4

Creating overly complex decorators.

---

# Internal Working

```text
Function Created

↓

Decorator Receives Function

↓

Wrapper Created

↓

Wrapper Returned

↓

Function Replaced

↓

Function Called

↓

Wrapper Executes

↓

Before Logic

↓

Original Function

↓

After Logic

↓

Output
```

---

# Interview Questions

## 1. What is a decorator?

### Answer

A decorator is a function that adds additional functionality to another function without modifying its original code.

---

## 2. Why are decorators used?

### Answer

To add reusable functionality such as logging, authentication, validation, and timing without duplicating code.

---

## 3. What is a higher-order function?

### Answer

A function that accepts another function as an argument or returns another function.

---

## 4. What is a wrapper function?

### Answer

A nested function inside the decorator that executes additional code before and/or after the original function.

---

## 5. Which symbol is used for decorators?

### Answer

```python
@
```

---

## 6. Can multiple decorators be applied to a function?

### Answer

Yes.

Multiple decorators can be stacked above a function.

---

## 7. Do decorators modify the original function?

### Answer

No.

They extend its behavior without changing its source code.

---

# Quick Revision

- Decorator → Adds functionality.
- Higher-Order Function.
- Wrapper Function.
- Nested Function.
- Uses `@`.
- Promotes code reuse.
- Common in professional Python projects.

---

# Chapter Summary

In this chapter, you learned:

- Decorators
- Higher-Order Functions
- Nested Functions
- Wrapper Functions
- @ Symbol
- Multiple Decorators
- Advantages
- Best Practices
- Common Mistakes
- Interview Questions
- Quick Revision


# Program 1 – Basic Decorator Without @ Symbol

## Problem Statement

Write a Python program to create a basic decorator without using the `@` symbol.

---

## Program

```python
def decorator(func):

    def wrapper():

        print("Before Function")

        func()

        print("After Function")

    return wrapper


def display():

    print("Hello Python")


decorated = decorator(display)

decorated()
```

---

## Output

```text
Before Function

Hello Python

After Function
```

---

## Explanation

The decorator receives the `display()` function.

The wrapper executes code before and after the original function.

---

# Program 2 – Decorator Using @ Symbol

## Program

```python
def decorator(func):

    def wrapper():

        print("Before Function")

        func()

        print("After Function")

    return wrapper


@decorator
def display():

    print("Learning Decorators")


display()
```

---

## Output

```text
Before Function

Learning Decorators

After Function
```

---

## Explanation

The `@decorator` syntax is equivalent to:

```python
display = decorator(display)
```

---

# Program 3 – Decorator with Function Arguments

## Program

```python
def decorator(func):

    def wrapper(a, b):

        print("Addition Started")

        func(a, b)

        print("Addition Completed")

    return wrapper


@decorator
def add(a, b):

    print("Result :", a + b)


add(10, 20)
```

---

## Output

```text
Addition Started

Result : 30

Addition Completed
```

---

## Explanation

The wrapper accepts the same arguments as the original function.

---

# Program 4 – Decorator Returning a Value

## Program

```python
def decorator(func):

    def wrapper(a, b):

        print("Calculating...")

        return func(a, b)

    return wrapper


@decorator
def multiply(a, b):

    return a * b


print(multiply(5, 6))
```

---

## Output

```text
Calculating...

30
```

---

## Explanation

The wrapper returns the value produced by the original function.

---

# Program 5 – Logging Decorator

## Program

```python
def logger(func):

    def wrapper():

        print("Function Execution Started")

        func()

        print("Function Execution Finished")

    return wrapper


@logger
def task():

    print("Processing Data")


task()
```

---

## Output

```text
Function Execution Started

Processing Data

Function Execution Finished
```

---

## Explanation

Logging decorators are commonly used to track function execution.

---

# Program 6 – Authentication Decorator

## Program

```python
def authenticate(func):

    def wrapper(user):

        if user == "admin":

            func(user)

        else:

            print("Access Denied")

    return wrapper


@authenticate
def dashboard(user):

    print("Welcome", user)


dashboard("admin")

dashboard("guest")
```

---

## Output

```text
Welcome admin

Access Denied
```

---

## Explanation

The decorator checks authentication before executing the function.

---

# Program 7 – Measuring Execution Time

## Program

```python
import time

def timer(func):

    def wrapper():

        start = time.time()

        func()

        end = time.time()

        print("Execution Time :", end - start)

    return wrapper


@timer
def task():

    time.sleep(2)


task()
```

---

## Sample Output

```text
Execution Time : 2.00...
```

---

## Explanation

The decorator measures how long a function takes to execute.

---

# Program 8 – Multiple Decorators

## Program

```python
def decorator1(func):

    def wrapper():

        print("Decorator 1")

        func()

    return wrapper


def decorator2(func):

    def wrapper():

        print("Decorator 2")

        func()

    return wrapper


@decorator1

@decorator2
def display():

    print("Original Function")


display()
```

---

## Output

```text
Decorator 1

Decorator 2

Original Function
```

---

## Explanation

Decorators execute from the top down.

The innermost decorator calls the original function.

---

# Program 9 – Using functools.wraps

## Program

```python
from functools import wraps

def decorator(func):

    @wraps(func)

    def wrapper():

        print("Before")

        func()

    return wrapper


@decorator
def display():

    """Display Function"""

    print("Hello")


print(display.__name__)

print(display.__doc__)
```

---

## Output

```text
display

Display Function
```

---

## Explanation

`functools.wraps` preserves the metadata of the original function, such as its name and documentation string.

---

# Program 10 – Complete Decorator Example

## Program

```python
from functools import wraps

def logger(func):

    @wraps(func)

    def wrapper(*args, **kwargs):

        print("Function Started")

        result = func(*args, **kwargs)

        print("Function Finished")

        return result

    return wrapper


@logger
def square(number):

    return number * number


print(square(6))
```

---

## Output

```text
Function Started

Function Finished

36
```

---

## Explanation

`*args` and `**kwargs` allow the decorator to work with functions that accept any number of positional and keyword arguments.

---

# Dry Run

```text
Function Defined

↓

Decorator Applied

↓

Wrapper Created

↓

Function Replaced

↓

Function Called

↓

Wrapper Executes

↓

Before Code

↓

Original Function

↓

After Code

↓

Result Returned
```

---

# Memory Representation

```text
Memory

│

├── Original Function

│

├── Decorator

│

└── Wrapper Function

        │

        ├── Before Logic

        ├── Original Function

        └── After Logic
```

---

# Advantages

- Promotes code reuse.
- Reduces duplicate code.
- Separates business logic from common tasks.
- Improves readability.
- Simplifies maintenance.
- Widely used in Python frameworks.

---

# Best Practices

- Use `functools.wraps` to preserve function metadata.
- Keep decorators focused on one responsibility.
- Use `*args` and `**kwargs` for reusable decorators.
- Keep wrapper functions simple.
- Write meaningful decorator names.

---

# Common Mistakes

## Mistake 1

Forgetting to return the wrapper.

---

## Mistake 2

Calling the function instead of passing it.

Incorrect

```python
decorator(display())
```

Correct

```python
decorator(display)
```

---

## Mistake 3

Not returning the original function's result.

---

## Mistake 4

Ignoring `*args` and `**kwargs`.

This limits the decorator to functions with fixed parameters.

---

# Interview Questions

## 1. What is a decorator?

### Answer

A decorator is a function that extends the behavior of another function without modifying its original code.

---

## 2. Why are decorators used?

### Answer

To add reusable functionality such as logging, authentication, caching, validation, and performance measurement.

---

## 3. Which symbol is used to apply decorators?

### Answer

```python
@
```

---

## 4. What is a wrapper function?

### Answer

A nested function inside the decorator that executes additional code before and/or after the original function.

---

## 5. Why is `functools.wraps` used?

### Answer

It preserves the original function's metadata, such as its name and documentation string.

---

## 6. Can multiple decorators be applied?

### Answer

Yes.

Multiple decorators can be stacked on a single function.

---

## 7. Why use `*args` and `**kwargs` in decorators?

### Answer

They allow decorators to work with functions that accept different numbers and types of arguments.

---

## 8. Do decorators modify the original function?

### Answer

No.

They extend its behavior while leaving the original implementation unchanged.

---

# Practice Programs

1. Create a decorator that prints messages before and after a function.
2. Create a logging decorator.
3. Create an authentication decorator.
4. Create a timing decorator.
5. Create a decorator using `functools.wraps`.
6. Apply multiple decorators to a function.
7. Create a decorator that accepts functions with different arguments.

---

# Quick Revision

- Decorator → Adds functionality.
- Uses `@`.
- Wrapper Function.
- Higher-Order Function.
- Nested Function.
- `functools.wraps`
- `*args`
- `**kwargs`
- Multiple Decorators.
- Promotes code reuse.

---

# Chapter Summary

In this chapter, you learned:

- Decorators
- Higher-Order Functions
- Nested Functions
- Wrapper Functions
- @ Symbol
- Decorators with Arguments
- Returning Values
- Logging Decorators
- Authentication Decorators
- Timing Decorators
- Multiple Decorators
- functools.wraps
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
