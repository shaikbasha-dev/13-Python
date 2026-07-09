---

# Question 11

## Display Tuple Elements Using for Loop

### Problem Statement

Write a Python program to traverse and display all elements of a tuple using a `for` loop.

---

### Program

```python
numbers = (10, 20, 30, 40)

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

# Question 12

## Display Tuple Elements Using while Loop

### Problem Statement

Write a Python program to traverse and display all elements of a tuple using a `while` loop.

---

### Program

```python
numbers = (10, 20, 30, 40)

index = 0

while index < len(numbers):
    print(numbers[index])
    index += 1
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

## Search an Element in a Tuple

### Problem Statement

Write a Python program to check whether an element exists in a tuple.

---

### Program

```python
numbers = (10, 20, 30, 40)

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

## Find the First Element

### Problem Statement

Write a Python program to display the first element of a tuple.

---

### Program

```python
numbers = (10, 20, 30, 40)

print(numbers[0])
```

---

### Output

```text
10
```

---

# Question 15

## Find the Last Element

### Problem Statement

Write a Python program to display the last element of a tuple.

---

### Program

```python
numbers = (10, 20, 30, 40)

print(numbers[-1])
```

---

### Output

```text
40
```

---

# Question 16

## Display Elements Using Slicing

### Problem Statement

Write a Python program to display elements using tuple slicing.

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

# Question 17

## Reverse a Tuple Using Slicing

### Problem Statement

Write a Python program to reverse a tuple using slicing.

---

### Program

```python
numbers = (10, 20, 30, 40)

print(numbers[::-1])
```

---

### Output

```text
(40, 30, 20, 10)
```

---

# Question 18

## Find the Maximum Element Without Using max()

### Problem Statement

Write a Python program to find the largest element in a tuple without using the `max()` function.

---

### Program

```python
numbers = (10, 50, 30, 80, 20)

largest = numbers[0]

for number in numbers:
    if number > largest:
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

Write a Python program to find the smallest element in a tuple without using the `min()` function.

---

### Program

```python
numbers = (10, 50, 30, 80, 20)

smallest = numbers[0]

for number in numbers:
    if number < smallest:
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

Write a Python program to calculate the sum of all elements in a tuple without using the `sum()` function.

---

### Program

```python
numbers = (10, 20, 30, 40)

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
