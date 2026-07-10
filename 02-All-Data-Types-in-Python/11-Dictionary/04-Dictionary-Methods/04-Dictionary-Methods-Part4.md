---

# items()

## Definition

The `items()` method returns a view object containing all key-value pairs of a dictionary as tuple objects.

---

## Why is items() Required?

Suppose a student management system stores student details in a dictionary.

To display both the field names and their corresponding values together, the `items()` method is used.

---

## Syntax

```python
dictionary.items()
```

---

## Parameters

This method does **not** take any parameters.

---

## Return Value

Returns a view object containing all key-value pairs as tuples.

---

## Program

```python
# Creating a dictionary
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

# Displaying all key-value pairs
print(student.items())
```

---

## Output

```text
dict_items([('id', 101), ('name', 'Basha'), ('course', 'Python')])
```

---

## Dry Run

```text
Dictionary

↓

items()

↓

(id, 101)

↓

(name, Basha)

↓

(course, Python)
```

---

## Pseudocode

```text
BEGIN

Create Dictionary

Call items()

Display Key-Value Pairs

END
```

---

## Line-by-Line Explanation

### Line 1

Creates a dictionary.

---

### Line 2

Calls `items()`.

---

### Line 3

Returns all key-value pairs of the dictionary.

---

### Line 4

Displays the key-value pairs.

---

## Real-World Applications

- Student Management Systems
- Employee Management Systems
- Banking Applications
- Inventory Management
- User Profile Management

---

## Best Practices

Use `items()` when both keys and values are required together.
