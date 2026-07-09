# Operators Interview Questions and Answers

## Introduction

This chapter contains the most frequently asked interview questions on **Python Operators**.

It covers:

- Arithmetic Operators
- Assignment Operators
- Comparison Operators
- Logical Operators
- Bitwise Operators
- Membership Operators
- Identity Operators
- Operator Precedence
- Output-Based Questions
- Frequently Asked Programs
- Viva Questions

---

# Basic Interview Questions

## Q1. What is an Operator?

### Answer

An **Operator** is a symbol that performs an operation on one or more operands and produces a result.

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

---

## Q2. What is an Operand?

### Answer

An operand is the value or variable on which an operator performs an operation.

Example

```python
a + b
```

Here,

- `+` → Operator
- `a` and `b` → Operands

---

## Q3. How many types of operators are available in Python?

### Answer

Python provides seven major categories of operators.

- Arithmetic Operators
- Assignment Operators
- Comparison Operators
- Logical Operators
- Bitwise Operators
- Membership Operators
- Identity Operators

---

# Arithmetic Operators

## Q4. What are Arithmetic Operators?

### Answer

Arithmetic operators perform mathematical operations.

Examples:

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Floor Division (`//`)
- Modulus (`%`)
- Exponent (`**`)

---

## Q5. Difference between `/` and `//`?

### Answer

| `/` | `//` |
|------|------|
| Returns floating-point result | Returns floor division result |

Example

```python
print(10 / 3)
```

Output

```text
3.3333333333333335
```

```python
print(10 // 3)
```

Output

```text
3
```

---

## Q6. Which operator returns the remainder?

### Answer

The Modulus operator (`%`).

Example

```python
print(25 % 4)
```

Output

```text
1
```

---

## Q7. Which operator calculates power?

### Answer

Exponent operator (`**`).

Example

```python
print(5 ** 3)
```

Output

```text
125
```

---

# Assignment Operators

## Q8. What are Assignment Operators?

### Answer

Assignment operators assign values or expression results to variables.

Example

```python
x = 10
```

---

## Q9. What is the difference between `=` and `+=`?

### Answer

- `=` assigns a value.
- `+=` adds a value and updates the variable.

Example

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

# Comparison Operators

## Q10. What are Comparison Operators?

### Answer

Comparison operators compare two values and return either **True** or **False**.

---

## Q11. What is the difference between `=` and `==`?

### Answer

| `=` | `==` |
|------|------|
| Assignment Operator | Comparison Operator |

Example

```python
print(10 == 10)
```

Output

```text
True
```

---

## Q12. What is the return type of comparison operators?

### Answer

Boolean (`True` or `False`).

---

# Logical Operators

## Q13. Which logical operators are available in Python?

### Answer

- `and`
- `or`
- `not`

---

## Q14. When does the `and` operator return `True`?

### Answer

Only when **both conditions are True**.

---

## Q15. When does the `or` operator return `True`?

### Answer

When **at least one condition is True**.

---

## Q16. What does the `not` operator do?

### Answer

It reverses the Boolean value.

Example

```python
print(not True)
```

Output

```text
False
```

---

# Bitwise Operators

## Q17. What are Bitwise Operators?

### Answer

Bitwise operators perform operations on binary values.

---

## Q18. Name all Bitwise Operators.

### Answer

- &
- |
- ^
- ~
- <<
- >>

---

## Q19. Why does `~5` return `-6`?

### Answer

Python uses the formula:

```text
~n = -(n + 1)
```

Therefore,

```text
~5 = -6
```

---

# Membership Operators

## Q20. What are Membership Operators?

### Answer

Membership operators check whether a value exists in a sequence.

Operators:

- `in`
- `not in`

---

## Q21. Which data types support Membership Operators?

### Answer

- Strings
- Lists
- Tuples
- Sets
- Dictionaries

---

## Q22. What is the return type of Membership Operators?

