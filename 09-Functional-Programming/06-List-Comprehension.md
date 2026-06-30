# List Comprehension in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is List Comprehension?
5. Why is List Comprehension Required?
6. Syntax
7. Components of List Comprehension
8. List Comprehension with Conditions
9. Nested List Comprehension
10. List Comprehension vs Traditional Loop
11. Internal Working
12. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand List Comprehension.
- Create lists using concise syntax.
- Use conditions in list comprehensions.
- Use nested list comprehensions.
- Compare list comprehensions with traditional loops.
- Apply list comprehensions in real-world programs.

---

# Prerequisites

Before learning this chapter, you should know:

- Lists
- Loops
- Conditional Statements
- Functions

---

# Introduction

In Python,

creating a list using loops is a common task.

Example:

```python
numbers = []

for i in range(1, 6):

    numbers.append(i)
```

Python provides a much shorter and cleaner way to achieve the same result using **List Comprehension**.

List comprehensions improve readability and reduce the amount of code required to create lists.

---

# What is List Comprehension?

## Definition

A **List Comprehension** is a concise way to create a new list by iterating over an iterable and optionally applying a condition.

---

## Simple Definition

> List Comprehension is a one-line method for creating lists.

---

# Why is List Comprehension Required?

Without list comprehension,

creating a new list requires multiple lines of code.

With list comprehension,

the same task can often be completed in a single line.

Benefits include:

- Less code
- Better readability
- Faster execution for many simple use cases
- Easy data transformation

---

# Syntax

```python
[expression for item in iterable]
```

---

# Syntax with Condition

```python
[expression for item in iterable if condition]
```

---

# Components of List Comprehension

A list comprehension consists of three parts:

### Expression

Produces the value to be stored.

### Item

Represents each element of the iterable.

### Iterable

The collection being traversed.

---

# Example

```python
numbers = [x * x for x in range(1, 6)]

print(numbers)
```

Output

```text
[1, 4, 9, 16, 25]
```

---

# List Comprehension with Conditions

Example

```python
even = [x for x in range(1,11) if x % 2 == 0]

print(even)
```

Output

```text
[2, 4, 6, 8, 10]
```

---

# Nested List Comprehension

List comprehensions can also be nested.

Example

```python
matrix = [

    [i * j for j in range(1,4)]

    for i in range(1,4)

]

print(matrix)
```

Output

```text
[[1,2,3],[2,4,6],[3,6,9]]
```

---

# List Comprehension vs Traditional Loop

| Traditional Loop | List Comprehension |
|------------------|-------------------|
| More lines of code | One-line syntax |
| Uses append() | Creates list directly |
| More verbose | More concise |
| Easier for beginners | Better for simple transformations |

---

# Internal Working

```text
Iterable

↓

Read Element

↓

Apply Expression

↓

Check Condition (Optional)

↓

Add to New List

↓

Repeat

↓

Return Final List
```

---

# Advantages

- Less code.
- Better readability.
- Cleaner syntax.
- Faster for many simple operations.
- Easy list creation.

---

# Limitations

- Not suitable for complex business logic.
- Deep nesting reduces readability.
- Difficult to debug if overly complex.

---

# Best Practices

- Keep comprehensions simple.
- Use meaningful variable names.
- Avoid excessive nesting.
- Use normal loops for complex logic.
- Add conditions only when necessary.

---

# Common Mistakes

## Mistake 1

Writing very long list comprehensions.

---

## Mistake 2

Using nested comprehensions unnecessarily.

---

## Mistake 3

Ignoring readability.

---

## Mistake 4

Using list comprehensions when a normal loop is easier to understand.

---

# Program 1 – Create a List

```python
numbers = [x for x in range(1,6)]

print(numbers)
```

---

## Output

```text
[1, 2, 3, 4, 5]
```

---

# Program 2 – Square Numbers

```python
numbers = [x*x for x in range(1,6)]

print(numbers)
```

---

## Output

```text
[1, 4, 9, 16, 25]
```

---

# Program 3 – Cube Numbers

