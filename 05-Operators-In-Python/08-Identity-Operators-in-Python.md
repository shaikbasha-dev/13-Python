# Identity Operators in Python

## Learning Objectives

After completing this chapter, you will be able to:

- Understand Identity Operators.
- Explain why identity operators are used.
- Learn the `is` and `is not` operators.
- Differentiate between identity and equality.
- Write programs using identity operators.
- Understand object references in Python.

---

# Introduction

In Python, two variables may contain the same value, but they may or may not refer to the same object in memory.

To determine whether two variables refer to the **same object**, Python provides **Identity Operators**.

Identity operators compare the **memory location (object identity)** of objects rather than just comparing their values.

---

# Definition

**Identity Operators** are used to check whether two variables refer to the same object in memory.

Python provides two identity operators.

- `is`
- `is not`

---

# Why do we use Identity Operators?

Identity operators help to:

- Compare object references.
- Check whether two variables refer to the same object.
- Compare objects with `None`.
- Understand Python's memory model.
- Debug object references.

---

# Types of Identity Operators

| Operator | Description |
|----------|-------------|
| `is` | Returns True if both variables refer to the same object |
| `is not` | Returns True if both variables refer to different objects |

---

# Memory Representation

Example

```python
a = [10, 20]

b = a

c = [10, 20]
```

```text
          a

          │

          ▼

      +-------------+

      | 10 | 20 |

      +-------------+

          ▲

          │

          b


          c

          │

          ▼

      +-------------+

      | 10 | 20 |

      +-------------+
```

Here,

- `a` and `b` refer to the **same object**.
- `c` refers to a **different object**, even though it has the same value.

---

# 1. is Operator

## Definition

The **is** operator returns **True** if two variables refer to the same object.

---

## Syntax

```python
variable1 is variable2
```

---

## Program

```python
a = [10, 20]

b = a

print(a is b)
```

### Output

```text
True
```

---

# 2. is not Operator

## Definition

The **is not** operator returns **True** if two variables refer to different objects.

---

## Syntax

```python
variable1 is not variable2
```

---

## Program

```python
a = [10, 20]

b = [10, 20]

print(a is not b)
```

### Output

```text
True
```

---

# Identity vs Equality

Identity operators compare **memory locations**, while equality operators compare **values**.

Example

```python
a = [10, 20]

b = [10, 20]

print(a == b)

print(a is b)
```

### Output

```text
True

False
```

Explanation

- `==` compares values.
- `is` compares object identity.

---

# Program 1: Compare Two Variables

## Problem Statement

Write a Python program to compare two variables using identity operators.

---

## Program

```python
a = [1, 2, 3]

b = a

print("a is b :", a is b)

print("a is not b :", a is not b)
```

---

## Output

```text
a is b : True

a is not b : False
```

---

# Program 2: Compare Different Objects

## Program

```python
a = [1, 2, 3]

b = [1, 2, 3]

print(a == b)

print(a is b)
```

---

## Output

```text
True

False
```

---

# Program 3: Checking None

```python
value = None

print(value is None)

print(value is not None)
```

---

## Output

```text
True

False
```

---

# Real-Time Applications

Identity operators are used in:

- Checking `None` values.
- Object reference comparison.
- Memory optimization.
- Python debugging.
- Object caching analysis.

---

# Advantages

- Compares object references directly.
- Useful when checking `None`.
- Improves code clarity.
- Helps understand Python's memory management.

---

# Difference between == and is

| == | is |
|----|----|
| Compares values | Compares object identity |
| Checks equality | Checks memory reference |
| Used for value comparison | Used for object comparison |

---

# Common Mistakes

## Using is Instead of ==

❌ Incorrect

```python
a = [10, 20]

b = [10, 20]

print(a is b)
```

Output

```text
False
```

Although both lists contain the same values, they are different objects.

---

✅ Correct

```python
print(a == b)
```

Output

```text
True
```

---

## Comparing with None Using ==

Instead of

```python
if value == None:
    print("No Value")
```

Prefer

```python
if value is None:
    print("No Value")
```

This is the recommended Python practice.

---

# Interview Questions

## 1. What are Identity Operators?

### Answer

Identity operators compare whether two variables refer to the same object in memory.

---

## 2. Which Identity Operators are available in Python?

### Answer

- `is`
- `is not`

---

## 3. What is the difference between `==` and `is`?

### Answer

- `==` compares values.
- `is` compares object identity (memory reference).

---

## 4. What is the best use of the `is` operator?

### Answer

The `is` operator is commonly used to compare a variable with `None`.

---

## 5. Can two variables have the same value but different identities?

### Answer

Yes.

Two variables can store equal values but refer to different objects in memory.

---

# Quick Revision

- `is` → Same object.
- `is not` → Different objects.
- Identity operators compare object references.
- Equality (`==`) compares values.
- Use `is None` to check for `None`.

---

# Summary

In this chapter, you learned:

- What Identity Operators are.
- The `is` operator.
- The `is not` operator.
- Identity vs Equality.
- Practical programs.
- Real-world applications.
- Common mistakes.
- Interview questions.
