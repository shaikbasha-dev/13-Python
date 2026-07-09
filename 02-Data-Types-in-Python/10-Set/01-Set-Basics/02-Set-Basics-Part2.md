---

# Pseudocode

```text
START

Create set numbers

Assign values

Create set languages

Assign values

Create set mixed

Assign values

Display all sets

STOP
```

---

# Line-by-Line Explanation

### Line 1

```python
numbers = {10, 20, 30}
```

Creates a set named `numbers` containing integer values.

---

### Line 2

```python
languages = {"Python", "Java", "C++"}
```

Creates a set named `languages` containing string values.

---

### Line 3

```python
mixed = {10, "Python", 99.5, True}
```

Creates a set named `mixed` containing different data types.

---

### Line 4

```python
print("Numbers :", numbers)
```

Displays the `numbers` set.

---

### Line 5

```python
print("Languages :", languages)
```

Displays the `languages` set.

---

### Line 6

```python
print("Mixed :", mixed)
```

Displays the `mixed` set.

---

# Characteristics of Set

- Unordered collection.
- Mutable data type.
- Does not allow duplicate values.
- Can store different data types.
- Supports set operations.
- Cannot be indexed.
- Cannot be sliced.

---

# Built-in Functions

| Function | Description |
|----------|-------------|
| `len()` | Returns the number of elements in the set |
| `type()` | Returns the data type |
| `max()` | Returns the largest element |
| `min()` | Returns the smallest element |
| `sum()` | Returns the sum of numeric elements |
| `set()` | Creates a set |

---

# Example

```python
numbers = {10, 20, 30, 40, 50}

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

<class 'set'>
```

---

# Summary

- `set` is used to store unique values in a single variable.
- Sets are unordered and mutable.
- Sets do not allow duplicate values.
- Sets can store different data types.
- Sets do not support indexing and slicing.
- Python provides built-in functions such as `len()`, `max()`, `min()`, `sum()`, `set()`, and `type()` for working with sets.
