---

# Question 31

## Find the Union of Three Sets

### Problem Statement

Write a Python program to find the union of three sets.

---

### Program

```python
set1 = {10, 20}

set2 = {20, 30}

set3 = {30, 40}

print(set1.union(set2, set3))
```

---

### Output

```text
{10, 20, 30, 40}
```

---

# Question 32

## Find the Intersection of Three Sets

### Problem Statement

Write a Python program to find the common elements of three sets.

---

### Program

```python
set1 = {10, 20, 30}

set2 = {20, 30, 40}

set3 = {20, 50, 60}

print(set1.intersection(set2, set3))
```

---

### Output

```text
{20}
```

---

# Question 33

## Check Whether Two Sets are Equal

### Problem Statement

Write a Python program to check whether two sets are equal.

---

### Program

```python
set1 = {10, 20, 30}

set2 = {30, 20, 10}

print(set1 == set2)
```

---

### Output

```text
True
```

---

# Question 34

## Find the Difference Between Two Sets

### Problem Statement

Write a Python program to find the difference between two sets.

---

### Program

```python
set1 = {10, 20, 30}

set2 = {20, 30, 40}

print(set1.difference(set2))
```

---

### Output

```text
{10}
```

---

# Question 35

## Find the Symmetric Difference Between Two Sets

### Problem Statement

Write a Python program to find the symmetric difference between two sets.

---

### Program

```python
set1 = {10, 20, 30}

set2 = {20, 30, 40}

print(set1.symmetric_difference(set2))
```

---

### Output

```text
{10, 40}
```

---

# Question 36

## Display All Elements of a Set

### Problem Statement

Write a Python program to display all elements of a set using a `for` loop.

---

### Program

```python
numbers = {100, 200, 300}

for number in numbers:
    print(number)
```

---

### Output

```text
100
200
300
```

---

# Question 37

## Calculate the Average of Set Elements

### Problem Statement

Write a Python program to calculate the average of all elements in a set.

---

### Program

```python
numbers = {10, 20, 30, 40}

average = sum(numbers) / len(numbers)

print(average)
```

---

### Output

```text
25.0
```

---

# Question 38

## Calculate the Product of Set Elements

### Problem Statement

Write a Python program to calculate the product of all elements in a set.

---

### Program

```python
numbers = {2, 3, 4}

product = 1

for number in numbers:
    product *= number

print(product)
```

---

### Output

```text
24
```

---

# Question 39

## Find the Maximum and Minimum Elements

### Problem Statement

Write a Python program to display both the maximum and minimum elements in a set.

---

### Program

```python
numbers = {10, 50, 30, 80, 20}

print(max(numbers))

print(min(numbers))
```

---

### Output

```text
80

10
```

---

# Question 40

## Find the Sum of Elements

### Problem Statement

Write a Python program to calculate the sum of all elements in a set.

---

### Program

```python
numbers = {10, 20, 30, 40}

print(sum(numbers))
```

---

### Output

```text
100
```

---

# Summary

In this section, you learned coding interview questions on:

- Adding Elements
- Removing Elements
- Membership Operators
- Union
- Intersection
- Difference
- Symmetric Difference
- Set Traversal
- Maximum and Minimum Elements
- Sum and Average
- Duplicate Removal

These coding questions help strengthen problem-solving skills and prepare you for Python technical interviews.
