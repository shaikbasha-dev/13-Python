# List Methods

## Introduction

Python provides several built-in methods to perform operations on lists.

These methods make it easy to:

- Add elements
- Remove elements
- Search elements
- Count occurrences
- Sort data
- Reverse data
- Copy lists
- Clear list contents

Instead of writing lengthy code, these built-in methods perform common tasks efficiently.

---

# Categories of List Methods

```text
List Methods

│

├── Adding Elements

│      ├── append()

│      ├── extend()

│      └── insert()

│

├── Removing Elements

│      ├── remove()

│      ├── pop()

│      └── clear()

│

├── Searching

│      ├── index()

│      └── count()

│

├── Ordering

│      ├── sort()

│      └── reverse()

│

└── Copying

       └── copy()
```

---

# append()

## Definition

The `append()` method adds a single element to the **end** of the list.

---

## Why is append() Required?

Suppose an online shopping application stores products inside a list.

Whenever a customer adds a new product, the application must store it at the end of the cart.

The `append()` method performs this task efficiently.

---

## Syntax

```python
list.append(element)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| element | Element to be added |

---

## Return Value

Returns **None**.

The original list is modified.

---

## Program

```python
# Creating a list of programming languages
languages = ["Python", "Java"]

# Adding a new language
languages.append("C++")

# Displaying the updated list
print(languages)
```

---

## Output

```text
['Python', 'Java', 'C++']
```

---

## Dry Run

```text
Initial List

['Python', 'Java']

↓

append("C++")

↓

['Python', 'Java', 'C++']
```

---

## Memory Representation

Before

```text
+------------------------+

| Python | Java |

+------------------------+
```

After

```text
+--------------------------------+

| Python | Java | C++ |

+--------------------------------+
```

---

## Pseudocode

```text
BEGIN

Create List

Call append()

Display List

END
```

---

## Line-by-Line Explanation

### Line 1

Creates a list.

---

### Line 2

Calls `append()`.

---

### Line 3

Adds `"C++"` at the end.

---

### Line 4

Displays the updated list.

---

## Real-World Applications

- Shopping Cart
- Student Registration
- Attendance Systems
- Order Management
- Inventory Systems

---

## Best Practices

Use `append()` when adding **one element**.
