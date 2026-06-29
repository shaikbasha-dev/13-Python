# String Methods in Python

## Learning Objectives

After completing this chapter, you will be able to:

- Understand String Methods.
- Explain why string methods are used.
- Learn commonly used string methods.
- Modify and analyze strings efficiently.
- Write programs using string methods.

---

# Introduction

Python provides many **built-in methods** to perform operations on strings.

These methods make string manipulation easier and reduce the amount of code we need to write.

Examples include:

- Converting text to uppercase.
- Converting text to lowercase.
- Removing spaces.
- Replacing characters.
- Searching for text.
- Counting characters.
- Splitting strings.

---

# Definition

A **String Method** is a built-in function that performs a specific operation on a string and returns the result.

Since strings are immutable, these methods do **not** modify the original string. Instead, they return a new string.

---

# Why do we use String Methods?

String methods help us to:

- Format text.
- Validate user input.
- Search data.
- Replace text.
- Remove unwanted spaces.
- Convert text into different formats.

---

# Commonly Used String Methods

| Method | Description |
|---------|-------------|
| upper() | Converts string to uppercase |
| lower() | Converts string to lowercase |
| title() | Converts first letter of every word to uppercase |
| capitalize() | Capitalizes the first letter of the string |
| swapcase() | Swaps uppercase to lowercase and vice versa |
| strip() | Removes spaces from both sides |
| lstrip() | Removes spaces from the left side |
| rstrip() | Removes spaces from the right side |
| replace() | Replaces one substring with another |
| find() | Finds the first occurrence of a substring |
| count() | Counts occurrences of a substring |
| startswith() | Checks whether a string starts with a value |
| endswith() | Checks whether a string ends with a value |
| split() | Splits a string into a list |
| join() | Joins elements into a string |

---

# 1. upper()

## Definition

Converts all characters into uppercase.

### Program

```python
text = "python"

print(text.upper())
```

### Output

```text
PYTHON
```

---

# 2. lower()

## Definition

Converts all characters into lowercase.

### Program

```python
text = "PYTHON"

print(text.lower())
```

### Output

```text
python
```

---

# 3. title()

## Definition

Converts the first letter of every word into uppercase.

### Program

```python
text = "python programming"

print(text.title())
```

### Output

```text
Python Programming
```

---

# 4. capitalize()

## Definition

Converts only the first letter of the string into uppercase.

### Program

```python
text = "python programming"

print(text.capitalize())
```

### Output

```text
Python programming
```

---

# 5. swapcase()

## Definition

Converts uppercase letters into lowercase and lowercase letters into uppercase.

### Program

```python
text = "Python"

print(text.swapcase())
```

### Output

```text
pYTHON
```

---

# 6. strip()

## Definition

Removes spaces from both sides.

### Program

```python
text = "   Python   "

print(text.strip())
```

### Output

```text
Python
```

---

# 7. lstrip()

## Definition

Removes spaces from the left side.

### Program

```python
text = "   Python"

print(text.lstrip())
```

### Output

```text
Python
```

---

# 8. rstrip()

## Definition

Removes spaces from the right side.

### Program

```python
text = "Python   "

print(text.rstrip())
```

### Output

```text
Python
```

---

# 9. replace()

## Definition

Replaces a specified substring with another substring.

### Program

```python
text = "I like Java"

print(text.replace("Java", "Python"))
```

### Output

```text
I like Python
```

---

# 10. find()

## Definition

Returns the index of the first occurrence of a substring.

### Program

```python
text = "Python Programming"

print(text.find("Program"))
```

### Output

```text
7
```

---

# 11. count()

## Definition

Returns the number of occurrences of a substring.

### Program

```python
text = "banana"

print(text.count("a"))
```

### Output

```text
3
```

---

# 12. startswith()

## Definition

Checks whether a string starts with the specified value.

### Program

```python
text = "Python Programming"

print(text.startswith("Python"))
```

### Output

```text
True
```

---

# 13. endswith()

## Definition

Checks whether a string ends with the specified value.

### Program

```python
text = "Python Programming"

print(text.endswith("Programming"))
```

### Output

```text
True
```

---

# 14. split()

## Definition

Splits a string into multiple parts and returns a list.

### Program

```python
text = "Python Java C++"

print(text.split())
```

### Output

```text
['Python', 'Java', 'C++']
```

---

# 15. join()

## Definition

Joins elements of a sequence into a single string.

### Program

```python
languages = ["Python", "Java", "C++"]

print(" - ".join(languages))
```

### Output

```text
Python - Java - C++
```

---

# Real-Time Applications

String methods are widely used in:

- Login Systems
- Form Validation
- Search Engines
- Text Editors
- Chat Applications
- Data Cleaning
- Report Generation

---

# Advantages

- Easy string manipulation.
- Reduces code complexity.
- Improves readability.
- Saves development time.
- Provides built-in optimized operations.

---

# Common Mistakes

## Forgetting Strings are Immutable

```python
text = "python"

text.upper()

print(text)
```

Output

```text
python
```

Correct

```python
text = text.upper()
```

---

## Using find() Incorrectly

If the substring is not found,

```python
find()
```

returns

```text
-1
```

It does **not** generate an error.

---

# Interview Questions

## 1. What are String Methods?

### Answer

String methods are built-in functions used to perform operations on strings.

---

## 2. Do String Methods modify the original string?

### Answer

No.

Strings are immutable. String methods return a new string.

---

## 3. What is the difference between upper() and lower()?

### Answer

- `upper()` converts all letters to uppercase.
- `lower()` converts all letters to lowercase.

---

## 4. Which method removes spaces?

### Answer

- `strip()`
- `lstrip()`
- `rstrip()`

---

## 5. What is the difference between find() and count()?

### Answer

- `find()` returns the index of the first occurrence.
- `count()` returns the number of occurrences.

---

# Quick Revision

- `upper()` → Uppercase
- `lower()` → Lowercase
- `title()` → Title Case
- `capitalize()` → First letter uppercase
- `swapcase()` → Reverse case
- `strip()` → Remove spaces
- `replace()` → Replace text
- `find()` → Find index
- `count()` → Count occurrences
- `split()` → Convert string to list
- `join()` → Convert list to string

---

# Summary

In this chapter, you learned:

- What String Methods are.
- Why they are used.
- The most commonly used string methods.
- Practical examples with outputs.
- Real-world applications.
- Common mistakes.
- Interview questions.

