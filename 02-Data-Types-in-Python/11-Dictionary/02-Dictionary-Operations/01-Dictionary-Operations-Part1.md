# Dictionary Operations

## Introduction

Python provides various operations that can be performed on dictionaries.

These operations help us to:

- Access values
- Add key-value pairs
- Update values
- Remove key-value pairs
- Search keys
- Traverse dictionaries

Since dictionaries are mutable, key-value pairs can be added, updated, and removed after creation.

---

# Categories of Dictionary Operations

```text
Dictionary Operations

│

├── Accessing Values

├── Adding Key-Value Pairs

├── Updating Values

├── Removing Key-Value Pairs

├── Membership Operations

└── Traversing Dictionary
```

---

# Accessing Values

## Definition

Accessing values means retrieving the value associated with a specified key.

---

## Syntax

```python
dictionary[key]
```

---

## Program

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

print(student["name"])

print(student["course"])
```

---

## Output

```text
Basha

Python
```

---

## Explanation

- `student["name"]` returns the value associated with the key `"name"`.
- `student["course"]` returns the value associated with the key `"course"`.

---

# Adding Key-Value Pairs

## Definition

New key-value pairs can be added by assigning a value to a new key.

---

## Syntax

```python
dictionary[new_key] = value
```

---

## Program

```python
student = {
    "id": 101,
    "name": "Basha"
}

student["course"] = "Python"

print(student)
```

---

## Output

```text
{'id': 101, 'name': 'Basha', 'course': 'Python'}
```

---

## Explanation

A new key `"course"` is added to the dictionary with the value `"Python"`.

---

# Updating Values

## Definition

Existing values can be updated by assigning a new value to an existing key.

---

## Syntax

```python
dictionary[key] = new_value
```

---

## Program

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Java"
}

student["course"] = "Python"

print(student)
```

---

## Output

```text
{'id': 101, 'name': 'Basha', 'course': 'Python'}
```

---

## Explanation

The value associated with the key `"course"` is updated from `"Java"` to `"Python"`.
