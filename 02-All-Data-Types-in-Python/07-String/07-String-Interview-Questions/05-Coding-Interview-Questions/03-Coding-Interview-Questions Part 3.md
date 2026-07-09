# Coding-Interview-Questions Part 3

---

# Question 21: String Compression (Run-Length Encoding)

## Problem Statement

Write a Python program to compress a string by replacing consecutive repeated characters with the character followed by its count.

---

## Example

Input

```text
aaabbccccd
```

Output

```text
a3b2c4d1
```

---

## Program

```python
text = "aaabbccccd"

result = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        result += text[i - 1] + str(count)
        count = 1

result += text[-1] + str(count)

print(result)
```

---

## Output

```text
a3b2c4d1
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

This problem is commonly known as **Run-Length Encoding (RLE)**.

---

# Question 22: Check Whether One String is Rotation of Another

## Problem Statement

Write a Python program to determine whether one string is a rotation of another.

---

## Example

```text
String 1 : ABCD

String 2 : CDAB
```

Output

```text
Rotation
```

---

## Program

```python
string1 = "ABCD"
string2 = "CDAB"

if len(string1) == len(string2) and string2 in (string1 + string1):
    print("Rotation")
else:
    print("Not Rotation")
```

---

## Output

```text
Rotation
```

---

## Time Complexity

```text
O(n)
```

---

## Interview Tip

The trick is to concatenate the first string with itself.

---

# Question 23: Find the Longest Common Prefix

## Problem Statement

Find the longest common prefix among multiple strings.

---

## Program

```python
words = ["flower", "flow", "flight"]

prefix = words[0]

for word in words[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]

print(prefix)
```

---

## Output

```text
fl
```

---

## Time Complexity

```text
O(n × m)
```

Where:

* **n** = Number of strings
* **m** = Length of the shortest string

---

# Question 24: Check Whether a String is a Valid Palindrome

## Problem Statement

Ignore spaces, punctuation, and letter case while checking whether a string is a palindrome.

---

## Example

```text
A man, a plan, a canal: Panama
```

Output

```text
Palindrome
```

---

## Program

```python
text = "A man, a plan, a canal: Panama"

cleaned = "".join(character.lower() for character in text if character.isalnum())

if cleaned == cleaned[::-1]:
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

## Time Complexity

```text
O(n)
```

---

# Question 25: Check Whether Two Strings are Isomorphic

## Problem Statement

Two strings are isomorphic if characters from one string can be replaced to obtain the other string while preserving order.

---

## Example

```text
egg

add
```

Output

```text
Isomorphic
```

---

## Program

```python
def is_isomorphic(first, second):
    if len(first) != len(second):
        return False

    mapping = {}
    used = {}

    for left, right in zip(first, second):
        if left in mapping:
            if mapping[left] != right:
                return False
        else:
            if right in used:
                return False
            mapping[left] = right
            used[right] = True

    return True


print(is_isomorphic("egg", "add"))
```

---

## Output

```text
True
```

---

## Time Complexity

```text
O(n)
```

---

# Question 26: Find All Permutations of a String

## Problem Statement

Generate every possible arrangement of the characters in a string.

---

## Program

```python
from itertools import permutations

text = "ABC"

for item in permutations(text):
    print("".join(item))
```

---

## Output

```text
ABC
ACB
BAC
BCA
CAB
CBA
```

---

## Time Complexity

```text
O(n!)
```

---

## Interview Tip

Interviewers often ask you to implement this **without using `itertools`** through recursion and backtracking.

---

# Question 27: Find the First Unique Character

## Problem Statement

Return the index of the first non-repeating character.

---

## Program

```python
text = "leetcode"

frequency = {}

for character in text:
    frequency[character] = frequency.get(character, 0) + 1

for index, character in enumerate(text):
    if frequency[character] == 1:
        print(index)
        break
```

---

## Output

```text
0
```

---

## Time Complexity

```text
O(n)
```

---

# Question 28: Remove Consecutive Duplicate Characters

## Problem Statement

Remove only consecutive duplicate characters.

---

## Example

Input

```text
aaabbbcca
```

Output

```text
abca
```

---

## Program

```python
text = "aaabbbcca"

result = text[0]

for character in text[1:]:
    if character != result[-1]:
        result += character

print(result)
```

---

## Output

```text
abca
```

---

## Time Complexity

```text
O(n)
```

---

# Question 29: Find the Largest Word in a Paragraph

## Problem Statement

Find the word with the maximum length.

---

## Program

```python
paragraph = "Python is an object oriented programming language"

words = paragraph.split()

largest = max(words, key=len)

print(largest)
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

# Question 30: Check Whether Two Strings are Equal Without Using `==`

## Problem Statement

Compare two strings without using the equality operator.

---

## Program

```python
first = "Python"
second = "Python"

if len(first) != len(second):
    print("Not Equal")
else:
    equal = True

    for left, right in zip(first, second):
        if left != right:
            equal = False
            break

    if equal:
        print("Equal")
    else:
        print("Not Equal")
```

---

## Output

```text
Equal
```

---

## Time Complexity

```text
O(n)
```

---

# Summary (Part 3)

In this section, you solved advanced interview problems involving:

* Run-Length Encoding (String Compression)
* String Rotation
* Longest Common Prefix
* Valid Palindrome
* Isomorphic Strings
* String Permutations
* First Unique Character
* Removing Consecutive Duplicates
* Largest Word
* Manual String Comparison

These questions are frequently asked in coding interviews because they evaluate algorithmic thinking, string manipulation skills, and knowledge of Python's built-in capabilities.

The final part will cover expert-level questions such as:

* Longest Palindromic Substring
* Longest Substring Without Repeating Characters
* Manual Implementation of `find()`
* Manual Implementation of `replace()`
* Manual Implementation of `split()`
* KMP Pattern Matching (Introduction)
* Rabin–Karp Algorithm (Introduction)
* Sliding Window Problems
* Dynamic Programming-based String Problems
* Frequently Asked FAANG-Level Interview Questions
