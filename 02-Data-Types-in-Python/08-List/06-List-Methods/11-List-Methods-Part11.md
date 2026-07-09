---

# copy()

## Definition

The `copy()` method creates a shallow copy of the list.

The copied list is a new list object containing the same elements as the original list.

---

## Why is copy() Required?

Suppose an application needs to create a backup of a list before making any modifications.

Instead of changing the original list, a copy is created.

The `copy()` method performs this task efficiently.

---

## Syntax

```python
list.copy()
```

---

## Parameters

This method does **not** take any parameters.

---

## Return Value

Returns a shallow copy of the list.

---

## Program

```python
# Creating a list
languages = ["Python", "Java", "C++"]

# Copying the list
new_list = languages.copy()

# Displaying both lists
print("Original List :", languages)

print("Copied List :", new_list)
```

---

## Output

```text
Original List : ['Python', 'Java', 'C++']

Copied List : ['Python', 'Java', 'C++']
```

---

## Dry Run

```text
Original List

['Python', 'Java', 'C++']

↓

copy()

↓

Copied List

['Python', 'Java', 'C++']
```

---

## Memory Representation

Before

```text
Original List

+--------------------------------+

| Python | Java | C++ |

+--------------------------------+
```

After

```text
Original List

+--------------------------------+

| Python | Java | C++ |

+--------------------------------+

            │

            │ copy()

            ▼

Copied List

+--------------------------------+

| Python | Java | C++ |

+--------------------------------+
```

---

## Pseudocode

```text
BEGIN

Create List

Call copy()

Store copied list

Display original list

Display copied list

END
```

---

## Line-by-Line Explanation

### Line 1

Creates a list.

---

### Line 2

Calls `copy()`.

---

### Line 3

Stores the copied list in a new variable.

---

### Line 4

Displays the original list.

---

### Line 5

Displays the copied list.

---

## Real-World Applications

- Data Backup
- Inventory Management
- Student Records
- Shopping Cart
- Report Generation

---

## Best Practices

Use `copy()` when a duplicate list is required without modifying the original list.

---

# Summary

In this section, you learned:

- `append()`
- `extend()`
- `insert()`
- `remove()`
- `pop()`
- `clear()`
- `index()`
- `count()`
- `sort()`
- `reverse()`
- `copy()`
- Their syntax
- Parameters
- Return values
- Internal working
- Memory representation
- Practical examples
- Best practices
- Real-World Applications
