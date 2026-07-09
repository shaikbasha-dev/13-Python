# Python Tuple Interview Questions

## Intermediate Interview Questions

---

# Question 1

## What is the difference between a Tuple and a List?

### Answer

| Tuple | List |
|--------|------|
| Immutable | Mutable |
| Uses `()` | Uses `[]` |
| Faster than List | Slower than Tuple |
| Suitable for fixed data | Suitable for dynamic data |

---

# Question 2

## Why are Tuples immutable?

### Answer

Tuples are immutable to ensure that the stored data remains unchanged after creation.

This provides better data integrity and reliability.

---

# Question 3

## Can a Tuple contain another Tuple?

### Answer

Yes.

A Tuple can contain one or more tuples as its elements.

### Example

```python
data = (10, 20, (30, 40), 50)

print(data)
```

---

# Question 4

## What are the built-in methods available for Tuples?

### Answer

Python provides only two built-in methods for tuples:

- `index()`
- `count()`

---

# Question 5

## Why does Tuple have fewer methods than List?

### Answer

Since tuples are immutable, their elements cannot be added, removed, or modified.

Therefore, methods like `append()`, `insert()`, `remove()`, `pop()`, and `clear()` are not available.

---

# Question 6

## What does the index() method return?

### Answer

The `index()` method returns the index of the first occurrence of the specified element.

---

# Question 7

## What does the count() method return?

### Answer

The `count()` method returns the number of occurrences of the specified element.

---

# Question 8

## Can a Tuple contain duplicate values?

### Answer

Yes.

Tuples allow duplicate values.

### Example

```python
numbers = (10, 20, 20, 30)

print(numbers)
```

---

# Question 9

## Can a Tuple store different data types?

### Answer

Yes.

A Tuple can store elements of different data types.

### Example

```python
data = (10, "Python", 25.5, True)
```

---

# Question 10

## Can Tuple elements be modified?

### Answer

No.

Tuple elements cannot be modified because tuples are immutable.
