---

# sort()

## Definition

The `sort()` method arranges the elements of a list in **ascending order** by default.

It can also arrange elements in descending order.

---

## Why is sort() Required?

Suppose a school stores student marks in a list.

To display the marks in ascending or descending order, the `sort()` method is used.

---

## Syntax

```python
list.sort()

list.sort(reverse=True)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| reverse (Optional) | If `True`, sorts the list in descending order |

---

## Return Value

Returns **None**.

The original list is modified.

---

## Program

```python
# Creating a list
numbers = [40, 10, 30, 20]

# Sorting the list
numbers.sort()

# Displaying the result
print(numbers)
```

---

## Output

```text
[10, 20, 30, 40]
```

---

## Program (Descending Order)

```python
# Creating a list
numbers = [40, 10, 30, 20]

# Sorting the list in descending order
numbers.sort(reverse=True)

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

[40, 10, 30, 20]

↓

sort()

↓

[10, 20, 30, 40]
```

---

## Memory Representation

Before

```text
+--------------------------------+

| 40 | 10 | 30 | 20 |

+--------------------------------+
```

After

```text
+--------------------------------+

| 10 | 20 | 30 | 40 |

+--------------------------------+
```

---

## Pseudocode

```text
BEGIN

Create List

Call sort()

Display List

END
```

---

## Line-by-Line Explanation

### Line 1

Creates a list.

---

### Line 2

Calls `sort()`.

---

### Line 3

Sorts the elements in ascending order.

---

### Line 4

Displays the sorted list.

---

## Real-World Applications

- Student Result Analysis
- Employee Salary Records
- Product Price Sorting
- Inventory Management
- Ranking Systems

---

## Best Practices

- Use `sort()` to sort the original list.
- Use `reverse=True` to sort the list in descending order.
