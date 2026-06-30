# try-except Block in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is a try Block?
5. What is an except Block?
6. Why are try-except Blocks Required?
7. Syntax
8. Flow of Execution
9. Multiple except Blocks
10. Nested try-except Blocks
11. Internal Working
12. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the try block.
- Understand the except block.
- Learn how Python handles exceptions.
- Use multiple except blocks.
- Implement nested try-except blocks.
- Write robust Python programs.

---

# Prerequisites

Before learning this chapter, you should know:

- Exception Handling
- Runtime Errors
- Variables
- Functions
- Control Statements

---

# Introduction

In the previous chapter,

we learned that runtime errors interrupt the normal execution of a program.

Consider the following example.

```python
number = 10

result = number / 0

print(result)

print("Program Completed")
```

Output

```text
ZeroDivisionError:
division by zero
```

The last statement

```python
print("Program Completed")
```

never executes.

To prevent this,

Python provides the

```python
try-except
```

mechanism.

It allows the program to handle exceptions gracefully and continue execution.

---

# What is a try Block?

## Definition

A **try block** contains code that may generate an exception.

Python continuously monitors the statements inside the try block.

If an exception occurs,

Python immediately stops executing the remaining statements inside the try block and searches for a matching except block.

---

## Simple Definition

> The try block contains code that may produce an exception.

---

# What is an except Block?

## Definition

An **except block** contains the code that handles an exception.

If a matching exception occurs inside the try block,

Python transfers control to the corresponding except block.

---

## Simple Definition

> The except block handles exceptions raised inside the try block.

---

# Why are try-except Blocks Required?

Suppose we are developing a Login System.

A user enters incorrect input.

Without Exception Handling,

the application may terminate.

With try-except,

the application can display a meaningful message such as

```text
Invalid Input

Please Try Again
```

and continue execution.

---

# Real-World Examples

try-except blocks are commonly used in:

- Banking Applications
- ATM Machines
- Login Systems
- File Handling
- Database Connections
- Network Communication
- Payment Gateways
- Web Applications

---

# Syntax

## Basic Syntax

```python
try:

    # Risky Code

except:

    # Exception Handling Code
```

---

## Handling a Specific Exception

```python
try:

    # Risky Code

except ZeroDivisionError:

    # Handle Division by Zero
```

---

## Handling Multiple Exceptions

```python
try:

    # Risky Code

except ValueError:

    # Handle ValueError

except TypeError:

    # Handle TypeError
```

---

# Flow of Execution

Python executes the try-except block in the following order.

```text
Program Starts

↓

Enter try Block

↓

Execute Statement

↓

Exception Occurs?

↓

No

↓

Skip except Block

↓

Continue Program

----------------------

Yes

↓

Search Matching except

↓

Found?

↓

Yes

↓

Execute except Block

↓

Continue Program

----------------------

No

↓

Program Terminates
```

---

# Multiple except Blocks

A try block can have multiple except blocks.

Each except block handles a specific type of exception.

Example

```python
try:

    # Risky Code

except ZeroDivisionError:

    pass

except ValueError:

    pass

except TypeError:

    pass
```

Python executes only the first matching except block.

---

# Nested try-except Blocks

A try block may contain another try-except block.

Example

```python
try:

    try:

        # Risky Code

    except ValueError:

        pass

except ZeroDivisionError:

    pass
```

Nested try-except blocks are useful when different parts of a program require independent exception handling.

---

# Internal Working

```text
Enter try Block

↓

Execute Statements

↓

Exception Raised?

↓

No

↓

Skip except Block

↓

Continue Program

--------------------

Yes

↓

Create Exception Object

↓

Search Matching except

↓

Execute Handler

↓

Continue Program
```

---

# Advantages

- Prevents abnormal program termination.
- Makes applications more reliable.
- Improves user experience.
- Separates normal logic from error-handling logic.
- Makes debugging easier.

---

# Best Practices

