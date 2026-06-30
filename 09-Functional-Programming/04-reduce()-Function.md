# reduce() Function in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is reduce()?
5. Why is reduce() Required?
6. Syntax
7. Parameters
8. Return Value
9. reduce() vs map() vs filter()
10. Internal Working
11. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the reduce() function.
- Use reduce() with lambda functions.
- Use reduce() with normal functions.
- Perform cumulative calculations.
- Apply reduce() to real-world problems.
- Differentiate map(), filter(), and reduce().

---

# Prerequisites

Before learning this chapter, you should know:

- Functions
- Lambda Functions
- map()
- filter()
- Lists
- Operators

---

# Introduction

Sometimes we need a single result from an entire collection.

Examples include:

- Sum of all numbers.
- Product of all numbers.
- Largest value.
- Smallest value.
- Concatenating strings.

Instead of writing loops,

Python provides the

```python
reduce()
```

function.

Unlike

```python
map()
```

and

```python
filter()
```

the

```python
reduce()
```

function returns **only one final value**.

---

# What is reduce()?

## Definition

The `reduce()` function repeatedly applies a function to the elements of an iterable until a single cumulative result is produced.

---

## Simple Definition

> `reduce()` combines all elements of an iterable into a single value.

---

# Why is reduce() Required?

Suppose we have

```text
[10,20,30,40]
```

If we need

```text
100
```

instead of writing a loop,

we can simply use

```python
reduce()
```

---

# Import Statement

The reduce() function belongs to

```python
functools
```

module.

```python
from functools import reduce
```

---

# Syntax

```python
reduce(function, iterable)
```

---

# Syntax with Initial Value

```python
reduce(function, iterable, initial_value)
```

---

# Parameters

## function

A function that accepts **two arguments** and returns one value.

The returned value becomes the first argument for the next iteration.

---

## iterable

Any iterable object.

Examples

- List
- Tuple
- Set

---

## initial_value (Optional)

An initial value supplied before processing the iterable.

---

# Return Value

Returns

```text
A single cumulative value
```

---

# How reduce() Works

Example

```python
numbers = [10,20,30,40]
```

Execution

```text
10 + 20 = 30

30 + 30 = 60

60 + 40 = 100
```

Final Result

```text
100
```

---

# reduce() vs map() vs filter()

| map() | filter() | reduce() |
|--------|-----------|-----------|
| Transforms values | Filters values | Combines values |
| Returns iterable | Returns iterable | Returns one value |
| Same number of elements | Fewer or equal elements | Single result |

---

# Internal Working

```text
Iterable

↓

First Two Elements

↓

Function Applied

↓

Result

↓

Next Element

↓

Function Applied

↓

Final Value

↓

Output
```

---

# Advantages

- Less code.
- Easy cumulative calculations.
- Works well with lambda.
- Improves readability.
- Useful in functional programming.

---

# Best Practices

- Use lambda for simple operations.
- Use normal functions for complex logic.
- Import reduce from functools.
- Use reduce only when a single cumulative value is required.
- Avoid overly complex lambda expressions.

---

# Common Mistakes

## Mistake 1

Using reduce() without importing it.

Incorrect

```python
reduce(...)
```

Correct

```python
from functools import reduce
```

---

## Mistake 2

Passing a function with only one parameter.

The function must accept **two parameters**.

---

## Mistake 3

Using reduce() when map() or filter() is more appropriate.

Remember:

- map() → Transform
- filter() → Select
- reduce() → Combine

---

# Program 1 – Sum of Numbers

```python
from functools import reduce

numbers = [10,20,30,40]

result = reduce(lambda x,y:x+y,numbers)

print(result)
```

---

## Output

```text
100
```

---

# Program 2 – Product of Numbers

```python
from functools import reduce

numbers=[2,3,4,5]

result=reduce(lambda x,y:x*y,numbers)

print(result)
```

---

## Output

```text
120
```

---

# Program 3 – Largest Number

```python
from functools import reduce

numbers=[12,45,8,67,25]

result=reduce(lambda x,y:x if x>y else y,numbers)

print(result)
```

---

## Output

```text
67
```

---

# Program 4 – Smallest Number

