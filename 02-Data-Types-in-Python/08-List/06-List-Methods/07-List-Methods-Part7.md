---

# index()

## Definition

The `index()` method returns the index position of the **first occurrence** of the specified element in the list.

---

## Why is index() Required?

Suppose a school stores student names in a list.

When we need to find the position of a particular student, the `index()` method helps locate the student's index efficiently.

---

## Syntax

```python
list.index(element)
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
# Creating a list
languages = ["Python", "Java", "C++", "Java"]

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
Initial List

['Python', 'Java', 'C++', 'Java']

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

Create List

Call index()

Display Index

END
```

---

## Line-by-Line Explanation

### Line 1

Creates a list.

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
