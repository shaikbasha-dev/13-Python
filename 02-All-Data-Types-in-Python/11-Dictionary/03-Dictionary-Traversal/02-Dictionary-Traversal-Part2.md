# Traversing Values Using values()

## Syntax

```python
for value in dictionary.values():
    statements
```

---

## Program

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

## Output

```text
101

Basha

Python
```

---

## Dry Run

```text
student

↓

101

↓

Basha

↓

Python
```

---

## Memory Representation

```text
+--------------------------------------+

| 101 | Basha | Python |

+--------------------------------------+

        ↓

101

        ↓

Basha

        ↓

Python
```

---

## Pseudocode

```text
START

Create Dictionary

Traverse values using values()

Display each value

STOP
```

---

## Line-by-Line Explanation

### Line 1

```python
student = {
    "id": 101,
    "name": "Basha",
    "course": "Python"
}
```

Creates a dictionary named `student`.

---

### Line 2

```python
for value in student.values():
```

The `for` loop visits each value of the dictionary one by one.

---

### Line 3

```python
print(value)
```

Displays the current value.

---

# Traversing Keys and Values Using items()

## Syntax

```python
for key, value in dictionary.items():
    statements
```

---

## Program

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

## Output

```text
id : 101

name : Basha

course : Python
```

---

## Explanation

The `items()` method returns both keys and values as key-value pairs.

The `for` loop visits each key-value pair and displays them.
