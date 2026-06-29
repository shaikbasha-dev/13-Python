# String Interview Questions and Answers

## Introduction

This chapter contains the most frequently asked interview questions on Python Strings.

It covers:

- String Basics
- String Creation
- String Indexing
- String Slicing
- String Methods
- split() Method
- Output-Based Questions
- Frequently Asked Programs
- Viva Questions

---

# Basic Interview Questions

## Q1. What is a String in Python?

### Answer

A String is a sequence of Unicode characters enclosed within single quotes (' '), double quotes (" "), triple single quotes (''' '''), or triple double quotes (""" """).

Example

```python
name = "Python"
```

---

## Q2. Which data type is used to store strings?

### Answer

The **str** data type.

Example

```python
text = "Hello"

print(type(text))
```

Output

```text
<class 'str'>
```

---

## Q3. Are Strings mutable or immutable?

### Answer

Strings are **immutable**.

Once a string is created, its contents cannot be changed.

---

## Q4. How many ways can a String be created?

### Answer

Python provides four ways.

- Single Quotes
- Double Quotes
- Triple Single Quotes
- Triple Double Quotes

---

## Q5. What is String Concatenation?

### Answer

Joining two or more strings using the **+** operator is called String Concatenation.

Example

```python
first = "Python"

second = "Programming"

print(first + " " + second)
```

Output

```text
Python Programming
```

---

## Q6. What is String Repetition?

### Answer

Repeating a string using the **\*** operator is called String Repetition.

Example

```python
print("Hi " * 3)
```

Output

```text
Hi Hi Hi
```

---

# String Indexing Interview Questions

## Q7. What is String Indexing?

### Answer

String Indexing is the process of accessing individual characters using index positions.

---

## Q8. What is Positive Indexing?

### Answer

Positive indexing starts from **0** and moves from left to right.

Example

```python
text = "Python"

print(text[0])
```

Output

```text
P
```

---

## Q9. What is Negative Indexing?

### Answer

Negative indexing starts from **-1** and moves from right to left.

Example

```python
text = "Python"

print(text[-1])
```

Output

```text
n
```

---

## Q10. What happens if an invalid index is used?

### Answer

Python raises

```text
IndexError: string index out of range
```

---

# String Slicing Interview Questions

## Q11. What is String Slicing?

### Answer

String Slicing extracts a portion of a string.

Syntax

```python
string[start:stop:step]
```

---

## Q12. Is the stop index included?

### Answer

No.

The stop index is excluded.

---

## Q13. How do you reverse a string?

### Answer

```python
text = "Python"

print(text[::-1])
```

Output

```text
nohtyP
```

---

## Q14. How do you copy a string?

### Answer

```python
copy = text[:]
```

---

## Q15. Can slicing use negative indexes?

### Answer

Yes.

Example

```python
text[-5:-1]
```

---

# String Methods Interview Questions

## Q16. What are String Methods?

### Answer

String methods are built-in functions used to perform operations on strings.

---

## Q17. Does upper() modify the original string?

### Answer

No.

Strings are immutable.

Example

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

## Q18. Difference between upper() and lower()?

### Answer

- upper() → Converts to uppercase.
- lower() → Converts to lowercase.

---

## Q19. What is replace()?

### Answer

The replace() method replaces one substring with another.

Example

```python
text = "Java"

print(text.replace("Java", "Python"))
```

Output

```text
Python
```

---

## Q20. What is find()?

### Answer

The find() method returns the index of the first occurrence of a substring.

If not found, it returns **-1**.

---

## Q21. What is count()?

### Answer

Returns the number of occurrences of a substring.

Example

```python
print("banana".count("a"))
```

Output

```text
3
```

---

## Q22. What is strip()?

### Answer

The strip() method removes spaces from both sides of a string.

---

## Q23. Difference between strip(), lstrip(), and rstrip()?

### Answer

- strip() → Removes spaces from both sides.
- lstrip() → Removes spaces from the left side.
- rstrip() → Removes spaces from the right side.

---

# split() Interview Questions

## Q24. What is split()?

### Answer

The split() method converts a string into a list.

---

## Q25. What is the default separator of split()?

### Answer

Whitespace (space).

---

## Q26. What is maxsplit?

### Answer

It specifies the maximum number of splits.

---

## Q27. What is the return type of split()?

### Answer

List

---

## Q28. Difference between split() and join()?

### Answer

| split() | join() |
|----------|---------|
| String → List | List → String |

---

# Output-Based Questions

## Q29. Predict the Output

```python
print("Python"[2])
```

Output

```text
t
```

---

## Q30. Predict the Output

```python
print("Python"[-2])
```

Output

```text
o
```

---

## Q31. Predict the Output

```python
print("Python"[1:5])
```

Output

```text
ytho
```

---

## Q32. Predict the Output

```python
print("Python"[::-1])
```

Output

```text
nohtyP
```

---

## Q33. Predict the Output

```python
print("Python".upper())
```

Output

