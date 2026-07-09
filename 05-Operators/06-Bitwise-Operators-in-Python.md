# Bitwise Operators in Python

## Learning Objectives

After completing this chapter, you will be able to:

- Understand Bitwise Operators.
- Explain why bitwise operators are used.
- Learn binary representation of numbers.
- Perform bitwise operations.
- Write programs using bitwise operators.
- Understand left shift and right shift operations.

---

# Introduction

Bitwise Operators perform operations directly on the **binary representation** (bits) of numbers.

Every integer inside a computer is stored in the form of **0s and 1s**.

Bitwise operators manipulate these bits to produce a new result.

They are mainly used in:

- System Programming
- Embedded Systems
- Networking
- Cryptography
- Device Drivers
- Performance Optimization

---

# Definition

A **Bitwise Operator** performs operations on the binary representation of integer values.

Python provides six bitwise operators.

---

# Why do we use Bitwise Operators?

Bitwise operators help to:

- Perform binary calculations.
- Manipulate bits.
- Optimize memory usage.
- Improve execution speed.
- Work with hardware devices.

---

# Binary Representation

Before learning bitwise operators, understand binary numbers.

Example

```text
Decimal      Binary

5            0101

3            0011
```

---

# Types of Bitwise Operators

| Operator | Name |
|----------|------|
| & | Bitwise AND |
| \| | Bitwise OR |
| ^ | Bitwise XOR |
| ~ | Bitwise NOT |
| << | Left Shift |
| >> | Right Shift |

---

# 1. Bitwise AND (&)

## Definition

Returns **1** only if both corresponding bits are **1**.

---

### Example

```text
5 = 0101

3 = 0011

--------------

& = 0001

--------------

Result = 1
```

### Program

```python
a = 5
b = 3

print(a & b)
```

### Output

```text
1
```

---

# 2. Bitwise OR (|)

## Definition

Returns **1** if at least one corresponding bit is **1**.

---

### Example

```text
5 = 0101

3 = 0011

--------------

| = 0111

--------------

Result = 7
```

### Program

```python
a = 5
b = 3

print(a | b)
```

### Output

```text
7
```

---

# 3. Bitwise XOR (^)

## Definition

Returns **1** only when corresponding bits are different.

---

### Example

```text
5 = 0101

3 = 0011

--------------

^ = 0110

--------------

Result = 6
```

### Program

```python
a = 5
b = 3

print(a ^ b)
```

### Output

```text
6
```

---

# 4. Bitwise NOT (~)

## Definition

Reverses every bit of the number.

---

### Program

```python
number = 5

print(~number)
```

### Output

```text
-6
```

---

### Explanation

Python calculates

```text
~n = -(n + 1)
```

Therefore,

```text
~5 = -(5 + 1)

= -6
```

---

# 5. Left Shift (<<)

## Definition

Moves all bits towards the left by the specified number of positions.

Each left shift multiplies the value by **2**.

---

### Example

```text
5 = 00000101

5 << 1

00001010

Result = 10
```

### Program

```python
print(5 << 1)
```

### Output

```text
10
```

---

# 6. Right Shift (>>)

## Definition

Moves all bits towards the right.

Each right shift divides the value by **2**.

---

### Example

```text
20 = 00010100

20 >> 2

00000101

Result = 5
```

### Program

```python
print(20 >> 2)
```

### Output

```text
5
```

---

# Program 1: Demonstrate All Bitwise Operators

## Problem Statement

Write a Python program to demonstrate all Bitwise Operators.

---

## Program

```python
a = 5
b = 3

print("AND :", a & b)
print("OR :", a | b)
print("XOR :", a ^ b)
print("NOT :", ~a)
print("LEFT SHIFT :", a << 1)
print("RIGHT SHIFT :", a >> 1)
```

---

## Output

```text
AND : 1
OR : 7
XOR : 6
NOT : -6
LEFT SHIFT : 10
RIGHT SHIFT : 2
```

---

## Pseudocode

```text
START

Create two variables

Perform all bitwise operations

Display the results

STOP
```

---

# Real-Time Applications

Bitwise operators are used in:

- Operating Systems
- Embedded Systems
- Computer Networks
- Image Processing
- Encryption Algorithms
- Device Drivers

---

# Advantages

- Faster execution.
- Efficient memory usage.
- Useful in low-level programming.
- Direct manipulation of binary data.

---

# Difference between Logical and Bitwise Operators

| Logical Operators | Bitwise Operators |
|-------------------|-------------------|
| Work with Boolean values | Work with binary bits |
| Return True or False | Return integer values |
| Used in conditions | Used for bit manipulation |

---

# Common Mistakes

## Using Bitwise Operators Instead of Logical Operators

❌ Incorrect

```python
if True & False:
    print("Hello")
```

Although this works with Boolean values, logical operators (`and`, `or`, `not`) should be used for conditions.

---

## Confusing XOR with OR

```text
5 = 0101

3 = 0011

OR  = 0111 = 7

XOR = 0110 = 6
```

Remember:

- OR returns 1 if either bit is 1.
- XOR returns 1 only if the bits are different.

---

# Interview Questions

## 1. What are Bitwise Operators?

### Answer

Bitwise operators perform operations on the binary representation of integers.

---

## 2. How many Bitwise Operators are available in Python?

### Answer

Six:

- &
- |
- ^
- ~
- <<
- >>

---

## 3. What does the Bitwise AND operator do?

### Answer

It returns 1 only when both corresponding bits are 1.

---

## 4. What is the purpose of the Left Shift operator?

### Answer

It shifts bits to the left and effectively multiplies the value by 2 for each shift position.

---

## 5. Why does `~5` return `-6`?

### Answer

Python evaluates the bitwise NOT using the formula:

```text
~n = -(n + 1)
```

Therefore,

```text
~5 = -6
```

---

# Quick Revision

- `&` → Bitwise AND
- `|` → Bitwise OR
- `^` → Bitwise XOR
- `~` → Bitwise NOT
- `<<` → Left Shift
- `>>` → Right Shift
- Bitwise operators work on binary numbers.

---

# Summary

In this chapter, you learned:

- What Bitwise Operators are.
- Binary representation.
- Types of Bitwise Operators.
- Practical examples.
- Real-world applications.
- Difference between logical and bitwise operators.
- Common mistakes.
- Interview questions.
