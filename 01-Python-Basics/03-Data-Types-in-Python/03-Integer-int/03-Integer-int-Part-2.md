# Integer (`int`) - Part 2

## Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations on integer values.

Python supports the following arithmetic operators.

| Operator | Description    | Example   | Result |
| -------- | -------------- | --------- | ------ |
| `+`      | Addition       | `10 + 5`  | `15`   |
| `-`      | Subtraction    | `10 - 5`  | `5`    |
| `*`      | Multiplication | `10 * 5`  | `50`   |
| `/`      | Division       | `10 / 5`  | `2.0`  |
| `//`     | Floor Division | `10 // 3` | `3`    |
| `%`      | Modulus        | `10 % 3`  | `1`    |
| `**`     | Exponentiation | `2 ** 3`  | `8`    |

---

## Program

```python
a = 20
b = 6

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
Addition : 26
Subtraction : 14
Multiplication : 120
Division : 3.3333333333333335
Floor Division : 3
Modulus : 2
Exponentiation : 64000000
```

---

## Dry Run

```text
a = 20
b = 6

20 + 6  → 26

20 - 6  → 14

20 * 6  → 120

20 / 6  → 3.3333333333333335

20 // 6 → 3

20 % 6  → 2

20 ** 6 → 64000000
```

---

## Real-World Applications

Arithmetic operators are widely used in:

* Banking applications
* Billing systems
* Student result calculations
* Payroll management
* Scientific calculations
* E-commerce applications
* Inventory systems

---

# Comparison Operators

Comparison operators compare two integer values and always return a Boolean value (`True` or `False`).

---

## Comparison Operators Table

| Operator | Meaning                  | Example    | Result |
| -------- | ------------------------ | ---------- | ------ |
| `==`     | Equal To                 | `10 == 10` | `True` |
| `!=`     | Not Equal To             | `10 != 5`  | `True` |
| `>`      | Greater Than             | `20 > 10`  | `True` |
| `<`      | Less Than                | `10 < 20`  | `True` |
| `>=`     | Greater Than or Equal To | `10 >= 10` | `True` |
| `<=`     | Less Than or Equal To    | `10 <= 20` | `True` |

---

## Program

```python
a = 20
b = 10

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
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

## Dry Run

```text
a = 20
b = 10

20 == 10 → False

20 != 10 → True

20 > 10 → True

20 < 10 → False

20 >= 10 → True

20 <= 10 → False
```

---

## Real-World Applications

Comparison operators are commonly used in:

* Login systems
* Eligibility checking
* Voting applications
* Age verification
* Student grading systems
* Employee management systems

---

# Assignment Operators

Assignment operators are used to assign values to variables and update existing values.

---

## Assignment Operators Table

| Operator | Example   | Equivalent To |
| -------- | --------- | ------------- |
| `=`      | `a = 10`  | Assign value  |
| `+=`     | `a += 5`  | `a = a + 5`   |
| `-=`     | `a -= 5`  | `a = a - 5`   |
| `*=`     | `a *= 5`  | `a = a * 5`   |
| `/=`     | `a /= 5`  | `a = a / 5`   |
| `//=`    | `a //= 5` | `a = a // 5`  |
| `%=`     | `a %= 5`  | `a = a % 5`   |
| `**=`    | `a **= 2` | `a = a ** 2`  |

---

## Program

```python
number = 20

number += 5
print(number)

number -= 10
print(number)

number *= 2
print(number)

number //= 3
print(number)

number %= 4
print(number)

number **= 3
print(number)
```

---

## Output

```text
25
15
30
10
2
8
```

---

## Dry Run

```text
number = 20

number += 5
20 + 5 = 25

↓

number -= 10
25 - 10 = 15

↓

number *= 2
15 × 2 = 30

↓

number //= 3
30 // 3 = 10

↓

number %= 4
10 % 4 = 2

↓

number **= 3
2³ = 8
```

---

## Advantages of Assignment Operators

