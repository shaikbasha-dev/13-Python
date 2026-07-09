# else and finally Block in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is the else Block?
5. What is the finally Block?
6. Why are else and finally Blocks Required?
7. Syntax
8. Execution Flow
9. else vs finally
10. Internal Working
11. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the purpose of the `else` block.
- Understand the purpose of the `finally` block.
- Learn the execution order of try-except-else-finally.
- Understand when to use each block.
- Write reliable programs that properly release resources.

---

# Prerequisites

Before learning this chapter, you should know:

- Exception Handling
- try Block
- except Block
- Runtime Exceptions

---

# Introduction

In the previous chapter,

we learned how to handle exceptions using

```python
try-except
```

However,

sometimes we need to execute certain statements only when **no exception occurs**.

Sometimes,

we also need code that must execute **regardless of whether an exception occurs or not**.

Python provides two additional blocks for this purpose:

- `else`
- `finally`

---

# What is the else Block?

## Definition

The **else** block executes only if the try block completes successfully without raising any exception.

---

## Simple Definition

> The `else` block executes only when no exception occurs.

---

# Example

```python
try:

    number = 100 / 5

except ZeroDivisionError:

    print("Cannot divide by zero.")

else:

    print("Division Successful")
```

Output

```text
Division Successful
```

Since no exception occurs,

the else block executes.

---

# What is the finally Block?

## Definition

The **finally** block always executes,

whether an exception occurs or not.

It is commonly used to release resources such as:

- Files
- Database Connections
- Network Connections
- Sockets

---

## Simple Definition

> The `finally` block always executes.

---

# Example

```python
try:

    print("Program Started")

finally:

    print("Program Finished")
```

Output

```text
Program Started

Program Finished
```

---

# Why are else and finally Blocks Required?

Suppose we open a file.

```python
file = open("student.txt")
```

If an exception occurs before

```python
file.close()
```

the file remains open.

This may lead to:

- Memory leaks
- Resource leaks
- File locking issues

Using

```python
finally
```

ensures that resources are released properly.

---

# Real-World Applications

The `finally` block is commonly used in:

- File Handling
- Database Connections
- API Calls
- Network Programming
- Banking Applications
- Payment Gateways
- Cloud Applications

The `else` block is useful when additional processing should occur only after successful execution.

---

# Syntax

## try-except-else

```python
try:

    # Risky Code

except Exception:

    # Handle Exception

else:

    # Executes if no exception occurs
```

---

## try-finally

```python
try:

    # Risky Code

finally:

    # Always Executes
```

---

## try-except-finally

```python
try:

    # Risky Code

except Exception:

    # Handle Exception

finally:

    # Always Executes
```

---

## Complete Syntax

```python
try:

    # Risky Code

except Exception:

    # Handle Exception

else:

    # Executes if no exception occurs

finally:

    # Always Executes
```

---

# Execution Flow

## Case 1 — No Exception

```text
try

↓

No Exception

↓

else

↓

finally

↓

Program Ends
```

---

## Case 2 — Exception Occurs

```text
try

↓

Exception

↓

except

↓

finally

↓

Program Ends
```

---

# else vs finally

| else | finally |
|------|----------|
| Executes only when no exception occurs | Always executes |
| Optional | Optional |
| Used for success logic | Used for cleanup logic |
| Skipped if exception occurs | Executes regardless of exceptions |

---

# Internal Working

```text
Enter try Block

↓

Execute Statements

↓

Exception Occurs?

↓

No

↓

Execute else

↓

Execute finally

↓

Continue Program

------------------------

Yes

↓

Execute except

↓

Execute finally

↓

Continue Program
```

---

# Advantages

- Separates success logic from error handling.
- Ensures resources are always released.
- Produces cleaner code.
- Prevents resource leaks.
- Improves application reliability.

---

# Best Practices

- Use `else` only for code that depends on successful execution.
- Use `finally` for cleanup operations.
- Close files and database connections inside `finally`.
- Keep cleanup code simple.
- Avoid writing business logic inside `finally`.

---

