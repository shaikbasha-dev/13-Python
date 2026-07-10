# Pseudocode

```text
START

Create dictionary student

Assign key-value pairs

Create dictionary employee

Assign key-value pairs

Display both dictionaries

STOP
```

---

# Line-by-Line Explanation

### Line 1

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}
```

Creates a dictionary named `student` containing student information as key-value pairs.

---

### Line 2

```python
employee = {
    "id": 1001,
    "name": "John",
    "salary": 50000
}
```

Creates a dictionary named `employee` containing employee information as key-value pairs.

---

### Line 3

```python
print(student)
```

Displays the `student` dictionary.

---

### Line 4

```python
print(employee)
```

Displays the `employee` dictionary.

---

# Characteristics of Dictionary

- Stores data as key-value pairs.
- Mutable data type.
- Keys must be unique.
- Values can be duplicated.
- Can store different data types.
- Supports nested dictionaries.
- Supports fast key-based lookup.

---

# Built-in Functions

| Function | Description |
|----------|-------------|
| `len()` | Returns the number of key-value pairs |
| `type()` | Returns the data type |
| `max()` | Returns the largest key |
| `min()` | Returns the smallest key |
| `dict()` | Creates a dictionary |

---

# Example

```python
student = {
    "id": 101,
    "name": "Basha",
    "marks": 95
}

print(len(student))

print(type(student))
```

---

# Output

```text
3

<class 'dict'>
```

---

# Summary

- `dict` is used to store data as key-value pairs.
- Dictionaries are mutable.
- Keys must be unique.
- Values can be duplicated.
- Dictionaries can store different data types.
- Python provides built-in functions such as `len()`, `type()`, and `dict()` for working with dictionaries.
