---

# values()

## Definition

The `values()` method returns a view object containing all the values present in the dictionary.

---

## Why is values() Required?

Suppose a student management system stores student details in a dictionary.

To display all stored information such as ID, Name, and Course values, the `values()` method is used.

---

## Syntax

```python
dictionary.values()
```

---

## Parameters

This method does **not** take any parameters.

---

## Return Value

Returns a view object containing all dictionary values.

---

## Program

```python
# Creating a dictionary
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

# Displaying all values
print(student.values())
```

---

## Output

```text
dict_values([101, 'Basha', 'Python'])
```

---

## Dry Run

```text
Dictionary

↓

values()

↓

101

↓

Basha

↓

Python
```

---

## Pseudocode

```text
BEGIN

Create Dictionary

Call values()

Display Values

END
```

---

## Line-by-Line Explanation

### Line 1

Creates a dictionary.

---

### Line 2

Calls `values()`.

---

### Line 3

Returns all values of the dictionary.

---

### Line 4

Displays the values.

---

## Real-World Applications

- Student Management Systems
- Employee Management Systems
- Banking Applications
- Inventory Management
- User Profile Management

---

## Best Practices

Use `values()` when only dictionary values are required.
