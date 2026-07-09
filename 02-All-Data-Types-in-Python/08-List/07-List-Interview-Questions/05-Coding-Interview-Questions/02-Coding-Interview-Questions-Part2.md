---

# Question 11

## Insert an Element at a Specific Position

### Problem Statement

Write a Python program to insert an element at a specified position in a list.

---

### Program

```python
numbers = [10, 20, 40, 50]

numbers.insert(2, 30)

print(numbers)
```

---

### Output

```text
[10, 20, 30, 40, 50]
```

---

# Question 12

## Remove an Element from a List

### Problem Statement

Write a Python program to remove a specified element from a list.

---

### Program

```python
numbers = [10, 20, 30, 40]

numbers.remove(20)

print(numbers)
```

---

### Output

```text
[10, 30, 40]
```

---

# Question 13

## Remove the Last Element

### Problem Statement

Write a Python program to remove the last element from a list.

---

### Program

```python
numbers = [10, 20, 30, 40]

numbers.pop()

print(numbers)
```

---

### Output

```text
[10, 20, 30]
```

---

# Question 14

## Count the Occurrence of an Element

### Problem Statement

Write a Python program to count the occurrence of a specific element in a list.

---

### Program

```python
numbers = [10, 20, 30, 20, 40, 20]

print(numbers.count(20))
```

---

### Output

```text
3
```

---

# Question 15

## Find the Index of an Element

### Problem Statement

Write a Python program to find the index of a specified element.

---

### Program

```python
numbers = [10, 20, 30, 40]

print(numbers.index(30))
```

---

### Output

```text
2
```

---

# Question 16

## Clear All Elements

### Problem Statement

Write a Python program to remove all elements from a list.

---

### Program

```python
numbers = [10, 20, 30, 40]

numbers.clear()

print(numbers)
```

---

### Output

```text
[]
```

---

# Question 17

## Extend a List

### Problem Statement

Write a Python program to merge two lists using the `extend()` method.

---

### Program

```python
list1 = [10, 20]

list2 = [30, 40]

list1.extend(list2)

print(list1)
```

---

### Output

```text
[10, 20, 30, 40]
```

---

# Question 18

## Append an Element

### Problem Statement

Write a Python program to add an element to the end of a list.

---

### Program

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

---

### Output

```text
[10, 20, 30, 40]
```

---

# Question 19

## Reverse a List Using Slicing

### Problem Statement

Write a Python program to reverse a list using slicing.

---

### Program

```python
numbers = [10, 20, 30, 40]

print(numbers[::-1])
```

---

### Output

```text
[40, 30, 20, 10]
```

---

# Question 20

## Display List Elements Using a for Loop

### Problem Statement

Write a Python program to traverse and display all elements of a list.

---

### Program

```python
numbers = [10, 20, 30, 40]

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
