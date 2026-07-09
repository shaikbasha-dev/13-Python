---

# Question 21

## Count the Number of Elements Without Using len()

### Problem Statement

Write a Python program to count the number of elements in a tuple without using the `len()` function.

---

### Program

```python
numbers = (10, 20, 30, 40)

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

## Check Whether a Tuple is Empty

### Problem Statement

Write a Python program to check whether a tuple is empty.

---

### Program

```python
numbers = ()

if len(numbers) == 0:
    print("Tuple is Empty")
else:
    print("Tuple is Not Empty")
```

---

### Output

```text
Tuple is Empty
```

---

# Question 23

## Find the Average of Elements

### Problem Statement

Write a Python program to calculate the average of all elements in a tuple.

---

### Program

```python
numbers = (10, 20, 30, 40)

average = sum(numbers) / len(numbers)

print(average)
```

---

### Output

```text
25.0
```

---

# Question 24

## Find the Product of All Elements

### Problem Statement

Write a Python program to calculate the product of all elements in a tuple.

---

### Program

```python
numbers = (2, 3, 4)

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

# Question 25

## Count Even Numbers

### Problem Statement

Write a Python program to count the number of even elements in a tuple.

---

### Program

```python
numbers = (10, 15, 20, 25, 30)

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

# Question 26

## Count Odd Numbers

### Problem Statement

Write a Python program to count the number of odd elements in a tuple.

---

### Program

```python
numbers = (10, 15, 20, 25, 30)

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

# Question 27

## Copy a Tuple

### Problem Statement

Write a Python program to create a copy of a tuple.

---

### Program

```python
numbers = (10, 20, 30, 40)

new_tuple = numbers[:]

print(new_tuple)
```

---

### Output

```text
(10, 20, 30, 40)
```

---

# Question 28

## Display Elements Using Negative Indexing

### Problem Statement

Write a Python program to display tuple elements using negative indexing.

---

### Program

```python
numbers = (10, 20, 30, 40)

print(numbers[-1])

print(numbers[-2])
```

---

### Output

```text
40

30
```

---

# Question 29

## Display Alternate Elements

### Problem Statement

Write a Python program to display alternate elements of a tuple.

---

### Program

```python
numbers = (10, 20, 30, 40, 50, 60)

print(numbers[::2])
```

---

### Output

```text
(10, 30, 50)
```

---

# Question 30

## Display Tuple Elements in Reverse Order

### Problem Statement

Write a Python program to display tuple elements in reverse order.

---

### Program

```python
numbers = (10, 20, 30, 40, 50)

for number in numbers[::-1]:
    print(number)
```

---

### Output

```text
50
40
30
20
10
```
