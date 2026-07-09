# Tuple Traversal

## Introduction

Tuple Traversal is the process of accessing each element of a tuple one by one.

Traversal is one of the most commonly performed operations on tuples.

Python provides different ways to traverse a tuple.

---

# Definition

**Tuple Traversal** is the process of visiting every element of a tuple sequentially.

---

# Why is Tuple Traversal Required?

Suppose a company stores employee IDs in a tuple.

To display every employee ID, the program must visit each element one by one.

Tuple traversal performs this task efficiently.

---

# Ways to Traverse a Tuple

Python provides multiple ways to traverse a tuple.

- Using `for` Loop
- Using `while` Loop

---

# Traversing Using for Loop

## Syntax

```python
for variable in tuple_name:
    statements
```

---

## Program

```python
languages = ("Python", "Java", "C++", "JavaScript")

for language in languages:
    print(language)
```

---

## Output

```text
Python

Java

C++

JavaScript
```

---

## Dry Run

```text
languages

↓

Python

↓

Java

↓

C++

↓

JavaScript
```

---

## Memory Representation

```text
+---------------------------------------------+

| Python | Java | C++ | JavaScript |

+---------------------------------------------+

        ↓

Python

        ↓

Java

        ↓

C++

        ↓

JavaScript
```

---

## Pseudocode

```text
START

Create Tuple

Traverse using for loop

Display each element

STOP
```

---

## Line-by-Line Explanation

### Line 1

```python
languages = ("Python", "Java", "C++", "JavaScript")
```

Creates a tuple named `languages`.

---

### Line 2

```python
for language in languages:
```

The `for` loop visits each element of the tuple one by one.

---

### Line 3

```python
print(language)
```

Displays the current element.
