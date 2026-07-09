# Python Tuple Coding Interview Questions

## Introduction

This document contains coding-based interview questions on Python Tuples.

These questions help improve problem-solving skills and prepare for Python technical interviews.

Each question includes:

- Problem Statement
- Program
- Output

---

# Question 1

## Reverse a Tuple

### Problem Statement

Write a Python program to reverse a tuple.

---

### Program

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[::-1])
```

---

### Output

```text
(50, 40, 30, 20, 10)
```

---

# Question 2

## Find the Largest Element

### Problem Statement

Write a Python program to find the largest element in a tuple.

---

### Program

```python
numbers = (10, 50, 30, 80, 20)

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

Write a Python program to find the smallest element in a tuple.

---

### Program

```python
numbers = (10, 50, 30, 80, 20)

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

Write a Python program to calculate the sum of all elements in a tuple.

---

### Program

```python
numbers = (10, 20, 30, 40)

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

Write a Python program to count the number of elements in a tuple.

---

### Program

```python
numbers = (10, 20, 30, 40)

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

Write a Python program to check whether an element exists in a tuple.

---

### Program

```python
numbers = (10, 20, 30, 40)

print(30 in numbers)
```

---

### Output

```text
True
```

---

# Question 7

## Concatenate Two Tuples

### Problem Statement

Write a Python program to concatenate two tuples.

---

### Program

```python
tuple1 = (10, 20)

tuple2 = (30, 40)

result = tuple1 + tuple2

print(result)
```

---

### Output

```text
(10, 20, 30, 40)
```

---

# Question 8

## Repeat a Tuple

### Problem Statement

Write a Python program to repeat a tuple multiple times.

---

### Program

```python
numbers = (10, 20)

print(numbers * 3)
```

---

### Output

```text
(10, 20, 10, 20, 10, 20)
```

---

# Question 9

## Count Occurrences of an Element

### Problem Statement

Write a Python program to count the occurrences of an element in a tuple.

---

### Program

```python
numbers = (10, 20, 30, 20, 40)

print(numbers.count(20))
```

---

### Output

```text
2
```

---

# Question 10

## Find the Index of an Element

### Problem Statement

Write a Python program to find the index of an element in a tuple.

---

### Program

```python
numbers = (10, 20, 30, 40)

print(numbers.index(30))
```

---

### Output

```text
2
```
