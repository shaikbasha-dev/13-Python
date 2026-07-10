---

# discard()

## Definition

The `discard()` method removes the specified element from a set.

If the element does not exist, no error is raised.

---

## Why is discard() Required?

Suppose an inventory system stores available product IDs in a set.

When a product is discontinued, the product ID can be removed safely even if it is not present.

The `discard()` method performs this task efficiently.

---

## Syntax

```python
set.discard(element)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| element | Element to be removed |

---

## Return Value

Returns **None**.

The original set is modified.

---

## Program

```python
# Creating a set
languages = {"Python", "Java", "C++"}

# Removing an element
languages.discard("Java")

# Displaying the updated set
print(languages)
```

---

## Output

```text
{'Python', 'C++'}
```

---

## Dry Run

```text
Initial Set

{'Python', 'Java', 'C++'}

↓

discard("Java")

↓

{'Python', 'C++'}
```

---

## Difference Between remove() and discard()

| remove() | discard() |
|-----------|------------|
| Raises `KeyError` if element is not found | Does not raise an error if element is not found |
| Used when element is guaranteed to exist | Used when element may or may not exist |

---

## Pseudocode

```text
BEGIN

Create Set

Call discard()

Display Set

END
```

---

## Line-by-Line Explanation

### Line 1

Creates a set.

---

### Line 2

Calls `discard()`.

---

### Line 3

Removes `"Java"` from the set if it exists.

---

### Line 4

Displays the updated set.

---

## Real-World Applications

- Inventory Management
- Student Registration
- Employee Records
- Access Control Systems
- Data Cleaning

---

## Best Practices

Use `discard()` when the element may or may not exist in the set.
