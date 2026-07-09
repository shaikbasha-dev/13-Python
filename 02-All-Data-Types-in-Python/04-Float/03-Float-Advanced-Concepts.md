# Float (`float`) - Advanced Concepts

## Introduction

After learning the fundamentals and operations of the `float` data type, it is important to understand how Python stores and manages floating-point numbers internally.

This chapter explains the internal working of float objects, memory management, IEEE 754 representation, immutability, performance considerations, common mistakes, and interview-oriented concepts.

---

# Internal Working of Float

Whenever a float value is created, Python performs several internal operations.

Example

```python
price = 499.99
```

Internally, Python performs the following steps.

```text
Interpreter Reads Statement

↓

Recognizes Floating-Point Value

↓

Creates Float Object

↓

Allocates Memory

↓

Stores Floating-Point Value

↓

Variable References the Float Object

↓

Execution Continues
```

Python variables store **references** to objects rather than the actual values.

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

If another variable is assigned the same object:

```python
a = 499.99
b = a
```

```text
       a          b
       │          │
       └────┬─────┘
            ▼
+-------------------------+
|     499.99 (float)      |
+-------------------------+
```

Both variables reference the same float object until one of them is reassigned.

---

# IEEE 754 Floating-Point Representation

Python uses the **IEEE 754 double-precision (64-bit)** standard to represent floating-point numbers.

A floating-point number consists of three parts:

```text
+-----------+-------------+----------------------+
| Sign Bit  | Exponent    | Fraction (Mantissa) |
+-----------+-------------+----------------------+
|    1 Bit  |   11 Bits   |       52 Bits        |
+-----------+-------------+----------------------+
```

### Components

* **Sign Bit** – Indicates whether the number is positive or negative.
* **Exponent** – Determines the scale of the number.
* **Mantissa (Fraction)** – Stores the significant digits of the value.

This representation enables Python to handle a very wide range of floating-point values.

---

# Memory Management

Python automatically manages memory for float objects.

Memory management includes:

* Object creation
* Reference counting
* Garbage collection

Example

```python
x = 25.5
y = x
```

Both variables reference the same object.

When one variable is reassigned:

```python
y = 100.5
```

Python creates a new float object and updates the reference.

---

# Float Immutability

Float objects are **immutable**.

Once a float object is created, its value cannot be modified.

Whenever a float appears to change, Python creates a new object.

Example

```python
price = 100.50

price = price + 25.25
```

Python creates a new float object instead of modifying the original object.

Memory Representation

Before

```text
price

  │

  ▼

+-----------+

| 100.50    |

+-----------+
```

After

```text
price

  │

  ▼

+-----------+

| 125.75    |

+-----------+
```

---

# Floating-Point Precision

Not every decimal value can be represented exactly in binary.

Example

```python
print(0.1 + 0.2)
```

Output

```text
0.30000000000000004
```

This is expected behavior and occurs because of binary floating-point representation.

---

# Comparing Float Values

Avoid comparing floating-point numbers directly using `==` when precision is important.

Instead, compare values within a small tolerance.

Example

```python
a = 0.1 + 0.2
b = 0.3

print(abs(a - b) < 1e-9)
```

Output

```text
True
```

This approach accounts for tiny floating-point precision differences.

---

# Performance Considerations

Float operations are generally efficient, but they are usually slower than integer operations because decimal calculations are more complex.

Use integers whenever decimal precision is not required.

Use floats only when working with fractional values.

---

# Advantages of Float

* Stores decimal values.
* Supports scientific notation.
* Handles very large and very small numbers.
* Suitable for engineering and scientific calculations.
* Supports arithmetic and comparison operations.
* Automatically managed by Python's memory system.

---

# Limitations of Float

* Cannot represent every decimal value exactly.
* Precision errors may occur.
* Slightly slower than integer operations.
* Not suitable for financial calculations requiring exact decimal precision.

For financial applications, Python's `decimal` module is often preferred.

---

# Best Practices

* Use float only when decimal values are required.
* Use `round()` to display user-friendly output.
* Avoid direct equality comparisons for floating-point values.
* Validate user input before converting strings to floats.
* Use integers when decimal precision is unnecessary.

---

# Common Mistakes

## 1. Comparing Float Values Using `==`

```python
print(0.1 + 0.2 == 0.3)
```

Output

```text
False
```

This happens because of floating-point precision limitations.

---

## 2. Invalid Float Conversion

```python
float("Python")
```

Output

```text
ValueError
```

Only numeric strings can be converted into float values.

---

## 3. Expecting Exact Decimal Storage

Many beginners assume that decimal values are stored exactly.

In reality, floating-point numbers are stored in binary, which may introduce tiny precision differences.

---

# Frequently Asked Interview Questions

## 1. What is a float in Python?

A float is a built-in numeric data type used to store numbers containing a fractional (decimal) part.

---

## 2. Are float objects mutable?

No.

Float objects are immutable.

---

## 3. Which standard does Python use to store float values?

Python uses the IEEE 754 double-precision floating-point standard.

---

## 4. Why does `0.1 + 0.2` produce `0.30000000000000004`?

Because many decimal values cannot be represented exactly in binary floating-point format.

---

## 5. When should you use float instead of int?

Use `float` when decimal values or fractional calculations are required.

---

## 6. What is the difference between `float` and `decimal.Decimal`?

| Float                               | Decimal                             |
| ----------------------------------- | ----------------------------------- |
| Faster                              | More precise for decimal arithmetic |
| Uses IEEE 754 binary representation | Uses decimal representation         |
| May introduce precision errors      | Suitable for financial calculations |

---

# Summary

In this chapter, you learned:

* Internal working of float objects
* Memory representation
* IEEE 754 floating-point representation
* Automatic memory management
* Float immutability
* Floating-point precision
* Performance considerations
* Advantages and limitations
* Best practices
* Common mistakes
* Frequently asked interview questions

You now have a complete understanding of Python's **Float (`float`)** data type, from basic concepts to advanced implementation details.

In the next chapter, you will learn about the **Complex (`complex`)** data type, including complex number representation, arithmetic operations, built-in attributes, internal working, and practical applications.