* Reduces the amount of code.
* Improves readability.
* Makes calculations easier.
* Reduces programming errors.
* Frequently used inside loops and mathematical computations.

---

## Best Practices

* Use compound assignment operators (`+=`, `-=`, `*=`, etc.) when updating an existing variable.
* Prefer meaningful variable names instead of single-letter variables in real applications.
* Use parentheses in complex expressions to improve readability.

---

## Section Summary

In this section, you learned:

* Arithmetic Operators
* Comparison Operators
* Assignment Operators
* Their syntax
* Sample programs
* Outputs
* Dry runs
* Real-world applications
* Best practices


---

# Bitwise Operators

Bitwise operators perform operations directly on the binary representation of integer values.

Before performing any operation, Python converts integers into binary numbers.

Bitwise operators are commonly used in:

* System programming
* Embedded systems
* Networking
* Cryptography
* Device drivers
* Performance optimization

---

## Binary Representation

Consider the following integers:

```text
10 = 00001010

6  = 00000110
```

Python performs bitwise operations on these binary values.

---

# Types of Bitwise Operators

| Operator | Name        | Description                           |                                    |
| -------- | ----------- | ------------------------------------- | ---------------------------------- |
| `&`      | Bitwise AND | Sets a bit to 1 if both bits are 1    |                                    |
| `        | `           | Bitwise OR                            | Sets a bit to 1 if either bit is 1 |
| `^`      | Bitwise XOR | Sets a bit to 1 if bits are different |                                    |
| `~`      | Bitwise NOT | Inverts all bits                      |                                    |
| `<<`     | Left Shift  | Shifts bits to the left               |                                    |
| `>>`     | Right Shift | Shifts bits to the right              |                                    |

---

# Bitwise AND (`&`)

The AND operator returns **1** only when both corresponding bits are **1**.

### Example

```python
a = 10
b = 6

print(a & b)
```

### Output

```text
2
```

### Explanation

```text
      10 = 1010

       6 = 0110

----------------

AND     0010

----------------

Decimal = 2
```

---

# Bitwise OR (`|`)

The OR operator returns **1** if at least one corresponding bit is **1**.

### Example

```python
a = 10
b = 6

print(a | b)
```

### Output

```text
14
```

### Explanation

```text
      10 = 1010

       6 = 0110

----------------

OR      1110

----------------

Decimal = 14
```

---

# Bitwise XOR (`^`)

The XOR operator returns **1** when the corresponding bits are different.

### Example

```python
a = 10
b = 6

print(a ^ b)
```

### Output

```text
12
```

### Explanation

```text
      10 = 1010

       6 = 0110

----------------

XOR     1100

----------------

Decimal = 12
```

---

# Bitwise NOT (`~`)

The NOT operator flips every bit.

### Example

```python
number = 10

print(~number)
```

### Output

```text
-11
```

### Explanation

Python represents negative integers using two's complement representation.

```text
~10 = -(10 + 1)

= -11
```

---

# Left Shift (`<<`)

The left shift operator shifts all bits toward the left.

Each left shift approximately multiplies the value by **2**.

### Example

```python
number = 10

print(number << 2)
```

### Output

```text
40
```

### Explanation

```text
10 = 1010

1010 << 2

↓

101000

↓

40
```

---

# Right Shift (`>>`)

The right shift operator shifts all bits toward the right.

Each right shift approximately divides the value by **2**.

### Example

```python
number = 10

print(number >> 1)
```

### Output

```text
5
```

### Explanation

```text
10 = 1010

1010 >> 1

↓

0101

↓

5
```

---

# Complete Program

```python
a = 10
b = 6

print("AND :", a & b)
print("OR :", a | b)
print("XOR :", a ^ b)
print("NOT :", ~a)
print("Left Shift :", a << 2)
print("Right Shift :", a >> 1)
```

---

# Output

```text
AND : 2

OR : 14

XOR : 12

NOT : -11

Left Shift : 40

Right Shift : 5
```

