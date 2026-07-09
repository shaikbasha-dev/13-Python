# List Traversal

## Introduction

List Traversal is the process of accessing each element of a list one by one.

Traversal is one of the most commonly performed operations on lists.

Python provides different ways to traverse a list.

---

# Definition

**List Traversal** is the process of visiting every element of a list sequentially.

---

# Why is List Traversal Required?

Suppose a school stores the names of all students in a list.

To display every student's name, the program must visit each element one by one.

List traversal performs this task efficiently.

---

# Ways to Traverse a List

Python provides multiple ways to traverse a list.

- Using `for` Loop
- Using `while` Loop

---

# Traversing Using for Loop

## Syntax

```python
for variable in list_name:
    statements
```

---

## Program

```python
languages = ["Python", "Java", "C++", "JavaScript"]

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

Create List

Traverse using for loop

Display each element

STOP
```

---

## Line-by-Line Explanation

### Line 1

```python
languages = ["Python", "Java", "C++", "JavaScript"]
```

Creates a list named `languages`.

---

### Line 2

```python
for language in languages:
```

The `for` loop visits each element of the list one by one.

---

### Line 3

```python
print(language)
```

Displays the current element.
