# Part 2

---

# Pseudocode

```text
START

Create list numbers

Assign values

Create list languages

Assign values

Create list mixed

Assign values

Display all lists

STOP
```

---

# Line-by-Line Explanation

### Line 1

```python
numbers = [10, 20, 30]
```

Creates a list named `numbers` containing three integer values.

---

### Line 2

```python
languages = ["Python", "Java", "C++"]
```

Creates a list named `languages` containing string values.

---

### Line 3

```python
mixed = [10, "Python", 99.5, True]
```

Creates a list named `mixed` containing different data types.

---

### Line 4

```python
print("Numbers :", numbers)
```

Displays the `numbers` list.

---

### Line 5

```python
print("Languages :", languages)
```

Displays the `languages` list.

---

### Line 6

```python
print("Mixed :", mixed)
```

Displays the `mixed` list.

---

# Characteristics of List

- Ordered collection.
- Mutable data type.
- Allows duplicate values.
- Supports indexing.
- Supports slicing.
- Can store different data types.
- Dynamic in size.
- Can store nested lists.

---

# Built-in Functions

| Function | Description |
|----------|-------------|
| `len()` | Returns the number of elements in the list |
| `type()` | Returns the data type |
| `max()` | Returns the largest element |
| `min()` | Returns the smallest element |
| `sum()` | Returns the sum of numeric elements |
| `list()` | Creates a list |

---

# Example

```python
numbers = [10, 20, 30, 40, 50]

print(len(numbers))

print(max(numbers))

print(min(numbers))

print(sum(numbers))

print(type(numbers))
```

---

# Output

```text
5

50

10

150

<class 'list'>
```

---

# Summary

- `list` is used to store multiple values in a single variable.
- Lists are ordered and mutable.
- Lists allow duplicate values.
- Lists support indexing and slicing.
- Lists can store different data types.
- Python provides built-in functions such as `len()`, `max()`, `min()`, `sum()`, `list()`, and `type()` for working with lists.
