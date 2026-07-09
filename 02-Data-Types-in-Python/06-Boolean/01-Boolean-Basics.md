# Boolean (`bool`) - Basics

## Introduction

A **Boolean (`bool`)** is one of Python's built-in **numeric data types** used to represent **logical values**.

A Boolean value can have only one of two possible values:

* `True`
* `False`

Boolean values are fundamental to programming because they control the flow of execution in decision-making, loops, comparisons, and logical expressions.

In Python, the `bool` data type is a subclass of the `int` data type, where:

* `True` behaves like `1`
* `False` behaves like `0`

Although `True` and `False` are internally related to integers, they should always be used to represent logical conditions rather than numeric values.

---

# Definition

A **Boolean (`bool`)** is a built-in data type that stores one of two logical values:

* `True`
* `False`

These values are primarily used to represent the result of conditions, comparisons, and logical operations.

---

# Syntax

```python
variable_name = True

variable_name = False
```

---

## Examples

```python
is_student = True

is_logged_in = False

payment_success = True

email_verified = False
```

---

# Boolean Examples

```python
True

False
```

---

# Why Do We Use Boolean?

Boolean values are used whenever a program needs to determine whether a condition is true or false.

Typical uses include:

* Decision making
* Login verification
* User authentication
* Form validation
* Permission checking
* Loop control
* Conditional execution

---

# Real-World Applications

| Scenario           | Boolean Value |
| ------------------ | ------------- |
| User Logged In     | True          |
| Payment Successful | True          |
| Email Verified     | False         |
| Student Passed     | True          |
| Account Active     | True          |
| File Exists        | False         |
| Admin Access       | True          |
| Product Available  | False         |

---

# Memory Representation

Example

```python
is_student = True
```

```text
      is_student
           │
           ▼
+----------------------+
|     True (bool)      |
+----------------------+
```

The variable stores a reference to the Boolean object in memory.

---

# Program

```python
is_student = True

is_logged_in = False

print("Student :", is_student)

print("Logged In :", is_logged_in)
```

---

# Output

```text
Student : True

Logged In : False
```

---

# Dry Run

```text
Step 1

is_student = True

is_logged_in = False

↓

Step 2

Print is_student

Output → True

↓

Step 3

Print is_logged_in

Output → False
```

---

# Pseudocode

```text
START

Create Boolean variable is_student

Assign True

Create Boolean variable is_logged_in

Assign False

Display both variables

STOP
```

---

# Line-by-Line Explanation

### Line 1

```python
is_student = True
```

Creates a Boolean object with the value `True` and stores its reference in the variable `is_student`.

---

### Line 2

```python
is_logged_in = False
```

Creates a Boolean object with the value `False` and stores its reference in the variable `is_logged_in`.

---

### Lines 3–4

The `print()` function displays the Boolean values stored in the variables.

---

# Characteristics of Boolean

* Stores only two values: `True` and `False`.
* Used for logical operations and decision making.
* Immutable data type.
* Automatically returned by comparison operators.
* Can participate in arithmetic because `bool` is a subclass of `int`.
* Frequently used with `if`, `elif`, `else`, and loops.

---

# Boolean Values in Python

Python recognizes only two Boolean constants.

| Value   | Meaning           |
| ------- | ----------------- |
| `True`  | Logical truth     |
| `False` | Logical falsehood |

Boolean values are case-sensitive.

Correct:

```python
True

False
```

Incorrect:

```python
true

false
TRUE
FALSE
```

These incorrect forms raise a `NameError`.

---

# Built-in Functions

Python provides several built-in functions for working with Boolean values.

| Function | Description                 |
| -------- | --------------------------- |
| `bool()` | Converts a value to Boolean |
| `type()` | Returns the data type       |
| `int()`  | Converts Boolean to integer |
| `str()`  | Converts Boolean to string  |

---

## Example

```python
print(bool(1))

print(bool(0))

print(int(True))

print(int(False))

print(type(True))
```

---

## Output

```text
True

False

1

0

<class 'bool'>
```

---

# Summary

In this chapter, you learned:

* Introduction to Boolean
* Definition
* Syntax
* Examples
* Why Boolean is used
* Real-world applications
* Memory representation
* Program and output
* Dry run
* Pseudocode
* Line-by-line explanation
* Characteristics
* Boolean values
* Built-in functions

In the next chapter, you will learn **Boolean Operations**, including comparison operators, logical operators, truth values, Boolean conversion rules, and practical examples.