- Keep the try block as small as possible.
- Catch only expected exceptions.
- Display meaningful error messages.
- Use specific exception classes whenever possible.
- Avoid writing unnecessary code inside the try block.

---

# Common Mistakes

## Mistake 1

Writing all program logic inside the try block.

Only risky statements should be placed inside try.

---

## Mistake 2

Using a generic except block unnecessarily.

Prefer

```python
except ZeroDivisionError:
```

instead of

```python
except:
```

whenever possible.

---

## Mistake 3

Ignoring exceptions completely.

Avoid empty exception handlers unless there is a valid reason.

---

# Interview Questions

## 1. What is a try block?

### Answer

A try block contains code that may generate an exception.

---

## 2. What is an except block?

### Answer

An except block handles exceptions raised inside the corresponding try block.

---

## 3. What happens if no exception occurs?

### Answer

The except block is skipped and the program continues normally.

---

## 4. Can one try block have multiple except blocks?

### Answer

Yes.

Each except block can handle a different type of exception.

---

## 5. Can try-except blocks be nested?

### Answer

Yes.

Python allows nested try-except blocks.

---

# Quick Revision

- try → Risky Code
- except → Exception Handling
- Multiple except blocks are supported.
- Nested try-except blocks are allowed.
- Python executes only the first matching except block.

---

# Chapter Summary

In this chapter, you learned:

- try Block
- except Block
- Flow of Execution
- Multiple except Blocks
- Nested try-except Blocks
- Internal Working
- Best Practices
- Common Mistakes
- Interview Questions
- Quick Revision


# Program 1 – Basic try-except Block

## Problem Statement

Write a Python program to handle a division by zero exception.

---

## Program

```python
try:

    number = 10

    result = number / 0

    print(result)

except ZeroDivisionError:

    print("Cannot divide by zero.")

print("Program Completed")
```

---

## Output

```text
Cannot divide by zero.

Program Completed
```

---

## Explanation

When division by zero occurs,

Python raises a `ZeroDivisionError`.

The matching `except` block executes,

and the program continues normally.

---

# Program 2 – Handling ValueError

## Program

```python
try:

    age = int(input("Enter Age : "))

    print("Age :", age)

except ValueError:

    print("Please enter a valid integer.")
```

---

## Sample Output

```text
Enter Age : abc

Please enter a valid integer.
```

---

## Explanation

If the user enters non-numeric data,

`int()` raises a `ValueError`.

---

# Program 3 – Handling Multiple Exceptions

## Program

```python
try:

    number = int(input("Enter Number : "))

    result = 100 / number

    print(result)

except ZeroDivisionError:

    print("Division by zero is not allowed.")

except ValueError:

    print("Please enter a valid integer.")
```

---

## Sample Output 1

```text
Enter Number : 0

Division by zero is not allowed.
```

---

## Sample Output 2

```text
Enter Number : abc

Please enter a valid integer.
```

---

## Explanation

Python executes only the first matching `except` block.

---

# Program 4 – Using Exception Object

## Program

```python
try:

    number = 10 / 0

except ZeroDivisionError as error:

    print("Exception :", error)
```

---

## Output

```text
Exception : division by zero
```

---

## Explanation

Using

```python
as error
```

stores the exception object,

allowing us to display the actual error message.

---

# Program 5 – Generic Exception Handler

## Program

```python
try:

    value = int("Python")

except Exception as error:

    print("Error :", error)
```

---

## Output

```text
Error : invalid literal for int() with base 10: 'Python'
```

---

## Explanation

`Exception` is the base class for most user-handled exceptions.

It can handle different exception types.

---

# Program 6 – Nested try-except

## Program

```python
try:

    print("Outer try")

    try:

        print(10 / 0)

    except ZeroDivisionError:

        print("Inner Exception Handled")

except Exception:

    print("Outer Exception Handled")
```

---

## Output

```text
Outer try

Inner Exception Handled
```

---

## Explanation

The inner `try-except` handles the exception.

Therefore,

