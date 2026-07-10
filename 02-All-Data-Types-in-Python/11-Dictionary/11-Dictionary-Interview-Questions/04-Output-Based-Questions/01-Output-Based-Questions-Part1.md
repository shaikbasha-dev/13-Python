# Python Dictionary Output-Based Interview Questions

## Introduction

This document contains output-based interview questions on Python Dictionaries.

These questions help improve logical thinking and understanding of Python Dictionary concepts.

---

# Question 1

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

print(student)
```

### Output

```text
{'id': 101, 'name': 'Basha'}
```

---

# Question 2

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

print(student["name"])
```

### Output

```text
Basha
```

---

# Question 3

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

student["course"] = "Python"

print(student)
```

### Output

```text
{'id': 101, 'name': 'Basha', 'course': 'Python'}
```

---

# Question 4

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Java"
}

student["course"] = "Python"

print(student)
```

### Output

```text
{'id': 101, 'name': 'Basha', 'course': 'Python'}
```

---

# Question 5

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

print(student.get("course"))
```

### Output

```text
Python
```

---

# Question 6

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

print(student.get("salary"))
```

### Output

```text
None
```

---

# Question 7

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

print(len(student))
```

### Output

```text
2
```

---

# Question 8

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

print(type(student))
```

### Output

```text
<class 'dict'>
```

---

# Question 9

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

print(student.keys())
```

### Output

```text
dict_keys(['id', 'name'])
```

---

# Question 10

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

print(student.values())
```

### Output

```text
dict_values([101, 'Basha'])
```
