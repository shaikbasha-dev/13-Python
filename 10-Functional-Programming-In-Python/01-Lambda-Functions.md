# Lambda Functions in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is a Lambda Function?
5. Why are Lambda Functions Required?
6. Syntax of Lambda Function
7. Characteristics of Lambda Functions
8. Lambda Function vs Normal Function
9. Internal Working
10. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand Lambda Functions.
- Differentiate normal functions and lambda functions.
- Write lambda expressions.
- Use lambda functions in real-world applications.
- Understand when lambda functions should and should not be used.

---

# Prerequisites

Before learning this chapter, you should know:

- Variables
- Operators
- Functions
- Return Statement

---

# Introduction

In Python,

functions are usually created using the **def** keyword.

However,

sometimes we need a small function that performs only one simple operation.

Writing a complete function using **def** becomes unnecessary.

Python provides **Lambda Functions** to solve this problem.

A lambda function is a short, anonymous function that can be written in a single line.

It is commonly used with functions such as:

- map()
- filter()
- reduce()
- sorted()
- max()
- min()

---

# What is a Lambda Function?

## Definition

A **Lambda Function** is an anonymous function that contains a single expression and returns its result automatically.

---

## Simple Definition

> A lambda function is a one-line anonymous function.

---

# Why are Lambda Functions Required?

Suppose we want to add two numbers.

Using a normal function

```python
def add(a, b):

    return a + b
```

Using lambda

```python
add = lambda a, b: a + b
```

The lambda function is shorter and easier to write.

---

# Syntax of Lambda Function

```python
lambda parameters : expression
```

Example

```python
square = lambda x: x * x
```

---

# Syntax Breakdown

```text
lambda

↓

Parameters

↓

:

↓

Expression

↓

Return Value
```

Unlike normal functions,

lambda functions do not require

- def
- return
- function name

The result of the expression is returned automatically.

---

# Characteristics of Lambda Functions

- Anonymous function.
- One-line function.
- Contains only one expression.
- Automatically returns the result.
- Can accept multiple parameters.
- Can be assigned to variables.
- Frequently used with higher-order functions.

---

# Lambda Function vs Normal Function

| Normal Function | Lambda Function |
|-----------------|-----------------|
| Uses `def` | Uses `lambda` |
| Has a name | Usually anonymous |
| Multiple statements allowed | Only one expression |
| Uses `return` | Returns automatically |
| Suitable for large logic | Suitable for small logic |

---

# When Should Lambda Functions Be Used?

Lambda functions are useful when:

- A function is used only once.
- The logic is very small.
- Passing a function as an argument.
- Working with `map()`, `filter()`, or `sorted()`.

---

# When Should Lambda Functions Be Avoided?

Avoid lambda functions when:

- Multiple statements are required.
- Complex business logic is involved.
- Readability decreases.
- The function will be reused many times.

---

# Internal Working

```text
Program Starts

↓

Lambda Function Created

↓

Parameters Received

↓

Expression Evaluated

↓

Result Returned Automatically

↓

Program Ends
```

---

# Advantages

- Short syntax.
- Easy to write.
- Improves readability for simple operations.
- No explicit return statement.
- Useful with functional programming.

---

# Limitations

- Only one expression is allowed.
- Cannot contain multiple statements.
- Less readable for complex logic.
- Not suitable for large functions.

---

# Best Practices

- Use lambda only for simple operations.
- Prefer normal functions for complex logic.
- Use meaningful variable names.
- Avoid nested lambda expressions.
- Keep expressions short.

---

# Common Mistakes

## Mistake 1

Trying to write multiple statements.

❌ Incorrect

```python
lambda x:

print(x)

return x
```

---

## Mistake 2

Using lambda for large programs.

---

## Mistake 3

Writing complicated expressions inside lambda.

---

## Mistake 4

Using lambda when a normal function improves readability.

---

# Program 1 – Simple Lambda Function

## Problem Statement

Write a lambda function to add two numbers.

---

## Program

```python
add = lambda a, b: a + b

print(add(10, 20))
```

---

## Output

```text
30
```

---

## Explanation

The lambda function accepts two parameters and returns their sum.

---

# Program 2 – Square of a Number

```python
square = lambda x: x * x

print(square(6))
```

---

## Output

```text
36
```

---

# Program 3 – Cube of a Number

```python
cube = lambda x: x ** 3

print(cube(4))
```

---

## Output

```text
64
```

---

# Program 4 – Find Maximum

```python
maximum = lambda a, b: a if a > b else b

print(maximum(25, 40))
```

---

## Output

```text
40
```

---

# Program 5 – Even or Odd

```python
even = lambda n: "Even" if n % 2 == 0 else "Odd"

print(even(18))

print(even(25))
```

---

## Output

```text
Even

Odd
```

---

# Program 6 – String Length

```python
length = lambda text: len(text)

print(length("Python"))
```

---

## Output

```text
6
```

---

# Program 7 – Convert to Uppercase

```python
upper = lambda text: text.upper()

print(upper("python"))
```

---

## Output

```text
PYTHON
```

---

# Program 8 – Multiply Three Numbers

```python
multiply = lambda a, b, c: a * b * c

print(multiply(2, 3, 4))
```

---

## Output

```text
24
```

---

# Program 9 – Check Positive Number

```python
positive = lambda n: "Positive" if n > 0 else "Not Positive"

print(positive(15))
```

---

## Output

```text
Positive
```

---

# Program 10 – Area of Circle

```python
area = lambda r: 3.14159 * r * r

print(area(5))
```

---

## Output

```text
78.53975
```

---

# Dry Run

```text
Lambda Created

↓

Arguments Passed

↓

Expression Evaluated

↓

Result Returned

↓

Output Displayed
```

---

# Memory Representation

```text
Memory

│

├── add

│      │

│      └── Lambda Function

│

├── square

│

├── cube

│

└── maximum
```

---

# Advantages

- Small and concise.
- Less code.
- Automatic return.
- Excellent for functional programming.
- Easy to pass as arguments.

---

# Best Practices

- Keep lambda expressions simple.
- Use descriptive variable names.
- Prefer normal functions for lengthy logic.
- Use with `map()`, `filter()`, and `sorted()` where appropriate.

---

# Common Mistakes

- Multiple statements inside lambda.
- Deeply nested lambda expressions.
- Poor variable names.
- Using lambda everywhere.

---

# Interview Questions

## 1. What is a lambda function?

### Answer

A lambda function is an anonymous function containing a single expression.

---

## 2. Which keyword is used to create a lambda function?

### Answer

```python
lambda
```

---

## 3. Can a lambda function contain multiple statements?

### Answer

No.

Only one expression is allowed.

---

## 4. Does a lambda function require a return statement?

### Answer

No.

The result is returned automatically.

---

## 5. Can lambda functions accept multiple arguments?

### Answer

Yes.

---

## 6. Why are lambda functions called anonymous functions?

### Answer

Because they are created without defining a named function using `def`.

---

## 7. Where are lambda functions commonly used?

### Answer

With `map()`, `filter()`, `reduce()`, `sorted()`, and other higher-order functions.

---

# Practice Programs

1. Find the square of a number.
2. Find the cube of a number.
3. Find the maximum of two numbers.
4. Check whether a number is even or odd.
5. Find the area of a circle.

---

# Quick Revision

- Lambda → Anonymous function
- One expression only
- Automatic return
- Uses `lambda`
- No `def`
- No explicit `return`
- Best for short operations

---

# Chapter Summary

In this chapter, we learned:

- Lambda Functions
- Syntax
- Characteristics
- Advantages
- Limitations
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
