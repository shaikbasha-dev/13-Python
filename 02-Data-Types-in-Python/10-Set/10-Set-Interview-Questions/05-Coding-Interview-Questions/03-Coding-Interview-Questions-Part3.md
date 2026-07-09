---

# Question 21

## Count the Number of Elements Without Using len()

### Problem Statement

Write a Python program to count the number of elements in a set without using the `len()` function.

---

### Program

```python
numbers = {10, 20, 30, 40}

count = 0

for number in numbers:
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

## Check Whether a Set is Empty

### Problem Statement

Write a Python program to check whether a set is empty.

---

### Program

```python
numbers = set()

if len(numbers) == 0:
    print("Set is Empty")
else:
    print("Set is Not Empty")
```

---

### Output

```text
Set is Empty
```

---

# Question 23

## Copy a Set

### Problem Statement

Write a Python program to create a copy of a set.

---

### Program

```python
numbers = {10, 20, 30, 40}

new_set = numbers.copy()

print(new_set)
```

---

### Output

```text
{10, 20, 30, 40}
```

---

# Question 24

## Check Membership Using in Operator

### Problem Statement

Write a Python program to check whether an element exists in a set using the `in` operator.

---

### Program

```python
numbers = {10, 20, 30, 40}

print(20 in numbers)
```

---

### Output

```text
True
```

---

# Question 25

## Check Membership Using not in Operator

### Problem Statement

Write a Python program to check whether an element does not exist in a set using the `not in` operator.

---

### Program

```python
numbers = {10, 20, 30, 40}

print(50 not in numbers)
```

---

### Output

```text
True
```

---

# Question 26

## Remove Duplicate Elements from a List Using Set

### Problem Statement

Write a Python program to remove duplicate elements from a list using a set.

---

### Program

```python
numbers = [10, 20, 20, 30, 40, 40, 50]

unique_numbers = set(numbers)

print(unique_numbers)
```

---

### Output

```text
{10, 20, 30, 40, 50}
```

---

# Question 27

## Find Common Elements Between Two Sets

### Problem Statement

Write a Python program to find the common elements between two sets.

---

### Program

```python
set1 = {10, 20, 30}

set2 = {20, 30, 40}

print(set1.intersection(set2))
```

---

### Output

```text
{20, 30}
```

---

# Question 28

## Find Unique Elements from the First Set

### Problem Statement

Write a Python program to find elements that exist only in the first set.

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

# Question 29

## Find Unique Elements from Both Sets

### Problem Statement

Write a Python program to find elements that are present in either set but not in both.

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

# Question 30

## Merge Two Sets

### Problem Statement

Write a Python program to merge two sets.

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
