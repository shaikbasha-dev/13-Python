# Coding-Interview-Questions Part 2

---

# Question 11: Count Frequency of Each Character

## Problem Statement

Write a Python program to count the frequency of each character in a string.

---

## Example

Input

```text
programming
```

Output

```text
p : 1
r : 2
o : 1
g : 2
a : 1
m : 2
i : 1
n : 1
```

---

## Program

```python
text = "programming"

frequency = {}

for character in text:
    frequency[character] = frequency.get(character, 0) + 1

for character, count in frequency.items():
    print(character, ":", count)
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

Using `dictionary.get()` makes the code shorter and avoids checking whether a key already exists.

---

# Question 12: Find Duplicate Characters

## Problem Statement

Write a Python program to print all duplicate characters in a string.

---

## Program

```python
text = "programming"

visited = set()

duplicates = set()

for character in text:
    if character in visited:
        duplicates.add(character)
    else:
        visited.add(character)

print(duplicates)
```

---

## Output

```text
{'r', 'g', 'm'}
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

# Question 13: Find the First Non-Repeating Character

## Problem Statement

Write a Python program to find the first character that appears only once.

---

## Program

```python
text = "programming"

frequency = {}

for character in text:
    frequency[character] = frequency.get(character, 0) + 1

for character in text:
    if frequency[character] == 1:
        print(character)
        break
```

---

## Output

```text
p
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

# Question 14: Find the First Repeating Character

## Problem Statement

Write a Python program to find the first repeating character.

---

## Program

```python
text = "programming"

visited = set()

for character in text:
    if character in visited:
        print(character)
        break
    visited.add(character)
```

---

## Output

```text
r
```

---

## Time Complexity

```text
O(n)
```

---

# Question 15: Check Whether Two Strings are Anagrams

## Problem Statement

Two strings are anagrams if they contain the same characters with the same frequencies.

---

## Program

```python
string1 = "listen"

string2 = "silent"

if sorted(string1) == sorted(string2):
    print("Anagram")
else:
    print("Not Anagram")
```

---

## Output

```text
Anagram
```

---

## Time Complexity

```text
O(n log n)
```

---

## Interview Tip

An interviewer may also ask for an **O(n)** solution using a dictionary or `collections.Counter`.

---

# Question 16: Remove Duplicate Characters

## Problem Statement

Write a Python program to remove duplicate characters while preserving their original order.

---

## Program

```python
text = "programming"

result = ""

for character in text:
    if character not in result:
        result += character

print(result)
```

---

## Output

```text
progamin
```

---

## Time Complexity

```text
O(n²)
```

---

## Interview Tip

A more efficient solution can be built using a `set()` along with a list or string builder.

---

# Question 17: Reverse Every Word in a Sentence

## Problem Statement

Reverse each word without changing the order of the words.

---

## Program

```python
sentence = "Python is awesome"

words = sentence.split()

result = []

for word in words:
    result.append(word[::-1])

print(" ".join(result))
```

---

## Output

```text
nohtyP si emosewa
```

---

## Time Complexity

```text
O(n)
```

---

# Question 18: Reverse the Order of Words

## Problem Statement

Reverse the order of words in a sentence.

---

## Program

```python
sentence = "Python is awesome"

words = sentence.split()

print(" ".join(words[::-1]))
```

---

## Output

```text
awesome is Python
```

---

## Time Complexity

```text
O(n)
```

---

# Question 19: Find the Longest Word

## Problem Statement

Write a Python program to find the longest word in a sentence.

---

## Program

```python
sentence = "Python is a powerful programming language"

words = sentence.split()

longest = max(words, key=len)

print(longest)
```

---

## Output

```text
programming
```

---

## Time Complexity

```text
O(n)
```

---

# Question 20: Find the Most Frequent Character

## Problem Statement

Write a Python program to find the character that appears most frequently.

---

## Program

```python
text = "programming"

frequency = {}

for character in text:
    frequency[character] = frequency.get(character, 0) + 1

most_frequent = max(frequency, key=frequency.get)

print(most_frequent)
```

---

## Output

```text
r
```

> **Note:** In this example, `r`, `g`, and `m` each appear twice. The `max()` function returns the first key with the highest value based on the dictionary's iteration order.

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

# Summary (Part 2)

In this part, you solved coding interview problems on:

* Character frequency
* Duplicate characters
* First non-repeating character
* First repeating character
* Anagrams
* Removing duplicate characters
* Reversing every word
* Reversing word order
* Finding the longest word
* Finding the most frequent character

These are among the most commonly asked string coding problems in Python interviews.

The next part will cover advanced coding problems, including:

* String compression
* Run-length encoding
* Character occurrence sorting
* Checking string rotation
* Longest common prefix
* Valid palindrome
* Isomorphic strings
* String permutations
* Substring search
* Manual implementation of common string methods
