# Python Set Coding Interview Questions

## Introduction

This document contains coding-based interview questions on Python Sets.

These questions help improve problem-solving skills and prepare for Python technical interviews.

Each question includes:

- Problem Statement
- Program
- Output

---

# Question 1

## Add an Element to a Set

### Problem Statement

Write a Python program to add an element to a set.

---

### Program

```python
numbers = {10, 20, 30}

numbers.add(40)

print(numbers)
```

---

### Output

```text
{10, 20, 30, 40}
```

---

# Question 2

## Add Multiple Elements to a Set

### Problem Statement

Write a Python program to add multiple elements to a set.

---

### Program

```python
numbers = {10, 20, 30}

numbers.update({40, 50})

print(numbers)
```

---

### Output

```text
{10, 20, 30, 40, 50}
```

---

# Question 3

## Remove an Element Using remove()

### Problem Statement

Write a Python program to remove an element using the `remove()` method.

---

### Program

```python
numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)
```

---

### Output

```text
{10, 30}
```

---

# Question 4

## Remove an Element Using discard()

### Problem Statement

Write a Python program to remove an element using the `discard()` method.

---

### Program

```python
numbers = {10, 20, 30}

numbers.discard(20)

print(numbers)
```

---

### Output

```text
{10, 30}
```

---

# Question 5

## Remove an Arbitrary Element

### Problem Statement

Write a Python program to remove an arbitrary element using the `pop()` method.

---

### Program

```python
numbers = {10, 20, 30}

removed = numbers.pop()

print(removed)

print(numbers)
```

---

### Output

```text
An arbitrary element is removed.

Remaining elements are displayed.
```

---

# Question 6

## Clear a Set

### Problem Statement

Write a Python program to remove all elements from a set.

---

### Program

```python
numbers = {10, 20, 30}

numbers.clear()

print(numbers)
```

---

### Output

```text
set()
```

---

# Question 7

## Copy a Set

### Problem Statement

Write a Python program to create a copy of a set.

---

### Program

```python
numbers = {10, 20, 30}

new_set = numbers.copy()

print(new_set)
```

---

### Output

```text
{10, 20, 30}
```

---

# Question 8

## Find the Number of Elements

### Problem Statement

Write a Python program to count the number of elements in a set.

---

### Program

```python
numbers = {10, 20, 30}

print(len(numbers))
```

---

### Output

```text
3
```

---

# Question 9

## Find the Largest Element

### Problem Statement

Write a Python program to find the largest element in a set.

---

### Program

```python
numbers = {10, 20, 30}

print(max(numbers))
```

---

### Output

```text
30
```

---

# Question 10

## Find the Smallest Element

### Problem Statement

Write a Python program to find the smallest element in a set.

---

### Program

```python
numbers = {10, 20, 30}

print(min(numbers))
```

---

### Output

```text
10
```
