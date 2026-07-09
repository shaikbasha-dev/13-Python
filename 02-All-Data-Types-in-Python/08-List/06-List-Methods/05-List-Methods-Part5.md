---

# pop()

## Definition

The `pop()` method removes and returns the element at the specified index.

If no index is specified, it removes the last element.

---

## Why is pop() Required?

Suppose an application maintains a list of recently opened files.

Whenever the user closes the latest file, the application removes the last file from the list.

The `pop()` method performs this task efficiently.

---

## Syntax

```python
list.pop(index)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| index (Optional) | Position of the element to remove |

---

## Return Value

Returns the removed element.

The original list is modified.

---

## Program

```python
# Creating a list
languages = ["Python", "Java", "C++"]

# Removing the last element
removed_element = languages.pop()

# Displaying removed element
print(removed_element)

# Displaying updated list
print(languages)
```

---

## Output

```text
C++

['Python', 'Java']
```

---

## Dry Run

```text
Initial List

['Python', 'Java', 'C++']

↓

pop()

↓

Removed Element

'C++'

↓

Updated List

['Python', 'Java']
```

---

## Memory Representation

Before

```text
+--------------------------------+

| Python | Java | C++ |

+--------------------------------+
```

After

```text
+--------------------------+

| Python | Java |

+--------------------------+
```

---

## Pseudocode

```text
BEGIN

Create List

Call pop()

Store removed element

Display removed element

Display updated list

END
```

---

## Line-by-Line Explanation

### Line 1

Creates a list.

---

### Line 2

Calls `pop()`.

---

### Line 3

Stores the removed element.

---

### Line 4

Displays the removed element.

---

### Line 5

Displays the updated list.

---

## Real-World Applications

- Undo Operations
- Browser History
- Stack Implementation
- Recently Opened Files
- Task Management

---

## Best Practices

- Use `pop()` when the position of the element is known.
- If no index is specified, `pop()` removes the last element.
