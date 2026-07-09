# Python Set Interview Questions

## Advanced Interview Questions

---

# Question 1

## What is the difference between a Set and a List?

### Answer

| Set | List |
|------|------|
| Unordered | Ordered |
| Stores unique elements | Allows duplicate elements |
| Does not support indexing | Supports indexing |
| Optimized for membership testing | Optimized for ordered collections |

---

# Question 2

## Why are Sets unordered?

### Answer

Sets are unordered because they are implemented using a hash table.

Therefore, elements are not stored based on insertion order.

---

# Question 3

## Can a Set contain duplicate values?

### Answer

No.

Sets automatically remove duplicate values.

---

# Question 4

## Can a Set contain different data types?

### Answer

Yes.

A Set can store elements of different data types.

### Example

```python
data = {10, "Python", 25.5, True}
```

---

# Question 5

## Which mathematical operations are supported by Sets?

### Answer

Python supports the following mathematical set operations:

- Union
- Intersection
- Difference
- Symmetric Difference

---

# Question 6

## Which methods are commonly used with Sets?

### Answer

Commonly used set methods are:

- `add()`
- `update()`
- `remove()`
- `discard()`
- `pop()`
- `clear()`
- `copy()`

---

# Question 7

## What happens if remove() is called for a missing element?

### Answer

Python raises a `KeyError`.

### Example

```python
numbers = {10, 20, 30}

numbers.remove(50)
```

---

# Question 8

## What happens if discard() is called for a missing element?

### Answer

No error is raised.

The set remains unchanged.

---

# Question 9

## Why does pop() return an arbitrary element?

### Answer

Since sets are unordered, there is no fixed first or last element.

Therefore, `pop()` removes and returns an arbitrary element.

---

# Question 10

## Why are Sets useful?

### Answer

Sets are useful when:

- Duplicate values should be removed.
- Fast membership testing is required.
- Mathematical set operations need to be performed.
