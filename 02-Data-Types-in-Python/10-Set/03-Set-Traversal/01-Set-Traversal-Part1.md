# Set Traversal

## Introduction

Set Traversal is the process of accessing each element of a set one by one.

Traversal is one of the most commonly performed operations on sets.

Since sets are unordered, the elements are accessed in an arbitrary order.

---

# Definition

**Set Traversal** is the process of visiting every element of a set sequentially.

---

# Why is Set Traversal Required?

Suppose a company stores employee IDs in a set.

To display every employee ID, the program must visit each element one by one.

Set traversal performs this task efficiently.

---

# Ways to Traverse a Set

Python provides the following way to traverse a set.

- Using `for` Loop

---

# Traversing Using for Loop

## Syntax

```python
for variable in set_name:
    statements
```

---

## Program

```python
languages = {"Python", "Java", "C++", "JavaScript"}

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

Create Set

Traverse using for loop

Display each element

STOP
```

---

## Line-by-Line Explanation

### Line 1

```python
languages = {"Python", "Java", "C++", "JavaScript"}
```

Creates a set named `languages`.

---

### Line 2

```python
for language in languages:
```

The `for` loop visits each element of the set one by one.

---

### Line 3

```python
print(language)
```

Displays the current element.