---

# Real-World Applications

Bitwise operators are used in:

* Encryption algorithms
* Image processing
* Compression algorithms
* Network packet manipulation
* Device driver development
* Embedded systems
* Operating systems

---

# Type Conversion

Type conversion is the process of converting one data type into another.

Python supports two types of type conversion.

* Implicit Type Conversion
* Explicit Type Conversion

---

# Implicit Type Conversion

Implicit type conversion is performed automatically by the Python interpreter.

Python converts the smaller compatible data type into a larger compatible data type to avoid data loss.

### Example

```python
integer = 10

floating = 5.5

result = integer + floating

print(result)

print(type(result))
```

### Output

```text
15.5

<class 'float'>
```

---

# Explicit Type Conversion

Explicit type conversion is performed manually by the programmer using built-in conversion functions.

### Example

```python
number = "100"

value = int(number)

print(value)

print(type(value))
```

### Output

```text
100

<class 'int'>
```

---

# Integer Conversion Using `int()`

The `int()` function converts compatible values into integers.

---

## Syntax

```python
int(value)
```

---

## Examples

### Float to Integer

```python
price = 99.95

print(int(price))
```

Output

```text
99
```

---

### Boolean to Integer

```python
print(int(True))

print(int(False))
```

Output

```text
1

0
```

---

### String to Integer

```python
number = "250"

print(int(number))
```

Output

```text
250
```

---

### Invalid Conversion

```python
text = "Python"

print(int(text))
```

Output

```text
ValueError: invalid literal for int()
```

---

# Common Type Conversion Functions

| Function    | Converts To |
| ----------- | ----------- |
| `int()`     | Integer     |
| `float()`   | Float       |
| `complex()` | Complex     |
| `str()`     | String      |
| `bool()`    | Boolean     |

---

# Best Practices

* Perform explicit conversion only when necessary.
* Validate user input before converting strings to integers.
* Handle invalid conversions using exception handling.
* Avoid unnecessary type conversions to improve readability.

---

# Interview Tips

### What is the difference between implicit and explicit type conversion?

**Implicit Conversion**

* Performed automatically by Python.
* No programmer intervention.
* Prevents data loss.

**Explicit Conversion**

* Performed manually.
* Uses conversion functions.
* Gives the programmer complete control over data conversion.

---

## Section Summary

In this section, you learned:

* Bitwise operators
* Binary representation
* Left and right shift operations
* Implicit type conversion
* Explicit type conversion
* The `int()` conversion function
* Common type conversion functions
* Best practices
* Interview tips


---

# Internal Working of Integer

Whenever an integer is created, Python performs several internal steps before the value is ready to use.

Consider the following statement:

```python
age = 21
```

Internally, Python performs the following operations:

```text
Interpreter Reads Statement

↓

Creates Integer Object

↓

Allocates Memory

↓

Stores Value (21)

↓

Variable "age" References the Integer Object

↓

Execution Continues
```

Unlike some programming languages, variables in Python do not directly store values. Instead, they store **references** to objects.

---

# Memory Representation

```text
        age
         │
         ▼
+----------------------+
|      21 (int)        |
+----------------------+
```

When another variable references the same integer:

```python
a = 21
b = a
```

Memory representation:

```text
      a           b
      │           │
      └──────┬────┘
             ▼
+----------------------+
|      21 (int)        |
+----------------------+
```

Both variables reference the same integer object.

---

# Integer Memory Management

Python automatically manages memory using:

* Object creation
* Reference counting
* Garbage Collection

The programmer does not need to manually allocate or free memory.

Example:

```python
x = 100
y = x

print(x)
print(y)
```

Both variables point to the same integer object until one of them is reassigned.

---

# Integer Caching

Python optimizes memory by reusing commonly used integer objects.

This optimization is known as **Integer Caching** or **Small Integer Interning**.

Typically, Python caches integers in the range:

```text
-5 to 256
```

### Example

