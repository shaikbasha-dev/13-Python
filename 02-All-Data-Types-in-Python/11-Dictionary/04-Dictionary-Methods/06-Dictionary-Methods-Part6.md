---

# clear()

## Definition

The `clear()` method removes all key-value pairs from the dictionary.

After calling this method, the dictionary becomes empty.

---

## Why is clear() Required?

Suppose a shopping application stores items in a customer's cart using a dictionary.

After the order is successfully placed, all cart items need to be removed.

The `clear()` method performs this task efficiently.

---

## Syntax

```python
dictionary.clear()
```

---

## Parameters

This method does **not** take any parameters.

---

## Return Value

Returns **None**.

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

# Clearing the dictionary
student.clear()

# Displaying the updated dictionary
print(student)
```

---

## Output

```text
{}
```

---

## Dry Run

```text
Initial Dictionary

{
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

↓

clear()

↓

{}
```

---

## Pseudocode

```text
BEGIN

Create Dictionary

Call clear()

Display Dictionary

END
```

---

## Line-by-Line Explanation

### Line 1

Creates a dictionary.

---

### Line 2

Calls the `clear()` method.

---

### Line 3

Removes all key-value pairs from the dictionary.

---

### Line 4

Displays the empty dictionary.

---

## Real-World Applications

- Shopping Cart Management
- Student Management Systems
- Employee Records
- Banking Applications
- Cache Management

---

## Best Practices

Use `clear()` when all key-value pairs need to be removed while keeping the dictionary object available.