# Common Mistakes

## Mistake 1

Writing cleanup code inside `try`.

If an exception occurs,

cleanup may never execute.

---

## Mistake 2

Using `else` as another `except`.

Remember,

`else` executes only when **no exception** occurs.

---

## Mistake 3

Placing important business logic inside `finally`.

The `finally` block should primarily be used for releasing resources.

---

# Interview Questions

## 1. What is the purpose of the `else` block?

### Answer

The `else` block executes only if no exception occurs in the `try` block.

---

## 2. What is the purpose of the `finally` block?

### Answer

The `finally` block always executes and is mainly used for cleanup operations.

---

## 3. Does the `finally` block execute even when an exception occurs?

### Answer

Yes.

The `finally` block executes whether an exception occurs or not.

---

## 4. Can a try block have both `else` and `finally`?

### Answer

Yes.

Python supports both blocks in the same try statement.

---

## 5. Which block is commonly used to close files?

### Answer

The `finally` block.

---

# Quick Revision

- `else` → Executes only when no exception occurs.
- `finally` → Always executes.
- `finally` is commonly used for cleanup.
- `else` separates successful execution from exception handling.

---

# Chapter Summary

In this chapter, we learned:

- else Block
- finally Block
- Execution Flow
- else vs finally
- Internal Working
- Advantages
- Best Practices
- Common Mistakes
- Interview Questions
- Quick Revision



# Program 1 – else Block (No Exception)

## Problem Statement

Write a Python program to demonstrate the `else` block when no exception occurs.

---

## Program

```python
try:

    number = 100 / 5

    print("Result :", number)

except ZeroDivisionError:

    print("Division by zero is not allowed.")

else:

    print("Division Successful.")
```

---

## Output

```text
Result : 20.0

Division Successful.
```

---

## Explanation

Since no exception occurs,

the `else` block executes after the `try` block.

---

# Program 2 – else Block (Exception Occurs)

## Program

```python
try:

    number = 100 / 0

    print(number)

except ZeroDivisionError:

    print("Division by zero is not allowed.")

else:

    print("Division Successful.")
```

---

## Output

```text
Division by zero is not allowed.
```

---

## Explanation

An exception occurs.

Therefore,

the `except` block executes,

and the `else` block is skipped.

---

# Program 3 – finally Block

## Program

```python
try:

    print("Inside try block")

finally:

    print("Inside finally block")
```

---

## Output

```text
Inside try block

Inside finally block
```

---

## Explanation

The `finally` block executes even though no exception occurs.

---

# Program 4 – finally with Exception

## Program

```python
try:

    print(10 / 0)

except ZeroDivisionError:

    print("Exception Handled")

finally:

    print("Finally Block Executed")
```

---

## Output

```text
Exception Handled

Finally Block Executed
```

---

## Explanation

The `finally` block executes regardless of whether an exception occurs.

---

# Program 5 – try-except-else-finally

## Program

```python
try:

    number = 100 / 10

except ZeroDivisionError:

    print("Exception")

else:

    print("No Exception")

finally:

    print("Execution Completed")
```

---

## Output

```text
No Exception

Execution Completed
```

---

## Explanation

Execution Order

```text
try

↓

else

↓

finally
```

---

# Program 6 – File Handling Example

## Program

```python
try:

    file = open("sample.txt", "r")

    print("File Opened Successfully")

except FileNotFoundError:

    print("File Not Found")

finally:

    print("Closing Resources")
```

---

## Sample Output

```text
File Not Found

Closing Resources
```

---

## Explanation

Whether the file exists or not,

the `finally` block executes.

> **Note:** In real applications, if the file is opened successfully, you should call `file.close()` inside the `finally` block (after checking that the file object exists).

---

# Program 7 – User Input Example

## Program

```python
try:

    age = int(input("Enter Age : "))

except ValueError:

    print("Invalid Age")

else:

    print("Age Accepted")

finally:

    print("Program Finished")
```

---

## Sample Output

```text
Enter Age : 25

Age Accepted

Program Finished
```

---

## Explanation

