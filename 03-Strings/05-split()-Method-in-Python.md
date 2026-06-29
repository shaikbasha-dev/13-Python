# split() Method in Python

## Learning Objectives

After completing this chapter, you will be able to:

- Understand the `split()` method.
- Explain why the `split()` method is used.
- Learn the syntax of the `split()` method.
- Split strings using different separators.
- Use the `maxsplit` parameter.
- Write practical programs using the `split()` method.

---

# Introduction

In many applications, data is stored as a single string.

For example:

```text
Python Java C++ JavaScript
```

Sometimes we need to separate this data into individual words.

Similarly,

```text
Apple,Mango,Orange,Grapes
```

needs to be separated into individual fruit names.

Python provides the **split()** method to perform this operation.

---

# Definition

The **split()** method is a built-in string method that divides a string into multiple parts and returns them as a **list**.

---

# Why do we use split()?

The `split()` method is used to:

- Separate words from a sentence.
- Process user input.
- Read CSV data.
- Extract values from files.
- Parse URLs and email addresses.
- Process log files.

---

# Syntax

```python
string.split(separator, maxsplit)
```

---

# Parameters

| Parameter | Description |
|-----------|-------------|
| separator | Character or substring used to split the string (optional). |
| maxsplit | Maximum number of splits to perform (optional). |

---

# Return Value

The `split()` method returns a **list of strings**.

---

# Default Behavior

If no separator is specified, Python automatically splits the string wherever it finds whitespace.

Example

```python
text = "Python Java C++"

print(text.split())
```

### Output

```text
['Python', 'Java', 'C++']
```

---

# Splitting Using a Comma

Example

```python
fruits = "Apple,Mango,Orange,Grapes"

print(fruits.split(","))
```

### Output

```text
['Apple', 'Mango', 'Orange', 'Grapes']
```

---

# Using maxsplit

Example

```python
text = "Python Java C++ JavaScript"

print(text.split(" ", 2))
```

### Output

```text
['Python', 'Java', 'C++ JavaScript']
```

Explanation

Only the first **two splits** are performed.

---

# Memory Representation

Example

```python
text = "Python Java C++"
```

After applying

```python
text.split()
```

Memory Representation

```text
+-----------------------------------+

| Python | Java | C++ |

+-----------------------------------+

↓

List

["Python", "Java", "C++"]
```

---

# Program 1: Split Words Using Default Separator

## Problem Statement

Write a Python program to split a sentence into individual words.

---

## Program

```python
sentence = "Python is Easy"

words = sentence.split()

print(words)
```

---

## Output

```text
['Python', 'is', 'Easy']
```

---

## Pseudocode

```text
START

Create string

Apply split()

Display list

STOP
```

---

## Line-by-Line Explanation

### Line 1

```python
sentence = "Python is Easy"
```

Creates a string.

---

### Line 2

```python
words = sentence.split()
```

Splits the string at every space.

---

### Line 3

```python
print(words)
```

Displays the resulting list.

---

# Program 2: Split Using Comma

## Program

```python
courses = "Java,Python,C++,HTML"

result = courses.split(",")

print(result)
```

---

## Output

```text
['Java', 'Python', 'C++', 'HTML']
```

---

# Program 3: Split Using Hyphen

## Program

```python
date = "29-06-2026"

result = date.split("-")

print(result)
```

---

## Output

```text
['29', '06', '2026']
```

---

# Program 4: Split Using maxsplit

## Program

```python
text = "Python Java C++ JavaScript"

result = text.split(" ", 2)

print(result)
```

---

## Output

```text
['Python', 'Java', 'C++ JavaScript']
```

---

# Program 5: Count Number of Words

## Program

```python
sentence = "Python Programming Language"

words = sentence.split()

print("Number of Words :", len(words))
```

---

## Output

```text
Number of Words : 3
```

---

# Real-Time Applications

The `split()` method is used in:

- Login Systems
- CSV File Processing
- Text Editors
- Search Engines
- Chat Applications
- Data Analysis
- File Handling

---

# Advantages

- Converts a string into a list.
- Supports custom separators.
- Easy to process textual data.
- Useful in file handling.
- Simplifies text parsing.

---

# Common Mistakes

## Forgetting the Separator

```python
text = "A,B,C"

print(text.split())
```

Output

```text
['A,B,C']
```

Reason:

Python splits only at spaces by default.

Correct

```python
print(text.split(","))
```

Output

```text
['A', 'B', 'C']
```

---

## Confusing split() with join()

Remember

```text
split()

String → List

join()

List → String
```

---

# Difference between split() and join()

| split() | join() |
|----------|---------|
| Converts String into List | Converts List into String |
| Returns a List | Returns a String |
| Used for breaking text | Used for combining text |

---

# Interview Questions

## 1. What is split() in Python?

### Answer

The `split()` method divides a string into multiple parts and returns them as a list.

---

## 2. What is the default separator of split()?

### Answer

Whitespace (space).

---

## 3. What is maxsplit?

### Answer

`maxsplit` specifies the maximum number of splits to perform.

---

## 4. What is the return type of split()?

### Answer

A **List**.

---

## 5. What is the difference between split() and join()?

### Answer

- `split()` converts a string into a list.
- `join()` converts a list into a string.

---

# Quick Revision

- `split()` converts a string into a list.
- Default separator is whitespace.
- Custom separators can be specified.
- `maxsplit` limits the number of splits.
- Return type is `list`.

---

# Summary

In this chapter, you learned:

- What the `split()` method is.
- Why it is used.
- Syntax and parameters.
- Default separator.
- Custom separators.
- `maxsplit`.
- Practical programs.
- Difference between `split()` and `join()`.
- Interview questions.
