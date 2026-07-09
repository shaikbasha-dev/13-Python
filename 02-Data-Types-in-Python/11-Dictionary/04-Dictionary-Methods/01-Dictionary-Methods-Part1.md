# Dictionary Methods

## Introduction

Python provides several built-in methods to perform operations on dictionaries.

These methods make it easy to:

- Access values
- Retrieve keys
- Retrieve values
- Retrieve key-value pairs
- Remove key-value pairs
- Copy dictionaries
- Clear dictionaries

---

# Categories of Dictionary Methods

```text
Dictionary Methods

│

├── Access Methods

│      ├── get()

│      ├── keys()

│      ├── values()

│      └── items()

│

├── Removing Methods

│      ├── pop()

│      └── clear()

│

└── Copying

       └── copy()
```

---

# get()

## Definition

The `get()` method returns the value associated with the specified key.

If the key is not found, it returns `None` instead of raising an error.

---

## Why is get() Required?

Suppose a student management system stores student details in a dictionary.

When retrieving a student's course, the `get()` method safely returns the value even if the key is missing.

---

## Syntax

```python
dictionary.get(key)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| key | Key whose value is to be returned |

---

## Return Value

Returns the value associated with the specified key.

Returns `None` if the key is not found.

---

## Program

```python
# Creating a dictionary
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

# Accessing a value
print(student.get("name"))
```

---

## Output

```text
Basha
```

---

## Dry Run

```text
Dictionary

↓

get("name")

↓

Basha
```

---

## Pseudocode

```text
BEGIN

Create Dictionary

Call get()

Display Value

END
```

---

## Line-by-Line Explanation

### Line 1

Creates a dictionary.

---

### Line 2

Calls `get()`.

---

### Line 3

Returns the value associated with the key `"name"`.

---

### Line 4

Displays the returned value.

---

## Real-World Applications

- Student Management Systems
- Employee Management Systems
- Banking Applications
- User Profile Management
- Inventory Systems

---

## Best Practices

Use `get()` when retrieving values to avoid errors if the key does not exist.
