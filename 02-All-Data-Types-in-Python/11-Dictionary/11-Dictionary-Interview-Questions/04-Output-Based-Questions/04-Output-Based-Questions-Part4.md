---

# Question 31

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

print(list(student.items()))
```

### Output

```text
[('id', 101), ('name', 'Basha')]
```

---

# Question 32

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

student.pop("name")

print(student)
```

### Output

```text
{'id': 101}
```

---

# Question 33

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

student.clear()

print(len(student))
```

### Output

```text
0
```

---

# Question 34

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

new_student = student.copy()

print(new_student == student)
```

### Output

```text
True
```

---

# Question 35

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

print(type(student.keys()))
```

### Output

```text
<class 'dict_keys'>
```

---

# Question 36

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

print(type(student.values()))
```

### Output

```text
<class 'dict_values'>
```

---

# Question 37

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

print(type(student.items()))
```

### Output

```text
<class 'dict_items'>
```

---

# Question 38

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

print(bool(student))
```

### Output

```text
True
```

---

# Question 39

## Predict the Output

```python
student = {}

print(bool(student))
```

### Output

```text
False
```

---

# Question 40

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

print("id" in student.keys())
```

### Output

```text
True
```

---

# Summary

In this section, you learned output-based interview questions on:

- Dictionary Creation
- Value Access
- get()
- keys()
- values()
- items()
- pop()
- clear()
- copy()
- Membership Operators
- Dictionary Traversal
- Built-in Functions

These output-based questions help improve logical thinking and prepare you for Python technical interviews.
