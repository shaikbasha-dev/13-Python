# Strings in Python

## Learning Objectives

After completing this chapter, you will be able to:

* Understand Strings in Python.
* Explain why strings are used.
* Learn different ways of creating strings.
* Understand the characteristics of strings.
* Perform basic string operations.
* Write simple string programs.

---

# Introduction

A **String** is one of the most commonly used data types in Python.

Almost every application works with textual information.

Examples include:

* Student Name
* Employee Name
* Address
* City
* Email ID
* Mobile Number
* Password
* Product Name

Python provides the **String (`str`)** data type to store and manipulate textual information.

---

# Definition

A **String** is a sequence of Unicode characters enclosed within quotes.

Python treats every string as an object of the `str` class.

---

# Why do we use Strings?

Strings are used to store and process textual information.

### Real-Time Examples

* User Name
* Email Address
* Company Name
* Book Title
* Website URL
* Customer Feedback

---

# Characteristics of Strings

* Strings are immutable.
* Strings are ordered collections of characters.
* Strings support indexing.
* Strings support slicing.
* Strings support concatenation.
* Strings support repetition.
* Strings can contain letters, numbers, and special characters.

---

# Ways to Create Strings

Python provides multiple ways to create strings.

## Using Single Quotes

```python
name = 'Python'
```

---

## Using Double Quotes

```python
name = "Python"
```

---

## Using Triple Single Quotes

```python
text = '''Welcome to
Python Programming'''
```

---

## Using Triple Double Quotes

```python
text = """Welcome to
Python Programming"""
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

+----------------------+

|      "Python"        |

|     String Object    |

+----------------------+
```

The variable stores the reference to the string object.

---

# Program 1: Create and Display a String

## Problem Statement

Write a Python program to create a string and display it.

---

## Program

```python
# Creating a string variable
language = "Python"

# Display the string
print("Language :", language)
```

---

## Output

```text
Language : Python
```

---

## Pseudocode

```text
START

Create string variable

Assign "Python"

Display the string

STOP
```

---

## Line-by-Line Explanation

### Line 1

```python
language = "Python"
```

Creates a string variable named `language` and stores the value `"Python"`.

---

### Line 2

```python
print("Language :", language)
```

Displays the value stored in the variable.

---

# Program 2: Store Student Information

## Program

```python
student_name = "Rahul"

college = "ABC Engineering College"

city = "Hyderabad"

print(student_name)

print(college)

print(city)
```

---

## Output

```text
Rahul
ABC Engineering College
Hyderabad
```

---

# Basic String Operations

## Concatenation

```python
first_name = "Shaik"

last_name = "Basha"

full_name = first_name + " " + last_name

print(full_name)
```

### Output

```text
Shaik Basha
```

---

## Repetition

```python
text = "Hi "

print(text * 3)
```

### Output

```text
Hi Hi Hi
```

---

# Real-Time Applications

Strings are widely used in:

* Login Systems
* Banking Applications
* Hospital Management Systems
* E-Commerce Websites
* Chat Applications
* Student Management Systems
* Search Engines

---

# Advantages

* Easy to store textual information.
* Supports many built-in methods.
* Supports indexing and slicing.
* Immutable and secure.
* Easy to manipulate.

---

# Interview Questions

## 1. What is a String?

### Answer

A String is a sequence of Unicode characters enclosed within quotes.

---

## 2. Are Strings mutable?

### Answer

No.

Strings are **immutable**, meaning they cannot be modified after creation.

---

## 3. How many ways can a String be created in Python?

### Answer

Four common ways:

* Single Quotes
* Double Quotes
* Triple Single Quotes
* Triple Double Quotes

---

## 4. What is String Concatenation?

### Answer

String concatenation is the process of joining two or more strings using the `+` operator.

---

## 5. What is String Repetition?

### Answer

String repetition is the process of repeating a string multiple times using the `*` operator.

---

# Quick Revision

* String stores textual data.
* Strings are immutable.
* Strings are enclosed within quotes.
* Python supports four ways to create strings.
* Strings support concatenation and repetition.

---

# Summary

In this chapter, you learned:

* What a String is.
* Why strings are used.
* Characteristics of strings.
* Different ways to create strings.
* Basic string operations.
* Practical programs.
* Real-world applications.
* Interview questions.

