# Tuple Indexing

## Introduction

Indexing is used to access individual elements from a tuple.

Each element in a tuple is assigned an index number.

Python supports two types of indexing:

- Positive Indexing
- Negative Indexing

---

# Positive Indexing

## Definition

Positive indexing starts from the beginning of the tuple.

The first element has an index value of **0**.

---

## Example

```python
languages = ("Python", "Java", "C++", "JavaScript")
```

```text
Element :   Python     Java      C++     JavaScript

Index   :      0         1         2           3
```

---

## Program

```python
languages = ("Python", "Java", "C++", "JavaScript")

print(languages[0])

print(languages[1])

print(languages[2])

print(languages[3])
```

---

## Output

```text
Python

Java

C++

JavaScript
```

---

## Explanation

- `languages[0]` returns the first element.
- `languages[1]` returns the second element.
- `languages[2]` returns the third element.
- `languages[3]` returns the fourth element.

---

# Negative Indexing

## Definition

Negative indexing starts from the end of the tuple.

The last element has an index value of **-1**.

---

## Example

```python
languages = ("Python", "Java", "C++", "JavaScript")
```

```text
Element :   Python     Java      C++     JavaScript

Index   :     -4        -3        -2          -1
```

---

## Program

```python
languages = ("Python", "Java", "C++", "JavaScript")

print(languages[-1])

print(languages[-2])

print(languages[-3])

print(languages[-4])
```

---

## Output

```text
JavaScript

C++

Java

Python
```

---

## Explanation

- `languages[-1]` returns the last element.
- `languages[-2]` returns the second last element.
- `languages[-3]` returns the third last element.
- `languages[-4]` returns the fourth last element.
