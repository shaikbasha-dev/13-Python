---

# remove()

## Definition

The `remove()` method removes the **first occurrence** of the specified element from the list.

---

## Why is remove() Required?

Suppose an online shopping application stores products inside a shopping cart.

When a customer removes a product, the application must delete that product from the list.

The `remove()` method performs this task efficiently.

---

## Syntax

```python
list.remove(element)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| element | Element to be removed |

---

## Return Value

Returns **None**.

The original list is modified.

---

## Program

```python
# Creating a list
languages = ["Python", "Java", "C++"]

# Removing an element
languages.remove("Java")

# Displaying result
print(languages)
```

---

## Output

```text
['Python', 'C++']
```

---

## Dry Run

```text
Initial List

['Python', 'Java', 'C++']

↓

remove("Java")

↓

['Python', 'C++']
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

| Python | C++ |

+--------------------------+
```

---

## Pseudocode

```text
BEGIN

Create List

Call remove()

Display List

END
```

---

## Line-by-Line Explanation

### Line 1

Creates a list.

---

### Line 2

Calls `remove()`.

---

### Line 3

Removes `"Java"` from the list.

---

### Line 4

Displays the updated list.

---

## Real-World Applications

- Shopping Cart
- Student Registration
- Employee Management
- Inventory Systems
- Library Management

---

## Best Practices

Use `remove()` when the element value is known.
