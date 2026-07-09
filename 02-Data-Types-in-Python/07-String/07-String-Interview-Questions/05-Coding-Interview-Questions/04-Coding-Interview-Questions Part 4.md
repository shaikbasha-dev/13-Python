# Coding-Interview-Questions Part 4

---

# Question 31: Longest Palindromic Substring

## Problem Statement

Write a Python program to find the longest palindromic substring.

---

## Example

Input

```text
babad
```

Possible Output

```text
bab
```

or

```text
aba
```

(Both are correct.)

---

## Program

```python
def longest_palindrome(text):
    if len(text) < 2:
        return text

    start = 0
    max_length = 1

    for i in range(len(text)):
        # Odd length palindrome
        left = right = i
        while left >= 0 and right < len(text) and text[left] == text[right]:
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1

        # Even length palindrome
        left, right = i, i + 1
        while left >= 0 and right < len(text) and text[left] == text[right]:
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1

    return text[start:start + max_length]


print(longest_palindrome("babad"))
```

---

## Time Complexity

```text
O(n²)
```

---

## Space Complexity

```text
O(1)
```

---

## Interview Tip

The "expand around center" approach is the most common interview solution. Some interviewers may ask about **Manacher's Algorithm**, which solves the problem in **O(n)** time.

---

# Question 32: Longest Substring Without Repeating Characters

## Problem Statement

Find the length of the longest substring without repeating characters.

---

## Example

Input

```text
abcabcbb
```

Output

```text
3
```

Explanation

The longest substring is:

```text
abc
```

---

## Program

```python
text = "abcabcbb"

seen = {}
left = 0
maximum = 0

for right, character in enumerate(text):
    if character in seen and seen[character] >= left:
        left = seen[character] + 1

    seen[character] = right
    maximum = max(maximum, right - left + 1)

print(maximum)
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

This is one of the most common **Sliding Window** interview questions.

---

# Question 33: Implement `find()` Without Using `find()`

## Problem Statement

Write your own implementation of the `find()` method.

---

## Program

```python
text = "Python Programming"
pattern = "Program"

position = -1

for i in range(len(text) - len(pattern) + 1):
    if text[i:i + len(pattern)] == pattern:
        position = i
        break

print(position)
```

---

## Output

```text
7
```

---

## Time Complexity

```text
O(n × m)
```

Where:

* **n** = Length of the text
* **m** = Length of the pattern

---

# Question 34: Implement `replace()` Without Using `replace()`

## Problem Statement

Replace all occurrences of one substring with another without using the built-in `replace()` method.

---

## Program

```python
text = "Python is fun"
old = "fun"
new = "awesome"

parts = text.split(old)
result = new.join(parts)

print(result)
```

---

## Output

```text
Python is awesome
```

---

## Interview Tip

A more advanced version avoids using both `split()` and `replace()` and performs manual substring matching.

---

# Question 35: Implement `split()` Without Using `split()`

## Problem Statement

Split a string into words without using the built-in `split()` method.

---

## Program

```python
text = "Python is powerful"

words = []
current = ""

for character in text:
    if character == " ":
        if current:
            words.append(current)
            current = ""
    else:
        current += character

if current:
    words.append(current)

print(words)
```

---

## Output

```text
['Python', 'is', 'powerful']
```

---

## Time Complexity

```text
O(n)
```

---

# Question 36: Check Whether One String is a Subsequence of Another

## Problem Statement

Determine whether one string is a subsequence of another.

---

## Example

```text
Text : programming

Pattern : pgm
```

Output

```text
True
```

---

## Program

```python
text = "programming"
pattern = "pgm"

index = 0

for character in text:
    if index < len(pattern) and character == pattern[index]:
        index += 1

print(index == len(pattern))
```

---

## Time Complexity

```text
O(n)
```

---

# Question 37: Pattern Matching (Naive Algorithm)

## Problem Statement

Find all occurrences of a pattern in a string.

---

## Program

```python
text = "ABABABA"
pattern = "ABA"

for i in range(len(text) - len(pattern) + 1):
    if text[i:i + len(pattern)] == pattern:
        print(i)
```

---

## Output

```text
0
2
4
```

---

## Interview Tip

The naive algorithm is easy to understand but not optimal for very large inputs.

---

# Question 38: Introduction to KMP Pattern Matching

## Concept

The **Knuth–Morris–Pratt (KMP)** algorithm improves pattern matching by avoiding unnecessary comparisons.

### Advantages

* Faster than the naive algorithm.
* Uses a preprocessing table called the **LPS (Longest Prefix Suffix)** array.
* Efficient for repeated pattern searches.

### Time Complexity

```text
O(n + m)
```

Where:

* **n** = Length of the text
* **m** = Length of the pattern

---

# Question 39: Introduction to Rabin–Karp Algorithm

## Concept

The **Rabin–Karp** algorithm uses hashing to search for patterns.

### Advantages

* Efficient for searching multiple patterns.
* Uses rolling hash values.

### Average Time Complexity

```text
O(n + m)
```

Worst Case

```text
O(n × m)
```

---

# Question 40: Sliding Window Technique

## Problem Statement

Explain why the Sliding Window technique is widely used in string interview problems.

---

## Answer

The Sliding Window technique processes a subset of characters while moving through the string one position at a time.

It avoids recomputing results from scratch, making many string algorithms significantly more efficient.

### Common Problems Solved Using Sliding Window

* Longest substring without repeating characters
* Minimum window substring
* Permutation in string
* Maximum vowels in a substring
* Fixed-size window problems

### Time Complexity

Most Sliding Window algorithms run in:

```text
O(n)
```

---

# Final Summary

Congratulations! You have completed the **Python String Coding Interview Questions** section.

This file covered:

* String reversal
* Palindrome problems
* Character counting
* Duplicate detection
* Frequency analysis
* Anagrams
* String compression
* String rotation
* Longest common prefix
* Isomorphic strings
* String permutations
* Pattern matching
* Longest palindromic substring
* Sliding Window technique
* KMP algorithm
* Rabin–Karp algorithm
* Manual implementation of common string methods
* FAANG-style interview concepts

By practicing these 40 coding questions and understanding their algorithms, dry runs, and complexity analysis, you will build a strong foundation for Python string coding interviews ranging from beginner to advanced levels.
