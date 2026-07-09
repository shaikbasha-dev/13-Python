---

# reverse()

## Definition

The `reverse()` method reverses the order of elements in the list.

The original list is modified.

---

## Why is reverse() Required?

Suppose a music application stores recently played songs in a list.

To display the most recently played songs first, the list needs to be reversed.

The `reverse()` method performs this task efficiently.

---

## Syntax

```python
list.reverse()
```

---

## Parameters

This method does **not** take any parameters.

---

## Return Value

Returns **None**.

The original list is modified.

---

## Program

```python
# Creating a list
numbers = [10, 20, 30, 40]

# Reversing the list
numbers.reverse()

# Displaying the result
print(numbers)
```

---

## Output

```text
[40, 30, 20, 10]
```

---

## Dry Run

```text
Initial List

[10, 20, 30, 40]

↓

reverse()

↓

[40, 30, 20, 10]
```

---

## Memory Representation

Before

```text
+--------------------------------+

| 10 | 20 | 30 | 40 |

+--------------------------------+
```

After

```text
+--------------------------------+

| 40 | 30 | 20 | 10 |

+--------------------------------+
```

---

## Pseudocode

```text
BEGIN

Create List

Call reverse()

Display List

END
```

---

## Line-by-Line Explanation

### Line 1

Creates a list.

---

### Line 2

Calls `reverse()`.

---

### Line 3

Reverses the order of the elements.

---

### Line 4

Displays the reversed list.

---

## Real-World Applications

- Music Playlist
- Browser History
- Recent Activities
- Order History
- Navigation Systems

---

## Best Practices

Use `reverse()` when you need to reverse the original list.
