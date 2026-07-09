---

# Reversing a List Using Slicing

A list can be reversed using slicing.

---

## Program

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[::-1])
```

---

## Output

```text
[50, 40, 30, 20, 10]
```

---

## Explanation

The slicing operation starts from the last element and moves towards the first element using a step value of `-1`.

---

# Memory Representation

Example

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

```text
Original List

+-----------------------------------+

| 10 | 20 | 30 | 40 | 50 |

+-----------------------------------+

            │

            ▼

Sliced List

+----------------------+

| 20 | 30 | 40 |

+----------------------+
```

---

# Real-World Applications

List slicing is commonly used in:

- Extracting student records
- Displaying a range of products
- Pagination in applications
- Data analysis
- Report generation
- Splitting datasets

---

# Best Practices

- Use slicing to extract required elements efficiently.
- Remember that the stop index is excluded.
- Use `[:]` to create a copy of a list.
- Use `[::-1]` to reverse a list.
- Use step values carefully to avoid unexpected results.

---

# Summary

In this section, you learned:

- List Slicing
- Start Index
- Stop Index
- Step Value
- Copying a List
- Negative Index Slicing
- Reversing a List
- Memory Representation
- Real-World Applications
- Best Practices

List slicing is one of the most powerful features in Python for extracting and manipulating list elements efficiently.
