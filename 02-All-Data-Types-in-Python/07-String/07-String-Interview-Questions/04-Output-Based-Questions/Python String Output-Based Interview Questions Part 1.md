# Python String Output-Based Interview Questions Part 1

## Introduction

Output-based questions are among the most frequently asked questions in Python interviews. They evaluate your understanding of Python's string behavior, indexing, slicing, operators, methods, immutability, and object handling.

For every question:

* Read the code carefully.
* Predict the output.
* Understand the explanation before moving to the next question.

---

# Question 1

## Predict the Output

```python
text = "Python"

print(text[0])
```

### Output

```text
P
```

### Explanation

Index `0` represents the first character of the string.

---

# Question 2

## Predict the Output

```python
text = "Python"

print(text[-1])
```

### Output

```text
n
```

### Explanation

Negative indexing starts from the end of the string.

`-1` refers to the last character.

---

# Question 3

## Predict the Output

```python
text = "Python"

print(text[1:5])
```

### Output

```text
ytho
```

### Explanation

The start index (`1`) is included.

The stop index (`5`) is excluded.

---

# Question 4

## Predict the Output

```python
text = "Python"

print(text[:4])
```

### Output

```text
Pyth
```

### Explanation

When the start index is omitted, slicing begins from index `0`.

---

# Question 5

## Predict the Output

```python
text = "Python"

print(text[3:])
```

### Output

```text
hon
```

### Explanation

When the stop index is omitted, slicing continues until the end of the string.

---

# Question 6

## Predict the Output

```python
text = "Python"

print(text[::-1])
```

### Output

```text
nohtyP
```

### Explanation

A step value of `-1` traverses the string in reverse order.

---

# Question 7

## Predict the Output

```python
text = "Programming"

print(text[::2])
```

### Output

```text
Pormig
```

### Explanation

Every second character is selected.

Indexes:

```text
0 2 4 6 8 10
```

Characters:

```text
P o r m i g
```

---

# Question 8

## Predict the Output

```python
text = "Python"

print(len(text))
```

### Output

```text
6
```

### Explanation

The `len()` function returns the total number of characters.

---

# Question 9

## Predict the Output

```python
print("Python" + " Programming")
```

### Output

```text
Python Programming
```

### Explanation

The `+` operator concatenates strings.

---

# Question 10

## Predict the Output

```python
print("Hi " * 3)
```

### Output

```text
Hi Hi Hi
```

### Explanation

The `*` operator repeats a string the specified number of times.

---

# Question 11

## Predict the Output

```python
print("Py" in "Python")
```

### Output

```text
True
```

### Explanation

The substring `"Py"` exists inside `"Python"`.

---

# Question 12

## Predict the Output

```python
print("Java" in "Python")
```

### Output

```text
False
```

### Explanation

The substring `"Java"` is not present.

---

# Question 13

## Predict the Output

```python
print("Python".upper())
```

### Output

```text
PYTHON
```

### Explanation

The `upper()` method converts all characters to uppercase.

---

# Question 14

## Predict the Output

```python
print("PYTHON".lower())
```

### Output

```text
python
```

### Explanation

The `lower()` method converts all characters to lowercase.

---

# Question 15

## Predict the Output

```python
print("Python".replace("Py", "My"))
```

### Output

```text
Mython
```

### Explanation

The `replace()` method replaces the specified substring.

---

# Question 16

## Predict the Output

```python
print("banana".count("a"))
```

### Output

```text
3
```

### Explanation

The character `"a"` appears three times.

---

# Question 17

## Predict the Output

```python
print("Python".find("th"))
```

### Output

```text
2
```

### Explanation

The substring `"th"` starts at index `2`.

---

# Question 18

## Predict the Output

```python
print("Python".find("Java"))
```

### Output

```text
-1
```

### Explanation

The `find()` method returns `-1` when the substring is not found.

---

# Question 19

## Predict the Output

```python
print("Python".startswith("Py"))
```

### Output

```text
True
```

### Explanation

The string begins with `"Py"`.

---

# Question 20

## Predict the Output

```python
print("report.pdf".endswith(".pdf"))
```

### Output

```text
True
```

### Explanation

The filename ends with the extension `.pdf`.

---

# Summary (Part 1)

In this part, you practiced output-based questions on:

* Indexing
* Slicing
* Reverse slicing
* Step slicing
* `len()`
* Concatenation
* Repetition
* Membership operators
* `upper()`
* `lower()`
* `replace()`
* `count()`
* `find()`
* `startswith()`
* `endswith()`

The next part will contain more challenging output-based questions involving string formatting, comparison operators, identity, immutability, Unicode, and tricky interview scenarios.
