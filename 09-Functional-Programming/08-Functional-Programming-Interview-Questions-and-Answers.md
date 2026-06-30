# Functional Programming Interview Questions and Answers in Python

## Table of Contents

1. Introduction
2. Lambda Functions
3. map() Function
4. filter() Function
5. reduce() Function
6. Decorators
7. List Comprehension
8. List Slicing
9. Scenario-Based Questions
10. Comparison Questions
11. Quick Revision
12. Final Notes

---

# Introduction

This document contains the most frequently asked interview questions on Python Functional Programming.

It is useful for:

- Freshers
- Python Developers
- Technical Interviews
- Placement Preparation
- Revision Before Interviews

---

# Lambda Functions

## 1. What is a Lambda Function?

### Answer

A lambda function is an anonymous function that consists of a single expression and returns its result automatically.

---

## 2. Why are Lambda Functions called anonymous functions?

### Answer

Because they are created without using the `def` keyword and usually do not have a function name.

---

## 3. What is the syntax of a Lambda Function?

### Answer

```python
lambda parameters: expression
```

---

## 4. Can a Lambda Function contain multiple statements?

### Answer

No.

A lambda function can contain only one expression.

---

## 5. Does a Lambda Function require a return statement?

### Answer

No.

The expression is returned automatically.

---

## 6. Can Lambda Functions accept multiple arguments?

### Answer

Yes.

Example:

```python
lambda a, b: a + b
```

---

## 7. Where are Lambda Functions commonly used?

### Answer

- map()
- filter()
- reduce()
- sorted()
- max()
- min()

---

## 8. When should Lambda Functions be avoided?

### Answer

When the logic is complex or requires multiple statements.

---

# map() Function

## 9. What is map()?

### Answer

`map()` applies a function to every element of an iterable and returns a map object.

---

## 10. What is the syntax of map()?

### Answer

```python
map(function, iterable)
```

---

## 11. What does map() return?

### Answer

A map object.

---

## 12. Can map() work with multiple iterables?

### Answer

Yes.

Example:

```python
map(lambda x, y: x + y, list1, list2)
```

---

## 13. Can map() work with normal functions?

### Answer

Yes.

It accepts both normal functions and lambda functions.

---

## 14. Why is list() often used with map()?

### Answer

Because map() returns a map object, which is commonly converted into a list for display or further processing.

---

## 15. Which iterable types are supported?

### Answer

- List
- Tuple
- Set
- Dictionary
- String

---

# filter() Function

## 16. What is filter()?

### Answer

`filter()` selects elements from an iterable that satisfy a given condition.

---

## 17. What does filter() return?

### Answer

A filter object.

---

## 18. What type of value should the filtering function return?

### Answer

A Boolean value (`True` or `False`).

---

## 19. Can filter() use lambda functions?

### Answer

Yes.

Lambda functions are commonly used with filter().

---

## 20. Can filter() use normal functions?

### Answer

Yes.

---

## 21. What happens when the condition returns False?

### Answer

The element is excluded from the result.

---

## 22. Why convert a filter object into a list?

### Answer

To view or use the filtered elements directly.

---

# reduce() Function

## 23. What is reduce()?

### Answer

`reduce()` combines all elements of an iterable into a single cumulative value.

---

## 24. Which module contains reduce()?

### Answer

```python
functools
```

---

## 25. How is reduce() imported?

### Answer

```python
from functools import reduce
```

---

## 26. What does reduce() return?

### Answer

A single cumulative value.

---

## 27. How many arguments should the reducing function accept?

### Answer

Two arguments.

---

## 28. Can reduce() accept an initial value?

### Answer

Yes.

Example:

```python
reduce(function, iterable, initial_value)
```

---

## 29. Give examples of problems solved using reduce().

### Answer

- Sum
- Product
- Maximum
- Minimum
- String concatenation

---

# Decorators

## 30. What is a Decorator?

### Answer

A decorator is a function that adds additional functionality to another function without modifying its original code.

---

## 31. Why are decorators used?

### Answer

To implement reusable features such as:

- Logging
- Authentication
- Validation
- Performance measurement
- Caching

---

## 32. What is a Higher-Order Function?

### Answer

A function that accepts another function as an argument or returns another function.

