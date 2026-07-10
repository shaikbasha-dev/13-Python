# Python Dictionary Interview Questions

## Introduction

This document contains the most frequently asked basic interview questions on Python Dictionaries.

These questions help beginners understand the fundamental concepts of Python Dictionaries and prepare for technical interviews.

---

# Question 1

## What is a Dictionary in Python?

### Answer

A Dictionary is a built-in data type in Python used to store data in the form of key-value pairs.

Each key must be unique, while values can be duplicated.

---

# Question 2

## What are the characteristics of a Dictionary?

### Answer

The characteristics of a Dictionary are:

- Stores data as key-value pairs.
- Mutable.
- Keys must be unique.
- Values can be duplicated.
- Can store different data types.
- Supports nested dictionaries.
- Provides fast key-based lookup.

---

# Question 3

## How do you create a Dictionary in Python?

### Answer

Dictionaries are created using curly braces (`{}`).

### Example

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}
```

---

# Question 4

## Can a Dictionary store different data types?

### Answer

Yes.

A Dictionary can store different data types as values.

### Example

```python
data = {
    "id": 101,
    "name": "Python",
    "price": 99.99,
    "available": True
}
```

---

# Question 5

## Are Dictionary keys unique?

### Answer

Yes.

Every key in a dictionary must be unique.

If duplicate keys are provided, the last value overwrites the previous one.

---

# Question 6

## Are Dictionary values unique?

### Answer

No.

Dictionary values can be duplicated.

---

# Question 7

## What is the difference between a Dictionary and a List?

### Answer

| Dictionary | List |
|------------|------|
| Stores key-value pairs | Stores values only |
| Uses `{}` | Uses `[]` |
| Accessed using keys | Accessed using indexes |
| Keys must be unique | Duplicate values are allowed |

---

# Question 8

## How do you access a value in a Dictionary?

### Answer

Values are accessed using their keys.

### Example

```python
student = {
    "name": "Basha"
}

print(student["name"])
```

---

# Question 9

## Is a Dictionary mutable?

### Answer

Yes.

Dictionaries are mutable, so key-value pairs can be added, updated, and removed after creation.

---

# Question 10

## Which built-in functions can be used with Dictionaries?

### Answer

Common built-in functions are:

- len()
- type()
- dict()
