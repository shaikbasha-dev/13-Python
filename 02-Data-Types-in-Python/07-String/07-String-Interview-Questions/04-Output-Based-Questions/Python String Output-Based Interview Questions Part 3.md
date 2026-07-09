Python String Output-Based Interview Questions Part 3

---

---

# Question 51

## Predict the Output

```python
text = "Python"

print(text[::])
```

### Output

```text
Python
```

### Explanation

Using `[:]` or `[::]` creates a complete copy of the string.

---

# Question 52

## Predict the Output

```python
text = "Python"

print(text[5:1:-1])
```

### Output

```text
noht
```

### Explanation

Traversal begins at index `5` (`n`) and moves backward until (but not including) index `1`.

Indexes visited:

```text
5 → 4 → 3 → 2
```

Characters:

```text
n o h t
```

---

# Question 53

## Predict the Output

```python
text = "Python"

print(text[1:5:2])
```

### Output

```text
yh
```

### Explanation

Selected indexes:

```text
1 → 3
```

Characters:

```text
y h
```

---

# Question 54

## Predict the Output

```python
text = "Python"

print(text[-4:-1])
```

### Output

```text
tho
```

### Explanation

Negative indexes:

```text
P  y  t  h  o  n
-6 -5 -4 -3 -2 -1
```

Slice:

```text
-4 → -2
```

Result:

```text
tho
```

---

# Question 55

## Predict the Output

```python
text = "Python"

print(text[::-3])
```

### Output

```text
nh
```

### Explanation

Python starts from the last character.

Indexes selected:

```text
5 → 2
```

Characters:

```text
n h
```

---

# Question 56

## Predict the Output

```python
print("Python".swapcase())
```

### Output

```text
pYTHON
```

### Explanation

`swapcase()` converts uppercase letters to lowercase and lowercase letters to uppercase.

---

# Question 57

## Predict the Output

```python
print("PyThOn".swapcase())
```

### Output

```text
pYtHoN
```

### Explanation

Each character changes its case individually.

---

# Question 58

## Predict the Output

```python
print("python".upper().lower())
```

### Output

```text
python
```

### Explanation

Method chaining is evaluated from left to right.

Steps:

```text
python

↓

PYTHON

↓

python
```

---

# Question 59

## Predict the Output

```python
print("Python".replace("P", "J").upper())
```

### Output

```text
JYTHON
```

### Explanation

Execution order:

```text
Python

↓

Jython

↓

JYTHON
```

---

# Question 60

## Predict the Output

```python
print("python".title())
```

### Output

```text
Python
```

### Explanation

The first letter of every word becomes uppercase.

---

# Question 61

## Predict the Output

```python
print("hello world".title())
```

### Output

```text
Hello World
```

### Explanation

Each word begins with a capital letter.

---

# Question 62

## Predict the Output

```python
print("HELLO".lower().capitalize())
```

### Output

```text
Hello
```

### Explanation

Execution:

```text
HELLO

↓

hello

↓

Hello
```

---

# Question 63

## Predict the Output

```python
print("Python".startswith("P"))
```

### Output

```text
True
```

---

### Explanation

The string begins with `"P"`.

---

# Question 64

## Predict the Output

```python
print("Python".endswith("n"))
```

### Output

```text
True
```

### Explanation

The last character is `"n"`.

---

# Question 65

## Predict the Output

```python
print("Python".startswith("p"))
```

### Output

```text
False
```

### Explanation

String comparisons are case-sensitive.

---

# Question 66

## Predict the Output

```python
print("Python".endswith("N"))
```

### Output

```text
False
```

### Explanation

`"n"` and `"N"` are different characters.

---

# Question 67

## Predict the Output

```python
print("".join(["A", "B", "C"]))
```

### Output

```text
ABC
```

### Explanation

The separator is an empty string, so the list elements are joined without spaces.

---

# Question 68

## Predict the Output

```python
print("-".join("Python"))
```

### Output

```text
P-y-t-h-o-n
```

### Explanation

A string is an iterable.

`join()` inserts `"-"` between each character.

---

# Question 69

## Predict the Output

```python
print("Python".split("t"))
```

### Output

```text
['Py', 'hon']
```

### Explanation

The string is split at every occurrence of `"t"`.

---

# Question 70

## Predict the Output

```python
print("one two three".split())
```

### Output

```text
['one', 'two', 'three']
```

### Explanation

Without arguments, `split()` separates the string using whitespace.

---

# Question 71

## Predict the Output

```python
print("Python".index("t"))
```

### Output

```text
2
```

### Explanation

The character `"t"` occurs at index `2`.

---

# Question 72

## Predict the Output

```python
print("Python".find("z"))
```

### Output

```text
-1
```

### Explanation

`find()` returns `-1` if the substring is not found.

---

# Question 73

## Predict the Output

```python
print("Python".index("z"))
```

### Output

```text
ValueError
```

### Explanation

Unlike `find()`, `index()` raises a `ValueError` when the substring is absent.

---

# Question 74

## Predict the Output

```python
print("Python".count("P"))
```

### Output

```text
1
```

### Explanation

The character `"P"` appears exactly once.

---

# Question 75

## Predict the Output

```python
print("banana".count("na"))
```

### Output

```text
2
```

### Explanation

The substring `"na"` occurs two times:

```text
ba[na][na]
```

---

# Summary (Part 3)

In this part, you practiced output-based interview questions on:

* Advanced slicing
* Reverse traversal
* Method chaining
* `swapcase()`
* `title()`
* `capitalize()`
* `startswith()`
* `endswith()`
* `join()`
* `split()`
* `find()`
* `index()`
* `count()`

The next part will be the **final section** of output-based interview questions. It will cover:

* Raw strings
* Escape sequences
* `isalpha()`, `isalnum()`, `isspace()`
* `partition()`
* `rpartition()`
* `zfill()`
* `center()`
* `ljust()`
* `rjust()`
* `encode()` and `decode()`
* Several tricky MNC-style interview questions.
