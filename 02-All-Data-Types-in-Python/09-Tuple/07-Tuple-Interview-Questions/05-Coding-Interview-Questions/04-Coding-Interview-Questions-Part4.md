---

# Question 31

## Merge Two Tuples

### Problem Statement

Write a Python program to merge two tuples.

---

### Program

```python
tuple1 = (10, 20, 30)

tuple2 = (40, 50, 60)

result = tuple1 + tuple2

print(result)
```

---

### Output

```text
(10, 20, 30, 40, 50, 60)
```

---

# Question 32

## Check Membership Using in Operator

### Problem Statement

Write a Python program to check whether an element exists in a tuple using the `in` operator.

---

### Program

```python
numbers = (10, 20, 30, 40)

print(20 in numbers)
```

---

### Output

```text
True
```

---

# Question 33

## Check Membership Using not in Operator

### Problem Statement

Write a Python program to check whether an element does not exist in a tuple using the `not in` operator.

---

### Program

```python
numbers = (10, 20, 30, 40)

print(50 not in numbers)
```

---

### Output

```text
True
```

---

# Question 34

## Display a Portion of a Tuple

### Problem Statement

Write a Python program to display a portion of a tuple using slicing.

---

### Program

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
```

---

### Output

```text
(20, 30, 40)
```

---

# Question 35

## Reverse a Tuple Using Slicing

### Problem Statement

Write a Python program to reverse a tuple using slicing.

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

# Question 36

## Find Maximum and Minimum Elements

### Problem Statement

Write a Python program to display both the maximum and minimum elements in a tuple.

---

### Program

```python
numbers = (10, 50, 30, 80, 20)

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

# Question 37

## Find the Sum and Average

### Problem Statement

Write a Python program to calculate the sum and average of tuple elements.

---

### Program

```python
numbers = (10, 20, 30, 40)

total = sum(numbers)

average = total / len(numbers)

print(total)

print(average)
```

---

### Output

```text
100

25.0
```

---

# Question 38

## Display Elements Using for Loop

### Problem Statement

Write a Python program to display all tuple elements using a `for` loop.

---

### Program

```python
numbers = (100, 200, 300)

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

# Question 39

## Display Elements Using while Loop

### Problem Statement

Write a Python program to display all tuple elements using a `while` loop.

---

### Program

```python
numbers = (100, 200, 300)

index = 0

while index < len(numbers):
    print(numbers[index])
    index += 1
```

---

### Output

```text
100
200
300
```

---

# Question 40

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

# Summary

In this section, you learned coding interview questions on:

- Tuple Traversal
- Tuple Slicing
- Membership Operators
- Concatenation
- Repetition
- Reverse Traversal
- Maximum and Minimum Elements
- Sum and Average
- Alternate Elements
- Tuple Searching

These coding questions help strengthen problem-solving skills and prepare you for Python technical interviews.
