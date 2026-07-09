# Python Tuple Interview Questions

## Introduction

This document contains the most frequently asked basic interview questions on Python Tuples.

These questions help beginners understand the fundamental concepts of Python Tuples and prepare for technical interviews.

---

# Question 1

## What is a Tuple in Python?

### Answer

A Tuple is a built-in data type in Python used to store multiple elements in a single variable.

Tuples are ordered, immutable, and allow duplicate values.

---

# Question 2

## What are the characteristics of a Tuple?

### Answer

The characteristics of a Tuple are:

- Ordered
- Immutable
- Allows duplicate values
- Supports indexing
- Supports slicing
- Can store different data types

---

# Question 3

## How do you create a Tuple in Python?

### Answer

Tuples are created using parentheses (`()`).

### Example

```python
numbers = (10, 20, 30)

languages = ("Python", "Java", "C++")
```

---

# Question 4

## Can a Tuple store different data types?

### Answer

Yes.

A Tuple can store different types of data together.

### Example

```python
data = (10, "Python", 25.5, True)
```

---

# Question 5

## Is a Tuple mutable?

### Answer

No.

Tuples are immutable, which means their elements cannot be modified after creation.

---

# Question 6

## Does a Tuple allow duplicate values?

### Answer

Yes.

Tuples allow duplicate values.

### Example

```python
numbers = (10, 20, 20, 30)

print(numbers)
```

---

# Question 7

## What is the difference between a Tuple and a List?

### Answer

| Tuple | List |
|--------|------|
| Immutable | Mutable |
| Uses `()` | Uses `[]` |
| Cannot be modified | Can be modified |

---

# Question 8

## What is indexing in a Tuple?

### Answer

Indexing is used to access individual elements from a tuple.

Tuples support both positive and negative indexing.

---

# Question 9

## What is slicing in a Tuple?

### Answer

Slicing is used to extract multiple elements from a tuple.

### Example

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
```

---

# Question 10

## Which built-in functions can be used with Tuples?

### Answer

Common built-in functions are:

- len()
- max()
- min()
- sum()
- tuple()
- type()
