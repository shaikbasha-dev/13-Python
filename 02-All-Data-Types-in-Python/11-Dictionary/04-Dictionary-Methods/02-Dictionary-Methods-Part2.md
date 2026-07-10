---

# keys()

## Definition

The `keys()` method returns a view object containing all the keys present in the dictionary.

---

## Why is keys() Required?

Suppose a student management system stores student details in a dictionary.

To display all available fields such as ID, Name, and Course, the `keys()` method is used.

---

## Syntax

```python
dictionary.keys()
```

---

## Parameters

This method does **not** take any parameters.

---

## Return Value

Returns a view object containing all dictionary keys.

---

## Program

```python
# Creating a dictionary
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

# Displaying all keys
print(student.keys())
```

---

## Output

```text
dict_keys(['id', 'name', 'course'])
```

---

## Dry Run

```text
Dictionary

↓

keys()

↓

id

↓

name

↓

course
```

---

## Pseudocode

```text
BEGIN

Create Dictionary

Call keys()

Display Keys

END
```

---

## Line-by-Line Explanation

### Line 1

Creates a dictionary.

---

### Line 2

Calls `keys()`.

---

### Line 3

Returns all keys of the dictionary.

---

### Line 4

Displays the keys.

---

## Real-World Applications

- Student Management Systems
- Employee Management Systems
- Banking Applications
- Inventory Management
- User Profile Management

---

## Best Practices

Use `keys()` when only dictionary keys are required.