```python
from functools import reduce

numbers=[12,45,8,67,25]

result=reduce(lambda x,y:x if x<y else y,numbers)

print(result)
```

---

## Output

```text
8
```

---

# Program 5 – String Concatenation

```python
from functools import reduce

words=["Python","Java","SQL"]

result=reduce(lambda x,y:x+" "+y,words)

print(result)
```

---

## Output

```text
Python Java SQL
```

---

# Program 6 – Sum Using Normal Function

```python
from functools import reduce

def add(a,b):

    return a+b

numbers=[5,10,15]

print(reduce(add,numbers))
```

---

## Output

```text
30
```

---

# Program 7 – Using Initial Value

```python
from functools import reduce

numbers=[1,2,3]

result=reduce(lambda x,y:x+y,numbers,10)

print(result)
```

---

## Output

```text
16
```

---

## Explanation

Initial value = 10

```
10 + 1 = 11

11 + 2 = 13

13 + 3 = 16
```

---

# Program 8 – Multiply with Initial Value

```python
from functools import reduce

numbers=[2,3,4]

print(reduce(lambda x,y:x*y,numbers,2))
```

---

## Output

```text
48
```

---

# Program 9 – Find Longest String

```python
from functools import reduce

names=["Java","Python","Oracle","SQL"]

result=reduce(

    lambda x,y:x if len(x)>len(y) else y,

    names

)

print(result)
```

---

## Output

```text
Python
```

---

# Program 10 – Count Total Characters

```python
from functools import reduce

words=["AI","ML","Python"]

result=reduce(

    lambda x,y:x+len(y),

    words[1:],

    len(words[0])

)

print(result)
```

---

## Output

```text
10
```

---

# Dry Run

```text
List

↓

reduce()

↓

First Two Elements

↓

Operation

↓

Result

↓

Next Element

↓

Operation

↓

Final Result

↓

Output
```

---

# Memory Representation

```text
numbers

│

├──10

├──20

├──30

└──40

↓

reduce()

↓

Lambda Function

↓

Accumulator

↓

100
```

---

# Advantages

- Produces a single result.
- Reduces manual looping.
- Excellent for cumulative calculations.
- Supports lambda and normal functions.
- Makes aggregation concise.

---

# Best Practices

- Import from `functools`.
- Use descriptive lambda expressions.
- Prefer normal functions for complex logic.
- Use initial values when appropriate.
- Choose reduce() only for aggregation tasks.

---

# Common Mistakes

- Forgetting to import `reduce`.
- Passing a one-parameter function.
- Using reduce() where map() or filter() is more suitable.
- Writing unreadable lambda expressions.

---

# Interview Questions

## 1. What is reduce()?

### Answer

`reduce()` combines all elements of an iterable into a single cumulative value.

---

## 2. Which module contains reduce()?

### Answer

```python
functools
```

---

## 3. What does reduce() return?

### Answer

A single value.

---

## 4. How many arguments should the reducing function accept?

### Answer

Two arguments.

---

## 5. Can reduce() work with lambda functions?

### Answer

Yes.

Lambda functions are commonly used with `reduce()`.

---

## 6. Can reduce() accept an initial value?

### Answer

Yes.

The initial value is processed before the iterable elements.

---

## 7. What is the difference between map(), filter(), and reduce()?

### Answer

- `map()` transforms values.
- `filter()` selects values.
- `reduce()` combines values into one result.

---

## 8. When should reduce() be used?

### Answer

When a single cumulative result is required, such as calculating a total, product, maximum, or minimum.

---

# Practice Programs

1. Find the sum of numbers.
2. Find the product of numbers.
3. Find the maximum value.
4. Find the minimum value.
5. Concatenate strings using reduce().

---

# Quick Revision

- `reduce()` → Combines values.
- Returns one value.
- Import from `functools`.
- Uses two-parameter function.
- Supports initial value.
- Best for aggregation.

---

# Chapter Summary

In this chapter, you learned:

- reduce() Function
- Syntax
- Parameters
- Initial Value
- Lambda with reduce()
- Normal Function with reduce()
- Practical Programs
- reduce() vs map() vs filter()
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
