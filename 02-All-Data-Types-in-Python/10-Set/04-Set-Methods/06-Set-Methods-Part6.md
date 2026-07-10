---

# clear()

## Definition

The `clear()` method removes all elements from the set.

After calling this method, the set becomes empty.

---

## Why is clear() Required?

Suppose an online registration system stores all registered users in a set.

After the registration session ends, all temporary records need to be removed.

The `clear()` method performs this task efficiently.

---

## Syntax

```python
set.clear()
```

---

## Parameters

This method does **not** take any parameters.

---

## Return Value

Returns **None**.

The original set is modified.

---

## Program

```python
# Creating a set
languages = {"Python", "Java", "C++"}

# Clearing the set
languages.clear()

# Displaying the updated set
print(languages)
```

---

## Output

```text
set()
```

---

## Dry Run

```text
Initial Set

{'Python', 'Java', 'C++'}

↓

clear()

↓

set()
```

---

## Pseudocode

```text
BEGIN

Create Set

Call clear()

Display Set

END
```

---

## Line-by-Line Explanation

### Line 1

Creates a set.

---

### Line 2

Calls `clear()`.

---

### Line 3

Removes all elements from the set.

---

### Line 4

Displays the empty set.

---

## Real-World Applications

- Registration Systems
- Shopping Cart Management
- Inventory Systems
- Cache Management
- Temporary Data Storage

---

## Best Practices

Use `clear()` when all elements of a set need to be removed without deleting the set object.
