# Dictionary (`dict`)

## Introduction

A **Dictionary** is one of the built-in data types in Python.

A dictionary is used to store data in the form of **key-value pairs**.

Each key in a dictionary must be unique.

Dictionaries are **mutable**, **unordered**, and store data as key-value pairs.

A dictionary can store:

- Integers
- Float values
- Strings
- Boolean values
- Lists
- Tuples
- Dictionaries
- Mixed Data Types

---

# Definition

A **Dictionary (`dict`)** is a mutable collection of key-value pairs enclosed within curly braces (`{}`).

Each key must be unique and is associated with a value.

---

# Syntax

```python
variable_name = {
    key1: value1,
    key2: value2,
    key3: value3
}
```

### Example

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

employee = {
    "id": 1001,
    "name": "John",
    "salary": 50000
}
```

---

# Dictionary Examples

```python
{"name": "Python", "version": 3}

{1: "One", 2: "Two", 3: "Three"}

{"id": 101, "name": "Basha"}

{"Java": 95, "Python": 98}

{1: "One", "name": "Python", True: "Yes"}
```

---

# Why do we use Dictionary?

The `dict` data type is used whenever data needs to be stored as key-value pairs.

### Real-Time Examples

| Scenario | Example |
|----------|---------|
| Student Records | {"id":101, "name":"Basha"} |
| Employee Details | {"id":1001, "salary":50000} |
| Product Information | {"id":"P101", "price":500} |
| Bank Account Details | {"account":12345, "balance":25000} |
| User Profile | {"username":"admin", "email":"abc@gmail.com"} |

---

# Memory Representation

Example

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}
```

```text
            student

               │

               ▼

+------------------------------------------+

| id : 101 |

| name : Basha |

| course : Python |

+------------------------------------------+
```

The variable stores the reference to the dictionary object.

---

# Program

```python
# Creating Dictionaries

student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

employee = {
    "id": 1001,
    "name": "John",
    "salary": 50000
}

# Displaying Dictionaries

print(student)

print(employee)
```

---

# Output

```text
{'id': 101, 'name': 'Basha', 'course': 'Python'}

{'id': 1001, 'name': 'John', 'salary': 50000}
```
