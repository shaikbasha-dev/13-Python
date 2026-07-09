# Arithmetic Operators in Python

## Learning Objectives

After completing this chapter, you will be able to:

- Understand Arithmetic Operators.
- Explain why arithmetic operators are used.
- Learn all arithmetic operators in Python.
- Perform mathematical calculations.
- Write programs using arithmetic operators.
- Understand operator precedence in arithmetic expressions.

---

# Introduction

Arithmetic operators are one of the most frequently used operators in Python.

They are used to perform mathematical calculations on numbers.

Examples include:

- Addition
- Subtraction
- Multiplication
- Division
- Finding the remainder
- Calculating powers
- Floor division

Arithmetic operators are widely used in banking applications, billing software, scientific calculations, payroll systems, and engineering applications.

---

# Definition

**Arithmetic Operators** are special symbols used to perform mathematical operations on numeric values.

Example

```python
a = 20
b = 10

print(a + b)
```

Output

```text
30
```

Here,

- `+` is the arithmetic operator.
- `20` and `10` are operands.

---

# Why do we use Arithmetic Operators?

Arithmetic operators are used to:

- Perform mathematical calculations.
- Calculate totals.
- Find averages.
- Calculate discounts.
- Compute salaries.
- Perform scientific calculations.

---

# Types of Arithmetic Operators

| Operator | Name | Example |
|----------|------|----------|
| + | Addition | a + b |
| - | Subtraction | a - b |
| * | Multiplication | a * b |
| / | Division | a / b |
| // | Floor Division | a // b |
| % | Modulus | a % b |
| ** | Exponent | a ** b |

---

# 1. Addition Operator (+)

## Definition

The Addition operator adds two operands.

### Program

```python
a = 25
b = 15

print("Addition :", a + b)
```

### Output

```text
Addition : 40
```

---

# 2. Subtraction Operator (-)

## Definition

The Subtraction operator subtracts one operand from another.

### Program

```python
a = 25
b = 15

print("Subtraction :", a - b)
```

### Output

```text
Subtraction : 10
```

---

# 3. Multiplication Operator (*)

## Definition

The Multiplication operator multiplies two operands.

### Program

```python
a = 25
b = 15

print("Multiplication :", a * b)
```

### Output

```text
Multiplication : 375
```

---

# 4. Division Operator (/)

## Definition

The Division operator divides one operand by another and always returns a float value.

### Program

```python
a = 25
b = 5

print("Division :", a / b)
```

### Output

```text
Division : 5.0
```

---

# 5. Floor Division Operator (//)

## Definition

The Floor Division operator returns the quotient without the decimal part.

### Program

```python
a = 25
b = 4

print("Floor Division :", a // b)
```

### Output

```text
Floor Division : 6
```

---

# 6. Modulus Operator (%)

## Definition

The Modulus operator returns the remainder after division.

### Program

```python
a = 25
b = 4

print("Remainder :", a % b)
```

### Output

```text
Remainder : 1
```

---

# 7. Exponent Operator (**)

## Definition

The Exponent operator calculates the power of a number.

### Program

```python
a = 5

print("Square :", a ** 2)

print("Cube :", a ** 3)
```

### Output

```text
Square : 25

Cube : 125
```

---

# Program 1: Perform All Arithmetic Operations

## Problem Statement

Write a Python program to perform all arithmetic operations on two numbers.

---

## Program

```python
# Store two numbers
a = 20
b = 6

print("Addition :", a + b)
print("Subtraction :", a - b)
print("Multiplication :", a * b)
print("Division :", a / b)
print("Floor Division :", a // b)
print("Modulus :", a % b)
print("Exponent :", a ** b)
```

---

## Output

```text
Addition : 26
Subtraction : 14
Multiplication : 120
Division : 3.3333333333333335
Floor Division : 3
Modulus : 2
Exponent : 64000000
```

---

## Pseudocode

```text
START

Create two variables

Perform all arithmetic operations

Display the results

STOP
```

---

## Line-by-Line Explanation

### Line 1

```python
a = 20
b = 6
```

Stores two integer values.

---

### Line 2 onwards

Each `print()` statement performs one arithmetic operation and displays the result.

---

# Operator Precedence

Arithmetic operators follow the following precedence.

```text
()

**

*, /, //, %

+, -
```

Example

```python
result = 10 + 5 * 2

print(result)
```

Output

```text
20
```

Explanation

Multiplication is performed before addition.

---

# Real-Time Applications

Arithmetic operators are used in:

- Banking Applications
- Payroll Systems
- Billing Software
- Shopping Applications
- Student Result Processing
- Scientific Calculations
- Engineering Software

---

# Advantages

- Easy mathematical calculations.
- Reduces coding effort.
- Improves readability.
- Supports complex calculations.

---

# Common Mistakes

## Confusing / and //

```python
print(10 / 3)
```

Output

```text
3.3333333333333335
```

```python
print(10 // 3)
```

Output

```text
3
```

---

## Division by Zero

```python
print(10 / 0)
```

Output

```text
ZeroDivisionError
```

---

# Interview Questions

## 1. What are Arithmetic Operators?

### Answer

Arithmetic operators perform mathematical operations on numeric values.

---

## 2. Which operator returns the remainder?

### Answer

The Modulus operator (`%`).

---

## 3. What is the difference between `/` and `//`?

### Answer

- `/` returns the actual division result (float).
- `//` returns the floor division result (integer quotient).

---

## 4. Which operator calculates power?

### Answer

The Exponent operator (`**`).

---

## 5. What happens when a number is divided by zero?

### Answer

Python raises a `ZeroDivisionError`.

---

# Quick Revision

- `+` → Addition
- `-` → Subtraction
- `*` → Multiplication
- `/` → Division
- `//` → Floor Division
- `%` → Modulus
- `**` → Exponent

---

# Summary

In this chapter, you learned:

- What Arithmetic Operators are.
- Types of Arithmetic Operators.
- Syntax and examples.
- Practical programs.
- Operator precedence.
- Real-world applications.
- Common mistakes.
- Interview questions.
