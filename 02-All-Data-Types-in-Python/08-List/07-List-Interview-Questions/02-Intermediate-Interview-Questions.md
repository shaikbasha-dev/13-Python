# Python List Interview Questions

## Intermediate Interview Questions

---

# Question 1

## What is the difference between append() and extend()?

### Answer

| append() | extend() |
|----------|-----------|
| Adds a single element | Adds multiple elements |
| Can add a nested list | Merges another iterable |
| Returns None | Returns None |

---

# Question 2

## What is the difference between append() and insert()?

### Answer

| append() | insert() |
|----------|-----------|
| Adds an element at the end | Adds an element at a specified index |
| Accepts one argument | Accepts index and element |
| Faster for end insertion | Used when position matters |

---

# Question 3

## What is the difference between remove() and pop()?

### Answer

| remove() | pop() |
|-----------|--------|
| Removes an element by value | Removes an element by index |
| Returns None | Returns the removed element |
| Raises ValueError if value is not found | Raises IndexError for an invalid index |

---

# Question 4

## What is the difference between sort() and reverse()?

### Answer

| sort() | reverse() |
|---------|-----------|
| Arranges elements in ascending order by default | Reverses the current order of elements |
| Changes element order based on value | Changes only the existing order |
| Modifies the original list | Modifies the original list |

---

# Question 5

## What is the difference between index() and count()?

### Answer

| index() | count() |
|----------|----------|
| Returns the index of the first occurrence | Returns the total number of occurrences |
| Used for searching position | Used for counting duplicates |

---

# Question 6

## What is the purpose of the copy() method?

### Answer

The `copy()` method creates a shallow copy of a list.

The copied list is a separate list object containing the same elements as the original list.

---

# Question 7

## Can a List contain another List?

### Answer

Yes.

A List can contain one or more lists as its elements.

### Example

```python
data = [10, 20, [30, 40], 50]

print(data)
```

---

# Question 8

## What happens if remove() is used for an element that does not exist?

### Answer

Python raises a `ValueError`.

### Example

```python
numbers = [10, 20, 30]

numbers.remove(50)
```

---

# Question 9

## What happens if pop() is used with an invalid index?

### Answer

Python raises an `IndexError`.

### Example

```python
numbers = [10, 20, 30]

numbers.pop(5)
```

---

# Question 10

## Can Lists store duplicate values?

### Answer

Yes.

Lists allow duplicate values and preserve the insertion order.

### Example

```python
numbers = [10, 20, 20, 30, 20]

print(numbers)
```
