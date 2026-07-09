# Float (`float`) - Operations

## Introduction

Python supports a wide range of mathematical and comparison operations on floating-point numbers. These operations make the `float` data type suitable for scientific calculations, financial applications, engineering computations, and data analysis.

In this chapter, you will learn how to perform arithmetic operations, comparison operations, assignment operations, type conversion, and understand floating-point precision.

---

# Arithmetic Operators

Arithmetic operators perform mathematical calculations on float values.

## Arithmetic Operators Table

| Operator | Description    | Example      | Result |
| -------- | -------------- | ------------ | ------ |
| `+`      | Addition       | `10.5 + 5.5` | `16.0` |
| `-`      | Subtraction    | `10.5 - 5.5` | `5.0`  |
| `*`      | Multiplication | `10.5 * 2`   | `21.0` |
| `/`      | Division       | `10.5 / 2`   | `5.25` |
| `//`     | Floor Division | `10.5 // 2`  | `5.0`  |
| `%`      | Modulus        | `10.5 % 2`   | `0.5`  |
| `**`     | Exponentiation | `2.5 ** 2`   | `6.25` |

---

## Program

```python
a = 20.5
b = 4.0

print("Addition :", a + b)
print("Subtraction :", a - b)
print("Multiplication :", a * b)
print("Division :", a / b)
print("Floor Division :", a // b)
print("Modulus :", a % b)
print("Exponentiation :", a ** b)
```

---

## Output

```text
Addition : 24.5
Subtraction : 16.5
Multiplication : 82.0
Division : 5.125
Floor Division : 5.0
Modulus : 0.5
Exponentiation : 176610.0625
```

---

## Real-World Applications

Arithmetic operations on float values are commonly used in:

* Financial calculations
* Tax calculations
* Billing systems
* Engineering software
* Scientific research
* Machine learning
* Data analysis

---

# Comparison Operators

Comparison operators compare two floating-point values and return either `True` or `False`.

## Comparison Operators Table

| Operator | Meaning                  | Example      | Result |
| -------- | ------------------------ | ------------ | ------ |
| `==`     | Equal To                 | `5.5 == 5.5` | `True` |
| `!=`     | Not Equal To             | `5.5 != 2.5` | `True` |
| `>`      | Greater Than             | `8.5 > 5.2`  | `True` |
| `<`      | Less Than                | `3.2 < 7.8`  | `True` |
| `>=`     | Greater Than or Equal To | `6.5 >= 6.5` | `True` |
| `<=`     | Less Than or Equal To    | `5.5 <= 6.0` | `True` |

---

## Program

```python
x = 12.5
y = 10.0

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
```

---

## Output

```text
False
True
True
False
True
False
```

---

# Assignment Operators

Assignment operators update the value of a float variable.

## Assignment Operators Table

| Operator | Example    | Equivalent To |
| -------- | ---------- | ------------- |
| `=`      | `x = 10.5` | Assignment    |
| `+=`     | `x += 2.5` | `x = x + 2.5` |
| `-=`     | `x -= 2.5` | `x = x - 2.5` |
| `*=`     | `x *= 2`   | `x = x * 2`   |
| `/=`     | `x /= 2`   | `x = x / 2`   |
| `//=`    | `x //= 2`  | `x = x // 2`  |
| `%=`     | `x %= 2`   | `x = x % 2`   |
| `**=`    | `x **= 2`  | `x = x ** 2`  |

---

## Program

```python
value = 10.5

value += 5
print(value)

value *= 2
print(value)

value /= 3
print(value)

value -= 2
print(value)
```

---

## Output

```text
15.5
31.0
10.333333333333334
8.333333333333334
```

---

# Type Conversion

Python allows conversion between float and other data types using built-in conversion functions.

## Float to Integer

```python
number = 99.95

print(int(number))
```

Output

```text
99
```

The decimal portion is removed (truncated), not rounded.

---

## Integer to Float

```python
number = 100

print(float(number))
```

Output

```text
100.0
```

---

## String to Float

```python
price = "499.99"

print(float(price))
```

Output

```text
499.99
```

---

## Boolean to Float

```python
print(float(True))

print(float(False))
```

Output

```text
1.0
0.0
```

---

# Floating-Point Precision

Computers store floating-point numbers using a binary representation.

Because some decimal values cannot be represented exactly in binary, very small precision errors may occur.

Example

```python
print(0.1 + 0.2)
```

Output

```text
0.30000000000000004
```

This is normal behavior and is caused by binary floating-point representation.

---

# Rounding Values

Python provides the `round()` function to round floating-point numbers.

## Syntax

```python
round(number, digits)
```

---

## Example

```python
value = 25.67891

print(round(value))

print(round(value, 2))

print(round(value, 4))
```

---

## Output

```text
26
25.68
25.6789
```

---

# Best Practices

* Use float only when decimal values are required.
* Avoid comparing float values directly using `==` when precision is important.
* Use `round()` to display user-friendly decimal values.
* Use meaningful variable names.
* Convert user input carefully before performing calculations.

---

# Common Mistakes

## Assuming Decimal Values Are Stored Exactly

```python
print(0.1 + 0.2)
```

Output

```text
0.30000000000000004
```

---

## Incorrect Float Conversion

```python
print(float("Python"))
```

Output

```text
ValueError
```

Only valid numeric strings can be converted into float values.

---

# Frequently Asked Interview Questions

## 1. What is a float in Python?

A float is a built-in numeric data type used to store numbers with a fractional (decimal) part.

---

## 2. Why does `0.1 + 0.2` not produce exactly `0.3`?

Because floating-point numbers are stored internally in binary, which cannot exactly represent certain decimal values.

---

## 3. What is the difference between `int()` and `float()`?

| `int()`              | `float()`                         |
| -------------------- | --------------------------------- |
| Converts to integer  | Converts to floating-point number |
| Removes decimal part | Preserves decimal values          |

---

## 4. Does Python automatically convert integers to float?

Yes.

When an integer participates in an operation with a float, Python automatically converts the integer to a float.

Example:

```python
print(10 + 5.5)
```

Output

```text
15.5
```

---

# Summary

In this chapter, you learned:

* Arithmetic operations
* Comparison operators
* Assignment operators
* Type conversion
* Floating-point precision
* Rounding techniques
* Best practices
* Common mistakes
* Frequently asked interview questions

In the next chapter, you will learn the advanced concepts of the `float` data type, including internal working, IEEE 754 representation, memory management, immutability, performance considerations, and advanced interview questions.
