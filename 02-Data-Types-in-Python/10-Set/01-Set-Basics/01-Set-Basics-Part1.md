# Set (`set`)

## Introduction

A **Set** is one of the built-in data types in Python.

A set is used to store **multiple unique values** in a single variable.

Unlike lists and tuples, sets do **not** allow duplicate values.

Sets are **unordered** and **mutable**.

A set can store:

- Integers
- Float values
- Strings
- Boolean values
- Mixed Data Types

---

# Definition

A **Set (`set`)** is an unordered, mutable collection of unique elements enclosed within curly braces (`{}`).

Duplicate values are automatically removed.

---

# Syntax

```python
variable_name = {element1, element2, element3}
```

### Example

```python
numbers = {10, 20, 30}

languages = {"Python", "Java", "C++"}

mixed = {10, "Python", 25.5, True}
```

---

# Set Examples

```python
{10, 20, 30}

{"Python", "Java", "C++"}

{10.5, 20.8, 30.2}

{True, False}

{1, "Python", 25.5, True}
```

---

# Why do we use Set?

The `set` data type is used whenever duplicate values should not be stored.

### Real-Time Examples

| Scenario | Example |
|----------|---------|
| Unique Student IDs | {101, 102, 103} |
| Unique Email Addresses | {"a@gmail.com", "b@gmail.com"} |
| Unique Product Codes | {"P101", "P102"} |
| Unique Employee IDs | {1001, 1002, 1003} |
| Unique Cities | {"Delhi", "Hyderabad", "Bangalore"} |

---

# Memory Representation

Example

```python
languages = {"Python", "Java", "C++"}
```

```text
          languages

              │

              ▼

+---------------------------------------+

| Python | Java | C++ |

+---------------------------------------+
```

The variable stores the reference to the set object.

---

# Program

```python
# Creating Sets

numbers = {10, 20, 30}

languages = {"Python", "Java", "C++"}

mixed = {10, "Python", 99.5, True}

# Displaying Sets

print("Numbers :", numbers)

print("Languages :", languages)

print("Mixed :", mixed)
```

---

# Output

```text
Numbers : {10, 20, 30}

Languages : {'Python', 'Java', 'C++'}

Mixed : {10, 'Python', 99.5, True}
```
