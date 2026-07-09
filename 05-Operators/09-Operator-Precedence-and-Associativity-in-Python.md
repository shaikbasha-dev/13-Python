# Operator Precedence and Associativity in Python

## Learning Objectives

After completing this chapter, you will be able to:

- Understand Operator Precedence.
- Understand Associativity.
- Learn the order of evaluation of expressions.
- Write expressions using multiple operators.
- Avoid mistakes caused by incorrect operator precedence.
- Write efficient and readable Python programs.

---

# Introduction

In Python, an expression may contain multiple operators.

For example,

```python
10 + 5 * 2
```

Which operation is performed first?

- Addition?
- Multiplication?

Python follows predefined rules called **Operator Precedence** and **Associativity** to evaluate expressions correctly.

Understanding these rules helps programmers write accurate and error-free programs.

---

# Definition

## Operator Precedence

Operator Precedence determines **which operator is evaluated first** when an expression contains multiple operators.

---

## Associativity

Associativity determines **the direction** in which operators having the same precedence are evaluated.

The direction may be:

- Left to Right
- Right to Left

---

# Why do we use Operator Precedence?

Operator precedence helps Python to:

- Evaluate expressions correctly.
- Avoid ambiguity.
- Produce consistent results.
- Reduce programming errors.

---

# Operator Precedence Table

Highest precedence to lowest precedence.

| Precedence | Operators |
|------------|-----------|
| Highest | `()` Parentheses |
| | `**` Exponent |
| | `+x`, `-x`, `~x` Unary Operators |
| | `*`, `/`, `//`, `%` |
| | `+`, `-` |
| | `<<`, `>>` |
| | `&` |
| | `^` |
| | `\|` |
| | `==`, `!=`, `>`, `<`, `>=`, `<=` |
| | `not` |
| | `and` |
| Lowest | `or` |

---

# Parentheses ()

Parentheses have the highest precedence.

## Example

```python
result = (10 + 5) * 2

print(result)
```

### Output

```text
30
```

Without parentheses,

```python
result = 10 + 5 * 2
```

Output

```text
20
```

---

# Exponent (**)

The exponent operator has higher precedence than multiplication and addition.

## Example

```python
print(2 ** 3 * 2)
```

### Output

```text
16
```

Explanation

```
2³ = 8

8 × 2 = 16
```

---

# Multiplication, Division, Floor Division and Modulus

These operators have higher precedence than addition and subtraction.

## Example

```python
print(10 + 4 * 5)
```

### Output

```text
30
```

Explanation

```
4 × 5 = 20

10 + 20 = 30
```

---

# Addition and Subtraction

Addition and subtraction are evaluated after multiplication and division.

Example

```python
print(30 - 5 + 2)
```

Output

```text
27
```

---

# Associativity

Operators with the same precedence are evaluated according to associativity.

---

## Left to Right Associativity

Most operators follow **Left to Right** evaluation.

Example

```python
print(20 - 5 - 3)
```

Output

```text
12
```

Explanation

```
20 - 5 = 15

15 - 3 = 12
```

---

## Right to Left Associativity

Exponent (`**`) follows **Right to Left** evaluation.

Example

```python
print(2 ** 3 ** 2)
```

Output

```text
512
```

Explanation

```
3² = 9

2⁹ = 512
```

---

# Program 1 : Demonstrate Operator Precedence

## Problem Statement

Write a Python program to demonstrate operator precedence.

---

## Program

```python
result = 10 + 5 * 2

print(result)
```

---

## Output

```text
20
```

---

# Program 2 : Using Parentheses

## Program

```python
result = (10 + 5) * 2

print(result)
```

---

## Output

```text
30
```

---

# Program 3 : Exponent Associativity

## Program

```python
result = 2 ** 3 ** 2

print(result)
```

---

## Output

```text
512
```

---

# Program 4 : Mixed Operators

## Program

```python
result = 50 // 5 + 10 * 2 - 3

print(result)
```

---

## Output

```text
27
```

Explanation

```
50 // 5 = 10

10 × 2 = 20

10 + 20 = 30

30 - 3 = 27
```

---

# Real-Time Applications

Operator precedence is used in:

- Banking Applications
- Billing Systems
- Payroll Software
- Scientific Calculations
- Financial Software
- Engineering Applications

---

# Advantages

- Eliminates ambiguity.
- Produces correct results.
- Makes expressions easier to understand.
- Improves program accuracy.

---

# Common Mistakes

## Ignoring Parentheses

```python
result = 10 + 5 * 2
```

Many beginners expect

```
30
```

Actual Output

```
20
```

---

## Forgetting Exponent Associativity

```python
2 ** 3 ** 2
```

Correct evaluation

```
2 ** (3 ** 2)
```

Not

```
(2 ** 3) ** 2
```

---

# Interview Questions

## 1. What is Operator Precedence?

### Answer

Operator Precedence determines which operator is evaluated first in an expression.

---

## 2. What is Associativity?

### Answer

Associativity determines the order of evaluation when operators have the same precedence.

---

## 3. Which operator has the highest precedence?

### Answer

Parentheses `()`.

---

## 4. Which operator follows Right to Left associativity?

### Answer

Exponent operator (`**`).

---

## 5. Why are parentheses used?

### Answer

Parentheses override the default operator precedence and improve readability.

---

# Quick Revision

- Parentheses have the highest precedence.
- Exponent (`**`) is evaluated before multiplication.
- Multiplication and division are evaluated before addition.
- Most operators follow Left to Right associativity.
- Exponent (`**`) follows Right to Left associativity.

---

# Summary

In this chapter, you learned:

- What Operator Precedence is.
- What Associativity is.
- Order of evaluation.
- Parentheses.
- Left-to-Right associativity.
- Right-to-Left associativity.
- Practical programs.
- Common mistakes.
- Interview questions.

In the next chapter, we will learn **Operator Interview Questions and Answers**, covering all operator types, output-based questions, frequently asked interview programs, and viva questions.
