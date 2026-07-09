# String (`str`) - Formatting

## Introduction

String formatting is the process of creating well-structured and readable output by combining strings with variables, expressions, and values.

Instead of manually concatenating multiple strings, Python provides several formatting techniques that make code cleaner, more readable, and easier to maintain.

String formatting is commonly used for:

* Reports
* User messages
* Billing systems
* Logging
* Console output
* Data presentation

---

# Why String Formatting?

Suppose we have the following variables:

```python
name = "Basha"
age = 24
course = "Python"
```

Without formatting:

```python
print("Name:", name)
print("Age:", age)
print("Course:", course)
```

Although correct, formatting provides cleaner and more flexible output.

---

# Methods of String Formatting

Python provides four common methods.

```text
String Formatting

│

├── String Concatenation

├── format()

├── f-Strings

└── Percentage Formatting (%)
```

---

# Method 1: String Concatenation

Strings can be combined using the `+` operator.

## Example

```python
name = "Basha"

print("Welcome " + name)
```

Output

```text
Welcome Basha
```

---

## Limitation

Concatenation cannot directly combine strings with numbers.

Incorrect

```python
age = 24

print("Age: " + age)
```

Output

```text
TypeError
```

Correct

```python
print("Age: " + str(age))
```

Output

```text
Age: 24
```

---

# Method 2: format() Method

The `format()` method inserts values into placeholders.

## Syntax

```python
"{}".format(value)
```

---

## Example

```python
name = "Basha"
course = "Python"

print("Student: {} | Course: {}".format(name, course))
```

Output

```text
Student: Basha | Course: Python
```

---

# Positional Formatting

```python
print("{1} is learning {0}".format("Python", "Basha"))
```

Output

```text
Basha is learning Python
```

---

# Named Placeholders

```python
print("{name} scored {marks}".format(name="Basha", marks=95))
```

Output

```text
Basha scored 95
```

---

# Method 3: f-Strings

Introduced in **Python 3.6**, f-Strings are the recommended way to format strings.

Prefix the string with `f`.

## Example

```python
name = "Basha"
age = 24

print(f"Name: {name}")

print(f"Age: {age}")
```

Output

```text
Name: Basha

Age: 24
```

---

# Expressions Inside f-Strings

Expressions can be evaluated directly.

```python
a = 10
b = 20

print(f"Sum = {a + b}")
```

Output

```text
Sum = 30
```

---

# Formatting Decimal Numbers

```python
price = 499.98765

print(f"{price:.2f}")
```

Output

```text
499.99
```

---

# Method 4: Percentage Formatting

Older versions of Python commonly used the `%` operator.

## Example

```python
name = "Basha"

print("Welcome %s" % name)
```

Output

```text
Welcome Basha
```

---

# Formatting Multiple Values

```python
name = "Basha"
age = 24

print("Name: %s Age: %d" % (name, age))
```

Output

```text
Name: Basha Age: 24
```

---

# Comparison of Formatting Methods

| Method         | Recommended        | Readability |
| -------------- | ------------------ | ----------- |
| Concatenation  | No                 | Medium      |
| `%` Formatting | Legacy             | Medium      |
| `format()`     | Yes                | Good        |
| f-Strings      | Highly Recommended | Excellent   |

---

# Real-World Applications

String formatting is used in:

* Invoice generation
* Salary slips
* Student reports
* Banking applications
* Chat applications
* Logging systems
* API responses
* Dashboard displays

---

# Best Practices

* Prefer **f-Strings** in modern Python programs.
* Use `format()` when dynamic placeholder positioning is required.
* Avoid excessive string concatenation.
* Format numbers before displaying them.
* Use meaningful placeholder names.

---

# Common Mistakes

## 1. Forgetting the `f`

Incorrect

```python
name = "Python"

print("{name}")
```

Output

```text
{name}
```

Correct

```python
print(f"{name}")
```

Output

```text
Python
```

---

## 2. Mixing Data Types with Concatenation

Incorrect

```python
age = 24

print("Age: " + age)
```

Output

```text
TypeError
```

---

## 3. Incorrect Placeholder Count

```python
print("{} {}".format("Python"))
```

Output

```text
IndexError
```

Every placeholder must have a corresponding value.

---

# Frequently Asked Interview Questions

## 1. What is string formatting?

String formatting is the process of inserting values into a string.

---

## 2. Which formatting method is recommended in modern Python?

**f-Strings**.

---

## 3. Which Python version introduced f-Strings?

Python **3.6**.

---

## 4. Can expressions be evaluated inside f-Strings?

Yes.

Example

```python
f"{10 + 20}"
```

---

## 5. Which formatting technique is considered legacy?

Percentage (`%`) formatting.

---

# Summary

In this chapter, you learned:

* Why string formatting is needed
* String concatenation
* `format()` method
* Positional formatting
* Named placeholders
* f-Strings
* Percentage formatting
* Decimal formatting
* Comparison of formatting methods
* Real-world applications
* Best practices
* Common mistakes
* Frequently asked interview questions

In the next chapter, you will learn **String Traversal**, including iteration using `for` loops, `while` loops, `enumerate()`, and efficient techniques for processing characters.
