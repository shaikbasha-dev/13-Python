# List Slicing

## Introduction

List slicing is used to extract one or more elements from a list.

Instead of accessing a single element, slicing returns a new list containing the required elements.

Python provides a simple and flexible slicing syntax.

---

# Definition

**List Slicing** is the process of extracting a portion of a list using the slicing operator (`:`).

---

# Syntax

```python
list_name[start : stop]
```

- **start** → Starting index (included)
- **stop** → Ending index (excluded)

---

## Example

```python
languages = ["Python", "Java", "C++", "JavaScript", "Go"]
```

---

# Program

```python
languages = ["Python", "Java", "C++", "JavaScript", "Go"]

print(languages[1:4])
```

---

# Output

```text
['Java', 'C++', 'JavaScript']
```

---

# Explanation

The slicing operation starts from index `1` and ends before index `4`.

Elements returned are:

- Java
- C++
- JavaScript

---

# Omitting Start Index

If the **start index** is omitted, Python starts slicing from the beginning of the list.

---

## Program

```python
languages = ["Python", "Java", "C++", "JavaScript", "Go"]

print(languages[:3])
```

---

## Output

```text
['Python', 'Java', 'C++']
```

---

## Explanation

Since the starting index is omitted, Python starts from index `0`.

The slicing operation stops before index `3`.

---

# Omitting Stop Index

If the **stop index** is omitted, Python extracts elements until the end of the list.

---

## Program

```python
languages = ["Python", "Java", "C++", "JavaScript", "Go"]

print(languages[2:])
```

---

## Output

```text
['C++', 'JavaScript', 'Go']
```

---

## Explanation

The slicing operation starts from index `2` and continues until the last element.
