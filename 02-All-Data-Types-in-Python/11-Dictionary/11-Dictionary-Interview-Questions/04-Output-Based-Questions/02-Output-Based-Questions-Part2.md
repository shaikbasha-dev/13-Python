# Question 11

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

print(student.items())
```

### Output

```text
dict_items([('id', 101), ('name', 'Basha')])
```

---

# Question 12

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

removed = student.pop("course")

print(removed)
```

### Output

```text
Python
```

---

# Question 13

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

student.clear()

print(student)
```

### Output

```text
{}
```

---

# Question 14

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

new_student = student.copy()

print(new_student)
```

### Output

```text
{'id': 101, 'name': 'Basha'}
```

---

# Question 15

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

print("name" in student)
```

### Output

```text
True
```

---

# Question 16

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

print("salary" not in student)
```

### Output

```text
True
```

---

# Question 17

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

for key in student:
    print(key)
```

### Output

```text
id
name
```

---

# Question 18

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

for value in student.values():
    print(value)
```

### Output

```text
101
Basha
```

---

# Question 19

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

for key, value in student.items():
    print(key, value)
```

### Output

```text
id 101
name Basha
```

---

# Question 20

## Predict the Output

```python
student = {
    "id": 101,
    "name": "Basha"
}

print(dict(student))
```

### Output

```text
{'id': 101, 'name': 'Basha'}
```
