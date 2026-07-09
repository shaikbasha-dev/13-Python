---

# IndexError

## Definition

If we try to access an index that does not exist in the list, Python raises an **IndexError**.

---

## Program

```python
languages = ["Python", "Java", "C++"]

print(languages[5])
```

---

## Output

```text
IndexError: list index out of range
```

---

## Explanation

The list contains only three elements.

Valid positive indexes are:

```text
0
1
2
```

Since index `5` does not exist, Python raises an `IndexError`.

---

# Real-World Applications

List indexing is commonly used in:

- Student Record Management
- Employee Management Systems
- Shopping Cart Applications
- Attendance Systems
- Inventory Management
- Banking Applications
- Library Management Systems

---

# Best Practices

- Always ensure the index is within the valid range.
- Use positive indexing when accessing elements from the beginning.
- Use negative indexing when accessing elements from the end.
- Avoid accessing indexes that do not exist.

---

# Summary

In this section, you learned:

- Positive Indexing
- Negative Indexing
- Accessing Elements Using Indexes
- IndexError
- Real-World Applications
- Best Practices

Indexing is one of the fundamental concepts used for accessing elements efficiently in Python lists.
