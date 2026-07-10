# Python Tuple Interview Questions

## Advanced Interview Questions

---

# Question 1

## What is the difference between a Tuple and a List?

### Answer

| Tuple | List |
|--------|------|
| Immutable | Mutable |
| Faster than List | Slower than Tuple |
| Uses less memory | Uses more memory |
| Suitable for fixed data | Suitable for frequently changing data |

---

# Question 2

## Why are Tuples faster than Lists?

### Answer

Tuples are faster because they are immutable.

Since their elements cannot be modified, Python performs fewer operations while accessing tuple elements.

---

# Question 3

## Can a Tuple be used as a dictionary key?

### Answer

Yes.

A Tuple can be used as a dictionary key because it is immutable.

### Example

```python
student = {
    (101, "Basha"): "Python"
}

print(student)
```

---

# Question 4

## What happens if an invalid index is accessed?

### Answer

Python raises an `IndexError`.

### Example

```python
numbers = (10, 20, 30)

print(numbers[5])
```

---

# Question 5

## What happens if index() cannot find an element?

### Answer

Python raises a `ValueError`.

### Example

```python
languages = ("Python", "Java")

print(languages.index("C++"))
```

---

# Question 6

## Which methods are available for Tuples?

### Answer

Python provides only two built-in tuple methods:

- `index()`
- `count()`

---

# Question 7

## Can Tuple elements be added or removed?

### Answer

No.

Tuple elements cannot be added or removed after creation because tuples are immutable.

---

# Question 8

## Can a Tuple contain duplicate values?

### Answer

Yes.

Tuples allow duplicate values.

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

## Which built-in functions are commonly used with Tuples?

### Answer

The commonly used built-in functions are:

- `len()`
- `max()`
- `min()`
- `sum()`
- `tuple()`
- `type()`
