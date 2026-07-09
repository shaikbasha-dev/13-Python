# Dictionary Traversal

## Introduction

Dictionary Traversal is the process of accessing each key-value pair of a dictionary one by one.

Traversal is one of the most commonly performed operations on dictionaries.

Python provides different ways to traverse a dictionary.

---

# Definition

**Dictionary Traversal** is the process of visiting every key and value in a dictionary sequentially.

---

# Why is Dictionary Traversal Required?

Suppose a company stores employee details in a dictionary.

To display every employee detail, the program must visit each key-value pair one by one.

Dictionary traversal performs this task efficiently.

---

# Ways to Traverse a Dictionary

Python provides multiple ways to traverse a dictionary.

- Using `keys()`
- Using `values()`
- Using `items()`

---

# Traversing Keys Using keys()

## Syntax

```python
for key in dictionary.keys():
    statements
```

---

## Program

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

for key in student.keys():
    print(key)
```

---

## Output

```text
id

name

course
```

---

## Dry Run

```text
student

↓

id

↓

name

↓

course
```

---

## Memory Representation

```text
+--------------------------------------+

| id | name | course |

+--------------------------------------+

        ↓

id

        ↓

name

        ↓

course
```

---

## Pseudocode

```text
START

Create Dictionary

Traverse keys using keys()

Display each key

STOP
```

---

## Line-by-Line Explanation

### Line 1

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}
```

Creates a dictionary named `student`.

---

### Line 2

```python
for key in student.keys():
```

The `for` loop visits each key of the dictionary one by one.

---

### Line 3

```python
print(key)
```

Displays the current key.
