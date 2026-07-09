---

# Question 21

## Display List Elements Using while Loop

### Problem Statement

Write a Python program to traverse and display all elements of a list using a `while` loop.

---

### Program

```python
numbers = [10, 20, 30, 40]

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

# Question 22

## Find the Maximum Element Without Using max()

### Problem Statement

Write a Python program to find the largest element without using the `max()` function.

---

### Program

```python
numbers = [10, 50, 30, 80, 20]

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

# Question 23

## Find the Minimum Element Without Using min()

### Problem Statement

Write a Python program to find the smallest element without using the `min()` function.

---

### Program

```python
numbers = [10, 50, 30, 80, 20]

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

# Question 24

## Calculate the Sum Without Using sum()

### Problem Statement

Write a Python program to calculate the sum of all elements without using the `sum()` function.

---

### Program

```python
numbers = [10, 20, 30, 40]

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

---

# Question 25

## Count the Number of Elements Without Using len()

### Problem Statement

Write a Python program to count the number of elements in a list without using the `len()` function.

---

### Program

```python
numbers = [10, 20, 30, 40]

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

# Question 26

## Check Whether a List is Empty

### Problem Statement

Write a Python program to check whether a list is empty.

---

### Program

```python
numbers = []

if len(numbers) == 0:
    print("List is Empty")
else:
    print("List is Not Empty")
```

---

### Output

```text
List is Empty
```

---

# Question 27

## Copy One List into Another

### Problem Statement

Write a Python program to copy one list into another.

---

### Program

```python
list1 = [10, 20, 30]

list2 = list1.copy()

print(list2)
```

---

### Output

```text
[10, 20, 30]
```

---

# Question 28

## Sort a List in Descending Order

### Problem Statement

Write a Python program to sort a list in descending order.

---

### Program

```python
numbers = [40, 10, 30, 20]

numbers.sort(reverse=True)

print(numbers)
```

---

### Output

```text
[40, 30, 20, 10]
```

---

# Question 29

## Reverse a List Using reverse()

### Problem Statement

Write a Python program to reverse a list using the `reverse()` method.

---

### Program

```python
numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)
```

---

### Output

```text
[40, 30, 20, 10]
```

---

# Question 30

## Search an Element in a List

### Problem Statement

Write a Python program to search whether an element exists in a list.

---

### Program

```python
numbers = [10, 20, 30, 40]

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
