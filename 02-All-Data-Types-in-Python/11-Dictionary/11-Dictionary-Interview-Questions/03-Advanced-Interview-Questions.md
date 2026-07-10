# Python Dictionary Interview Questions

## Advanced Interview Questions

---

# Question 1

## What is a Dictionary in Python?

### Answer

A Dictionary is a built-in mutable data type that stores data as key-value pairs.

Each key is unique and is used to access its corresponding value efficiently.

---

# Question 2

## Why are Dictionary keys required to be unique?

### Answer

Keys are used to identify values uniquely.

If duplicate keys are provided, the last assigned value overwrites the previous value.

---

# Question 3

## Can Dictionary values be duplicated?

### Answer

Yes.

Dictionary values can be duplicated because uniqueness is enforced only on keys.

---

# Question 4

## Can a Dictionary contain another Dictionary?

### Answer

Yes.

A Dictionary can contain another dictionary as its value.

### Example

```python
student = {
    "id": 101,
    "details": {
        "name": "Basha",
        "course": "Python"
    }
}
```

---

# Question 5

## What are the commonly used Dictionary methods?

### Answer

Commonly used dictionary methods are:

- `get()`
- `keys()`
- `values()`
- `items()`
- `pop()`
- `clear()`
- `copy()`

---

# Question 6

## What happens if get() is used with a missing key?

### Answer

The `get()` method returns `None`.

It does not raise a `KeyError`.

---

# Question 7

## What happens if pop() is used with a missing key?

### Answer

Python raises a `KeyError`.

---

# Question 8

## Which method returns all keys of a Dictionary?

### Answer

The `keys()` method returns all keys as a dictionary view object.

---

# Question 9

## Which method returns all values of a Dictionary?

### Answer

The `values()` method returns all values as a dictionary view object.

---

# Question 10

## Which method returns all key-value pairs of a Dictionary?

### Answer

The `items()` method returns all key-value pairs as tuple objects in a dictionary view.
