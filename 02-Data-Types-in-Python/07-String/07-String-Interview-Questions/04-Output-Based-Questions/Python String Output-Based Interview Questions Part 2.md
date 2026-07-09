# Python String Output-Based Interview Questions Part 2

---

---

# Question 21

## Predict the Output

```python
print("Python" == "Python")
```

### Output

```text
True
```

### Explanation

Both strings have the same value, so the `==` operator returns `True`.

---

# Question 22

## Predict the Output

```python
print("Python" == "python")
```

### Output

```text
False
```

### Explanation

String comparison is **case-sensitive**.

---

# Question 23

## Predict the Output

```python
print("Apple" < "Banana")
```

### Output

```text
True
```

### Explanation

Strings are compared lexicographically (dictionary order) using Unicode values.

Since `"Apple"` comes before `"Banana"`, the result is `True`.

---

# Question 24

## Predict the Output

```python
print("Zoo" > "Apple")
```

### Output

```text
True
```

### Explanation

The Unicode value of `'Z'` is greater than the Unicode value of `'A'`.

---

# Question 25

## Predict the Output

```python
print(ord("A"))
```

### Output

```text
65
```

### Explanation

The `ord()` function returns the Unicode code point of a character.

---

# Question 26

## Predict the Output

```python
print(chr(97))
```

### Output

```text
a
```

### Explanation

The `chr()` function returns the character corresponding to the Unicode code point.

---

# Question 27

## Predict the Output

```python
text = "Python"

print(text.isalpha())
```

### Output

```text
True
```

### Explanation

All characters are alphabetic.

---

# Question 28

## Predict the Output

```python
print("Python123".isalpha())
```

### Output

```text
False
```

### Explanation

Digits are present, so `isalpha()` returns `False`.

---

# Question 29

## Predict the Output

```python
print("12345".isdigit())
```

### Output

```text
True
```

### Explanation

Every character is a digit.

---

# Question 30

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

# Question 31

## Predict the Output

```python
print("   Python   ".strip())
```

### Output

```text
Python
```

### Explanation

The `strip()` method removes leading and trailing whitespace.

---

# Question 32

## Predict the Output

```python
print("Python".center(10, "*"))
```

### Output

```text
**Python**
```

### Explanation

The string is centered in a field of width `10`, with `*` used as the fill character.

---

# Question 33

## Predict the Output

```python
print(",".join(["A", "B", "C"]))
```

### Output

```text
A,B,C
```

### Explanation

The `join()` method combines list elements using the specified separator.

---

# Question 34

## Predict the Output

```python
print("Python,Java,C++".split(","))
```

### Output

```text
['Python', 'Java', 'C++']
```

### Explanation

The `split()` method divides the string into a list using the comma as the separator.

---

# Question 35

## Predict the Output

```python
print("banana".replace("a", "@"))
```

### Output

```text
b@n@n@
```

### Explanation

Every occurrence of `"a"` is replaced with `"@"`.

---

# Question 36

## Predict the Output

```python
text = "Python"

print(text[0:100])
```

### Output

```text
Python
```

### Explanation

The stop index exceeds the string length.

Python safely returns all available characters without raising an exception.

---

# Question 37

## Predict the Output

```python
text = "Python"

print(text[100:])
```

### Output

```text
```

### Explanation

The starting index is beyond the end of the string.

Python returns an empty string.

---

# Question 38

## Predict the Output

```python
text = "Python"

print(text[::-2])
```

### Output

```text
nhy
```

### Explanation

Traversal starts from the last character and moves backward by two positions.

Characters selected:

```text
n h y
```

---

# Question 39

## Predict the Output

```python
print(bool(""))
```

### Output

```text
False
```

### Explanation

An empty string evaluates to `False`.

---

# Question 40

## Predict the Output

```python
print(bool(" "))
```

### Output

```text
True
```

### Explanation

The string contains one space.

It is **not** empty.

---

# Question 41

## Predict the Output

```python
print(bool("Python"))
```

### Output

```text
True
```

### Explanation

Any non-empty string evaluates to `True`.

---

# Question 42

## Predict the Output

```python
name = "Basha"

print(f"Welcome {name}")
```

### Output

```text
Welcome Basha
```

### Explanation

An f-string inserts the value of the variable directly into the string.

---

# Question 43

## Predict the Output

```python
print("{} {}".format("Python", "Programming"))
```

### Output

```text
Python Programming
```

### Explanation

The `format()` method replaces placeholders with the supplied values.

---

# Question 44

## Predict the Output

```python
print("%s %d" % ("Age", 25))
```

### Output

```text
Age 25
```

### Explanation

The `%` formatting operator inserts values according to the specified format specifiers.

---

# Question 45

## Predict the Output

```python
text = "Python"

print(id(text) == id(text))
```

### Output

```text
True
```

### Explanation

The same variable refers to the same object, so both calls to `id()` return the same identity during that execution.

---

# Question 46

## Predict the Output

```python
a = "Python"

b = "Python"

print(a is b)
```

### Output

```text
True
```

### Explanation

Python commonly interns identical string literals.

Both variables reference the same string object.

---

# Question 47

## Predict the Output

```python
a = "Python"

b = a

print(a is b)
```

### Output

```text
True
```

### Explanation

Variable `b` references the same object as `a`.

---

# Question 48

## Predict the Output

```python
text = "Python"

print(text.capitalize())
```

### Output

```text
Python
```

### Explanation

The first character is already uppercase, so the string remains unchanged.

---

# Question 49

## Predict the Output

```python
print("python".capitalize())
```

### Output

```text
Python
```

### Explanation

The first character becomes uppercase while the remaining characters become lowercase.

---

# Question 50

## Predict the Output

```python
print("PYTHON".title())
```

### Output

```text
Python
```

### Explanation

The `title()` method converts the first character of each word to uppercase and the remaining characters to lowercase.

---

# Summary (Part 2)

In this part, you practiced output-based interview questions on:

* String comparison
* Unicode functions (`ord()` and `chr()`)
* Character classification methods
* `strip()`
* `join()`
* `split()`
* `replace()`
* Boolean evaluation of strings
* String formatting
* Object identity
* String interning
* `capitalize()`
* `title()`

The next part will contain more advanced and tricky interview questions involving exceptions, indexing edge cases, slicing behavior, escape sequences, raw strings, nested operations, and method chaining.
