---

# insert()

## Definition

The `insert()` method inserts an element at a specified index.

---

## Syntax

```python
list.insert(index, element)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| index | Position |
| element | Value to insert |

---

## Program

```python
# Creating a list
numbers = [10, 20, 40]

# Inserting 30
numbers.insert(2, 30)

# Displaying result
print(numbers)
```

---

## Output

```text
[10, 20, 30, 40]
```

---

## Dry Run

```text
Original

10 20 40

↓

Insert 30 at Index 2

↓

10 20 30 40
```

---

## Real-World Applications

- Student Ranking
- Priority Queues
- Playlist Management
- Task Scheduling

---

## Internal Working

When Python executes

```python
numbers.insert(2, 30)
```

Internally,

```text
Interpreter Reads Statement

↓

Locate List Object

↓

Shift Existing Elements

↓

Insert New Element

↓

Update List

↓

Execution Complete
```

---

## Best Practices

- Use `insert()` when position matters.
- Use `append()` if inserting at the end.

---

# Summary

In this section, you learned:

- `append()`
- `extend()`
- `insert()`
- Their syntax
- Parameters
- Internal working
- Memory representation
- Practical examples
- Best practices
- Real-world applications
