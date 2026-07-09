# Operators in Python

## Learning Objectives

After completing this chapter, you will be able to:

- Understand Operators in Python.
- Explain why operators are used.
- Learn different types of operators.
- Perform arithmetic and logical operations.
- Write programs using operators.
- Understand operator precedence.

---

# Introduction

In Python, operators are special symbols used to perform operations on variables and values.

For example,

- Add two numbers.
- Compare two values.
- Check multiple conditions.
- Assign values to variables.
- Perform bit-level operations.

Without operators, performing calculations and making decisions in programs would not be possible.

---

# Definition

An **Operator** is a symbol that performs a specific operation on one or more operands and produces a result.

Example

```python
a = 10
b = 20

print(a + b)
```

Output

```text
30
```

Here,

- `+` is the operator.
- `10` and `20` are operands.

---

# Why do we use Operators?

Operators are used to:

- Perform mathematical calculations.
- Compare values.
- Assign values.
- Combine multiple conditions.
- Manipulate binary values.
- Check object identity.
- Check membership.

---

# Types of Operators

Python provides the following types of operators.

```text
Operators

│

├── Arithmetic Operators

├── Assignment Operators

├── Comparison (Relational) Operators

├── Logical Operators

├── Bitwise Operators

├── Membership Operators

└── Identity Operators
```

---

# Arithmetic Operators

Arithmetic operators perform mathematical calculations.

| Operator | Description | Example |
|----------|-------------|----------|
| + | Addition | 10 + 5 |
| - | Subtraction | 10 - 5 |
| * | Multiplication | 10 * 5 |
| / | Division | 10 / 5 |
| // | Floor Division | 10 // 3 |
| % | Modulus | 10 % 3 |
| ** | Exponent | 2 ** 3 |

---

## Program

```python
a = 20
b = 10

print("Addition :", a + b)
print("Subtraction :", a - b)
print("Multiplication :", a * b)
print("Division :", a / b)
print("Floor Division :", a // b)
print("Modulus :", a % b)
print("Power :", a ** 2)
```

### Output

```text
Addition : 30
Subtraction : 10
Multiplication : 200
Division : 2.0
Floor Division : 2
Modulus : 0
Power : 400
```

---

# Assignment Operators

Assignment operators assign values to variables.

| Operator | Example |
|----------|----------|
| = | x = 10 |
| += | x += 5 |
| -= | x -= 5 |
| *= | x *= 5 |
| /= | x /= 5 |
| //= | x //= 5 |
| %= | x %= 5 |
| **= | x **= 2 |

---

## Example

```python
x = 10

x += 5

print(x)
```

Output

```text
15
```

---

# Comparison (Relational) Operators

Comparison operators compare two values and return either **True** or **False**.

| Operator | Description |
|----------|-------------|
| == | Equal to |
| != | Not Equal to |
| > | Greater than |
| < | Less than |
| >= | Greater than or Equal |
| <= | Less than or Equal |

---

## Example

```python
a = 10
b = 20

print(a == b)
print(a != b)
print(a < b)
print(a > b)
```

### Output

```text
False
True
True
False
```

---

# Logical Operators

Logical operators combine multiple conditions.

| Operator | Description |
|----------|-------------|
| and | Returns True if both conditions are True |
| or | Returns True if at least one condition is True |
| not | Reverses the result |

---

## Example

```python
age = 22
citizen = True

print(age >= 18 and citizen)
```

### Output

```text
True
```

---

# Bitwise Operators

Bitwise operators perform operations at the binary level.

| Operator | Description |
|----------|-------------|
| & | AND |
| \| | OR |
| ^ | XOR |
| ~ | NOT |
| << | Left Shift |
| >> | Right Shift |

---

## Example

```python
print(5 & 3)
print(5 | 3)
```

### Output

```text
1
7
```

---

# Membership Operators

Membership operators check whether a value exists in a sequence.

| Operator | Description |
|----------|-------------|
| in | Returns True if value exists |
| not in | Returns True if value does not exist |

---

## Example

```python
language = "Python"

print("P" in language)

print("Z" in language)
```

### Output

```text
True
False
```

---

# Identity Operators

Identity operators compare whether two variables refer to the same object.

| Operator | Description |
|----------|-------------|
| is | Same object |
| is not | Different object |

---

## Example

```python
a = [1, 2]

b = a

print(a is b)

print(a is not b)
```

### Output

```text
True
False
```

---

# Operator Precedence

Python follows precedence rules while evaluating expressions.

Highest to Lowest

```text
()

**

*, /, //, %

+, -

<, >, <=, >=

==, !=

not

and

or
```

---

# Real-Time Applications

Operators are used in:

- Banking Systems
- Billing Software
- Payroll Systems
- Student Management Systems
- Inventory Systems
- E-Commerce Applications

---

# Advantages

- Simplifies calculations.
- Supports decision making.
- Reduces code complexity.
- Improves program readability.

---

# Interview Questions

## 1. What is an Operator?

### Answer

An operator is a symbol that performs an operation on one or more operands.

---

## 2. How many types of operators are available in Python?

### Answer

Seven major types:

- Arithmetic
- Assignment
- Comparison
- Logical
- Bitwise
- Membership
- Identity

---

## 3. Which operator checks equality?

### Answer

`==`

---

## 4. What is the difference between `=` and `==`?

### Answer

- `=` is an assignment operator.
- `==` is a comparison operator.

---

## 5. Which operator is used to calculate the remainder?

### Answer

`%` (Modulus Operator)

---

# Quick Revision

- Operators perform operations on operands.
- Python provides seven major categories of operators.
- Arithmetic operators perform calculations.
- Logical operators combine conditions.
- Membership operators work with sequences.
- Identity operators compare object references.

---

# Summary

In this chapter, you learned:

- What operators are.
- Types of operators.
- Arithmetic operators.
- Assignment operators.
- Comparison operators.
- Logical operators.
- Bitwise operators.
- Membership operators.
- Identity operators.
- Operator precedence.
- Practical examples.
- Interview questions.

