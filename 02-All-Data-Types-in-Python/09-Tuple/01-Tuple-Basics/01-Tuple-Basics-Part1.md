# Tuple (`tuple`)

## Introduction

A **Tuple** is one of the built-in data types in Python.

A tuple is used to store **multiple values** in a single variable.

Unlike lists, tuples are **immutable**, which means their elements cannot be modified after creation.

A tuple can store:

- Integers
- Float values
- Strings
- Boolean values
- Complex numbers
- Other Tuples
- Mixed Data Types

Tuples are **ordered**, **immutable**, and allow **duplicate values**.

---

# Definition

A **Tuple (`tuple`)** is an ordered, immutable collection of elements enclosed within parentheses (`()`).

Tuples can store elements of the same data type or different data types.

---

# Syntax

```python
variable_name = (element1, element2, element3)
```

### Example

```python
numbers = (10, 20, 30)

languages = ("Python", "Java", "C++")

mixed = (10, "Python", 25.5, True)
```

---

# Tuple Examples

```python
(10, 20, 30)

("Python", "Java", "C++")

(10.5, 20.8, 30.2)

(True, False)

(1, "Python", 25.5, True)
```

---

# Why do we use Tuple?

The `tuple` data type is used whenever we need to store multiple related values that should not be modified.

### Real-Time Examples

| Scenario | Example |
|----------|---------|
| Student Roll Numbers | (101, 102, 103) |
| Months of the Year | ("Jan", "Feb", "Mar") |
| RGB Color Values | (255, 255, 255) |
| Geographic Coordinates | (17.3850, 78.4867) |
| Employee IDs | (1001, 1002, 1003) |

---

# Memory Representation

Example

```python
languages = ("Python", "Java", "C++")
```

```text
          languages

              │

              ▼

+---------------------------------------+

| Python | Java | C++ |

+---------------------------------------+
```

The variable stores the reference to the tuple object.

---

# Program

```python
# Creating Tuples

numbers = (10, 20, 30)

languages = ("Python", "Java", "C++")

mixed = (10, "Python", 99.5, True)

# Displaying Tuples

print("Numbers :", numbers)

print("Languages :", languages)

print("Mixed :", mixed)
```

---

# Output

```text
Numbers : (10, 20, 30)

Languages : ('Python', 'Java', 'C++')

Mixed : (10, 'Python', 99.5, True)
```
