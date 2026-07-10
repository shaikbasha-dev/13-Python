---

# Question 31

## Merge Two Dictionaries

### Problem Statement

Write a Python program to merge two dictionaries.

---

### Program

```python
student1 = {
    "id": 101,
    "name": "Basha"
}

student2 = {
    "course": "Python",
    "marks": 95
}

student1.update(student2)

print(student1)
```

---

### Output

```text
{'id': 101, 'name': 'Basha', 'course': 'Python', 'marks': 95}
```

---

# Question 32

## Find the Total of Numeric Values

### Problem Statement

Write a Python program to calculate the sum of all numeric values in a dictionary.

---

### Program

```python
marks = {
    "Java": 90,
    "Python": 95,
    "SQL": 85
}

print(sum(marks.values()))
```

---

### Output

```text
270
```

---

# Question 33

## Find the Highest Value

### Problem Statement

Write a Python program to find the highest value in a dictionary.

---

### Program

```python
marks = {
    "Java": 90,
    "Python": 95,
    "SQL": 85
}

print(max(marks.values()))
```

---

### Output

```text
95
```

---

# Question 34

## Find the Lowest Value

### Problem Statement

Write a Python program to find the lowest value in a dictionary.

---

### Program

```python
marks = {
    "Java": 90,
    "Python": 95,
    "SQL": 85
}

print(min(marks.values()))
```

---

### Output

```text
85
```

---

# Question 35

## Display Dictionary in Sorted Key Order

### Problem Statement

Write a Python program to display dictionary keys in sorted order.

---

### Program

```python
student = {
    "course": "Python",
    "id": 101,
    "name": "Basha"
}

for key in sorted(student.keys()):
    print(key, ":", student[key])
```

---

### Output

```text
course : Python
id : 101
name : Basha
```

---

# Question 36

## Count Numeric Values

### Problem Statement

Write a Python program to count numeric values in a dictionary.

---

### Program

```python
data = {
    "a": 10,
    "b": "Python",
    "c": 20,
    "d": 30
}

count = 0

for value in data.values():
    if isinstance(value, (int, float)):
        count += 1

print(count)
```

---

### Output

```text
3
```

---

# Question 37

## Convert Keys to a List

### Problem Statement

Write a Python program to convert all dictionary keys into a list.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

print(list(student.keys()))
```

---

### Output

```text
['id', 'name', 'course']
```

---

# Question 38

## Convert Values to a List

### Problem Statement

Write a Python program to convert all dictionary values into a list.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

print(list(student.values()))
```

---

### Output

```text
[101, 'Basha', 'Python']
```

---

# Question 39

## Convert Items to a List

### Problem Statement

Write a Python program to convert all key-value pairs into a list.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha"
}

print(list(student.items()))
```

---

### Output

```text
[('id', 101), ('name', 'Basha')]
```

---

# Question 40

## Display Dictionary Using items()

### Problem Statement

Write a Python program to display all key-value pairs using the `items()` method.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

for key, value in student.items():
    print(key, ":", value)
```

---

### Output

```text
id : 101
name : Basha
course : Python
```

---

# Summary

In this section, you learned coding interview questions on:

- Dictionary Creation
- Accessing Values
- Adding and Updating Key-Value Pairs
- Searching Keys and Values
- Dictionary Traversal
- `get()`
- `keys()`
- `values()`
- `items()`
- `pop()`
- `clear()`
- `copy()`
- Dictionary Merging
- Numeric Value Processing

These coding questions help strengthen problem-solving skills and prepare you for Python technical interviews.
