# Float (`float`) - Basics

## Introduction

A **Float (`float`)** is one of Python's built-in **numeric data types** used to store **decimal (floating-point) numbers**. Unlike integers, float values contain a decimal point, allowing Python to represent fractional values accurately.

Float values are commonly used in scientific calculations, financial applications, engineering, data analysis, and anywhere decimal precision is required.

Python follows the IEEE 754 standard for representing floating-point numbers internally.

---

# Definition

A **Float (`float`)** is a built-in numeric data type used to store numbers that contain a fractional (decimal) part.

A float can represent:

* Positive decimal numbers
* Negative decimal numbers
* Zero
* Scientific notation values

---

# Syntax

```python
variable_name = float_value
```

---

## Examples

```python
percentage = 91.5

price = 499.99

temperature = -10.8

pi = 3.1415926535

distance = 0.0
```

---

# Float Examples

```python
10.5

25.75

0.0

-35.8

999.999

3.14159
```

---

# Why Do We Use Float?

The `float` data type is used whenever a program needs to store decimal values.

Unlike integers, float values allow calculations involving fractions and measurements.

Typical use cases include:

* Product prices
* Student percentages
* Heights and weights
* Temperature readings
* Scientific calculations
* Interest rates

---

# Real-World Applications

| Scenario               | Example      |
| ---------------------- | ------------ |
| Student Percentage     | 91.5         |
| Product Price          | 499.99       |
| Bank Interest Rate     | 7.25         |
| Temperature            | 36.8         |
| Height                 | 175.5 cm     |
| Weight                 | 68.75 kg     |
| Fuel Quantity          | 25.40 Litres |
| Currency Exchange Rate | 83.52        |

---

# Memory Representation

Example

```python
price = 499.99
```

```text
        price
          │
          ▼
+-------------------------+
|     499.99 (float)      |
+-------------------------+
```

The variable stores a reference to the float object created in memory.

---

# Program

```python
# Float variables

percentage = 91.5

price = 499.99

temperature = 36.8

print("Percentage :", percentage)

print("Price :", price)

print("Temperature :", temperature)
```

---

# Output

```text
Percentage : 91.5

Price : 499.99

Temperature : 36.8
```

---

# Dry Run

```text
Step 1

percentage = 91.5

price = 499.99

temperature = 36.8

↓

Step 2

Print percentage

Output → 91.5

↓

Step 3

Print price

Output → 499.99

↓

Step 4

Print temperature

Output → 36.8
```

---

# Pseudocode

```text
START

Create float variable percentage

Assign 91.5

Create float variable price

Assign 499.99

Create float variable temperature

Assign 36.8

Display all values

STOP
```

---

# Line-by-Line Explanation

### Line 1

```python
percentage = 91.5
```

Creates a float object with the value **91.5** and stores its reference in the variable `percentage`.

---

### Line 2

```python
price = 499.99
```

Creates a float object with the value **499.99** and stores its reference in the variable `price`.

---

### Line 3

```python
temperature = 36.8
```

Creates a float object with the value **36.8** and stores its reference in the variable `temperature`.

---

### Lines 4–6

The `print()` function displays the values stored in the variables.

---

# Characteristics of Float

* Stores decimal numbers.
* Supports positive values.
* Supports negative values.
* Supports zero.
* Immutable data type.
* Supports arithmetic operations.
* Supports comparison operations.
* Supports scientific notation.
* Automatically recognized by Python.
* Follows the IEEE 754 floating-point standard.

---

# Floating-Point Literals

Python allows float values to be written in different formats.

## Decimal Notation

```python
price = 499.99
```

---

## Scientific Notation

```python
distance = 1.5e3

mass = 7.2e-4
```

---

### Example

```python
number1 = 2.5e2

number2 = 4.2e-3

print(number1)

print(number2)
```

---

### Output

```text
250.0

0.0042
```

---

# Built-in Functions

Python provides several built-in functions for working with float values.

| Function  | Description                   |
| --------- | ----------------------------- |
| `float()` | Converts a value into a float |
| `round()` | Rounds a float value          |
| `abs()`   | Returns the absolute value    |
| `pow()`   | Returns the power of a number |
| `type()`  | Returns the data type         |

---

## Example

```python
number = 25.6789

print(round(number))

print(round(number, 2))

print(abs(-35.75))

print(pow(2.5, 2))

print(type(number))
```

---

## Output

```text
26

25.68

35.75

6.25

<class 'float'>
```

---

# Summary

In this chapter, you learned:

* Introduction to Float
* Definition
* Syntax
* Examples
* Why Float is used
* Real-world applications
* Memory representation
* Program and output
* Dry run
* Pseudocode
* Line-by-line explanation
* Characteristics
* Floating-point literals
* Built-in functions

In the next chapter, you will learn **Float Operations**, including arithmetic operators, comparison operators, assignment operators, type conversion, and floating-point precision.
