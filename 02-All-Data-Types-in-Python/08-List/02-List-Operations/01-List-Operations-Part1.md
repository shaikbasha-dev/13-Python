# List Operations

## Introduction

Python provides various operations that can be performed on lists.

These operations help us to:

- Access elements
- Update elements
- Add elements
- Remove elements
- Traverse elements
- Search elements
- Combine lists
- Repeat lists

Using these operations, we can efficiently manipulate list data.

---

# Categories of List Operations

```text
List Operations

│

├── Accessing Elements

├── Updating Elements

├── Adding Elements

├── Removing Elements

├── Traversing Elements

├── Membership Operations

├── Concatenation

└── Repetition
```

---

# Accessing Elements

## Definition

Accessing elements means retrieving one or more values from a list using their index position.

---

## Syntax

```python
list_name[index]
```

---

## Program

```python
languages = ["Python", "Java", "C++", "JavaScript"]

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

# Updating Elements

## Definition

Updating means changing the value of an existing element in a list.

---

## Syntax

```python
list_name[index] = new_value
```

---

## Program

```python
languages = ["Python", "Java", "C++"]

languages[1] = "JavaScript"

print(languages)
```

---

## Output

```text
['Python', 'JavaScript', 'C++']
```

---

## Explanation

The element at index `1` is replaced with `"JavaScript"`.

---

# Adding Elements

## Definition

New elements can be added to a list using built-in list methods.

Common methods include:

- append()
- extend()
- insert()

Detailed explanation of these methods is covered in the **List Methods** section.
