---

# copy()

## Definition

The `copy()` method creates a shallow copy of a dictionary.

The copied dictionary is a new dictionary object containing the same key-value pairs as the original dictionary.

---

## Why is copy() Required?

Suppose a student management system needs to create a backup of student records before updating them.

Instead of modifying the original dictionary, a copy is created.

The `copy()` method performs this task efficiently.

---

## Syntax

```python
dictionary.copy()
```

---

## Parameters

This method does **not** take any parameters.

---

## Return Value

Returns a shallow copy of the dictionary.

---

## Program

```python
# Creating a dictionary
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

# Copying the dictionary
new_student = student.copy()

# Displaying both dictionaries
print("Original Dictionary :", student)

print("Copied Dictionary :", new_student)
```

---

## Output

```text
Original Dictionary : {'id': 101, 'name': 'Basha', 'course': 'Python'}

Copied Dictionary : {'id': 101, 'name': 'Basha', 'course': 'Python'}
```

---

## Dry Run

```text
Original Dictionary

{
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

↓

copy()

↓

Copied Dictionary

{
    "id": 101,
    "name": "Basha",
    "course": "Python"
}
```

---

## Pseudocode

```text
BEGIN

Create Dictionary

Call copy()

Store copied dictionary

Display original dictionary

Display copied dictionary

END
```

---

## Line-by-Line Explanation

### Line 1

Creates a dictionary.

---

### Line 2

Calls the `copy()` method.

---

### Line 3

Stores the copied dictionary in a new variable.

---

### Line 4

Displays the original dictionary.

---

### Line 5

Displays the copied dictionary.

---

## Real-World Applications

- Student Management Systems
- Employee Management Systems
- Banking Applications
- Inventory Management
- Data Backup
- Report Generation

---

## Best Practices

Use `copy()` when a duplicate dictionary is required without modifying the original dictionary.

---

# Summary

In this section, you learned:

- `get()`
- `keys()`
- `values()`
- `items()`
- `pop()`
- `clear()`
- `copy()`
- Their syntax
- Parameters
- Return values
- Practical examples
- Best Practices
- Real-World Applications
