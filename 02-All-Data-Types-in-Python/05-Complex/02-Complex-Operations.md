# Complex (`complex`) - Operations

## Introduction

Python provides built-in support for performing mathematical operations on complex numbers. A complex number consists of a real part and an imaginary part, and Python allows arithmetic operations, attribute access, and mathematical calculations directly on complex objects.

In this chapter, you will learn how to perform arithmetic operations, access the real and imaginary parts, compute conjugates, convert values to complex numbers, and understand the limitations of comparison operations.

---

# Arithmetic Operations

Complex numbers support all basic arithmetic operations.

## Arithmetic Operators Table

| Operator | Description    | Example           |
| -------- | -------------- | ----------------- |
| `+`      | Addition       | `(2+3j) + (4+5j)` |
| `-`      | Subtraction    | `(6+4j) - (2+1j)` |
| `*`      | Multiplication | `(2+3j) * (4+5j)` |
| `/`      | Division       | `(8+6j) / (2+1j)` |

---

## Program

```python
a = 4 + 3j
b = 2 + 1j

print("Addition :", a + b)
print("Subtraction :", a - b)
print("Multiplication :", a * b)
print("Division :", a / b)
```

---

## Output

```text
Addition : (6+4j)
Subtraction : (2+2j)
Multiplication : (5+10j)
Division : (2.2+0.4j)
```

---

# Accessing the Real Part

Every complex object provides the `.real` attribute.

## Example

```python
number = 8 + 6j

print(number.real)
```

Output

```text
8.0
```

---

# Accessing the Imaginary Part

Every complex object provides the `.imag` attribute.

## Example

```python
number = 8 + 6j

print(number.imag)
```

Output

```text
6.0
```

---

# Accessing Both Parts

```python
number = 5 + 9j

print("Real Part :", number.real)

print("Imaginary Part :", number.imag)
```

Output

```text
Real Part : 5.0

Imaginary Part : 9.0
```

---

# Complex Conjugate

The conjugate of a complex number changes the sign of the imaginary part.

General form

```text
a + bj

↓

a − bj
```

Python provides the `conjugate()` method.

## Example

```python
number = 4 + 6j

print(number.conjugate())
```

Output

```text
(4-6j)
```

---

# Magnitude (Absolute Value)

The magnitude of a complex number is calculated using the formula:

```text
√(a² + b²)
```

Python provides the `abs()` function.

## Example

```python
number = 3 + 4j

print(abs(number))
```

Output

```text
5.0
```

---

# Type Conversion

Python provides the `complex()` function to create complex numbers.

## Syntax

```python
complex(real, imaginary)
```

---

## Integer to Complex

```python
number = complex(10)

print(number)
```

Output

```text
(10+0j)
```

---

## Float to Complex

```python
number = complex(10.5)

print(number)
```

Output

```text
(10.5+0j)
```

---

## Two Values

```python
number = complex(5, 3)

print(number)
```

Output

```text
(5+3j)
```

---

# Invalid Conversion

```python
complex("Python")
```

Output

```text
ValueError
```

Only valid numeric values can be converted into complex numbers.

---

# Comparison Operations

Unlike integers and floats, complex numbers **cannot** be compared using ordering operators.

The following operators are **not supported**:

* `<`
* `>`
* `<=`
* `>=`

Example

```python
a = 2 + 3j
b = 4 + 5j

print(a > b)
```

Output

```text
TypeError
```

---

# Equality Comparison

Complex numbers can be compared using:

* `==`
* `!=`

Example

```python
a = 3 + 4j
b = 3 + 4j
c = 5 + 2j

print(a == b)

print(a != c)
```

Output

```text
True

True
```

---

# Common Built-in Functions

| Function    | Description              |
| ----------- | ------------------------ |
| `complex()` | Creates a complex number |
| `abs()`     | Returns the magnitude    |
| `type()`    | Returns the data type    |

---

# Common Attributes and Methods

| Attribute / Method | Description                   |
| ------------------ | ----------------------------- |
| `.real`            | Returns the real part         |
| `.imag`            | Returns the imaginary part    |
| `.conjugate()`     | Returns the complex conjugate |

---

# Real-World Applications

Complex number operations are used in:

* Electrical engineering
* Signal processing
* Quantum physics
* Robotics
* Telecommunications
* Image processing
* Scientific simulations

---

# Best Practices

* Use `.real` and `.imag` to access individual components.
* Use `abs()` to calculate magnitude.
* Use `conjugate()` instead of implementing the logic manually.
* Avoid using comparison operators such as `<` or `>` with complex numbers.
* Use meaningful variable names when representing mathematical quantities.

---

# Common Mistakes

## 1. Using Comparison Operators

```python
print((3+4j) > (2+1j))
```

Output

```text
TypeError
```

---

## 2. Invalid Conversion

```python
complex("Hello")
```

Output

```text
ValueError
```

---

## 3. Forgetting to Use `j`

Incorrect

```python
number = 5 + 3
```

Correct

```python
number = 5 + 3j
```

---

# Frequently Asked Interview Questions

## 1. What is a complex number in Python?

A complex number is a numeric data type consisting of a real part and an imaginary part.

---

## 2. Which letter represents the imaginary part?

Python uses **`j`** to represent the imaginary unit.

---

## 3. How do you access the real part?

Using the `.real` attribute.

---

## 4. How do you access the imaginary part?

Using the `.imag` attribute.

---

## 5. Can complex numbers be compared using `<` or `>`?

No.

Python raises a `TypeError`.

---

## 6. How do you calculate the magnitude of a complex number?

Use the built-in `abs()` function.

---

## Summary

In this chapter, you learned:

* Arithmetic operations on complex numbers
* Accessing the real and imaginary parts
* Computing complex conjugates
* Finding the magnitude
* Type conversion
* Comparison behavior
* Built-in attributes and methods
* Best practices
* Common mistakes
* Frequently asked interview questions

In the next chapter, you will learn advanced concepts of the `complex` data type, including internal working, memory management, immutability, implementation details, and performance considerations.
