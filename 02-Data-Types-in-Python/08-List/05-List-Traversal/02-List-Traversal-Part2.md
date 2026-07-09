---

# Traversing Using while Loop

## Syntax

```python
index = 0

while index < len(list_name):
    statements
    index += 1
```

---

## Program

```python
languages = ["Python", "Java", "C++", "JavaScript"]

index = 0

while index < len(languages):
    print(languages[index])
    index += 1
```

---

## Output

```text
Python

Java

C++

JavaScript
```

---

## Dry Run

```text
index = 0

↓

Python

↓

index = 1

↓

Java

↓

index = 2

↓

C++

↓

index = 3

↓

JavaScript

↓

Loop Ends
```

---

## Memory Representation

```text
              index

                │

                ▼

+---------------------------------------------+

| Python | Java | C++ | JavaScript |

+---------------------------------------------+

    0         1       2         3
```

---

## Pseudocode

```text
START

Create List

Initialize index = 0

Repeat while index is less than list length

Display current element

Increment index

STOP
```

---

## Line-by-Line Explanation

### Line 1

```python
languages = ["Python", "Java", "C++", "JavaScript"]
```

Creates a list named `languages`.

---

### Line 2

```python
index = 0
```

Initializes the index variable with `0`.

---

### Line 3

```python
while index < len(languages):
```

The loop continues until the index becomes equal to the length of the list.

---

### Line 4

```python
print(languages[index])
```

Displays the current element using its index.

---

### Line 5

```python
index += 1
```

Increments the index to move to the next element.