```text
PYTHON
```

---

## Q34. Predict the Output

```python
print("PYTHON".lower())
```

Output

```text
python
```

---

## Q35. Predict the Output

```python
print("banana".count("a"))
```

Output

```text
3
```

---

## Q36. Predict the Output

```python
print("Python Programming".find("Program"))
```

Output

```text
7
```

---

## Q37. Predict the Output

```python
print("A,B,C".split(","))
```

Output

```text
['A', 'B', 'C']
```

---

## Q38. Predict the Output

```python
print("Python".replace("Python","Java"))
```

Output

```text
Java
```

---

# Frequently Asked Interview Programs

## Program 1

Print every character of a string using a **for** loop.

```python
text = "Python"

for character in text:
    print(character)
```

---

## Program 2

Reverse a string.

```python
text = "Python"

print(text[::-1])
```

---

## Program 3

Count the number of words.

```python
sentence = "Python Programming Language"

words = sentence.split()

print(len(words))
```

---

## Program 4

Convert a string into uppercase.

```python
text = "python"

print(text.upper())
```

---

## Program 5

Replace one word with another.

```python
text = "I Love Java"

print(text.replace("Java", "Python"))
```

---

# Viva Questions

- What is a String?
- Is String mutable?
- What is String Indexing?
- What is Positive Indexing?
- What is Negative Indexing?
- What is String Slicing?
- Explain the syntax of slicing.
- What is String Concatenation?
- What is String Repetition?
- What is split()?
- What is join()?
- What is upper()?
- What is lower()?
- What is replace()?
- What is strip()?
- What is find()?
- What is count()?
- Difference between split() and join().
- Difference between Indexing and Slicing.
- Difference between Positive and Negative Indexing.

---

# Quick Revision

- String → Sequence of Unicode characters.
- Strings are immutable.
- Indexing returns one character.
- Slicing returns multiple characters.
- Positive indexing starts with **0**.
- Negative indexing starts with **-1**.
- `upper()` converts to uppercase.
- `lower()` converts to lowercase.
- `replace()` replaces text.
- `find()` returns the index.
- `count()` counts occurrences.
- `split()` converts String → List.
- `join()` converts List → String.
- `[::-1]` reverses a string.

---

# Summary

In this interview guide, you learned:

- String Basics
- String Indexing
- String Slicing
- String Methods
- split() Method
- Output-Based Questions
- Frequently Asked Programs
- Viva Questions
- Quick Revision
# String Interview Questions and Answers

## Introduction

This chapter contains the most frequently asked interview questions on Python Strings.

It covers:

- String Basics
- String Creation
- String Indexing
- String Slicing
- String Methods
- split() Method
- Output-Based Questions
- Frequently Asked Programs
- Viva Questions

---

# Basic Interview Questions

## Q1. What is a String in Python?

### Answer

A String is a sequence of Unicode characters enclosed within single quotes (' '), double quotes (" "), triple single quotes (''' '''), or triple double quotes (""" """).

Example

```python
name = "Python"
```

---

## Q2. Which data type is used to store strings?

### Answer

The **str** data type.

Example

```python
text = "Hello"

print(type(text))
```

Output

```text
<class 'str'>
```

---

## Q3. Are Strings mutable or immutable?

### Answer

Strings are **immutable**.

Once a string is created, its contents cannot be changed.

---

## Q4. How many ways can a String be created?

### Answer

Python provides four ways.

- Single Quotes
- Double Quotes
- Triple Single Quotes
- Triple Double Quotes

---

## Q5. What is String Concatenation?

### Answer

Joining two or more strings using the **+** operator is called String Concatenation.

Example

```python
first = "Python"

second = "Programming"

print(first + " " + second)
```

Output

```text
Python Programming
```

---

## Q6. What is String Repetition?

### Answer

Repeating a string using the **\*** operator is called String Repetition.

Example

```python
print("Hi " * 3)
```

Output

```text
Hi Hi Hi
```

---

# String Indexing Interview Questions

## Q7. What is String Indexing?

### Answer

String Indexing is the process of accessing individual characters using index positions.

---

## Q8. What is Positive Indexing?

### Answer

Positive indexing starts from **0** and moves from left to right.

Example

```python
text = "Python"

print(text[0])
```

Output

```text
P
```

---

## Q9. What is Negative Indexing?

### Answer

Negative indexing starts from **-1** and moves from right to left.

Example

```python
text = "Python"

print(text[-1])
```

Output

```text
n
```

---

## Q10. What happens if an invalid index is used?

### Answer

Python raises

```text
IndexError: string index out of range
```

---

# String Slicing Interview Questions

## Q11. What is String Slicing?

### Answer

String Slicing extracts a portion of a string.

Syntax

```python
string[start:stop:step]
```

---

## Q12. Is the stop index included?

### Answer

No.

The stop index is excluded.

---

## Q13. How do you reverse a string?

### Answer

```python
text = "Python"

print(text[::-1])
```

Output

