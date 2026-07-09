# Python List Coding Interview Questions

## Introduction

This document contains coding-based interview questions on Python Lists.

These questions help improve problem-solving skills and prepare for Python technical interviews.

Each question includes:

- Problem Statement
- Program
- Output

---

# Question 1

## Reverse a List

### Problem Statement

Write a Python program to reverse a list.

---

### Program

```python
numbers = [10, 20, 30, 40, 50]

numbers.reverse()

print(numbers)
```

---

### Output

```text
[50, 40, 30, 20, 10]
```

---

# Question 2

## Find the Largest Element

### Problem Statement

Write a Python program to find the largest element in a list.

---

### Program

```python
numbers = [10, 50, 30, 80, 20]

print(max(numbers))
```

---

### Output

```text
80
```

---

# Question 3

## Find the Smallest Element

### Problem Statement

Write a Python program to find the smallest element in a list.

---

### Program

```python
numbers = [10, 50, 30, 80, 20]

print(min(numbers))
```

---

### Output

```text
10
```

---

# Question 4

## Find the Sum of Elements

### Problem Statement

Write a Python program to calculate the sum of all elements in a list.

---

### Program

```python
numbers = [10, 20, 30, 40]

print(sum(numbers))
```

---

### Output

```text
100
```

---

# Question 5

## Count the Number of Elements

### Problem Statement

Write a Python program to count the number of elements in a list.

---

### Program

```python
numbers = [10, 20, 30, 40]

print(len(numbers))
```

---

### Output

```text
4
```

---

# Question 6

## Check Whether an Element Exists

### Problem Statement

Write a Python program to check whether an element exists in a list.

---

### Program

```python
numbers = [10, 20, 30, 40]

print(30 in numbers)
```

---

### Output

```text
True
```

---

# Question 7

## Concatenate Two Lists

### Problem Statement

Write a Python program to concatenate two lists.

---

### Program

```python
list1 = [10, 20]

list2 = [30, 40]

result = list1 + list2

print(result)
```

---

### Output

```text
[10, 20, 30, 40]
```

---

# Question 8

## Repeat a List

### Problem Statement

Write a Python program to repeat a list multiple times.

---

### Program

```python
numbers = [10, 20]

print(numbers * 3)
```

---

### Output

```text
[10, 20, 10, 20, 10, 20]
```

---

# Question 9

## Copy a List

### Problem Statement

Write a Python program to create a copy of a list.

---

### Program

```python
languages = ["Python", "Java", "C++"]

new_list = languages.copy()

print(new_list)
```

---

### Output

```text
['Python', 'Java', 'C++']
```

---

# Question 10

## Sort a List

### Problem Statement

Write a Python program to sort a list in ascending order.

---

### Program

```python
numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)
```

---

### Output

```text
[10, 20, 30, 40]
```
