# String Slicing in Python

## Learning Objectives

After completing this chapter, you will be able to:

- Understand String Slicing.
- Explain why slicing is used.
- Learn the syntax of string slicing.
- Perform positive and negative slicing.
- Use the step parameter in slicing.
- Write programs using string slicing.

---

# Introduction

Sometimes we need to extract **multiple characters** from a string instead of accessing a single character.

For example:

- Extract a student's first name.
- Display the first five characters of a product name.
- Reverse a string.
- Extract a domain name from an email address.

To perform these operations, Python provides **String Slicing**.

---

# Definition

**String Slicing** is the process of extracting a portion (substring) of a string using index positions.

Unlike indexing, which returns a single character, slicing returns multiple characters.

---

# Why do we use String Slicing?

String slicing is used to:

- Extract part of a string.
- Reverse a string.
- Skip characters.
- Process substrings.
- Manipulate text efficiently.

---

# Syntax

```python
string_name[start : stop]
```

or

```python
string_name[start : stop : step]
```

---

# Understanding the Parameters

| Parameter | Description |
|-----------|-------------|
| start | Starting index (included) |
| stop | Ending index (excluded) |
| step | Number of positions to move |

---

# Memory Representation

Example

```python
language = "Python"
```

```text
Characters

 P   y   t   h   o   n

 0   1   2   3   4   5

-6 -5 -4 -3 -2 -1
```

---

# Positive Slicing

Positive slicing starts from the left side.

Example

```python
language = "Python"

print(language[1:4])
```

### Output

```text
yth
```

Explanation

- Start = 1
- Stop = 4 (excluded)

Characters returned:

```text
y t h
```

---

# Negative Slicing

Negative slicing starts from the right side.

Example

```python
language = "Python"

print(language[-5:-2])
```

### Output

```text
yth
```

---

# Slicing with Step

Example

```python
language = "Python"

print(language[0:6:2])
```

### Output

```text
Pto
```

Explanation

The step value `2` skips every alternate character.

---

# Reverse a String

Example

```python
language = "Python"

print(language[::-1])
```

### Output

```text
nohtyP
```

---

# Program 1: Extract First Three Characters

## Problem Statement

Write a Python program to display the first three characters of a string.

---

## Program

```python
language = "Python"

print(language[0:3])
```

---

## Output

```text
Pyt
```

---

## Pseudocode

```text
START

Create string

Slice from index 0 to 3

Display result

STOP
```

---

## Line-by-Line Explanation

### Line 1

```python
language = "Python"
```

Creates a string named `language`.

---

### Line 2

```python
print(language[0:3])
```

Extracts characters from index `0` to `2`.

---

# Program 2: Extract Last Three Characters

## Program

```python
language = "Python"

print(language[-3:])
```

---

## Output

```text
hon
```

---

# Program 3: Reverse a String

## Program

```python
language = "Python"

print(language[::-1])
```

---

## Output

```text
nohtyP
```

---

# Program 4: Display Alternate Characters

## Program

```python
language = "Python"

print(language[::2])
```

---

## Output

```text
Pto
```

---

# Program 5: Copy a String

## Program

```python
language = "Python"

copy = language[:]

print(copy)
```

---

## Output

```text
Python
```

---

# Real-Time Applications

String slicing is used in:

- Data Extraction
- Report Generation
- Email Processing
- File Name Processing
- URL Parsing
- Text Analytics

---

# Advantages

- Easy extraction of substrings.
- Supports forward and backward traversal.
- Efficient string manipulation.
- Reduces the need for loops.

---

# Difference between Indexing and Slicing

| Indexing | Slicing |
|----------|----------|
| Returns one character | Returns multiple characters |
| Uses one index | Uses start and stop indexes |
| Example: `text[0]` | Example: `text[0:3]` |

---

# Common Mistakes

## Forgetting that Stop Index is Excluded

```python
text = "Python"

print(text[0:3])
```

Output

```text
Pyt
```

Not

```text
Pyth
```

---

## Using Invalid Step Value

```python
text = "Python"

print(text[::0])
```

Output

```text
ValueError: slice step cannot be zero
```

---

# Interview Questions

## 1. What is String Slicing?

### Answer

String Slicing is the process of extracting a portion of a string using index positions.

---

## 2. What is the syntax of String Slicing?

### Answer

```python
string[start:stop:step]
```

---

## 3. Is the stop index included?

### Answer

No.

The stop index is always excluded.

---

## 4. How can you reverse a string?

### Answer

```python
text[::-1]
```

---

## 5. Can slicing create a copy of a string?

### Answer

Yes.

```python
copy = text[:]
```

creates a copy of the string.

---

# Quick Revision

- Slicing extracts multiple characters.
- Syntax: `string[start:stop:step]`
- Start index is included.
- Stop index is excluded.
- Step controls movement.
- `[::-1]` reverses a string.
- `[:]` creates a copy.

---

# Summary

In this chapter, you learned:

- What String Slicing is.
- Syntax of slicing.
- Positive slicing.
- Negative slicing.
- Step value.
- Reverse string.
- Practical programs.
- Difference between indexing and slicing.
- Interview questions.

