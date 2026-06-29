# String Indexing in Python

## Learning Objectives

After completing this chapter, you will be able to:

* Understand String Indexing.
* Explain why indexing is used.
* Learn positive and negative indexing.
* Access individual characters from a string.
* Write programs using string indexing.
* Understand common indexing errors.

---

# Introduction

A string is a sequence of characters.

Each character in a string is assigned a unique position called an **index**.

Using an index, we can access any individual character from a string.

For example,

```text
Python
```

contains six characters, and each character has its own index value.

---

# Definition

**String Indexing** is the process of accessing individual characters of a string using their position number (index).

Python supports two types of indexing:

* Positive Indexing
* Negative Indexing

---

# Why do we use String Indexing?

String indexing is used to:

* Access individual characters.
* Process specific characters.
* Perform string manipulation.
* Search characters.
* Validate user input.

---

# Positive Indexing

Positive indexing starts from the **left side** of the string.

The first character always has index **0**.

### Example

```text
String :  P   y   t   h   o   n

Index :   0   1   2   3   4   5
```

---

# Negative Indexing

Negative indexing starts from the **right side** of the string.

The last character always has index **-1**.

### Example

```text
String :   P    y    t    h    o    n

Index :   -6   -5   -4   -3   -2   -1
```

---

# Memory Representation

Example

```python
language = "Python"
```

```text
              language

                  │

                  ▼

      +-----------------------+

      | P | y | t | h | o | n |

      +-----------------------+

        0   1   2   3   4   5

       -6 -5 -4 -3 -2 -1
```

---

# Syntax

```python
string_name[index]
```

---

# Program 1: Access First Character

## Problem Statement

Write a Python program to display the first character of a string.

---

## Program

```python
# Creating a string
language = "Python"

# Display the first character
print(language[0])
```

---

## Output

```text
P
```

---

## Pseudocode

```text
START

Create string

Access index 0

Display character

STOP
```

---

## Line-by-Line Explanation

### Line 1

```python
language = "Python"
```

Creates a string variable named `language`.

---

### Line 2

```python
print(language[0])
```

Accesses and displays the character at index `0`.

---

# Program 2: Access Last Character

## Problem Statement

Write a Python program to display the last character of a string.

---

## Program

```python
language = "Python"

print(language[-1])
```

---

## Output

```text
n
```

---

# Program 3: Display All Characters Using Indexing

## Program

```python
language = "Python"

print(language[0])
print(language[1])
print(language[2])
print(language[3])
print(language[4])
print(language[5])
```

---

## Output

```text
P
y
t
h
o
n
```

---

# IndexError

## Definition

If we try to access an index that does not exist, Python raises an **IndexError**.

---

## Example

```python
language = "Python"

print(language[10])
```

---

## Output

```text
IndexError: string index out of range
```

---

# Difference between Positive and Negative Indexing

| Positive Indexing          | Negative Indexing          |
| -------------------------- | -------------------------- |
| Starts from left           | Starts from right          |
| Begins with `0`            | Begins with `-1`           |
| Easy for forward traversal | Easy for reverse traversal |

---

# Real-Time Applications

String indexing is used in:

* Password Validation
* OTP Verification
* Character Searching
* Text Processing
* Compiler Design
* Data Validation

---

# Advantages

* Easy access to characters.
* Supports forward and backward traversal.
* Improves string manipulation.
* Simple and efficient.

---

# Common Mistakes

## Accessing Invalid Index

❌ Incorrect

```python
text = "Python"

print(text[10])
```

---

✅ Correct

```python
text = "Python"

print(text[5])
```

---

## Confusing Positive and Negative Indexes

Remember:

```text
Positive

0 1 2 3 4 5

Negative

-6 -5 -4 -3 -2 -1
```

---

# Interview Questions

## 1. What is String Indexing?

### Answer

String Indexing is the process of accessing individual characters of a string using index positions.

---

## 2. What is Positive Indexing?

### Answer

Positive indexing starts from the left side of the string, beginning with index `0`.

---

## 3. What is Negative Indexing?

### Answer

Negative indexing starts from the right side of the string, beginning with index `-1`.

---

## 4. What happens when an invalid index is accessed?

### Answer

Python raises an **IndexError** with the message:

```text
IndexError: string index out of range
```

---

## 5. Are string indexes mutable?

### Answer

No.

Strings are immutable. Characters cannot be modified using indexing.

---

# Quick Revision

* Indexing accesses individual characters.
* Positive indexing starts from `0`.
* Negative indexing starts from `-1`.
* Invalid indexes raise `IndexError`.
* Strings are immutable.

---

# Summary

In this chapter, you learned:

* What String Indexing is.
* Positive indexing.
* Negative indexing.
* Memory representation.
* Practical programs.
* IndexError.
* Real-world applications.
* Interview questions.

