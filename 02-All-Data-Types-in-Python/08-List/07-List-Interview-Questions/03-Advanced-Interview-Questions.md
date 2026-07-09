# Python List Interview Questions

## Advanced Interview Questions

---

# Question 1

## What is the difference between a shallow copy and a deep copy?

### Answer

| Shallow Copy | Deep Copy |
|--------------|-----------|
| Copies only the outer object | Copies the outer object and all nested objects |
| Nested objects are shared | Nested objects are copied independently |
| Created using `copy()` | Created using `deepcopy()` |

---

# Question 2

## Is a List mutable?

### Answer

Yes.

Lists are mutable, which means their elements can be modified after creation.

---

# Question 3

## Can a List store duplicate values?

### Answer

Yes.

Lists allow duplicate values.

---

# Question 4

## Can a List store different data types?

### Answer

Yes.

A List can store elements of different data types.

### Example

```python
data = [10, "Python", 25.5, True]
```

---

# Question 5

## What happens if an invalid index is accessed?

### Answer

Python raises an `IndexError`.

### Example

```python
numbers = [10, 20, 30]

print(numbers[5])
```

---

# Question 6

## What happens if index() cannot find an element?

### Answer

Python raises a `ValueError`.

### Example

```python
languages = ["Python", "Java"]

print(languages.index("C++"))
```

---

# Question 7

## Which methods modify the original List?

### Answer

The following methods modify the original list:

- append()
- extend()
- insert()
- remove()
- pop()
- clear()
- sort()
- reverse()

---

# Question 8

## Which method creates a copy of a List?

### Answer

The `copy()` method creates a shallow copy of a list.

---

# Question 9

## Which method returns the index of an element?

### Answer

The `index()` method returns the index of the first occurrence of the specified element.

---

# Question 10

## Which method returns the number of occurrences of an element?

### Answer

The `count()` method returns the total number of occurrences of the specified element.
