---

# copy()

## Definition

The `copy()` method creates a shallow copy of a set.

The copied set is a new set object containing the same elements as the original set.

---

## Why is copy() Required?

Suppose an inventory management system needs to create a backup of the current inventory before making updates.

Instead of modifying the original set, a copy is created.

The `copy()` method performs this task efficiently.

---

## Syntax

```python
set.copy()
```

---

## Parameters

This method does **not** take any parameters.

---

## Return Value

Returns a shallow copy of the set.

---

## Program

```python
# Creating a set
languages = {"Python", "Java", "C++"}

# Copying the set
new_set = languages.copy()

# Displaying both sets
print("Original Set :", languages)

print("Copied Set :", new_set)
```

---

## Output

```text
Original Set : {'Python', 'Java', 'C++'}

Copied Set : {'Python', 'Java', 'C++'}
```

---

## Dry Run

```text
Original Set

{'Python', 'Java', 'C++'}

↓

copy()

↓

Copied Set

{'Python', 'Java', 'C++'}
```

---

## Pseudocode

```text
BEGIN

Create Set

Call copy()

Store copied set

Display original set

Display copied set

END
```

---

## Line-by-Line Explanation

### Line 1

Creates a set.

---

### Line 2

Calls `copy()`.

---

### Line 3

Stores the copied set in a new variable.

---

### Line 4

Displays the original set.

---

### Line 5

Displays the copied set.

---

## Real-World Applications

- Data Backup
- Inventory Management
- Student Records
- Employee Management
- Report Generation

---

## Best Practices

Use `copy()` when a duplicate set is required without modifying the original set.

---

# Summary

In this section, you learned:

- `add()`
- `update()`
- `remove()`
- `discard()`
- `pop()`
- `clear()`
- `copy()`
- Their syntax
- Parameters
- Return values
- Practical examples
- Best Practices
- Real-World Applications