the outer `except` block is not executed.

---

# Program 7 – File Handling Exception

## Program

```python
try:

    file = open("student.txt")

except FileNotFoundError:

    print("File does not exist.")
```

---

## Output

```text
File does not exist.
```

---

## Explanation

Attempting to open a non-existing file raises a `FileNotFoundError`.

---

# Program 8 – Handling IndexError

## Program

```python
try:

    numbers = [10, 20, 30]

    print(numbers[5])

except IndexError:

    print("Invalid list index.")
```

---

## Output

```text
Invalid list index.
```

---

# Program 9 – Handling KeyError

## Program

```python
try:

    student = {

        "name": "Rahul"

    }

    print(student["age"])

except KeyError:

    print("Key not found.")
```

---

## Output

```text
Key not found.
```

---

# Program 10 – Successful Execution

## Program

```python
try:

    number = 100 / 5

    print(number)

except ZeroDivisionError:

    print("Exception Occurred")

print("Program Completed")
```

---

## Output

```text
20.0

Program Completed
```

---

## Explanation

Since no exception occurs,

the `except` block is skipped.

Execution continues normally.

---

# Dry Run

```text
Enter try Block

↓

Execute Statement

↓

Exception Occurs?

↓

No

↓

Skip except

↓

Continue Execution

--------------------

Yes

↓

Matching except Found

↓

Execute except Block

↓

Continue Program
```

---

# Memory Representation

```text
Program

↓

try Block

↓

Risky Statements

↓

Exception?

↓

No → Continue

↓

Yes

↓

Exception Object

↓

except Block

↓

Program Continues
```

---

# Advantages

- Prevents abnormal program termination.
- Improves application reliability.
- Separates error-handling logic from business logic.
- Makes debugging easier.
- Improves user experience.

---

# Best Practices

- Keep the `try` block as small as possible.
- Catch specific exceptions whenever possible.
- Use `Exception` only when necessary.
- Display meaningful error messages.
- Avoid empty `except` blocks.

---

# Common Mistakes

## Mistake 1

Using

```python
except:
```

for every exception.

Prefer

```python
except ValueError:
```

or another specific exception.

---

## Mistake 2

Writing too many statements inside the `try` block.

Only risky code should be placed inside it.

---

## Mistake 3

Ignoring exception details.

Use

```python
except Exception as error:
```

when you need to inspect the exception message.

---

## Mistake 4

Assuming execution returns to the failed statement.

After an exception is handled,

execution continues with the first statement after the entire `try-except` block.

---

# Interview Questions

## 1. What is a try block?

### Answer

A `try` block contains code that may raise an exception.

---

## 2. What is an except block?

### Answer

An `except` block handles exceptions raised inside the corresponding `try` block.

---

## 3. Can one try block have multiple except blocks?

### Answer

Yes.

Python executes only the first matching `except` block.

---

## 4. What is the purpose of `Exception as e`?

### Answer

It stores the exception object so that its message can be accessed and displayed.

---

## 5. What happens if no exception occurs?

### Answer

The `except` block is skipped, and program execution continues normally.

---

## 6. Can try-except blocks be nested?

### Answer

Yes.

Nested `try-except` blocks are supported in Python.

---

## 7. Should you always use `except Exception`?

### Answer

No.

Specific exception classes should be preferred whenever possible.

---

# Practice Programs

1. Handle `ZeroDivisionError`.
2. Handle `ValueError` from user input.
3. Handle `IndexError` in a list.
4. Handle `KeyError` in a dictionary.
5. Demonstrate nested `try-except`.

---

# Quick Revision

- `try` → Risky code
- `except` → Exception handler
- Multiple `except` blocks are supported.
- Nested `try-except` is allowed.
- `Exception as e` provides the exception object.
- Python executes only the first matching `except` block.

---

# Chapter Summary

In this chapter, you learned:

- try Block
- except Block
- Multiple Exception Handling
- Nested try-except
- Exception Objects
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision

