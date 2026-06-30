# filter() Function in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is filter()?
5. Why is filter() Required?
6. Syntax
7. Parameters
8. Return Value
9. Internal Working
10. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the purpose of the filter() function.
- Filter iterable objects based on conditions.
- Use filter() with normal functions.
- Use filter() with lambda functions.
- Convert filter objects into lists, tuples, and sets.
- Apply filter() in real-world applications.

---

# Prerequisites

Before learning this chapter, you should know:

- Functions
- Lambda Functions
- Lists
- Conditional Statements
- map() Function

---

# Introduction

In Python,

there are situations where we need only specific elements from a collection.

For example,

- Select only even numbers.
- Select only positive numbers.
- Select students who passed.
- Select names starting with a specific letter.

Instead of writing loops,

Python provides the

```python
filter()
```

function.

---

# What is filter()?

## Definition

The `filter()` function filters elements from an iterable based on a condition and returns only those elements that satisfy the condition.

---

## Simple Definition

> `filter()` selects only the elements that satisfy a given condition.

---

# Why is filter() Required?

Suppose we have

```text
[10, 15, 20, 25, 30]
```

If we need only even numbers,

instead of writing loops,

we use

```python
filter()
```

---

# Syntax

```python
filter(function, iterable)
```

---

# Parameters

## function

A function that returns either

```python
True
```

or

```python
False
```

It can be

- Normal Function
- Lambda Function

---

## iterable

Any iterable object such as

- List
- Tuple
- Set
- Dictionary
- String

---

# Return Value

Returns a

```python
filter object
```

which can be converted into

- list
- tuple
- set

---

# How filter() Works

Example

```python
numbers = [10,15,20,25]

result = filter(lambda x: x % 2 == 0, numbers)
```

Execution

```text
10 → True

15 → False

20 → True

25 → False
```

Result

```text
10

20
```

---

# filter() vs map()

| map() | filter() |
|--------|-----------|
| Transforms every element | Selects specific elements |
| Output size is generally the same as input | Output size may be smaller |
| Returns modified values | Returns original values that satisfy the condition |

---

# Internal Working

```text
Iterable

↓

filter()

↓

Condition Checked

↓

True ?

↓

Yes

↓

Keep Element

↓

No

↓

Discard Element

↓

Filter Object

↓

list()

↓

Output
```

---

# Advantages

- Less code.
- Easy filtering.
- Improves readability.
- Works well with lambda.
- Useful for data processing.

---

# Best Practices

- Keep filtering conditions simple.
- Use lambda only for short conditions.
- Use normal functions for complex logic.
- Convert filter objects into lists when required.
- Choose meaningful variable names.

---

# Common Mistakes

## Mistake 1

Printing a filter object directly.

Incorrect

```python
result = filter(lambda x:x>10,[1,2,3])

print(result)
```

Correct

```python
print(list(result))
```

---

## Mistake 2

Returning values other than Boolean.

Although Python evaluates truthy and falsy values, writing conditions that clearly return `True` or `False` makes the code easier to understand.

---

## Mistake 3

Using filter() when map() is required.

Remember

- map() → modifies values
- filter() → selects values

---

# Program 1 – Even Numbers

```python
numbers = [1,2,3,4,5,6,7,8]

result = filter(lambda x:x%2==0,numbers)

print(list(result))
```

---

## Output

```text
[2, 4, 6, 8]
```

---

# Program 2 – Odd Numbers

```python
numbers = [1,2,3,4,5,6]

result = filter(lambda x:x%2!=0,numbers)

print(list(result))
```

---

## Output

```text
[1, 3, 5]
```

---

# Program 3 – Positive Numbers

```python
numbers = [-5,-2,0,4,8,-1]

result = filter(lambda x:x>0,numbers)

print(list(result))
```

---

## Output

```text
[4, 8]
```

---

# Program 4 – Negative Numbers

```python
numbers = [-8,5,-4,7,-1]

result = filter(lambda x:x<0,numbers)

print(list(result))
```

---

## Output

```text
[-8, -4, -1]
```

---

# Program 5 – Numbers Greater than 50

```python
numbers = [20,55,80,35,90]

result = filter(lambda x:x>50,numbers)

print(list(result))
```

---

## Output

```text
[55, 80, 90]
```

---

# Program 6 – Passed Students

```python
marks = [35,80,65,20,90,40]

result = filter(lambda x:x>=35,marks)

print(list(result))
```

---

## Output

```text
[35, 80, 65, 90, 40]
```

---

# Program 7 – Filter String Length

```python
names = ["Java","Python","C","Oracle"]

result = filter(lambda x:len(x)>4,names)

print(list(result))
```

---

## Output

```text
['Python', 'Oracle']
```

---

# Program 8 – Names Starting with 'A'

```python
names = ["Amit","Rahul","Anil","Kiran"]

result = filter(lambda x:x.startswith("A"),names)

print(list(result))
```

---

## Output

```text
['Amit', 'Anil']
```

---

# Program 9 – Using Normal Function

```python
def even(number):

    return number%2==0

numbers=[10,15,20,25,30]

result=filter(even,numbers)

print(list(result))
```

---

## Output

```text
[10, 20, 30]
```

---

# Program 10 – Remove Empty Strings

```python
names=["Python","","Java","","SQL"]

result=filter(None,names)

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

filter()

↓

Condition Checked

↓

True ?

↓

Keep Element

↓

False ?

↓

Ignore Element

↓

Filter Object

↓

list()

↓

Output
```

---

# Memory Representation

```text
numbers

│

├──10

├──15

├──20

├──25

├──30

↓

filter()

↓

Lambda Function

↓

Filter Object

↓

List
```

---

# Advantages

- Efficient filtering.
- Shorter code.
- Better readability.
- Supports lambda functions.
- Useful for data analysis.

---

# Best Practices

- Use simple filtering conditions.
- Prefer lambda for one-line conditions.
- Use normal functions for complex conditions.
- Convert filter objects into lists when necessary.

---

# Common Mistakes

- Printing filter objects directly.
- Using filter() instead of map().
- Writing overly complex lambda expressions.
- Forgetting that filter() returns original elements, not modified ones.

---

# Interview Questions

## 1. What is filter()?

### Answer

`filter()` selects elements from an iterable that satisfy a given condition.

---

## 2. What does filter() return?

### Answer

A filter object.

---

## 3. Can filter() work with lambda?

### Answer

Yes.

Lambda functions are commonly used with `filter()`.

---

## 4. What should the filtering function return?

### Answer

A Boolean value (`True` or `False`).

---

## 5. What happens if the condition returns True?

### Answer

The element is included in the output.

---

## 6. What happens if the condition returns False?

### Answer

The element is excluded from the output.

---

## 7. What is the difference between map() and filter()?

### Answer

`map()` transforms every element.

`filter()` selects only the elements that satisfy a condition.

---

## 8. Can filter() work with normal functions?

### Answer

Yes.

It works with both normal functions and lambda functions.

---

## Practice Programs

1. Find even numbers using filter().
2. Find odd numbers.
3. Find positive numbers.
4. Find students who passed.
5. Find names beginning with a specific letter.

---

# Quick Revision

- `filter()` → Selects elements.
- Returns a filter object.
- Uses Boolean conditions.
- Works with lambda.
- Convert using `list()`.

---

# Chapter Summary

In this chapter, you learned:

- filter() Function
- Syntax
- Parameters
- Return Value
- Lambda with filter()
- Normal Function with filter()
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
