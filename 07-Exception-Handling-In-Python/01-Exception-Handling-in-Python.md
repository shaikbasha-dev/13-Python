# Exception Handling in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is an Exception?
5. Why is Exception Handling Required?
6. Error vs Exception
7. Types of Errors
8. Types of Exceptions
9. Exception Hierarchy
10. Exception Handling Flow
11. Internal Working
12. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand Exception Handling.
- Differentiate Errors and Exceptions.
- Learn why Exception Handling is important.
- Understand Python's Exception Hierarchy.
- Identify different types of Exceptions.
- Understand the flow of Exception Handling.

---

# Prerequisites

Before learning this chapter, you should know:

- Variables
- Operators
- Functions
- Classes
- Objects
- Control Statements

---

# Introduction

While developing software,

errors may occur during program execution.

Some errors terminate the program immediately.

Consider the following example.

```python
number = 10

result = number / 0

print(result)
```

Output

```text
ZeroDivisionError:
division by zero
```

The program terminates because Python cannot divide a number by zero.

Instead of allowing the program to terminate unexpectedly,

Python provides **Exception Handling**.

Exception Handling allows us to detect errors and continue program execution gracefully.

---

# What is an Exception?

## Definition

An **Exception** is an abnormal event that occurs during the execution of a program and interrupts the normal flow of execution.

When an exception occurs,

Python creates an Exception Object and searches for code that can handle it.

---

# Simple Definition

> An Exception is a runtime event that disrupts the normal execution of a program.

---

# Why is Exception Handling Required?

Suppose we are developing an ATM Application.

The customer enters

```text
Withdraw Amount

↓

1000
```

Current Balance

```text
500
```

Without Exception Handling,

the application may terminate unexpectedly.

With Exception Handling,

the application displays

```text
Insufficient Balance
```

and continues execution.

This improves user experience.

---

# Real-World Examples

Exception Handling is used in:

- ATM Machines
- Banking Applications
- Online Shopping
- Login Systems
- Hospital Management
- Airline Reservation Systems
- Payment Gateways
- Database Applications

---

# Error vs Exception

| Error | Exception |
|--------|-----------|
| Serious problem | Recoverable problem |
| Difficult to handle | Can be handled |
| Program may terminate | Program can continue |
| Example: Syntax Error | Example: ZeroDivisionError |

---

# Types of Errors

Errors are mainly classified into two categories.

## 1. Syntax Errors

Syntax Errors occur when Python rules are violated.

Example

```python
if True

    print("Hello")
```

Output

```text
SyntaxError
```

The program does not execute.

---

## 2. Runtime Errors (Exceptions)

Runtime Errors occur while the program is executing.

Example

```python
print(10 / 0)
```

Output

```text
ZeroDivisionError
```

---

# Types of Exceptions

Some commonly used exceptions are:

| Exception | Description |
|------------|-------------|
| ZeroDivisionError | Division by zero |
| NameError | Variable not found |
| TypeError | Invalid data type operation |
| ValueError | Invalid value |
| IndexError | Invalid list index |
| KeyError | Dictionary key not found |
| AttributeError | Invalid object attribute |
| FileNotFoundError | File does not exist |
| ImportError | Module cannot be imported |
| ModuleNotFoundError | Module not found |

---

# Exception Hierarchy

Python organizes exceptions into a hierarchy.

```text
BaseException

│

├── SystemExit

├── KeyboardInterrupt

├── GeneratorExit

└── Exception

     │

     ├── ArithmeticError

     │      ├── ZeroDivisionError

     │      ├── OverflowError

     │      └── FloatingPointError

     │

     ├── LookupError

     │      ├── IndexError

     │      └── KeyError

     │

     ├── TypeError

     ├── ValueError

     ├── NameError

     ├── AttributeError

     ├── FileNotFoundError

     ├── ImportError

     └── RuntimeError
```

Most user programs handle exceptions derived from

```text
Exception
```

---

# Exception Handling Flow

When an exception occurs,

Python follows this sequence.

```text
Program Starts

↓

Statements Execute

↓

Exception Occurs?

↓

No

↓

Continue Execution

↓

Program Ends

----------------------------

Yes

↓

Create Exception Object

↓

Search for Matching Handler

↓

Handler Found?

↓

Yes

↓

Execute Handler

↓

Continue Program

----------------------------

No

↓

Program Terminates
```

---

# Internal Working

```text
Statement Executes

↓

Exception Raised

↓

Python Creates Exception Object

↓

Searches for Matching except Block

↓

Handler Found?

↓

Yes

↓

Execute Handler

↓

Continue Execution

----------------------

No

↓

Program Terminates
```

---

# Advantages of Exception Handling

- Prevents abnormal program termination.
- Improves software reliability.
- Improves user experience.
- Makes debugging easier.
- Separates error-handling logic from business logic.
- Produces maintainable applications.

---

# Best Practices

- Handle only expected exceptions.
- Keep exception handling simple.
- Display meaningful error messages.
- Avoid suppressing exceptions unnecessarily.
- Use specific exception classes instead of generic ones.

---

# Common Mistakes

## Mistake 1

Confusing Errors and Exceptions.

- Syntax Errors occur before execution.
- Exceptions occur during execution.

---

## Mistake 2

Ignoring possible runtime exceptions.

Programs should anticipate common runtime failures.

---

## Mistake 3

Using overly broad exception handling.

Avoid handling every exception with a generic handler unless necessary.

---

# Interview Questions

## 1. What is an Exception?

### Answer

An Exception is an abnormal event that occurs during program execution and interrupts the normal flow of the program.

---

## 2. Why is Exception Handling required?

### Answer

It prevents abnormal program termination and allows programs to recover gracefully from runtime problems.

---

## 3. What is the difference between an Error and an Exception?

### Answer

Errors usually indicate serious problems such as syntax issues, while Exceptions are runtime events that can often be handled.

---

## 4. What is the base class for most user-handled exceptions?

### Answer

```python
Exception
```

---

## 5. Name some common built-in exceptions.

### Answer

- ZeroDivisionError
- ValueError
- TypeError
- IndexError
- KeyError
- NameError
- AttributeError
- FileNotFoundError

---

# Quick Revision

- Exception → Runtime abnormal event
- Syntax Error → Before execution
- Runtime Error → During execution
- Exception Handling prevents program termination
- Python creates an Exception Object
- Searches for a matching handler
- Executes handler if found

---

# Chapter Summary

In this chapter, we learned:

- Exception Handling
- Errors vs Exceptions
- Syntax Errors
- Runtime Errors
- Exception Hierarchy
- Exception Handling Flow
- Internal Working
- Advantages
- Best Practices
- Common Mistakes
- Interview Questions
- Quick Revision

