# Assignment Operators in Python

## Learning Objectives

After completing this chapter, you will be able to:

- Understand Assignment Operators.
- Explain why assignment operators are used.
- Learn different assignment operators.
- Perform compound assignments.
- Write programs using assignment operators.
- Understand the advantages of compound assignments.

---

# Introduction

Assignment operators are used to assign values to variables.

Besides assigning values, Python also provides **compound assignment operators** that perform an operation and assignment in a single statement.

For example,

Instead of writing

```python
x = x + 5
```

we can write

```python
x += 5
```

This makes the code shorter, cleaner, and easier to understand.

---

# Definition

An **Assignment Operator** is an operator used to assign a value or the result of an expression to a variable.

---

# Why do we use Assignment Operators?

Assignment operators are used to:

- Store values in variables.
- Update variable values.
- Simplify mathematical operations.
- Reduce code length.
- Improve readability.

---

# Types of Assignment Operators

| Operator | Description | Example |
|----------|-------------|---------|
| = | Assign | x = 10 |
| += | Add and Assign | x += 5 |
| -= | Subtract and Assign | x -= 5 |
| *= | Multiply and Assign | x *= 5 |
| /= | Divide and Assign | x /= 5 |
| //= | Floor Divide and Assign | x //= 5 |
| %= | Modulus and Assign | x %= 5 |
| **= | Exponent and Assign | x **= 2 |

---

# 1. Assignment Operator (=)

## Definition

Assigns a value to a variable.

### Program

```python
number = 100

print(number)
```

### Output

```text
100
```

---

# 2. Addition Assignment Operator (+=)

## Definition

Adds the right operand to the left operand and stores the result.

### Program

```python
number = 20

number += 10

print(number)
```

### Output

```text
30
```

---

# 3. Subtraction Assignment Operator (-=)

## Definition

Subtracts the right operand from the left operand and stores the result.

### Program

```python
number = 20

number -= 5

print(number)
```

### Output

```text
15
```

---

# 4. Multiplication Assignment Operator (*=)

## Definition

Multiplies the variable by a value and stores the result.

### Program

```python
number = 10

number *= 5

print(number)
```

### Output

```text
50
```

---

# 5. Division Assignment Operator (/=)

## Definition

Divides the variable by a value and stores the result.

### Program

```python
number = 20

number /= 4

print(number)
```

### Output

```text
5.0
```

---

# 6. Floor Division Assignment Operator (//=)

## Definition

Performs floor division and stores the result.

### Program

```python
number = 25

number //= 4

print(number)
```

### Output

```text
6
```

---

# 7. Modulus Assignment Operator (%=)

## Definition

Stores the remainder after division.

### Program

```python
number = 25

number %= 4

print(number)
```

### Output

```text
1
```

---

# 8. Exponent Assignment Operator (**=)

## Definition

Raises the variable to the specified power and stores the result.

### Program

```python
number = 5

number **= 2

print(number)
```

### Output

```text
25
```

---

# Program 1: Demonstrate All Assignment Operators

## Problem Statement

Write a Python program to demonstrate all assignment operators.

---

## Program

```python
number = 20

print("Original Value :", number)

number += 5
print("After += :", number)

number -= 3
print("After -= :", number)

number *= 2
print("After *= :", number)

number /= 4
print("After /= :", number)

number //= 2
print("After //= :", number)

number %= 3
print("After %= :", number)

number **= 2
print("After **= :", number)
```

---

## Output

```text
Original Value : 20
After += : 25
After -= : 22
After *= : 44
After /= : 11.0
After //= : 5.0
After %= : 2.0
After **= : 4.0
```

---

## Pseudocode

```text
START

Create variable

Apply each assignment operator

Display the updated value

STOP
```

---

## Line-by-Line Explanation

Each assignment operator performs an operation and immediately stores the updated result back into the same variable.

---

# Real-Time Applications

Assignment operators are commonly used in:

- Banking Applications
- Shopping Cart Systems
- Payroll Software
- Student Result Processing
- Inventory Management
- Scientific Calculations

---

# Advantages

- Reduces code length.
- Improves readability.
- Makes code easier to maintain.
- Performs assignment and operation in one step.

---

# Difference between = and +=

| = | += |
|---|----|
| Assigns a new value | Adds and updates the existing value |
| Example: x = 10 | Example: x += 5 |

---

# Common Mistakes

## Using = instead of ==

❌ Incorrect

```python
if number = 10:
    print(number)
```

Output

```text
SyntaxError
```

---

✅ Correct

```python
if number == 10:
    print(number)
```

---

## Forgetting Compound Assignment Updates the Variable

```python
number = 10

number += 5

print(number)
```

Output

```text
15
```

The original value is updated.

---

# Interview Questions

## 1. What are Assignment Operators?

### Answer

Assignment operators assign values or expression results to variables.

---

## 2. What is the purpose of += ?

### Answer

It adds a value to the existing variable and stores the updated result.

---

## 3. What is the difference between = and += ?

### Answer

- `=` assigns a value.
- `+=` adds a value and updates the variable.

---

## 4. Name all Assignment Operators.

### Answer

- =
- +=
- -=
- *=
- /=
- //=
- %=
- **=

---

## 5. Why are Assignment Operators useful?

### Answer

They reduce code length, improve readability, and make programs easier to maintain.

---

# Quick Revision

- `=` → Assign
- `+=` → Add and Assign
- `-=` → Subtract and Assign
- `*=` → Multiply and Assign
- `/=` → Divide and Assign
- `//=` → Floor Divide and Assign
- `%=` → Modulus and Assign
- `**=` → Exponent and Assign

---

# Summary

In this chapter, you learned:

- What Assignment Operators are.
- Types of Assignment Operators.
- Practical examples.
- Compound assignments.
- Real-world applications.
- Common mistakes.
- Interview questions.

