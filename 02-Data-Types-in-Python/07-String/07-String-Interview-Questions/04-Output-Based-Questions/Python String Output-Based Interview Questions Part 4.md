Python String Output-Based Interview Questions Part 4

---

---

# Question 76

## Predict the Output

```python
print(r"C:\new\test")
```

### Output

```text
C:\new\test
```

### Explanation

The prefix `r` creates a **raw string**, so backslashes are treated as ordinary characters instead of escape sequences.

---

# Question 77

## Predict the Output

```python
print("C:\\new\\test")
```

### Output

```text
C:\new\test
```

### Explanation

The backslash (`\`) is an escape character.

To print a literal backslash, use `\\`.

---

# Question 78

## Predict the Output

```python
print("Hello\nPython")
```

### Output

```text
Hello
Python
```

### Explanation

`\n` inserts a new line.

---

# Question 79

## Predict the Output

```python
print("Name\tAge")
```

### Output

```text
Name    Age
```

### Explanation

`\t` inserts a horizontal tab.

---

# Question 80

## Predict the Output

```python
print("Python".isupper())
```

### Output

```text
False
```

### Explanation

Not all alphabetic characters are uppercase.

---

# Question 81

## Predict the Output

```python
print("PYTHON".isupper())
```

### Output

```text
True
```

### Explanation

Every alphabetic character is uppercase.

---

# Question 82

## Predict the Output

```python
print("python".islower())
```

### Output

```text
True
```

### Explanation

Every alphabetic character is lowercase.

---

# Question 83

## Predict the Output

```python
print("Python123".isalnum())
```

### Output

```text
True
```

### Explanation

The string contains only letters and digits.

---

# Question 84

## Predict the Output

```python
print("Python 123".isalnum())
```

### Output

```text
False
```

### Explanation

The space character is neither a letter nor a digit.

---

# Question 85

## Predict the Output

```python
print("Python".isalpha())
```

### Output

```text
True
```

### Explanation

Every character is alphabetic.

---

# Question 86

## Predict the Output

```python
print("Python123".isdigit())
```

### Output

```text
False
```

### Explanation

The string contains alphabetic characters, so `isdigit()` returns `False`.

---

# Question 87

## Predict the Output

```python
print("123456".isdigit())
```

### Output

```text
True
```

### Explanation

Every character is a digit.

---

# Question 88

## Predict the Output

```python
print("   ".isspace())
```

### Output

```text
True
```

### Explanation

The string contains only whitespace characters.

---

# Question 89

## Predict the Output

```python
print("Python".isspace())
```

### Output

```text
False
```

### Explanation

The string contains alphabetic characters.

---

# Question 90

## Predict the Output

```python
print("Python".partition("t"))
```

### Output

```text
('Py', 't', 'hon')
```

### Explanation

`partition()` returns a tuple with:

* Text before the separator
* The separator
* Text after the separator

---

# Question 91

## Predict the Output

```python
print("one-two-three".rpartition("-"))
```

### Output

```text
('one-two', '-', 'three')
```

### Explanation

`rpartition()` splits the string at the **last** occurrence of the separator.

---

# Question 92

## Predict the Output

```python
print("25".zfill(5))
```

### Output

```text
00025
```

### Explanation

`zfill()` pads the string on the left with zeros until it reaches the specified width.

---

# Question 93

## Predict the Output

```python
print("Python".center(12, "-"))
```

### Output

```text
---Python---
```

### Explanation

The string is centered within a width of 12 using `-` as the fill character.

---

# Question 94

## Predict the Output

```python
print("Python".ljust(10, "*"))
```

### Output

```text
Python****
```

### Explanation

`ljust()` left-aligns the string and fills the remaining positions on the right.

---

# Question 95

## Predict the Output

```python
print("Python".rjust(10, "*"))
```

### Output

```text
****Python
```

### Explanation

`rjust()` right-aligns the string and fills the remaining positions on the left.

---

# Question 96

## Predict the Output

```python
print("Python".encode())
```

### Output

```text
b'Python'
```

### Explanation

`encode()` converts the string into a bytes object using UTF-8 by default.

---

# Question 97

## Predict the Output

```python
data = b'Python'

print(data.decode())
```

### Output

```text
Python
```

### Explanation

`decode()` converts bytes back into a string.

---

# Question 98

## Predict the Output

```python
text = "Python"

print(text * 0)
```

### Output

```text
```

### Explanation

Repeating a string zero times returns an empty string.

---

# Question 99

## Predict the Output

```python
text = ""

print(len(text))
```

### Output

```text
0
```

### Explanation

An empty string contains zero characters.

---

# Question 100

## Predict the Output

```python
text = "Python"

print(text[:])
```

### Output

```text
Python
```

### Explanation

`[:]` creates a full slice of the string, effectively returning a copy of the original string.

---

# Final Summary

In this complete output-based interview guide, you practiced questions covering:

* Positive and negative indexing
* String slicing
* Step slicing
* Reverse slicing
* Concatenation
* Repetition
* Membership operators
* Comparison operators
* String formatting
* String methods
* Method chaining
* Boolean evaluation
* Escape sequences
* Raw strings
* Character classification methods
* `partition()` and `rpartition()`
* `zfill()`, `center()`, `ljust()`, and `rjust()`
* Encoding and decoding
* Unicode concepts
* Object identity
* String interning
* Common interview edge cases

These 100 output-based questions provide strong preparation for Python technical interviews and help build confidence in understanding how Python strings behave in different scenarios.
