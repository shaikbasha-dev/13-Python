# Set Methods

## Introduction

Python provides several built-in methods to perform operations on sets.

These methods make it easy to:

- Add elements
- Add multiple elements
- Remove elements
- Delete arbitrary elements
- Clear the set
- Copy the set

---

# Categories of Set Methods

```text
Set Methods

│

├── Adding Elements

│      ├── add()

│      └── update()

│

├── Removing Elements

│      ├── remove()

│      ├── discard()

│      ├── pop()

│      └── clear()

│

└── Copying

       └── copy()
```

---

# add()

## Definition

The `add()` method adds a single element to a set.

If the element already exists, it is not added again.

---

## Why is add() Required?

Suppose an employee management system stores employee IDs in a set.

Whenever a new employee joins the company, the new employee ID should be added to the set.

The `add()` method performs this task efficiently.

---

## Syntax

```python
set.add(element)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| element | Element to be added |

---

## Return Value

Returns **None**.

The original set is modified.

---

## Program

```python
# Creating a set
languages = {"Python", "Java"}

# Adding a new element
languages.add("C++")

# Displaying the updated set
print(languages)
```

---

## Output

```text
{'Python', 'Java', 'C++'}
```

---

## Dry Run

```text
Initial Set

{'Python', 'Java'}

↓

add("C++")

↓

{'Python', 'Java', 'C++'}
```

---

## Pseudocode

```text
BEGIN

Create Set

Call add()

Display Set

END
```

---

## Line-by-Line Explanation

### Line 1

Creates a set.

---

### Line 2

Calls `add()`.

---

### Line 3

Adds `"C++"` to the set.

---

### Line 4

Displays the updated set.

---

## Real-World Applications

- Employee Management
- Student Registration
- Inventory Systems
- Library Management
- Access Control Systems

---

## Best Practices

Use `add()` when adding a single element to a set.
