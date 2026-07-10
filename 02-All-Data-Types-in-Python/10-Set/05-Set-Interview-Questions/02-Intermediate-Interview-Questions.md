# Python Set Interview Questions

## Intermediate Interview Questions

---

# Question 1

## What is the difference between a Set and a List?

### Answer

| Set | List |
|------|------|
| Unordered | Ordered |
| Does not allow duplicate values | Allows duplicate values |
| Uses `{}` | Uses `[]` |
| Does not support indexing | Supports indexing |
| Mutable | Mutable |

---

# Question 2

## Why are duplicate values not allowed in a Set?

### Answer

Sets are designed to store only unique elements.

If duplicate values are added, Python automatically removes them.

---

# Question 3

## Can a Set contain another Set?

### Answer

No.

A Set cannot contain another set because sets are mutable.

---

# Question 4

## What are the built-in methods available for Sets?

### Answer

Some commonly used built-in methods are:

- `add()`
- `update()`
- `remove()`
- `discard()`
- `pop()`
- `clear()`
- `copy()`

---

# Question 5

## What is the difference between remove() and discard()?

### Answer

| remove() | discard() |
|-----------|-----------|
| Raises `KeyError` if the element is not found | Does not raise an error if the element is not found |
| Used when the element is guaranteed to exist | Used when the element may or may not exist |

---

# Question 6

## What does the pop() method do?

### Answer

The `pop()` method removes and returns an arbitrary element from the set.

---

# Question 7

## What does the clear() method do?

### Answer

The `clear()` method removes all elements from the set.

---

# Question 8

## What does the copy() method do?

### Answer

The `copy()` method creates a shallow copy of a set.

---

# Question 9

## Does a Set support indexing or slicing?

### Answer

No.

Sets do not support indexing or slicing because they are unordered.

---

# Question 10

## Can a Set store different data types?

### Answer

Yes.

A Set can store elements of different data types.

### Example

```python
data = {10, "Python", 25.5, True}
```
