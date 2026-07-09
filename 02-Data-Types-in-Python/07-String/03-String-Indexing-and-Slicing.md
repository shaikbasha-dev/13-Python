# String (`str`) - Indexing and Slicing

## Introduction

A string is a **sequence of characters**, and each character occupies a specific position called an **index**.

Python allows us to access individual characters using **indexing** and multiple characters using **slicing**.

Understanding indexing and slicing is essential because many string operations such as searching, reversing, extracting substrings, and parsing data depend on these concepts.

---

# What is Indexing?

**Indexing** is the process of accessing a single character from a string using its position.

Python supports two types of indexing:

* Positive Indexing
* Negative Indexing

---

# Positive Indexing

Positive indexing starts from the **left side** of the string.

The first character always has an index of **0**.

Example

```python
language = "Python"
```

```text
Character :   P    y    t    h    o    n
Positive :    0    1    2    3    4    5
```

---

## Program

```python
language = "Python"

print(language[0])

print(language[1])

print(language[5])
```

---

## Output

```text
P

y

n
```

---

# Negative Indexing

Negative indexing starts from the **right side** of the string.

The last character always has an index of **-1**.

Example

```python
language = "Python"
```

```text
Character :   P    y    t    h    o    n
Negative :   -6   -5   -4   -3   -2   -1
```

---

## Program

```python
language = "Python"

print(language[-1])

print(language[-2])

print(language[-6])
```

---

## Output

```text
n

o

P
```

---

# Accessing Individual Characters

Characters can be accessed using either positive or negative indexes.

Example

```python
text = "Programming"

print(text[0])

print(text[4])

print(text[-1])
```

---

## Output

```text
P

r

g
```

---

# IndexError

Trying to access an index that does not exist raises an exception.

Example

```python
language = "Python"

print(language[10])
```

---

## Output

```text
IndexError: string index out of range
```

Always ensure that the index is within the valid range.

---

# What is Slicing?

**Slicing** extracts a portion (substring) of a string.

Instead of accessing one character, slicing returns multiple characters.

---

# Slice Syntax

```python
string[start : stop]
```

* `start` → Starting index (inclusive)
* `stop` → Ending index (exclusive)

---

## Example

```python
language = "Python"

print(language[0:4])

print(language[2:6])
```

---

## Output

```text
Pyth

thon
```

---

# Omitting the Start Index

If the starting index is omitted, Python starts from index `0`.

Example

```python
language = "Python"

print(language[:4])
```

Output

```text
Pyth
```

---

# Omitting the Stop Index

If the stop index is omitted, Python continues to the end of the string.

Example

```python
language = "Python"

print(language[2:])
```

Output

```text
thon
```

---

# Complete Copy Using Slicing

A complete copy of a string can be created using slicing.

Example

```python
language = "Python"

copy = language[:]

print(copy)
```

Output

```text
Python
```

---

# Step Value in Slicing

Python allows a third parameter called **step**.

Syntax

```python
string[start : stop : step]
```

The step value determines how many positions Python moves after selecting each character.

---

## Example

```python
language = "Python"

print(language[0:6:2])
```

Output

```text
Pto
```

Explanation

Python selects every second character.

---

# Reverse a String

A negative step can reverse a string.

Example

```python
language = "Python"

print(language[::-1])
```

Output

```text
nohtyP
```

---

# Negative Slicing

Negative indexes can also be used in slicing.

Example

```python
language = "Programming"

print(language[-11:-4])
```

Output

```text
Program
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
+---+---+---+---+---+---+
| P | y | t | h | o | n |
+---+---+---+---+---+---+
  0   1   2   3   4   5
 -6  -5  -4  -3  -2  -1
```

---

# Real-World Applications

Indexing and slicing are widely used in:

* Username extraction
* Email processing
* File extension detection
* URL parsing
* Data cleaning
* Text processing
* Log analysis
* Report generation

---

# Best Practices

* Use positive indexing when reading from left to right.
* Use negative indexing when working from the end of a string.
* Remember that the stop index is excluded.
* Use slicing instead of loops for extracting substrings.
* Use `[::-1]` to reverse strings efficiently.

---

# Common Mistakes

## 1. Assuming the Stop Index is Included

Incorrect assumption

```python
text = "Python"

print(text[0:3])
```

Output

```text
Pyt
```

The character at index `3` is **not included**.

---

## 2. Accessing an Invalid Index

```python
text = "Python"

print(text[100])
```

Output

```text
IndexError
```

---

## 3. Using an Incorrect Step Value

```python
text = "Python"

print(text[::0])
```

Output

```text
ValueError: slice step cannot be zero
```

The step value must never be zero.

---

# Frequently Asked Interview Questions

## 1. What is indexing?

Indexing is the process of accessing a single character using its position.

---

## 2. What are the two types of indexing?

* Positive indexing
* Negative indexing

---

## 3. What is slicing?

Slicing extracts a portion of a string.

---

## 4. Is the stop index included in slicing?

No.

The stop index is always excluded.

---

## 5. How do you reverse a string using slicing?

```python
text[::-1]
```

---

## 6. What happens if an invalid index is accessed?

Python raises an `IndexError`.

---

## 7. Can slicing be performed using negative indexes?

Yes.

Python fully supports negative indexes in slicing.

---

# Summary

In this chapter, you learned:

* Positive indexing
* Negative indexing
* Accessing individual characters
* IndexError
* String slicing
* Slice syntax
* Start, stop, and step values
* Reverse slicing
* Negative slicing
* Memory representation
* Real-world applications
* Best practices
* Common mistakes
* Frequently asked interview questions

In the next chapter, you will learn **String Traversal**, including different ways to iterate through strings using loops, built-in functions, and efficient traversal techniques.
