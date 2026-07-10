# Python Set Interview Questions

## Introduction

This document contains the most frequently asked basic interview questions on Python Sets.

These questions help beginners understand the fundamental concepts of Python Sets and prepare for technical interviews.

---

# Question 1

## What is a Set in Python?

### Answer

A Set is a built-in data type in Python used to store multiple unique elements in a single variable.

Sets are unordered, mutable, and do not allow duplicate values.

---

# Question 2

## What are the characteristics of a Set?

### Answer

The characteristics of a Set are:

- Unordered
- Mutable
- Does not allow duplicate values
- Can store different data types
- Supports mathematical set operations
- Does not support indexing
- Does not support slicing

---

# Question 3

## How do you create a Set in Python?

### Answer

Sets are created using curly braces (`{}`).

### Example

```python
numbers = {10, 20, 30}

languages = {"Python", "Java", "C++"}
```

---

# Question 4

## Can a Set store different data types?

### Answer

Yes.

A Set can store different types of data together.

### Example

```python
data = {10, "Python", 25.5, True}
```

---

# Question 5

## Is a Set mutable?

### Answer

Yes.

Sets are mutable, which means elements can be added or removed after creation.

---

# Question 6

## Does a Set allow duplicate values?

### Answer

No.

Sets automatically remove duplicate values.

### Example

```python
numbers = {10, 20, 20, 30}

print(numbers)
```

---

# Question 7

## What is the difference between a Set and a List?

### Answer

| Set | List |
|------|------|
| Unordered | Ordered |
| Does not allow duplicates | Allows duplicates |
| Uses `{}` | Uses `[]` |
| Does not support indexing | Supports indexing |

---

# Question 8

## Does a Set support indexing?

### Answer

No.

Sets do not support indexing because they are unordered.

---

# Question 9

## Does a Set support slicing?

### Answer

No.

Sets do not support slicing because they are unordered.

---

# Question 10

## Which built-in functions can be used with Sets?

### Answer

Common built-in functions are:

- len()
- max()
- min()
- sum()
- set()
- type()
