# Integer (`int`) - Part 1

## Introduction

An **Integer (`int`)** is one of Python's built-in **numeric data types** used to store **whole numbers**. Unlike floating-point numbers, integers do not contain a decimal point.

Integers are one of the most commonly used data types in Python because many real-world values such as age, marks, salary, quantity, population, and roll numbers are represented as whole numbers.

Unlike many programming languages, Python supports integers of **unlimited size**, limited only by the available system memory.

---

# Definition

An **Integer (`int`)** is a built-in numeric data type used to store **positive numbers, negative numbers, and zero without any fractional (decimal) part**.

---

# Syntax

```python
variable_name = integer_value
```

## Examples

```python
age = 21

marks = 95

temperature = -10

count = 0

population = 1450000000
```

---

# Integer Examples

```python
100

250

0

-50

99999

-999999
```

---

# Why Do We Use Integer?

The `int` data type is used whenever a program needs to store **whole numbers**.

Integers are ideal for:

* Counting values
* Performing arithmetic calculations
* Storing identifiers
* Managing indexes
* Representing quantities

Since integers do not contain decimal values, they are more suitable than floating-point numbers for whole-number calculations.

---

# Real-World Applications

| Scenario            | Example    |
| ------------------- | ---------- |
| Student Age         | 21         |
| Roll Number         | 101        |
| Number of Employees | 250        |
| Product Quantity    | 500        |
| Population          | 1450000000 |
| Mobile OTP          | 548921     |
| Invoice Number      | 10025      |
| Number of Books     | 350        |

---

# Memory Representation

Example

```python
age = 21
```

```text
        age
         │
         ▼
+----------------------+
|      21 (int)        |
+----------------------+
```

The variable stores a **reference** to the integer object rather than storing the actual value directly.

---

# Program

```python
# Integer variables

age = 21

marks = 95

employees = 250

print("Age :", age)

print("Marks :", marks)

print("Employees :", employees)
```

---

# Output

```text
Age : 21

Marks : 95

Employees : 250
```

---

# Dry Run

```text
Step 1

age = 21

marks = 95

employees = 250

↓

Step 2

Print age

Output → 21

↓

Step 3

Print marks

Output → 95

↓

Step 4

Print employees

Output → 250
```

---

# Pseudocode

```text
START

Create integer variable age

Assign value 21

Create integer variable marks

Assign value 95

Create integer variable employees

Assign value 250

Display all variables

STOP
```

---

# Line-by-Line Explanation

### Line 1

```python
age = 21
```

Creates an integer object with value **21** and stores its reference in the variable `age`.

---

### Line 2

```python
marks = 95
```

Creates an integer object with value **95** and stores its reference in the variable `marks`.

---

### Line 3

```python
employees = 250
```

Creates an integer object with value **250** and stores its reference in the variable `employees`.

---

### Lines 4–6

The `print()` function displays the values stored in the variables.

---

# Characteristics of Integer

* Stores whole numbers.
* Stores positive values.
* Stores negative values.
* Stores zero.
* Does not store decimal values.
* Immutable data type.
* Supports arithmetic operations.
* Supports comparison operations.
* Supports bitwise operations.
* Python automatically identifies integer values.
* Integer size is not fixed in Python.

---

# Integer Literals

Python supports integers in multiple number systems.

| Number System | Prefix | Example  | Decimal Value |
| ------------- | ------ | -------- | ------------- |
| Decimal       | None   | `100`    | 100           |
| Binary        | `0b`   | `0b1010` | 10            |
| Octal         | `0o`   | `0o17`   | 15            |
| Hexadecimal   | `0x`   | `0x2A`   | 42            |

---

## Example

```python
decimal_number = 100

binary_number = 0b1010

octal_number = 0o17

hexadecimal_number = 0x2A

print(decimal_number)

print(binary_number)

print(octal_number)

print(hexadecimal_number)
```

---

## Output

```text
100

10

15

42
```

---

# Built-in Functions

Python provides several built-in functions to work with integers.

| Function   | Description                        |
| ---------- | ---------------------------------- |
| `int()`    | Converts a value into an integer   |
| `abs()`    | Returns the absolute value         |
| `bin()`    | Converts an integer to binary      |
| `oct()`    | Converts an integer to octal       |
| `hex()`    | Converts an integer to hexadecimal |
| `pow()`    | Returns the power of a number      |
| `divmod()` | Returns quotient and remainder     |
| `type()`   | Returns the data type              |

---

## Example

```python
number = -25

print(abs(number))

print(bin(10))

print(oct(10))

print(hex(255))

print(pow(2,5))

print(divmod(17,5))

print(type(number))
```

---

## Output

```text
25

0b1010

0o12

0xff

32

(3, 2)

<class 'int'>
```

---

# Summary

In this part, you learned:

* Introduction to Integer
* Definition
* Syntax
* Examples
* Real-world applications
* Memory representation
* Program and output
* Dry run
* Pseudocode
* Line-by-line explanation
* Characteristics
* Integer literals
* Built-in functions

In **Part 2**, you will learn arithmetic operations, comparison operators, assignment operators, bitwise operators, type conversion, internal working, memory management, integer caching, and immutability.