```text
nohtyP
```

---

## Q14. How do you copy a string?

### Answer

```python
copy = text[:]
```

---

## Q15. Can slicing use negative indexes?

### Answer

Yes.

Example

```python
text[-5:-1]
```

---

# String Methods Interview Questions

## Q16. What are String Methods?

### Answer

String methods are built-in functions used to perform operations on strings.

---

## Q17. Does upper() modify the original string?

### Answer

No.

Strings are immutable.

Example

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

## Q18. Difference between upper() and lower()?

### Answer

- upper() → Converts to uppercase.
- lower() → Converts to lowercase.

---

## Q19. What is replace()?

### Answer

The replace() method replaces one substring with another.

Example

```python
text = "Java"

print(text.replace("Java", "Python"))
```

Output

```text
Python
```

---

## Q20. What is find()?

### Answer

The find() method returns the index of the first occurrence of a substring.

If not found, it returns **-1**.

---

## Q21. What is count()?

### Answer

Returns the number of occurrences of a substring.

Example

```python
print("banana".count("a"))
```

Output

```text
3
```

---

## Q22. What is strip()?

### Answer

The strip() method removes spaces from both sides of a string.

---

## Q23. Difference between strip(), lstrip(), and rstrip()?

### Answer

- strip() → Removes spaces from both sides.
- lstrip() → Removes spaces from the left side.
- rstrip() → Removes spaces from the right side.

---

# split() Interview Questions

## Q24. What is split()?

### Answer

The split() method converts a string into a list.

---

## Q25. What is the default separator of split()?

### Answer

Whitespace (space).

---

## Q26. What is maxsplit?

### Answer

It specifies the maximum number of splits.

---

## Q27. What is the return type of split()?

### Answer

List

---

## Q28. Difference between split() and join()?

### Answer

| split() | join() |
|----------|---------|
| String → List | List → String |

---

# Output-Based Questions

## Q29. Predict the Output

```python
print("Python"[2])
```

Output

```text
t
```

---

## Q30. Predict the Output

```python
print("Python"[-2])
```

Output

```text
o
```

---

## Q31. Predict the Output

```python
print("Python"[1:5])
```

Output

```text
ytho
```

---

## Q32. Predict the Output

```python
print("Python"[::-1])
```

Output

```text
nohtyP
```

---

## Q33. Predict the Output

```python
print("Python".upper())
```

Output

```text
PYTHON
```

---

## Q34. Predict the Output

```python
print("PYTHON".lower())
```

Output

```text
python
```

---

## Q35. Predict the Output

```python
print("banana".count("a"))
```

Output

```text
3
```

---

## Q36. Predict the Output

```python
print("Python Programming".find("Program"))
```

Output

```text
7
```

---

## Q37. Predict the Output

```python
print("A,B,C".split(","))
```

Output

```text
['A', 'B', 'C']
```

---

## Q38. Predict the Output

```python
print("Python".replace("Python","Java"))
```

Output

```text
Java
```

---

# Frequently Asked Interview Programs

## Program 1

Print every character of a string using a **for** loop.

```python
text = "Python"

for character in text:
    print(character)
```

---

## Program 2

Reverse a string.

```python
text = "Python"

print(text[::-1])
```

---

## Program 3

Count the number of words.

```python
sentence = "Python Programming Language"

words = sentence.split()

print(len(words))
```

---

## Program 4

Convert a string into uppercase.

```python
text = "python"

print(text.upper())
```

---

## Program 5

Replace one word with another.

```python
text = "I Love Java"

print(text.replace("Java", "Python"))
```

---

# Viva Questions

- What is a String?
- Is String mutable?
- What is String Indexing?
- What is Positive Indexing?
- What is Negative Indexing?
- What is String Slicing?
- Explain the syntax of slicing.
- What is String Concatenation?
- What is String Repetition?
- What is split()?
- What is join()?
- What is upper()?
- What is lower()?
- What is replace()?
- What is strip()?
- What is find()?
- What is count()?
- Difference between split() and join().
- Difference between Indexing and Slicing.
- Difference between Positive and Negative Indexing.

---

# Quick Revision

- String → Sequence of Unicode characters.
- Strings are immutable.
- Indexing returns one character.
- Slicing returns multiple characters.
- Positive indexing starts with **0**.
- Negative indexing starts with **-1**.
- `upper()` converts to uppercase.
- `lower()` converts to lowercase.
- `replace()` replaces text.
- `find()` returns the index.
- `count()` counts occurrences.
- `split()` converts String → List.
- `join()` converts List → String.
- `[::-1]` reverses a string.

---

# Summary

In this interview guide, you learned:

- String Basics
- String Indexing
- String Slicing
- String Methods
- split() Method
- Output-Based Questions
- Frequently Asked Programs
- Viva Questions
- Quick Revision

This document serves as a complete interview preparation guide for the **03-Strings** folder and is suitable for freshers preparing for technical interviews, campus placements, coding assessments, and Python viva examinations.
