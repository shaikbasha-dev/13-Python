# Coding-Interview-Questions Part 1

# Python String Coding Interview Questions

## Introduction

This document contains coding-based interview questions on Python Strings. These problems are commonly asked in technical interviews and coding assessments.

Each question includes:

* Problem Statement
* Example
* Python Program
* Output
* Algorithm
* Dry Run
* Time Complexity
* Space Complexity
* Interview Tips

---

# Question 1: Reverse a String

## Problem Statement

Write a Python program to reverse a given string.

---

## Example

Input

```text
Python
```

Output

```text
nohtyP
```

---

## Program

```python
text = "Python"

reversed_text = text[::-1]

print(reversed_text)
```

---

## Output

```text
nohtyP
```

---

## Algorithm

```text
START

Read the string

Reverse using slicing

Display the reversed string

STOP
```

---

## Dry Run

```text
Python

↓

nohtyP
```

---

## Time Complexity

```text
O(n)
```

---

## Space Complexity

```text
O(n)
```

---

## Interview Tip

Slicing (`[::-1]`) is the most concise solution in Python, but interviewers may also ask you to solve it without slicing.

---

# Question 2: Check Whether a String is a Palindrome

## Problem Statement

Write a program to determine whether a string reads the same forwards and backwards.

---

## Example

Input

```text
madam
```

Output

```text
Palindrome
```

---

## Program

```python
text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
```

---

## Output

```text
Palindrome
```

---

## Algorithm

```text
START

Read the string

Reverse the string

Compare original and reversed strings

If equal

Display Palindrome

Else

Display Not Palindrome

STOP
```

---

## Dry Run

```text
madam

↓

madam

↓

Equal

↓

Palindrome
```

---

## Time Complexity

```text
O(n)
```

---

## Space Complexity

```text
O(n)
```

---

## Interview Tip

Interviewers often ask for a solution without creating a reversed copy by comparing characters from both ends.

---

# Question 3: Count Vowels in a String

## Problem Statement

Write a program to count the number of vowels in a string.

---

## Example

Input

```text
Programming
```

Output

```text
3
```

---

## Program

```python
text = "Programming"

count = 0

for character in text.lower():
    if character in "aeiou":
        count += 1

print(count)
```

---

## Output

```text
3
```

---

## Algorithm

```text
START

Read the string

Initialize count = 0

Traverse each character

If character is a vowel

Increment count

Display count

STOP
```

---

## Dry Run

```text
Programming

↓

o ✓

a ✓

i ✓

↓

Count = 3
```

---

## Time Complexity

```text
O(n)
```

---

## Space Complexity

```text
O(1)
```

---

## Interview Tip

Convert the string to lowercase (or uppercase) first to avoid checking both uppercase and lowercase vowels.

---

# Question 4: Count Consonants in a String

## Problem Statement

Write a program to count consonants in a string.

---

## Program

```python
text = "Programming"

count = 0

for character in text.lower():
    if character.isalpha() and character not in "aeiou":
        count += 1

print(count)
```

---

## Output

```text
8
```

---

## Time Complexity

```text
O(n)
```

---

## Space Complexity

```text
O(1)
```

---

## Interview Tip

Always check `isalpha()` before counting consonants to avoid counting digits and symbols.

---

# Question 5: Count Digits in a String

## Problem Statement

Write a program to count the number of digits present in a string.

---

## Program

```python
text = "Python12345"

count = 0

for character in text:
    if character.isdigit():
        count += 1

print(count)
```

---

## Output

```text
5
```

---

## Time Complexity

```text
O(n)
```

---

## Space Complexity

```text
O(1)
```

---

# Question 6: Remove Spaces from a String

## Problem Statement

Write a Python program to remove all spaces from a string.

---

## Program

```python
text = "Python Programming Language"

result = text.replace(" ", "")

print(result)
```

---

## Output

```text
PythonProgrammingLanguage
```

---

## Time Complexity

```text
O(n)
```

---

# Question 7: Count Words in a String

## Problem Statement

Write a Python program to count the total number of words in a sentence.

---

## Program

```python
sentence = "Python is an easy programming language"

words = sentence.split()

print(len(words))
```

---

## Output

```text
6
```

---

## Time Complexity

```text
O(n)
```

---

## Interview Tip

Using `split()` is the simplest and most Pythonic solution.

---

# Question 8: Convert Uppercase to Lowercase

## Problem Statement

Write a program to convert a string into lowercase.

---

## Program

```python
text = "PYTHON PROGRAMMING"

print(text.lower())
```

---

## Output

```text
python programming
```

---

# Question 9: Convert Lowercase to Uppercase

## Problem Statement

Write a program to convert a string into uppercase.

---

## Program

```python
text = "python programming"

print(text.upper())
```

---

## Output

```text
PYTHON PROGRAMMING
```

---

# Question 10: Find the Length of a String Without Using `len()`

## Problem Statement

Write a program to determine the length of a string without using the built-in `len()` function.

---

## Program

```python
text = "Python"

count = 0

for _ in text:
    count += 1

print(count)
```

---

## Output

```text
6
```

---

## Algorithm

```text
START

Read the string

Initialize count = 0

Traverse each character

Increment count

Display count

STOP
```

---

## Time Complexity

```text
O(n)
```

---

## Space Complexity

```text
O(1)
```

---

# Summary (Part 1)

In this part, you solved coding interview problems on:

* Reverse a string
* Palindrome
* Count vowels
* Count consonants
* Count digits
* Remove spaces
* Count words
* Convert case
* Find string length without `len()`

These are among the most frequently asked beginner-level coding questions in Python interviews.

The next part will cover:

* Character frequency
* Duplicate characters
* First non-repeating character
* First repeating character
* Anagram
* String compression
* Reverse words
* Remove duplicate characters
* Longest word
* Most frequent character
