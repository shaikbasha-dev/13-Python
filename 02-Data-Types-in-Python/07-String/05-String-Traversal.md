# String (`str`) - Traversal

## Introduction

**String Traversal** is the process of accessing each character of a string one by one.

Since a string is a sequence of characters, Python provides multiple ways to traverse it.

String traversal is commonly used in:

* Searching characters
* Counting vowels
* Finding digits
* Password validation
* Text processing
* Pattern matching
* Encryption algorithms
* Data validation

---

# Why String Traversal?

Suppose we have the following string:

```python
language = "Python"
```

To process every character individually, we need to traverse the string.

---

# Methods of String Traversal

Python provides several ways to traverse a string.

```text
String Traversal

│

├── for Loop

├── while Loop

├── enumerate()

├── range() with Index

└── Iterators
```

---

# Method 1: Using for Loop

The `for` loop is the simplest and most commonly used method.

## Syntax

```python
for variable in string:
    statements
```

---

## Program

```python
language = "Python"

for character in language:
    print(character)
```

---

## Output

```text
P
y
t
h
o
n
```

---

## Dry Run

```text
language = "Python"

↓

Iteration 1 → P

Iteration 2 → y

Iteration 3 → t

Iteration 4 → h

Iteration 5 → o

Iteration 6 → n
```

---

# Method 2: Using while Loop

A `while` loop traverses the string using an index.

## Program

```python
language = "Python"

index = 0

while index < len(language):
    print(language[index])
    index += 1
```

---

## Output

```text
P
y
t
h
o
n
```

---

# Method 3: Using range()

The `range()` function generates indexes.

## Program

```python
language = "Python"

for index in range(len(language)):
    print(language[index])
```

---

## Output

```text
P
y
t
h
o
n
```

---

# Method 4: Using enumerate()

The `enumerate()` function returns both the index and the corresponding character.

## Program

```python
language = "Python"

for index, character in enumerate(language):
    print(index, character)
```

---

## Output

```text
0 P
1 y
2 t
3 h
4 o
5 n
```

---

# Method 5: Using an Iterator

Strings are iterable objects.

Python allows explicit iteration using `iter()` and `next()`.

## Program

```python
language = "Python"

iterator = iter(language)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

---

## Output

```text
P
y
t
```

---

# Traversing in Reverse Order

Python allows reverse traversal using slicing.

## Example

```python
language = "Python"

for character in language[::-1]:
    print(character)
```

---

## Output

```text
n
o
h
t
y
P
```

---

# Traversing Every Second Character

```python
language = "Python"

for character in language[::2]:
    print(character)
```

---

## Output

```text
P
t
o
```

---

# Counting Characters

Example

```python
text = "Programming"

count = 0

for character in text:
    count += 1

print(count)
```

---

## Output

```text
11
```

Although `len()` is simpler, this example demonstrates manual traversal.

---

# Counting Vowels

Example

```python
text = "Python Programming"

count = 0

for character in text.lower():
    if character in "aeiou":
        count += 1

print(count)
```

---

## Output

```text
4
```

---

# Finding Digits

Example

```python
text = "Python123"

for character in text:
    if character.isdigit():
        print(character)
```

---

## Output

```text
1
2
3
```

---

# Memory Representation

```python
language = "Python"
```

```text
          language
              │
              ▼
+---+---+---+---+---+---+
| P | y | t | h | o | n |
+---+---+---+---+---+---+
  0   1   2   3   4   5
```

During traversal, Python accesses one character at a time from left to right unless instructed otherwise.

---

# Real-World Applications

String traversal is widely used in:

* Password validation
* Email validation
* Text editors
* Spell checking
* Search engines
* Log analysis
* File parsing
* Natural Language Processing (NLP)

---

# Best Practices

* Use a `for` loop for simple traversal.
* Use `enumerate()` when both the index and character are required.
* Use `while` loops only when index manipulation is necessary.
* Use slicing (`[::-1]`) for reverse traversal.
* Prefer built-in functions when available.

---

# Common Mistakes

## 1. Going Beyond the String Length

Incorrect

```python
language = "Python"

print(language[6])
```

Output

```text
IndexError
```

---

## 2. Forgetting to Increment the Index

Incorrect

```python
index = 0

while index < len(language):
    print(language[index])
```

This creates an infinite loop because `index` never changes.

---

## 3. Calling `next()` Too Many Times

```python
iterator = iter("Hi")

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output

```text
StopIteration
```

An iterator raises `StopIteration` when there are no more elements.

---

# Frequently Asked Interview Questions

## 1. What is string traversal?

String traversal is the process of accessing every character of a string one by one.

---

## 2. Which loop is most commonly used for string traversal?

The `for` loop.

---

## 3. What does `enumerate()` return?

It returns both the index and the corresponding element.

---

## 4. How do you traverse a string in reverse?

Using slicing:

```python
text[::-1]
```

---

## 5. Why is `enumerate()` useful?

It provides both the index and the value during iteration.

---

## 6. What exception does `next()` raise when an iterator is exhausted?

`StopIteration`

---

# Summary

In this chapter, you learned:

* String traversal
* Traversal using `for`
* Traversal using `while`
* Traversal using `range()`
* Traversal using `enumerate()`
* Traversal using iterators
* Reverse traversal
* Traversing alternate characters
* Counting characters
* Counting vowels
* Finding digits
* Real-world applications
* Best practices
* Common mistakes
* Frequently asked interview questions

In the next chapter, you will learn **String Advanced Concepts**, including string immutability, memory management, string interning, Unicode representation, object identity, performance optimization, and Python's internal implementation.