### Answer

Boolean (`True` or `False`).

---

# Identity Operators

## Q23. What are Identity Operators?

### Answer

Identity operators compare object references.

Operators:

- `is`
- `is not`

---

## Q24. Difference between `==` and `is`?

### Answer

| `==` | `is` |
|------|------|
| Compares values | Compares object identity |

---

## Q25. When should `is` be used?

### Answer

The `is` operator is commonly used when comparing with `None`.

Example

```python
value = None

print(value is None)
```

Output

```text
True
```

---

# Operator Precedence

## Q26. What is Operator Precedence?

### Answer

Operator precedence determines which operator is evaluated first in an expression.

---

## Q27. What is Associativity?

### Answer

Associativity determines the evaluation order of operators having the same precedence.

---

## Q28. Which operator has the highest precedence?

### Answer

Parentheses `()`.

---

## Q29. Which operator follows Right-to-Left associativity?

### Answer

Exponent operator (`**`).

---

# Output-Based Questions

## Q30. Predict the Output

```python
print(10 + 5 * 2)
```

Output

```text
20
```

---

## Q31. Predict the Output

```python
print((10 + 5) * 2)
```

Output

```text
30
```

---

## Q32. Predict the Output

```python
print(10 // 3)
```

Output

```text
3
```

---

## Q33. Predict the Output

```python
print(10 % 3)
```

Output

```text
1
```

---

## Q34. Predict the Output

```python
print(2 ** 3)
```

Output

```text
8
```

---

## Q35. Predict the Output

```python
print(5 & 3)
```

Output

```text
1
```

---

## Q36. Predict the Output

```python
print(5 | 3)
```

Output

```text
7
```

---

## Q37. Predict the Output

```python
print(5 ^ 3)
```

Output

```text
6
```

---

## Q38. Predict the Output

```python
print("P" in "Python")
```

Output

```text
True
```

---

## Q39. Predict the Output

```python
print("Java" not in "Python")
```

Output

```text
True
```

---

## Q40. Predict the Output

```python
a = [1, 2]
b = a

print(a is b)
```

Output

```text
True
```

---

# Frequently Asked Interview Programs

## Program 1

Perform all arithmetic operations.

```python
a = 20
b = 10

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** 2)
```

---

## Program 2

Check voting eligibility.

```python
age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible")
```

---

## Program 3

Check whether a course exists.

```python
courses = ["Java", "Python", "SQL"]

print("Python" in courses)
```

---

## Program 4

Compare two objects.

```python
a = [1, 2]

b = a

print(a is b)
```

---

## Program 5

Demonstrate operator precedence.

```python
print(10 + 5 * 2)

print((10 + 5) * 2)
```

---

# Viva Questions

- What is an operator?
- What is an operand?
- Name the different types of operators.
- What is the difference between `/` and `//`?
- What is the modulus operator?
- What is an assignment operator?
- Difference between `=` and `==`.
- Difference between `==` and `is`.
- What are logical operators?
- What are bitwise operators?
- What are membership operators?
- What are identity operators?
- What is operator precedence?
- What is associativity?
- Which operator has the highest precedence?
- Which operator has right-to-left associativity?

---

# Quick Revision

- Arithmetic → Mathematical calculations
- Assignment → Assign values
- Comparison → Returns `True` or `False`
- Logical → `and`, `or`, `not`
- Bitwise → Binary operations
- Membership → `in`, `not in`
- Identity → `is`, `is not`
- Parentheses have the highest precedence.
- Exponent (`**`) is right-to-left associative.

---

# Summary

In this chapter, you learned:

- Basic operator concepts.
- Arithmetic operators.
- Assignment operators.
- Comparison operators.
- Logical operators.
- Bitwise operators.
- Membership operators.
- Identity operators.
- Operator precedence.
- Output-based interview questions.
- Frequently asked interview programs.
- Viva questions.
- Quick revision.
