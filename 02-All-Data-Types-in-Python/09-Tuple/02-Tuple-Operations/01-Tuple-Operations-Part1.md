# Tuple Operations

## Introduction

Python provides various operations that can be performed on tuples.

These operations help us to:

- Access elements
- Traverse elements
- Search elements
- Combine tuples
- Repeat tuples
- Find the length
- Check membership

Since tuples are immutable, elements cannot be added, updated, or removed after creation.

---

# Categories of Tuple Operations

```text
Tuple Operations

│

├── Accessing Elements

├── Traversing Elements

├── Membership Operations

├── Concatenation

├── Repetition

└── Length Operation
```

---

# Accessing Elements

## Definition

Accessing elements means retrieving one or more values from a tuple using their index position.

---

## Syntax

```python
tuple_name[index]
```

---

## Program

```python
languages = ("Python", "Java", "C++", "JavaScript")

print(languages[0])

print(languages[2])
```

---

## Output

```text
Python

C++
```

---

## Explanation

- `languages[0]` returns the first element.
- `languages[2]` returns the third element.

---

# Traversing Elements

## Definition

Traversing means visiting each element of a tuple one by one.

Traversal is commonly performed using loops.

---

## Program

```python
languages = ("Python", "Java", "C++")

for language in languages:
    print(language)
```

---

## Output

```text
Python

Java

C++
```

---

## Explanation

The `for` loop visits each element of the tuple and displays it.

---

# Membership Operations

## Definition

Membership operators are used to check whether an element exists in a tuple.

Python provides two membership operators:

- `in`
- `not in`

---

## Program

```python
languages = ("Python", "Java", "C++")

print("Python" in languages)

print("HTML" not in languages)
```

---

## Output

```text
True

True
```
