# Set Operations

## Introduction

Python provides various operations that can be performed on sets.

These operations help us to:

- Add elements
- Remove elements
- Search elements
- Perform mathematical set operations
- Traverse elements
- Check membership

Since sets are mutable, elements can be added and removed after creation.

---

# Categories of Set Operations

```text
Set Operations

│

├── Adding Elements

├── Removing Elements

├── Membership Operations

├── Mathematical Set Operations

└── Traversing Elements
```

---

# Adding Elements

## Definition

Adding elements means inserting new values into an existing set.

Python provides the `add()` method to insert a single element into a set.

---

## Syntax

```python
set.add(element)
```

---

## Program

```python
languages = {"Python", "Java"}

languages.add("C++")

print(languages)
```

---

## Output

```text
{'Python', 'Java', 'C++'}
```

---

## Explanation

The `add()` method inserts the specified element into the set.

If the element already exists, it is not added again.

---

# Removing Elements

## Definition

Removing elements means deleting existing values from a set.

Python provides the `remove()` method to delete a specified element.

---

## Syntax

```python
set.remove(element)
```

---

## Program

```python
languages = {"Python", "Java", "C++"}

languages.remove("Java")

print(languages)
```

---

## Output

```text
{'Python', 'C++'}
```

---

## Explanation

The `remove()` method deletes the specified element from the set.

If the element does not exist, Python raises a `KeyError`.

---

# Membership Operations

## Definition

Membership operators are used to check whether an element exists in a set.

Python provides two membership operators:

- `in`
- `not in`

---

## Program

```python
languages = {"Python", "Java", "C++"}

print("Python" in languages)

print("HTML" not in languages)
```

---

## Output

```text
True

True
```
