# Comparison (Relational) Operators in Python

## Learning Objectives

After completing this chapter, you will be able to:

- Understand Comparison Operators.
- Explain why comparison operators are used.
- Learn all comparison operators.
- Compare different values.
- Write programs using comparison operators.
- Understand Boolean results.

---

# Introduction

Comparison Operators are used to compare two values.

The result of every comparison is either:

- True
- False

These operators are mainly used in:

- if statements
- while loops
- Decision making
- Login validation
- Eligibility checking

Without comparison operators, programs cannot make decisions.

---

# Definition

A **Comparison (Relational) Operator** compares two operands and returns a Boolean value (`True` or `False`).

Example

```python
a = 20
b = 15

print(a > b)
```

Output

```text
True
```

---

# Why do we use Comparison Operators?

Comparison operators help to:

- Compare two values.
- Make decisions.
- Control program flow.
- Validate user input.
- Check conditions.

---

# Types of Comparison Operators

| Operator | Description | Example |
|----------|-------------|---------|
| == | Equal to | a == b |
| != | Not Equal to | a != b |
| > | Greater than | a > b |
| < | Less than | a < b |
| >= | Greater than or Equal to | a >= b |
| <= | Less than or Equal to | a <= b |

---

# 1. Equal To (==)

## Definition

Returns **True** if both operands are equal.

### Program

```python
a = 10
b = 10

print(a == b)
```

### Output

```text
True
```

---

# 2. Not Equal To (!=)

## Definition

Returns **True** if both operands are different.

### Program

```python
a = 10
b = 20

print(a != b)
```

### Output

```text
True
```

---

# 3. Greater Than (>)

## Definition

Returns **True** if the left operand is greater than the right operand.

### Program

```python
a = 25
b = 15

print(a > b)
```

### Output

```text
True
```

---

# 4. Less Than (<)

## Definition

Returns **True** if the left operand is smaller than the right operand.

### Program

```python
a = 10
b = 25

print(a < b)
```

### Output

```text
True
```

---

# 5. Greater Than or Equal To (>=)

## Definition

Returns **True** if the left operand is greater than or equal to the right operand.

### Program

```python
marks = 75

print(marks >= 35)
```

### Output

```text
True
```

---

# 6. Less Than or Equal To (<=)

## Definition

Returns **True** if the left operand is less than or equal to the right operand.

### Program

```python
age = 18

print(age <= 25)
```

### Output

```text
True
```

---

# Program 1: Demonstrate All Comparison Operators

## Problem Statement

Write a Python program to demonstrate all comparison operators.

---

## Program

```python
a = 20
b = 10

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)
```

---

## Output

```text
a == b : False
a != b : True
a > b  : True
a < b  : False
a >= b : True
a <= b : False
```

---

## Pseudocode

```text
START

Create two variables

Compare using all comparison operators

Display the results

STOP
```

---

## Line-by-Line Explanation

### Line 1

```python
a = 20
b = 10
```

Creates two integer variables.

---

### Remaining Lines

Each `print()` statement compares the two values and displays either `True` or `False`.

---

# Boolean Result

Comparison operators always return a Boolean value.

Example

```python
print(15 > 5)
print(15 == 5)
```

Output

```text
True
False
```

---

# Real-Time Applications

Comparison operators are used in:

- Login Authentication
- ATM Applications
- Banking Software
- Online Examinations
- Student Result Systems
- Age Verification
- E-Commerce Websites

---

# Advantages

- Supports decision making.
- Controls program execution.
- Produces Boolean values.
- Easy to understand and use.

---

# Difference between = and ==

| = | == |
|---|----|
| Assignment Operator | Comparison Operator |
| Assigns value | Compares values |
| Does not return True/False | Returns True or False |

---

# Common Mistakes

## Using = Instead of ==

❌ Incorrect

```python
if age = 18:
    print("Eligible")
```

Output

```text
SyntaxError
```

---

✅ Correct

```python
if age == 18:
    print("Eligible")
```

---

## Comparing Different Data Types

```python
print(10 == "10")
```

Output

```text
False
```

Reason:

One value is an integer and the other is a string.

---

# Interview Questions

## 1. What are Comparison Operators?

### Answer

Comparison operators compare two values and return either `True` or `False`.

---

## 2. How many Comparison Operators are available in Python?

### Answer

Six:

- ==
- !=
- >
- <
- >=
- <=

---

## 3. What is the return type of Comparison Operators?

### Answer

Boolean (`True` or `False`).

---

## 4. What is the difference between = and ==?

### Answer

- `=` assigns a value.
- `==` compares two values.

---

## 5. Can Comparison Operators compare strings?

### Answer

Yes.

Example

```python
print("Apple" == "Apple")
```

Output

```text
True
```

---

# Quick Revision

- `==` → Equal To
- `!=` → Not Equal To
- `>` → Greater Than
- `<` → Less Than
- `>=` → Greater Than or Equal To
- `<=` → Less Than or Equal To
- Always returns `True` or `False`.

---

# Summary

In this chapter, you learned:

- What Comparison Operators are.
- Types of Comparison Operators.
- Practical examples.
- Boolean results.
- Real-world applications.
- Common mistakes.
- Interview questions.
