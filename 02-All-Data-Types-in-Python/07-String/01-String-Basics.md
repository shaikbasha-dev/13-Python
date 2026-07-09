# String (`str`) - Basics

## Introduction

A **String (`str`)** is one of Python's built-in **sequence data types** used to store **textual data**.

A string is a sequence of one or more Unicode characters enclosed within quotes. Strings are used to represent names, addresses, messages, passwords, email addresses, file paths, and many other forms of textual information.

Python provides powerful built-in support for working with strings, making them one of the most frequently used data types in programming.

---

# Definition

A **String (`str`)** is an immutable sequence of Unicode characters enclosed within single quotes, double quotes, or triple quotes.

---

# Syntax

```python
variable_name = "Text"

variable_name = 'Text'

variable_name = """Text"""

variable_name = '''Text'''
```

---

# Examples

```python
name = "Basha"

city = 'Hyderabad'

course = "Python"

company = "OpenAI"

message = """Welcome to
Python Programming"""
```

---

# String Examples

```python
"Python"

"Java"

"Hello"

"ChatGPT"

"Full Stack Development"
```

---

# Why Do We Use Strings?

Strings are used whenever a program needs to store or process textual information.

Typical uses include:

* Student names
* Email addresses
* Passwords
* City names
* Messages
* Product names
* URLs
* File paths

---

# Real-World Applications

| Scenario     | Example                                             |
| ------------ | --------------------------------------------------- |
| Student Name | "Basha"                                             |
| City         | "Hyderabad"                                         |
| Email        | "[student@example.com](mailto:student@example.com)" |
| Company      | "OpenAI"                                            |
| Product Name | "Laptop"                                            |
| Website URL  | "https://example.com"                               |
| Password     | "Secure@123"                                        |
| File Name    | "report.pdf"                                        |

---

# Memory Representation

Example

```python
name = "Python"
```

```text
        name
          │
          ▼
+----------------------+
|    "Python" (str)    |
+----------------------+
```

The variable stores a reference to the string object created in memory.

---

# Program

```python
name = "Basha"

city = "Hyderabad"

course = "Python"

print("Name :", name)

print("City :", city)

print("Course :", course)
```

---

# Output

```text
Name : Basha

City : Hyderabad

Course : Python
```

---

# Dry Run

```text
Step 1

name = "Basha"

city = "Hyderabad"

course = "Python"

↓

Step 2

Print name

Output → Basha

↓

Step 3

Print city

Output → Hyderabad

↓

Step 4

Print course

Output → Python
```

---

# Pseudocode

```text
START

Create string variable name

Assign "Basha"

Create string variable city

Assign "Hyderabad"

Create string variable course

Assign "Python"

Display all values

STOP
```

---

# Line-by-Line Explanation

### Line 1

```python
name = "Basha"
```

Creates a string object containing `"Basha"` and stores its reference in the variable `name`.

---

### Line 2

```python
city = "Hyderabad"
```

Creates a string object containing `"Hyderabad"` and stores its reference in the variable `city`.

---

### Line 3

```python
course = "Python"
```

Creates a string object containing `"Python"` and stores its reference in the variable `course`.

---

### Lines 4–6

The `print()` function displays the string values stored in the variables.

---

# Ways to Create Strings

Python supports multiple ways to create strings.

## Single Quotes

```python
language = 'Python'
```

---

## Double Quotes

```python
language = "Python"
```

---

## Triple Single Quotes

```python
text = '''Welcome to
Python Programming'''
```

---

## Triple Double Quotes

```python
text = """Welcome to
Python Programming"""
```

---

# Characteristics of Strings

* Stores textual data.
* Sequence of Unicode characters.
* Immutable data type.
* Supports indexing.
* Supports slicing.
* Supports iteration.
* Supports concatenation.
* Supports repetition.
* Automatically managed by Python.

---

# Built-in Functions

| Function | Description                                    |
| -------- | ---------------------------------------------- |
| `str()`  | Converts a value into a string                 |
| `len()`  | Returns the number of characters               |
| `type()` | Returns the data type                          |
| `ord()`  | Returns the Unicode code point of a character  |
| `chr()`  | Returns the character for a Unicode code point |

---

## Example

```python
name = "Python"

print(len(name))

print(str(100))

print(ord("A"))

print(chr(65))

print(type(name))
```

---

## Output

```text
6

100

65

A

<class 'str'>
```

---

# Summary

In this chapter, you learned:

* Introduction to Strings
* Definition
* Syntax
* Examples
* Why Strings are used
* Real-world applications
* Memory representation
* Program and output
* Dry run
* Pseudocode
* Line-by-line explanation
* Ways to create strings
* Characteristics
* Built-in functions

In the next chapter, you will learn **String Operations**, including concatenation, repetition, membership operators, comparison operators, and common string operations.
