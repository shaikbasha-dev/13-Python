---

# Question 11

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

# Question 12

## Traverse a Set Using for Loop

### Problem Statement

Write a Python program to traverse and display all elements of a set using a `for` loop.

---

### Program

```python
numbers = {10, 20, 30, 40}

for number in numbers:
    print(number)
```

---

### Output

```text
10
20
30
40
```

---

# Question 13

## Check Whether an Element Exists

### Problem Statement

Write a Python program to check whether an element exists in a set.

---

### Program

```python
numbers = {10, 20, 30, 40}

if 20 in numbers:
    print("Element Found")
else:
    print("Element Not Found")
```

---

### Output

```text
Element Found
```

---

# Question 14

## Perform Union Operation

### Problem Statement

Write a Python program to perform the union of two sets.

---

### Program

```python
set1 = {10, 20, 30}

set2 = {30, 40, 50}

print(set1.union(set2))
```

---

### Output

```text
{10, 20, 30, 40, 50}
```

---

# Question 15

## Perform Intersection Operation

### Problem Statement

Write a Python program to find the common elements of two sets.

---

### Program

```python
set1 = {10, 20, 30}

set2 = {30, 40, 50}

print(set1.intersection(set2))
```

---

### Output

```text
{30}
```

---

# Question 16

## Perform Difference Operation

### Problem Statement

Write a Python program to find the difference between two sets.

---

### Program

```python
set1 = {10, 20, 30}

set2 = {30, 40, 50}

print(set1.difference(set2))
```

---

### Output

```text
{10, 20}
```

---

# Question 17

## Perform Symmetric Difference Operation

### Problem Statement

Write a Python program to find the symmetric difference between two sets.

---

### Program

```python
set1 = {10, 20, 30}

set2 = {30, 40, 50}

print(set1.symmetric_difference(set2))
```

---

### Output

```text
{10, 20, 40, 50}
```

---

# Question 18

## Find the Maximum Element Without Using max()

### Problem Statement

Write a Python program to find the largest element in a set without using the `max()` function.

---

### Program

```python
numbers = {10, 50, 30, 80, 20}

largest = None

for number in numbers:
    if largest is None or number > largest:
        largest = number

print(largest)
```

---

### Output

```text
80
```

---

# Question 19

## Find the Minimum Element Without Using min()

### Problem Statement

Write a Python program to find the smallest element in a set without using the `min()` function.

---

### Program

```python
numbers = {10, 50, 30, 80, 20}

smallest = None

for number in numbers:
    if smallest is None or number < smallest:
        smallest = number

print(smallest)
```

---

### Output

```text
10
```

---

# Question 20

## Calculate the Sum Without Using sum()

### Problem Statement

Write a Python program to calculate the sum of all elements in a set without using the `sum()` function.

---

### Program

```python
numbers = {10, 20, 30, 40}

total = 0

for number in numbers:
    total += number

print(total)
```

---

### Output

```text
100
```
