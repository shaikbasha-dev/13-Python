# List (`list`)

## Introduction

A **List** is one of the most commonly used built-in data types in Python.

A list is used to store **multiple values** in a single variable.

Unlike numeric data types that store only one value, a list can store:

- Integers
- Float values
- Strings
- Boolean values
- Complex numbers
- Other Lists
- Mixed Data Types

Lists are **ordered**, **mutable**, and allow **duplicate values**.

---

# Definition

A **List (`list`)** is an ordered, mutable collection of elements enclosed within square brackets (`[]`).

Lists can store elements of the same data type or different data types.

---

# Syntax

```python
variable_name = [element1, element2, element3]
```

### Example

```python
numbers = [10, 20, 30]

languages = ["Python", "Java", "C++"]

mixed = [10, "Python", 25.5, True]
```

---

# List Examples

```python
[10, 20, 30]

["Python", "Java", "C++"]

[10.5, 20.8, 30.2]

[True, False]

[1, "Python", 25.5, True]
```

---

# Why do we use List?

The `list` data type is used whenever we need to store and manage multiple related values together.

### Real-Time Examples

| Scenario | Example |
|----------|---------|
| Student Names | ["Rahul", "Basha", "Aman"] |
| Employee IDs | [101, 102, 103] |
| Product Prices | [199.99, 299.99, 499.99] |
| Shopping Cart | ["Laptop", "Mouse", "Keyboard"] |
| Student Marks | [85, 90, 78, 95] |

---

# Memory Representation

Example

```python
languages = ["Python", "Java", "C++"]
```

```text
          languages

              │

              ▼

+---------------------------------------+

| Python | Java | C++ |

+---------------------------------------+
```

The variable stores the reference to the list object.

---

# Program

```python
# Creating Lists

numbers = [10, 20, 30]

languages = ["Python", "Java", "C++"]

mixed = [10, "Python", 99.5, True]

# Displaying Lists

print("Numbers :", numbers)

print("Languages :", languages)

print("Mixed :", mixed)
```

---

# Output

```text
Numbers : [10, 20, 30]

Languages : ['Python', 'Java', 'C++']

Mixed : [10, 'Python', 99.5, True]
```