```python
a = 100
b = 100

print(a is b)
```

Output

```text
True
```

Both variables reference the same cached integer object.

---

### Example

```python
a = 1000
b = 1000

print(a == b)
print(a is b)
```

Possible Output

```text
True
False
```

Explanation:

* `==` compares values.
* `is` compares object identity (memory reference).
* Larger integers are not guaranteed to be cached.

> **Note:** Integer caching behavior is an implementation detail (commonly seen in CPython) and should not be relied upon for program logic.

---

# Integer Immutability

Integers are **immutable**.

Once an integer object is created, its value cannot be modified.

When an integer appears to change, Python creates a **new integer object**.

Example:

```python
number = 10

number = number + 5
```

Python does **not** modify the existing object.

Instead:

```text
Old Object (10)

↓

Create New Object (15)

↓

Variable points to New Object
```

Memory Representation

Before

```text
number

   │

   ▼

+-----------+

|    10     |

+-----------+
```

After

```text
number

   │

   ▼

+-----------+

|    15     |

+-----------+
```

---

# Advantages of Integer

* Stores whole numbers accurately.
* Supports unlimited precision.
* Faster than floating-point operations for whole numbers.
* Supports arithmetic, comparison, and bitwise operations.
* Immutable, making integer objects safe and predictable.
* Automatically managed memory.

---

# Limitations of Integer

* Cannot store decimal values.
* Division (`/`) returns a floating-point result.
* Very large integers require more memory and processing time.
* Cannot directly represent fractional quantities.

---

# Common Mistakes

## 1. Dividing Two Integers

```python
print(10 / 2)
```

Output

```text
5.0
```

Even though both operands are integers, `/` returns a **float**.

Use floor division when an integer result is required.

```python
print(10 // 2)
```

Output

```text
5
```

---

## 2. Invalid Integer Conversion

```python
text = "Python"

print(int(text))
```

Output

```text
ValueError
```

Always ensure the string contains a valid numeric value before converting.

---

## 3. Confusing `==` and `is`

Incorrect assumption:

```python
a = 1000
b = 1000

print(a is b)
```

Use:

* `==` for comparing values.
* `is` for comparing object identity.

---

# Best Practices

* Use integers for whole-number calculations.
* Use meaningful variable names.
* Prefer `//` when integer division is required.
* Validate user input before calling `int()`.
* Avoid relying on integer caching behavior.
* Use `==` instead of `is` for numeric value comparison.

---

# Frequently Asked Interview Questions

## 1. What is an integer in Python?

An integer is a built-in numeric data type used to store whole numbers without a decimal point.

---

## 2. Are integers mutable?

No.

Integers are immutable objects.

---

## 3. Does Python limit the size of integers?

No.

Python integers can grow as large as available system memory allows.

---

## 4. What is integer caching?

Integer caching is Python's optimization that reuses commonly used small integer objects (typically from `-5` to `256`) to improve performance and reduce memory usage.

---

## 5. What is the difference between `/` and `//`?

| `/`                 | `//`                          |
| ------------------- | ----------------------------- |
| Returns a float     | Returns floor division result |
| `10 / 3 = 3.333...` | `10 // 3 = 3`                 |

---

## 6. What is the difference between `==` and `is`?

| `==`            | `is`                                                    |
| --------------- | ------------------------------------------------------- |
| Compares values | Compares object identity                                |
| Checks equality | Checks whether both references point to the same object |

---

# Summary

In this chapter, you learned:

* Internal working of integers
* Memory representation
* Reference-based object storage
* Automatic memory management
* Integer caching
* Integer immutability
* Advantages and limitations
* Common programming mistakes
* Best practices
* Frequently asked interview questions

You now have a complete understanding of Python's **Integer (`int`)** data type, from basic concepts to advanced implementation details.

In the next chapter, you will learn about the **Float (`float`)** data type, including floating-point representation, arithmetic operations, precision, built-in functions, internal working, and practical applications.

