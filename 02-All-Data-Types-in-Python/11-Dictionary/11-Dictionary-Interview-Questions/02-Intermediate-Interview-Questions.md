# Python Dictionary Interview Questions

## Intermediate Interview Questions

---

# Question 1

## What is the difference between a Dictionary and a List?

### Answer

| Dictionary | List |
|------------|------|
| Stores key-value pairs | Stores values only |
| Uses `{}` | Uses `[]` |
| Accessed using keys | Accessed using indexes |
| Keys must be unique | Duplicate values are allowed |

---

# Question 2

## What happens if duplicate keys are used in a Dictionary?

### Answer

If duplicate keys are provided, the last value overwrites the previous value.

### Example

```python
student = {
    "id": 101,
    "id": 102
}

print(student)
```

---

# Question 3

## Can Dictionary values be duplicated?

### Answer

Yes.

Dictionary values can be duplicated because uniqueness is enforced only on keys.

---

# Question 4

## What are the commonly used Dictionary methods?

### Answer

Some commonly used dictionary methods are:

- `get()`
- `keys()`
- `values()`
- `items()`
- `pop()`
- `clear()`
- `copy()`

---

# Question 5

## What is the difference between get() and square bracket notation?

### Answer

| `get()` | `[]` |
|----------|------|
| Returns `None` if the key does not exist | Raises `KeyError` if the key does not exist |
| Safer for unknown keys | Used when the key is guaranteed to exist |

---

# Question 6

## What does the keys() method return?

### Answer

The `keys()` method returns a view object containing all dictionary keys.

---

# Question 7

## What does the values() method return?

### Answer

The `values()` method returns a view object containing all dictionary values.

---

# Question 8

## What does the items() method return?

### Answer

The `items()` method returns a view object containing key-value pairs as tuples.

---

# Question 9

## What does the pop() method do?

### Answer

The `pop()` method removes the specified key and returns its corresponding value.

---

# Question 10

## What does the clear() method do?

### Answer

The `clear()` method removes all key-value pairs from the dictionary.