---

## 33. What is a Wrapper Function?

### Answer

A nested function inside the decorator that executes additional code before and/or after the original function.

---

## 34. Which symbol is used to apply decorators?

### Answer

```python
@
```

---

## 35. Can multiple decorators be applied?

### Answer

Yes.

Multiple decorators can be stacked on the same function.

---

## 36. Why is functools.wraps used?

### Answer

To preserve the metadata of the original function, such as its name and documentation string.

---

# List Comprehension

## 37. What is List Comprehension?

### Answer

A concise way to create lists using a single line of code.

---

## 38. What is its syntax?

### Answer

```python
[expression for item in iterable]
```

---

## 39. Can conditions be used?

### Answer

Yes.

Example:

```python
[x for x in range(10) if x % 2 == 0]
```

---

## 40. Can List Comprehension be nested?

### Answer

Yes.

---

## 41. What are its advantages?

### Answer

- Less code
- Better readability
- Easy transformations
- Efficient list creation

---

## 42. When should List Comprehension be avoided?

### Answer

When the logic is too complex and reduces readability.

---

# List Slicing

## 43. What is List Slicing?

### Answer

List slicing extracts a portion of a list using index positions.

---

## 44. What is the syntax?

### Answer

```python
list[start:stop:step]
```

---

## 45. Is the stop index included?

### Answer

No.

The stop index is excluded.

---

## 46. How do you reverse a list using slicing?

### Answer

```python
list[::-1]
```

---

## 47. How do you create a copy of a list?

### Answer

```python
copy = list[:]
```

---

## 48. Can slicing modify a list?

### Answer

Yes.

Using slice assignment.

Example:

```python
numbers[1:3] = [100, 200]
```

---

# Comparison Questions

## 49. Difference between map() and filter()

| map() | filter() |
|--------|-----------|
| Transforms elements | Selects elements |
| Function returns modified value | Function returns Boolean |
| Output size is usually the same | Output size may be smaller |

---

## 50. Difference between filter() and reduce()

| filter() | reduce() |
|-----------|-----------|
| Returns iterable | Returns one value |
| Selects elements | Combines elements |

---

## 51. Difference between map() and reduce()

| map() | reduce() |
|--------|-----------|
| Returns iterable | Returns one value |
| Transforms values | Aggregates values |

---

## 52. Difference between Lambda Function and Normal Function

| Lambda | Normal Function |
|---------|----------------|
| Uses lambda keyword | Uses def keyword |
| One expression | Multiple statements allowed |
| Automatic return | Uses return statement |

---

## 53. Difference between List Comprehension and map()

| List Comprehension | map() |
|--------------------|-------|
| Python-specific syntax | Built-in function |
| Easy for simple transformations | Useful when applying existing functions |
| Supports conditions directly | Often combined with filter() |

---

# Scenario-Based Questions

## 54. You need to transform every value in a list. Which function will you use?

### Answer

`map()`

---

## 55. You need to select only even numbers from a list. Which function will you use?

### Answer

`filter()`

---

## 56. You need the sum of all elements in a list. Which function will you use?

### Answer

`reduce()`

---

## 57. You need to add logging to multiple functions without changing their code. Which Python feature will you use?

### Answer

Decorators.

---

## 58. You need to create a list of squares in one line. Which feature will you use?

### Answer

List Comprehension.

---

## 59. You need the last five elements of a list. Which feature will you use?

### Answer

List Slicing.

---

## 60. You need to reverse a list quickly. Which syntax will you use?

### Answer

```python
list[::-1]
```

---

# Quick Revision

Remember:

- Lambda → Anonymous function
- map() → Transform values
- filter() → Select values
- reduce() → Aggregate values
- Decorator → Extend function behavior
- List Comprehension → One-line list creation
- List Slicing → Extract part of a list
- `@` → Decorator syntax
- `[::-1]` → Reverse list
- `[:]` → Copy list

---

# Final Notes

After completing this chapter, you should be able to:

- Write and use lambda functions.
- Apply map(), filter(), and reduce() appropriately.
- Create reusable decorators.
- Use list comprehensions effectively.
- Perform list slicing operations confidently.
- Answer common Functional Programming interview questions.
