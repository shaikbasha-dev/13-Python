# map() Function in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is map()?
5. Why is map() Required?
6. Syntax
7. Parameters
8. Return Value
9. Internal Working
10. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the purpose of the map() function.
- Apply a function to iterable objects.
- Use map() with normal functions.
- Use map() with lambda functions.
- Process multiple iterables using map().
- Convert map objects into lists, tuples, and sets.

---

# Prerequisites

Before learning this chapter, you should know:

- Functions
- Lambda Functions
- Lists
- Tuples
- Loops

---

# Introduction

In Python,

it is common to perform the same operation on every element of a collection.

For example,

- Add 10 to every number.
- Convert every string to uppercase.
- Calculate the square of every number.

Using loops,

the code becomes longer.

Python provides the

```python
map()
```

function to perform these operations efficiently.

---

# What is map()?

## Definition

The `map()` function applies a specified function to every item of an iterable and returns a map object.

---

## Simple Definition

> `map()` applies one function to every element in an iterable.

---

# Why is map() Required?

Suppose we have

```text
[1,2,3,4,5]
```

and we want

```text
[1,4,9,16,25]
```

Instead of writing a loop,

`map()` performs the transformation automatically.

---

# Syntax

```python
map(function, iterable)
```

---

## Multiple Iterables

```python
map(function, iterable1, iterable2)
```

---

# Parameters

## function

The function applied to every element.

It can be:

- Normal function
- Lambda function
- Built-in function

---

## iterable

Any iterable object.

Examples:

- List
- Tuple
- Set
- Dictionary
- String

---

# Return Value

The `map()` function returns a

```python
map object
```

which can be converted into

- list
- tuple
- set

---

# Internal Working

```text
Iterable

↓

map()

↓

Function Applied

↓

Each Element Processed

↓

Map Object Created

↓

Convert to List/Tuple/Set

↓

Output
```

---

# Advantages

- Less code.
- Faster than manual loops for many use cases.
- Easy to combine with lambda.
- Improves readability.
- Supports multiple iterables.

---

# Best Practices

- Use lambda for simple transformations.
- Use normal functions for complex logic.
- Convert the map object into a list or tuple when required.
- Use meaningful function names.
- Avoid unnecessary nested map() calls.

---

# Common Mistakes

## Mistake 1

Printing a map object directly.

```python
result = map(lambda x: x*x,[1,2,3])

print(result)
```

Output

```text
<map object at ...>
```

Always convert it.

```python
print(list(result))
```

---

## Mistake 2

Passing a function call instead of the function itself.

Incorrect

```python
map(square(), numbers)
```

Correct

```python
map(square, numbers)
```

---

## Mistake 3

Providing iterables of different lengths.

The iteration stops when the shortest iterable is exhausted.

---

# Program 1 – Square of Numbers

```python
numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * x, numbers)

print(list(result))
```

---

## Output

```text
[1, 4, 9, 16, 25]
```

---

# Program 2 – Cube of Numbers

```python
numbers = [1, 2, 3, 4]

result = map(lambda x: x ** 3, numbers)

print(list(result))
```

---

## Output

```text
[1, 8, 27, 64]
```

---

# Program 3 – Convert to Uppercase

```python
names = ["python", "java", "sql"]

result = map(str.upper, names)

print(list(result))
```

---

## Output

```text
['PYTHON', 'JAVA', 'SQL']
```

---

# Program 4 – Add Two Lists

```python
list1 = [10, 20, 30]

list2 = [1, 2, 3]

result = map(lambda x, y: x + y, list1, list2)

print(list(result))
```

---

## Output

```text
[11, 22, 33]
```

---

# Program 5 – Multiply Two Lists

```python
a = [2, 3, 4]

b = [5, 6, 7]

result = map(lambda x, y: x * y, a, b)

print(list(result))
```

---

## Output

```text
[10, 18, 28]
```

---

# Program 6 – Calculate String Length

```python
words = ["Apple", "Banana", "Orange"]

result = map(len, words)

print(list(result))
```

---

## Output

```text
[5, 6, 6]
```

---

# Program 7 – Convert Integers to Strings

```python
numbers = [10, 20, 30]

result = map(str, numbers)

print(list(result))
```

---

## Output

```text
['10', '20', '30']
```

---

# Program 8 – Using Normal Function

```python
def square(number):

    return number * number

numbers = [5, 6, 7]

result = map(square, numbers)

print(list(result))
```

---

## Output

```text
[25, 36, 49]
```

---

# Program 9 – Convert to Float

```python
numbers = [10, 20, 30]

result = map(float, numbers)

print(list(result))
```

---

## Output

```text
[10.0, 20.0, 30.0]
```

---

# Program 10 – Remove Extra Spaces

```python
names = ["  Python ", " Java ", " SQL "]

result = map(str.strip, names)

print(list(result))
```

---

## Output

```text
['Python', 'Java', 'SQL']
```

---

# Dry Run

```text
List

↓

map()

↓

Function Applied

↓

Each Element Processed

↓

Map Object

↓

list()

↓

Output Displayed
```

---

# Memory Representation

```text
numbers

│

├── 1

├── 2

├── 3

├── 4

└── 5

↓

map()

↓

Lambda Function

↓

Map Object

↓

List
```

---

# Interview Questions

## 1. What is map()?

### Answer

`map()` applies a function to every element of an iterable.

---

## 2. What does map() return?

### Answer

A map object.

---

## 3. Can map() work with lambda functions?

### Answer

Yes.

Lambda functions are commonly used with `map()`.

---

## 4. Can map() process multiple iterables?

### Answer

Yes.

Example

```python
map(lambda x, y: x + y, list1, list2)
```

---

## 5. Which iterable types are supported?

### Answer

- List
- Tuple
- Set
- Dictionary
- String

---

## 6. Why convert the result to a list?

### Answer

Because `map()` returns a map object, not a list.

---

## 7. Is map() faster than writing loops?

### Answer

For many transformation tasks, `map()` provides a concise and efficient approach. Performance depends on the specific use case and readability should also be considered.

---

## 8. Can built-in functions be passed to map()?

### Answer

Yes.

Examples:

- `len`
- `str`
- `float`
- `int`

---

## Practice Programs

1. Find squares using map().
2. Find cubes using map().
3. Convert names to uppercase.
4. Add two lists using map().
5. Convert integers into strings.

---

# Quick Revision

- `map()` → Applies a function to each element.
- Returns a map object.
- Convert using `list()`.
- Supports multiple iterables.
- Works with lambda and normal functions.

---

# Chapter Summary

In this chapter, we learned:

- map() Function
- Syntax
- Parameters
- Return Value
- Lambda with map()
- Multiple Iterables
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
