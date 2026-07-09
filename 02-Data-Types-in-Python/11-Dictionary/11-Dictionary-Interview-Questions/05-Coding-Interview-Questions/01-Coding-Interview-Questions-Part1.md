# Python Dictionary Coding Interview Questions

## Introduction

This document contains coding-based interview questions on Python Dictionaries.

These questions help improve problem-solving skills and prepare for Python technical interviews.

Each question includes:

- Problem Statement
- Program
- Output

---

# Question 1

## Create a Dictionary

### Problem Statement

Write a Python program to create and display a dictionary.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

print(student)
```

---

### Output

```text
{'id': 101, 'name': 'Basha', 'course': 'Python'}
```

---

# Question 2

## Access a Value Using a Key

### Problem Statement

Write a Python program to access a value from a dictionary using its key.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

print(student["name"])
```

---

### Output

```text
Basha
```

---

# Question 3

## Add a New Key-Value Pair

### Problem Statement

Write a Python program to add a new key-value pair to a dictionary.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha"
}

student["course"] = "Python"

print(student)
```

---

### Output

```text
{'id': 101, 'name': 'Basha', 'course': 'Python'}
```

---

# Question 4

## Update an Existing Value

### Problem Statement

Write a Python program to update the value of an existing key.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Java"
}

student["course"] = "Python"

print(student)
```

---

### Output

```text
{'id': 101, 'name': 'Basha', 'course': 'Python'}
```

---

# Question 5

## Retrieve a Value Using get()

### Problem Statement

Write a Python program to retrieve a value using the `get()` method.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha"
}

print(student.get("name"))
```

---

### Output

```text
Basha
```

---

# Question 6

## Remove a Key Using pop()

### Problem Statement

Write a Python program to remove a key-value pair using the `pop()` method.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

student.pop("course")

print(student)
```

---

### Output

```text
{'id': 101, 'name': 'Basha'}
```

---

# Question 7

## Display All Keys

### Problem Statement

Write a Python program to display all keys of a dictionary.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

print(student.keys())
```

---

### Output

```text
dict_keys(['id', 'name', 'course'])
```

---

# Question 8

## Display All Values

### Problem Statement

Write a Python program to display all values of a dictionary.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

print(student.values())
```

---

### Output

```text
dict_values([101, 'Basha', 'Python'])
```

---

# Question 9

## Display All Key-Value Pairs

### Problem Statement

Write a Python program to display all key-value pairs of a dictionary.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

print(student.items())
```

---

### Output

```text
dict_items([('id', 101), ('name', 'Basha'), ('course', 'Python')])
```

---

# Question 10

## Count the Number of Key-Value Pairs

### Problem Statement

Write a Python program to count the number of key-value pairs in a dictionary.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

print(len(student))
```

---

### Output

```text
3
```
