---

# Question 31

## Merge Two Lists

### Problem Statement

Write a Python program to merge two lists.

---

### Program

```python
list1 = [10, 20, 30]

list2 = [40, 50, 60]

list1.extend(list2)

print(list1)
```

---

### Output

```text
[10, 20, 30, 40, 50, 60]
```

---

# Question 32

## Remove Duplicate Elements

### Problem Statement

Write a Python program to remove duplicate elements from a list.

---

### Program

```python
numbers = [10, 20, 20, 30, 40, 40, 50]

unique_numbers = list(set(numbers))

print(unique_numbers)
```

---

### Output

```text
[10, 20, 30, 40, 50]
```

---

# Question 33

## Find the Second Largest Element

### Problem Statement

Write a Python program to find the second largest element in a list.

---

### Program

```python
numbers = [10, 50, 30, 80, 20]

numbers.sort()

print(numbers[-2])
```

---

### Output

```text
50
```

---

# Question 34

## Find the Second Smallest Element

### Problem Statement

Write a Python program to find the second smallest element in a list.

---

### Program

```python
numbers = [10, 50, 30, 80, 20]

numbers.sort()

print(numbers[1])
```

---

### Output

```text
20
```

---

# Question 35

## Count Even Numbers

### Problem Statement

Write a Python program to count the number of even elements in a list.

---

### Program

```python
numbers = [10, 15, 20, 25, 30]

count = 0

for number in numbers:
    if number % 2 == 0:
        count += 1

print(count)
```

---

### Output

```text
3
```

---

# Question 36

## Count Odd Numbers

### Problem Statement

Write a Python program to count the number of odd elements in a list.

---

### Program

```python
numbers = [10, 15, 20, 25, 30]

count = 0

for number in numbers:
    if number % 2 != 0:
        count += 1

print(count)
```

---

### Output

```text
2
```

---

# Question 37

## Find the Average of Elements

### Problem Statement

Write a Python program to calculate the average of all elements in a list.

---

### Program

```python
numbers = [10, 20, 30, 40]

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

## Find the Product of All Elements

### Problem Statement

Write a Python program to calculate the product of all elements in a list.

---

### Program

```python
numbers = [2, 3, 4]

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

## Find the First Element

### Problem Statement

Write a Python program to display the first element of a list.

---

### Program

```python
numbers = [10, 20, 30, 40]

print(numbers[0])
```

---

### Output

```text
10
```

---

# Question 40

## Find the Last Element

### Problem Statement

Write a Python program to display the last element of a list.

---

### Program

```python
numbers = [10, 20, 30, 40]

print(numbers[-1])
```

---

### Output

```text
40
```

---

# Summary

In this section, you learned coding interview questions on:

- Merge Two Lists
- Remove Duplicate Elements
- Second Largest Element
- Second Smallest Element
- Count Even Numbers
- Count Odd Numbers
- Average of Elements
- Product of Elements
- First Element
- Last Element

These coding questions help strengthen problem-solving skills and prepare you for Python technical interviews.
