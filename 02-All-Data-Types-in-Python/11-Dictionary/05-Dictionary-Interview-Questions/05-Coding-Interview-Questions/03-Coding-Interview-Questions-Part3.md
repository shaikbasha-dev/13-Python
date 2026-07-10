---

# Question 21

## Count the Number of Keys Without Using len()

### Problem Statement

Write a Python program to count the number of keys in a dictionary without using the `len()` function.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python",
    "marks": 95
}

count = 0

for key in student:
    count += 1

print(count)
```

---

### Output

```text
4
```

---

# Question 22

## Check Whether a Dictionary is Empty

### Problem Statement

Write a Python program to check whether a dictionary is empty.

---

### Program

```python
student = {}

if len(student) == 0:
    print("Dictionary is Empty")
else:
    print("Dictionary is Not Empty")
```

---

### Output

```text
Dictionary is Empty
```

---

# Question 23

## Search for a Key

### Problem Statement

Write a Python program to search for a key in a dictionary.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha"
}

key = "name"

if key in student:
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

# Question 24

## Search for a Value

### Problem Statement

Write a Python program to search for a value in a dictionary.

---

### Program

```python
student = {
    "id": 101,
    "name": "Basha"
}

value = "Basha"

if value in student.values():
    print("Value Found")
else:
    print("Value Not Found")
```

---

### Output

```text
Value Found
```

---

# Question 25

## Display Only Keys

### Problem Statement

Write a Python program to display only the keys of a dictionary.

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

# Question 26

## Display Only Values

### Problem Statement

Write a Python program to display only the values of a dictionary.

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

# Question 27

## Display Key-Value Pairs

### Problem Statement

Write a Python program to display all key-value pairs.

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

# Question 28

## Remove a Key-Value Pair

### Problem Statement

Write a Python program to remove a key-value pair from a dictionary.

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

# Question 29

## Copy a Dictionary

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

# Question 30

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