Valid input executes the `else` block,

and `finally` executes afterward.

---

# Program 8 – Multiple Exceptions with finally

## Program

```python
try:

    number = int(input("Enter Number : "))

    result = 100 / number

except ValueError:

    print("Invalid Number")

except ZeroDivisionError:

    print("Cannot Divide by Zero")

finally:

    print("Thank You")
```

---

## Sample Output

```text
Enter Number : 0

Cannot Divide by Zero

Thank You
```

---

# Program 9 – Nested try-finally

## Program

```python
try:

    print("Outer Try")

    try:

        print("Inner Try")

    finally:

        print("Inner Finally")

finally:

    print("Outer Finally")
```

---

## Output

```text
Outer Try

Inner Try

Inner Finally

Outer Finally
```

---

## Explanation

Each `finally` block executes before leaving its corresponding `try` block.

---

# Program 10 – Database Connection Simulation

## Program

```python
try:

    print("Database Connected")

    print("Executing Query")

except Exception:

    print("Database Error")

finally:

    print("Database Connection Closed")
```

---

## Output

```text
Database Connected

Executing Query

Database Connection Closed
```

---

## Explanation

Database connections should always be closed,

even if an exception occurs.

The `finally` block ensures proper cleanup.

---

# Dry Run

```text
Enter try Block

↓

Execute Statements

↓

Exception?

↓

No

↓

Execute else

↓

Execute finally

↓

Program Ends

-------------------------

Yes

↓

Execute except

↓

Execute finally

↓

Program Ends
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

No

↓

else

↓

finally

↓

Program Ends

------------------------

Yes

↓

except

↓

finally

↓

Program Ends
```

---

# Advantages

- Separates successful execution from exception handling.
- Ensures cleanup code always executes.
- Prevents resource leaks.
- Improves reliability.
- Makes code easier to understand.

---

# Best Practices

- Use `else` for statements that should execute only after successful completion of the `try` block.
- Use `finally` to release resources such as files, database connections, and network sockets.
- Keep cleanup code inside `finally`.
- Avoid placing unrelated business logic inside `finally`.
- Handle only expected exceptions.

---

# Common Mistakes

## Mistake 1

Using `else` for exception handling.

The `else` block is executed only when no exception occurs.

---

## Mistake 2

Forgetting to release resources.

Always use `finally` (or a context manager such as `with`) when appropriate.

---

## Mistake 3

Putting cleanup code inside the `try` block.

If an exception occurs,

cleanup statements may never execute.

---

## Mistake 4

Assuming `finally` executes only when an exception occurs.

The `finally` block executes whether an exception occurs or not.

---

# Interview Questions

## 1. What is the purpose of the `else` block?

### Answer

It executes only when the `try` block completes successfully without raising an exception.

---

## 2. What is the purpose of the `finally` block?

### Answer

It always executes and is primarily used for cleanup operations.

---

## 3. Can a `try` block have both `else` and `finally`?

### Answer

Yes.

A single `try` statement can contain both.

---

## 4. Does the `finally` block execute if an exception occurs?

### Answer

Yes.

The `finally` block executes regardless of whether an exception occurs.

---

## 5. Is the `else` block mandatory?

### Answer

No.

It is optional.

---

## 6. Is the `finally` block mandatory?

### Answer

No.

It is optional, but highly recommended for resource cleanup.

---

## 7. Which block is commonly used to close files?

### Answer

The `finally` block.

---

# Practice Programs

1. Demonstrate `try-except-else`.
2. Demonstrate `try-finally`.
3. Demonstrate `try-except-finally`.
4. Handle file opening using `finally`.
5. Simulate database connection cleanup using `finally`.

---

# Quick Revision

- `else` executes only if no exception occurs.
- `finally` always executes.
- `finally` is used for cleanup operations.
- `else` is used for success logic.
- `try-except-else-finally` provides complete exception handling.

---

# Chapter Summary

In this chapter, we learned:

- else Block
- finally Block
- try-except-else
- try-finally
- try-except-finally
- Complete execution flow
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
