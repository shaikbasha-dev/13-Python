---

# clear()

## Definition

The `clear()` method removes **all elements** from the list.

After calling this method, the list becomes empty.

---

## Why is clear() Required?

Suppose an online shopping application stores products inside a shopping cart.

After the customer successfully places an order, the shopping cart should become empty.

The `clear()` method performs this task efficiently.

---

## Syntax

```python
list.clear()
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
languages = ["Python", "Java", "C++"]

# Clearing the list
languages.clear()

# Displaying the updated list
print(languages)
```

---

## Output

```text
[]
```

---

## Dry Run

```text
Initial List

['Python', 'Java', 'C++']

↓

clear()

↓

[]
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
+------------+

|            |

+------------+
```

---

## Pseudocode

```text
BEGIN

Create List

Call clear()

Display List

END
```

---

## Line-by-Line Explanation

### Line 1

Creates a list.

---

### Line 2

Calls `clear()`.

---

### Line 3

Removes all elements from the list.

---

### Line 4

Displays the empty list.

---

## Real-World Applications

- Shopping Cart
- Student Registration
- Attendance Systems
- Inventory Systems
- Temporary Data Storage

---

## Best Practices

Use `clear()` when all elements of a list need to be removed without deleting the list object.