```python
numbers = [x**3 for x in range(1,6)]

print(numbers)
```

---

## Output

```text
[1, 8, 27, 64, 125]
```

---

# Program 4 – Even Numbers

```python
even = [x for x in range(1,11) if x%2==0]

print(even)
```

---

## Output

```text
[2, 4, 6, 8, 10]
```

---

# Program 5 – Odd Numbers

```python
odd = [x for x in range(1,11) if x%2!=0]

print(odd)
```

---

## Output

```text
[1, 3, 5, 7, 9]
```

---

# Program 6 – Convert to Uppercase

```python
names = ["python","java","sql"]

result = [name.upper() for name in names]

print(result)
```

---

## Output

```text
['PYTHON', 'JAVA', 'SQL']
```

---

# Program 7 – String Length

```python
names = ["Python","Java","Oracle"]

result = [len(name) for name in names]

print(result)
```

---

## Output

```text
[6, 4, 6]
```

---

# Program 8 – Positive Numbers

```python
numbers = [-5,-2,0,4,7]

result = [x for x in numbers if x>0]

print(result)
```

---

## Output

```text
[4, 7]
```

---

# Program 9 – First Letter of Each Word

```python
words = ["Python","Java","SQL"]

result = [word[0] for word in words]

print(result)
```

---

## Output

```text
['P', 'J', 'S']
```

---

# Program 10 – Nested List Comprehension

```python
matrix = [

    [i*j for j in range(1,4)]

    for i in range(1,4)

]

print(matrix)
```

---

## Output

```text
[[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

---

# Dry Run

```text
Iterable

↓

Read Element

↓

Apply Expression

↓

Condition Checked

↓

True?

↓

Add to List

↓

Repeat

↓

Final List
```

---

# Memory Representation

```text
Original List

│

├──1

├──2

├──3

├──4

└──5

↓

List Comprehension

↓

Expression Applied

↓

New List

│

├──1

├──4

├──9

├──16

└──25
```

---

# Advantages

- Short syntax.
- Better readability.
- Efficient list creation.
- Supports conditions.
- Supports nested structures.

---

# Best Practices

- Keep expressions simple.
- Avoid deeply nested comprehensions.
- Use descriptive variable names.
- Prefer loops when readability decreases.

---

# Common Mistakes

- Overcomplicating list comprehensions.
- Ignoring readability.
- Using nested comprehensions excessively.
- Forgetting conditions.

---

# Interview Questions

## 1. What is List Comprehension?

### Answer

List Comprehension is a concise way to create lists using a single line of code.

---

## 2. What is the syntax of List Comprehension?

### Answer

```python
[expression for item in iterable]
```

---

## 3. Can conditions be used in List Comprehension?

### Answer

Yes.

Example:

```python
[x for x in range(10) if x % 2 == 0]
```

---

## 4. Can List Comprehension replace loops?

### Answer

Yes.

For simple list creation and transformations, list comprehensions often provide a shorter alternative to loops.

---

## 5. Can List Comprehension be nested?

### Answer

Yes.

Nested list comprehensions are supported, but they should be used carefully to maintain readability.

---

## 6. Is List Comprehension faster than a loop?

### Answer

For many simple list-building operations, list comprehensions can be more concise and may perform well, but clarity should be prioritized.

---

## 7. What are the advantages of List Comprehension?

### Answer

- Less code
- Better readability
- Efficient list creation
- Easy transformations

---

# Practice Programs

1. Create a list of squares.
2. Create a list of cubes.
3. Create a list of even numbers.
4. Convert names to uppercase.
5. Create a multiplication table using nested list comprehension.

---

# Quick Revision

- List Comprehension → One-line list creation.
- Syntax → `[expression for item in iterable]`
- Supports conditions.
- Supports nesting.
- Cleaner than many traditional loops.

---

# Chapter Summary

In this chapter, we learned:

- List Comprehension
- Syntax
- Components
- Conditional List Comprehension
- Nested List Comprehension
- Practical Programs
- Advantages
- Limitations
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
