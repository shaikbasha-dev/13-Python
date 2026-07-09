# Python List Interview Questions

## Introduction

This document contains the most frequently asked basic interview questions on Python Lists.

These questions help beginners understand the fundamental concepts of Python Lists and prepare for technical interviews.

---

# Question 1

## What is a List in Python?

### Answer

A List is a built-in data type in Python used to store multiple elements in a single variable.

Lists are ordered, mutable, and allow duplicate values.

---

# Question 2

## What are the characteristics of a List?

### Answer

The characteristics of a List are:

- Ordered
- Mutable
- Allows duplicate values
- Supports indexing
- Supports slicing
- Can store different data types
- Dynamic in size

---

# Question 3

## How do you create a List in Python?

### Answer

Lists are created using square brackets (`[]`).

### Example

```python
numbers = [10, 20, 30]

languages = ["Python", "Java", "C++"]
```

---

# Question 4

## Can a List store different data types?

### Answer

Yes.

A List can store different types of data together.

### Example

```python
data = [10, "Python", 25.5, True]
```

---

# Question 5

## Is a List mutable?

### Answer

Yes.

Lists are mutable, which means their elements can be modified after creation.

### Example

```python
numbers = [10, 20, 30]

numbers[1] = 50

print(numbers)
```

### Output

```text
[10, 50, 30]
```

---

# Question 6

## Does a List allow duplicate values?

### Answer

Yes.

Lists allow duplicate values.

### Example

```python
numbers = [10, 20, 20, 30]

print(numbers)
```

---

# Question 7

## What is the difference between a List and a Tuple?

### Answer

| List | Tuple |
|------|-------|
| Mutable | Immutable |
| Uses `[]` | Uses `()` |
| Can be modified | Cannot be modified |

---

# Question 8

## What is indexing in a List?

### Answer

Indexing is used to access individual elements from a list.

Lists support both positive and negative indexing.

---

# Question 9

## What is slicing in a List?

### Answer

Slicing is used to extract multiple elements from a list.

### Example

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

---

# Question 10

## Which built-in functions can be used with Lists?

### Answer

Common built-in functions are:

- len()
- max()
- min()
- sum()
- list()
- type()
