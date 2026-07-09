---

# Removing Key-Value Pairs

## Definition

Removing key-value pairs means deleting an existing key and its associated value from a dictionary.

Python provides the `pop()` method to remove a specified key.

---

## Syntax

```python
dictionary.pop(key)
```

---

## Program

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

student.pop("course")

print(student)
```

---

## Output

```text
{'id': 101, 'name': 'Basha'}
```

---

## Explanation

The `pop()` method removes the specified key and its corresponding value from the dictionary.

---

# Membership Operations

## Definition

Membership operators are used to check whether a key exists in a dictionary.

Python provides two membership operators:

- `in`
- `not in`

---

## Program

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

print("name" in student)

print("salary" not in student)
```

---

## Output

```text
True

True
```

---

## Explanation

- `"name" in student` returns `True` because the key exists.
- `"salary" not in student` returns `True` because the key does not exist.

---

# Traversing Dictionary

## Definition

Traversing a dictionary means visiting each key-value pair one by one.

Traversal is commonly performed using a `for` loop.

---

## Program

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

for key, value in student.items():
    print(key, ":", value)
```

---

## Output

```text
id : 101

name : Basha

course : Python
```

---

## Explanation

The `items()` method returns both keys and values.

The `for` loop visits each key-value pair and displays them.
