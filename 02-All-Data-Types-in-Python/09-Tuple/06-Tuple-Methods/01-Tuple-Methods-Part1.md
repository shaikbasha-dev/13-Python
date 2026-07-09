# Tuple Methods

## Introduction

Unlike lists, tuples are immutable.

Therefore, Python provides only two built-in methods for tuples.

These methods make it easy to:

- Count occurrences of an element
- Find the index of an element

---

# Categories of Tuple Methods

```text
Tuple Methods

│

├── Searching

│      ├── index()

│      └── count()
```

---

# index()

## Definition

The `index()` method returns the index position of the **first occurrence** of the specified element in the tuple.

---

## Why is index() Required?

Suppose a company stores employee IDs in a tuple.

When we need to find the position of a particular employee ID, the `index()` method helps locate the element efficiently.

---

## Syntax

```python
tuple.index(element)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| element | Element to search |

---

## Return Value

Returns the index of the first matching element.

---

## Program

```python
# Creating a tuple
languages = ("Python", "Java", "C++", "Java")

# Finding the index of Java
position = languages.index("Java")

# Displaying the result
print(position)
```

---

## Output

```text
1
```

---

## Dry Run

```text
Initial Tuple

('Python', 'Java', 'C++', 'Java')

↓

index("Java")

↓

1
```

---

## Memory Representation

```text
+------------------------------------------+

| Python | Java | C++ | Java |

+------------------------------------------+

    0        1      2      3
```

---

## Pseudocode

```text
BEGIN

Create Tuple

Call index()

Display Index

END
```

---

## Line-by-Line Explanation

### Line 1

Creates a tuple.

---

### Line 2

Calls `index()`.

---

### Line 3

Stores the returned index.

---

### Line 4

Displays the index value.

---

## Real-World Applications

- Student Management Systems
- Employee Records
- Product Search
- Inventory Systems
- Attendance Systems

---

## Best Practices

Use `index()` when the position of an element is required.
