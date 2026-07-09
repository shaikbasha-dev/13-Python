# Complex (`complex`) - Basics

## Introduction

A **Complex (`complex`)** is one of Python's built-in **numeric data types** used to represent **complex numbers**.

A complex number consists of two parts:

* **Real Part**
* **Imaginary Part**

In Python, the imaginary part is represented using the letter **`j`** instead of **`i`**, which is commonly used in mathematics.

Complex numbers are widely used in scientific computing, electrical engineering, signal processing, control systems, robotics, and advanced mathematical calculations.

---

# Definition

A **Complex (`complex`)** is a built-in numeric data type that stores a number containing both a **real part** and an **imaginary part**.

The general form of a complex number is:

```text
a + bj
```

Where:

* `a` → Real Part
* `b` → Imaginary Part
* `j` → Imaginary Unit (`√-1`)

---

# Syntax

```python
variable_name = real + imaginaryj
```

---

## Examples

```python
number1 = 5 + 3j

number2 = 10 - 2j

number3 = -4 + 7j

number4 = 8j

number5 = 15 + 0j
```

---

# Complex Number Examples

```python
5 + 3j

10 - 2j

2j

-8 + 6j

7 + 0j
```

---

# Why Do We Use Complex Numbers?

Complex numbers are used whenever calculations involve **imaginary numbers**.

They are essential in fields where mathematical models require both real and imaginary components.

---

# Real-World Applications

| Field                  | Application               |
| ---------------------- | ------------------------- |
| Electrical Engineering | AC Circuit Analysis       |
| Signal Processing      | Waveform Analysis         |
| Robotics               | Control Systems           |
| Physics                | Quantum Mechanics         |
| Scientific Computing   | Numerical Simulations     |
| Telecommunications     | Digital Signal Processing |
| Aerospace              | Flight Control Systems    |
| Mathematics            | Complex Analysis          |

---

# Memory Representation

Example

```python
number = 5 + 3j
```

```text
        number
           │
           ▼
+---------------------------+
|      5 + 3j (complex)     |
+---------------------------+
```

The variable stores a reference to the complex object in memory.

---

# Program

```python
number1 = 5 + 3j

number2 = 8 - 2j

print("Number 1 :", number1)

print("Number 2 :", number2)
```

---

# Output

```text
Number 1 : (5+3j)

Number 2 : (8-2j)
```

---

# Dry Run

```text
Step 1

number1 = 5 + 3j

number2 = 8 - 2j

↓

Step 2

Print number1

Output → (5+3j)

↓

Step 3

Print number2

Output → (8-2j)
```

---

# Pseudocode

```text
START

Create complex variable number1

Assign value 5 + 3j

Create complex variable number2

Assign value 8 - 2j

Display both variables

STOP
```

---

# Line-by-Line Explanation

### Line 1

```python
number1 = 5 + 3j
```

Creates a complex object containing a real part (`5`) and an imaginary part (`3j`).

---

### Line 2

```python
number2 = 8 - 2j
```

Creates another complex object with real part `8` and imaginary part `-2j`.

---

### Lines 3–4

The `print()` function displays the values stored in both variables.

---

# Characteristics of Complex Numbers

* Stores real and imaginary values together.
* Uses `j` to represent the imaginary unit.
* Immutable data type.
* Supports arithmetic operations.
* Automatically recognized by Python.
* Belongs to the numeric data type family.
* Useful for scientific and engineering computations.

---

# Creating Complex Numbers

Complex numbers can be created in multiple ways.

## Method 1: Direct Assignment

```python
number = 5 + 3j
```

---

## Method 2: Using the `complex()` Function

```python
number = complex(5, 3)

print(number)
```

Output

```text
(5+3j)
```

---

# Built-in Functions

Python provides several built-in functions for working with complex numbers.

| Function    | Description                            |
| ----------- | -------------------------------------- |
| `complex()` | Creates a complex number               |
| `abs()`     | Returns the magnitude (absolute value) |
| `type()`    | Returns the data type                  |

---

## Example

```python
number = complex(3, 4)

print(number)

print(abs(number))

print(type(number))
```

---

## Output

```text
(3+4j)

5.0

<class 'complex'>
```

---

# Summary

In this chapter, you learned:

* Introduction to Complex numbers
* Definition
* Syntax
* Examples
* Why Complex numbers are used
* Real-world applications
* Memory representation
* Program and output
* Dry run
* Pseudocode
* Line-by-line explanation
* Characteristics
* Creating complex numbers
* Built-in functions

In the next chapter, you will learn **Complex Number Operations**, including arithmetic operations, comparison behavior, built-in attributes, type conversion, and practical examples.
