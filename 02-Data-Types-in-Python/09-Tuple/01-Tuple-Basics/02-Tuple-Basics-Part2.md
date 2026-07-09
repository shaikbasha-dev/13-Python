---

# Pseudocode

```text
START

Create tuple numbers

Assign values

Create tuple languages

Assign values

Create tuple mixed

Assign values

Display all tuples

STOP
```

---

# Line-by-Line Explanation

### Line 1

```python
numbers = (10, 20, 30)
```

Creates a tuple named `numbers` containing three integer values.

---

### Line 2

```python
languages = ("Python", "Java", "C++")
```

Creates a tuple named `languages` containing string values.

---

### Line 3

```python
mixed = (10, "Python", 99.5, True)
```

Creates a tuple named `mixed` containing different data types.

---

### Line 4

```python
print("Numbers :", numbers)
```

Displays the `numbers` tuple.

---

### Line 5

```python
print("Languages :", languages)
```

Displays the `languages` tuple.

---

### Line 6

```python
print("Mixed :", mixed)
```

Displays the `mixed` tuple.

---

# Characteristics of Tuple

- Ordered collection.
- Immutable data type.
- Allows duplicate values.
- Supports indexing.
- Supports slicing.
- Can store different data types.
- Can store nested tuples.

---

# Built-in Functions

| Function | Description |
|----------|-------------|
| `len()` | Returns the number of elements in the tuple |
| `type()` | Returns the data type |
| `max()` | Returns the largest element |
| `min()` | Returns the smallest element |
| `sum()` | Returns the sum of numeric elements |
| `tuple()` | Creates a tuple |

---

# Example

```python
numbers = (10, 20, 30, 40, 50)

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

<class 'tuple'>
```

---

# Summary

- `tuple` is used to store multiple values in a single variable.
- Tuples are ordered and immutable.
- Tuples allow duplicate values.
- Tuples support indexing and slicing.
- Tuples can store different data types.
- Python provides built-in functions such as `len()`, `max()`, `min()`, `sum()`, `tuple()`, and `type()` for working with tuples.
