---

# update()

## Definition

The `update()` method adds multiple elements from another iterable into a set.

Duplicate values are ignored automatically.

---

## Why is update() Required?

Suppose an employee management system maintains two sets of employee IDs.

When employees from another branch join the main branch, all employee IDs need to be added together.

The `update()` method performs this task efficiently.

---

## Syntax

```python
set.update(iterable)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| iterable | List, Tuple, Set, etc. |

---

## Return Value

Returns **None**.

The original set is modified.

---

## Program

```python
# Creating sets
set1 = {"Python", "Java"}

set2 = {"C++", "JavaScript"}

# Updating set1
set1.update(set2)

# Displaying the updated set
print(set1)
```

---

## Output

```text
{'Python', 'Java', 'C++', 'JavaScript'}
```

---

## Dry Run

```text
Initial Set

{'Python', 'Java'}

↓

update({"C++", "JavaScript"})

↓

{'Python', 'Java', 'C++', 'JavaScript'}
```

---

## Pseudocode

```text
BEGIN

Create Set1

Create Set2

Call update()

Display Updated Set

END
```

---

## Line-by-Line Explanation

### Line 1

Creates the first set.

---

### Line 2

Creates the second set.

---

### Line 3

Calls `update()`.

---

### Line 4

Adds all unique elements from the second set into the first set.

---

### Line 5

Displays the updated set.

---

## Real-World Applications

- Employee Management
- Student Registration
- Inventory Management
- Contact Management
- Data Merging

---

## Best Practices

Use `update()` when adding multiple elements to a set at once.
