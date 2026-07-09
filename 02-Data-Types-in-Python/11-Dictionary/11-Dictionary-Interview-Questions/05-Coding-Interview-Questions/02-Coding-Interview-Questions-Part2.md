---

# Question 11

## Traverse Dictionary Using keys()

### Problem Statement

Write a Python program to traverse all keys of a dictionary.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

for key in student.keys():
    print(key)
```

---

### Output

```text
id
name
course
```

---

# Question 12

## Traverse Dictionary Using values()

### Problem Statement

Write a Python program to traverse all values of a dictionary.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

for value in student.values():
    print(value)
```

---

### Output

```text
101
Basha
Python
```

---

# Question 13

## Traverse Dictionary Using items()

### Problem Statement

Write a Python program to traverse all key-value pairs of a dictionary.

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

# Question 14

## Check Whether a Key Exists

### Problem Statement

Write a Python program to check whether a key exists in a dictionary.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha"
}

if "name" in student:
    print("Key Found")
else:
    print("Key Not Found")
```

---

### Output

```text
Key Found
```

---

# Question 15

## Check Whether a Key Does Not Exist

### Problem Statement

Write a Python program to check whether a key does not exist in a dictionary.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha"
}

if "salary" not in student:
    print("Key Not Found")
else:
    print("Key Found")
```

---

### Output

```text
Key Not Found
```

---

# Question 16

## Create a Copy of a Dictionary

### Problem Statement

Write a Python program to create a copy of a dictionary.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha"
}

new_student = student.copy()

print(new_student)
```

---

### Output

```text
{'id': 101, 'name': 'Basha'}
```

---

# Question 17

## Clear a Dictionary

### Problem Statement

Write a Python program to remove all key-value pairs from a dictionary.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha"
}

student.clear()

print(student)
```

---

### Output

```text
{}
```

---

# Question 18

## Display Dictionary Size

### Problem Statement

Write a Python program to display the total number of key-value pairs in a dictionary.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python",
    "marks": 95
}

print(len(student))
```

---

### Output

```text
4
```

---

# Question 19

## Update Multiple Values

### Problem Statement

Write a Python program to update multiple values in a dictionary.

---

### Program

```python
student = {
    "name": "Basha",
    "course": "Java"
}

student["course"] = "Python"
student["city"] = "Hyderabad"

print(student)
```

---

### Output

```text
{'name': 'Basha', 'course': 'Python', 'city': 'Hyderabad'}
```

---

# Question 20

## Access All Values One by One

### Problem Statement

Write a Python program to access and display all values one by one.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}

for value in student.values():
    print(value)
```

---

### Output

```text
101
Basha
Python
```
