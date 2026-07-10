---

# pop()

## Definition

The `pop()` method removes the specified key from the dictionary and returns its corresponding value.

If the key does not exist, Python raises a `KeyError`.

---

## Why is pop() Required?

Suppose a student management system stores student details in a dictionary.

When a student leaves the course, the student's record can be removed using the `pop()` method.

---

## Syntax

```python
dictionary.pop(key)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| key | Key to be removed |

---

## Return Value

Returns the value associated with the removed key.

The original dictionary is modified.

---

## Program

```python
# Creating a dictionary
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

# Removing a key
removed_value = student.pop("course")

print("Removed Value :", removed_value)

print(student)
```

---

## Output

```text
Removed Value : Python

{'id': 101, 'name': 'Basha'}
```

---

## Dry Run

```text
Dictionary

↓

pop("course")

↓

Returns "Python"

↓

Removes course key

↓

Updated Dictionary
```

---

## Pseudocode

```text
BEGIN

Create Dictionary

Call pop()

Store returned value

Display removed value

Display updated dictionary

END
```

---

## Line-by-Line Explanation

### Line 1

Creates a dictionary.

---

### Line 2

Calls the `pop()` method with the key `"course"`.

---

### Line 3

Stores the removed value.

---

### Line 4

Displays the removed value.

---

### Line 5

Displays the updated dictionary.

---

## Real-World Applications

- Student Management Systems
- Employee Management Systems
- Banking Applications
- Inventory Management
- User Profile Management

---

## Best Practices

Use `pop()` when you need both to remove a key and retrieve its associated value.
