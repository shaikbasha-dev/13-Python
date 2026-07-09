# Membership Operators in Python

## Learning Objectives

After completing this chapter, you will be able to:

- Understand Membership Operators.
- Explain why membership operators are used.
- Learn the `in` and `not in` operators.
- Check whether an element exists in a sequence.
- Write programs using membership operators.
- Understand real-world applications.

---

# Introduction

Membership Operators are used to determine whether a particular value exists in a sequence.

Python supports membership testing for several data types such as:

- Strings
- Lists
- Tuples
- Sets
- Dictionaries

Membership operators always return either **True** or **False**.

These operators are widely used in searching, validation, authentication, and filtering operations.

---

# Definition

A **Membership Operator** checks whether a specified value exists in a sequence.

Python provides two membership operators:

- `in`
- `not in`

---

# Why do we use Membership Operators?

Membership operators help to:

- Search elements in a sequence.
- Validate user input.
- Verify usernames.
- Check product availability.
- Search records.
- Improve program readability.

---

# Types of Membership Operators

| Operator | Description |
|----------|-------------|
| `in` | Returns True if the value exists in the sequence |
| `not in` | Returns True if the value does not exist in the sequence |

---

# 1. in Operator

## Definition

The **in** operator returns **True** if the specified value is present in a sequence.

---

## Syntax

```python
value in sequence
```

---

## Program

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

# 2. not in Operator

## Definition

The **not in** operator returns **True** if the specified value is **not** present in a sequence.

---

## Syntax

```python
value not in sequence
```

---

## Program

```python
language = "Python"

print("Z" not in language)
print("P" not in language)
```

### Output

```text
True
False
```

---

# Membership Operators with Different Data Types

## Strings

```python
text = "Python"

print("t" in text)
```

Output

```text
True
```

---

## Lists

```python
numbers = [10, 20, 30, 40]

print(20 in numbers)
```

Output

```text
True
```

---

## Tuples

```python
colors = ("Red", "Green", "Blue")

print("Green" in colors)
```

Output

```text
True
```

---

## Sets

```python
fruits = {"Apple", "Mango", "Orange"}

print("Apple" in fruits)
```

Output

```text
True
```

---

## Dictionaries

By default, membership operators check **keys**.

```python
student = {
    "id":101,
    "name":"Rahul"
}

print("name" in student)
```

Output

```text
True
```

---

# Program 1: Check Course Availability

## Problem Statement

Write a Python program to check whether "Python" is available in the course list.

---

## Program

```python
courses = ["Java", "Python", "SQL", "HTML"]

if "Python" in courses:
    print("Course Available")
```

---

## Output

```text
Course Available
```

---

# Program 2: Username Validation

## Problem Statement

Write a Python program to check whether a username already exists.

---

## Program

```python
users = ["admin", "manager", "student"]

username = "admin"

if username in users:
    print("Username Already Exists")
```

---

## Output

```text
Username Already Exists
```

---

# Program 3: Product Availability

## Program

```python
products = ["Laptop", "Mouse", "Keyboard"]

item = "Mouse"

if item in products:
    print("Product Available")
else:
    print("Product Not Available")
```

---

## Output

```text
Product Available
```

---

# Program 4: Character Search

## Program

```python
word = "Programming"

print("g" in word)
```

---

## Output

```text
True
```

---

# Real-Time Applications

Membership operators are used in:

- Login Systems
- User Authentication
- Search Applications
- Student Management Systems
- Inventory Management
- E-Commerce Websites
- Library Management Systems

---

# Advantages

- Easy element searching.
- Improves readability.
- Works with multiple sequence types.
- Returns Boolean values.
- Reduces the need for loops.

---

# Difference between in and not in

| in | not in |
|----|---------|
| Returns True if value exists | Returns True if value does not exist |
| Used for presence checking | Used for absence checking |

---

# Common Mistakes

## Confusing Strings with Lists

```python
text = "Python"

print("Py" in text)
```

Output

```text
True
```

The operator searches for substrings in strings.

---

## Dictionary Membership

```python
student = {
    "id":101,
    "name":"Rahul"
}

print("Rahul" in student)
```

Output

```text
False
```

Reason:

Membership operators check **keys**, not values.

To check values:

```python
print("Rahul" in student.values())
```

Output

```text
True
```

---

# Interview Questions

## 1. What are Membership Operators?

### Answer

Membership operators check whether a value exists in a sequence.

---

## 2. Which Membership Operators are available in Python?

### Answer

- `in`
- `not in`

---

## 3. What is the return type of Membership Operators?

### Answer

Boolean (`True` or `False`).

---

## 4. Can Membership Operators be used with dictionaries?

### Answer

Yes.

They check dictionary **keys** by default.

---

## 5. Which data types support Membership Operators?

### Answer

- Strings
- Lists
- Tuples
- Sets
- Dictionaries

---

# Quick Revision

- `in` → Checks whether a value exists.
- `not in` → Checks whether a value does not exist.
- Returns `True` or `False`.
- Works with strings, lists, tuples, sets, and dictionaries.
- Dictionary membership checks keys by default.

---

# Summary

In this chapter, you learned:

- What Membership Operators are.
- The `in` operator.
- The `not in` operator.
- Membership testing with different data types.
- Practical programs.
- Real-world applications.
- Common mistakes.
- Interview questions.
