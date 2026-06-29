# for Loop in Python

## Learning Objectives

After completing this chapter, you will be able to:

* Understand the `for` loop.
* Explain why the `for` loop is used.
* Learn the `range()` function.
* Iterate over sequences using the `for` loop.
* Write programs using the `for` loop.
* Differentiate between `while` and `for` loops.

---

# Introduction

In programming, there are situations where we need to execute a block of code repeatedly for a **known number of times**.

For example:

* Print numbers from 1 to 10.
* Display a multiplication table.
* Print each character of a string.
* Display all elements of a list.

Instead of writing the same statement repeatedly, Python provides the **`for` loop**.

---

# Definition

A **`for` loop** is an iterative control statement used to execute a block of code repeatedly by iterating over a sequence or a range of values.

---

# Why do we use the for Loop?

The `for` loop is used when:

* The number of iterations is known.
* Iterating over strings.
* Iterating over lists.
* Iterating over tuples.
* Iterating over dictionaries.
* Processing collections of data.

---

# Syntax

```python
for variable in sequence:
    statements
```

---

# Flow Diagram

```text
              Start

                │

                ▼

      Select Sequence

                │

                ▼

       Next Element?

         /        \

      Yes        No

       │          │

       ▼          ▼

 Execute Block   Stop

       │

       ▼

 Next Element
```

---

# Working of for Loop

1. Select a sequence.
2. The loop variable receives the first value.
3. Execute the loop body.
4. Move to the next value.
5. Repeat until all values are processed.
6. Exit the loop.

---

# The range() Function

## Definition

The `range()` function generates a sequence of numbers.

It is commonly used with the `for` loop.

---

## Syntax

```python
range(stop)
```

or

```python
range(start, stop)
```

or

```python
range(start, stop, step)
```

---

## Types of range()

### 1. range(stop)

Example

```python
for number in range(5):
    print(number)
```

Output

```text
0
1
2
3
4
```

---

### 2. range(start, stop)

Example

```python
for number in range(1, 6):
    print(number)
```

Output

```text
1
2
3
4
5
```

---

### 3. range(start, stop, step)

Example

```python
for number in range(2, 11, 2):
    print(number)
```

Output

```text
2
4
6
8
10
```

---

# Program 1: Print Numbers from 1 to 5

## Problem Statement

Write a Python program to print numbers from 1 to 5.

---

## Program

```python
# Print numbers from 1 to 5
for number in range(1, 6):

    print(number)
```

---

## Output

```text
1
2
3
4
5
```

---

## Pseudocode

```text
START

FOR number from 1 to 5

    Display number

END FOR

STOP
```

---

## Line-by-Line Explanation

### Line 1

```python
for number in range(1, 6):
```

The `range(1, 6)` function generates numbers from **1 to 5**.

The loop variable `number` stores one value at a time.

---

### Line 2

```python
print(number)
```

Displays the current value of `number`.

---

# Program 2: Print Even Numbers

## Program

```python
for number in range(2, 11, 2):

    print(number)
```

---

## Output

```text
2
4
6
8
10
```

---

# Program 3: Multiplication Table of 5

## Program

```python
for number in range(1, 11):

    print("5 x", number, "=", 5 * number)
```

---

## Output

```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

---

# Program 4: Print Characters of a String

## Program

```python
name = "Python"

for character in name:

    print(character)
```

---

## Output

```text
P
y
t
h
o
n
```

---

# Program 5: Print Elements of a List

## Program

```python
numbers = [10, 20, 30, 40, 50]

for number in numbers:

    print(number)
```

---

## Output

```text
10
20
30
40
50
```

---

# Real-Time Applications

The `for` loop is used in:

* Reading files
* Processing lists
* Displaying records
* Generating reports
* Data Analysis
* Machine Learning
* Automation Scripts

---

# Advantages

* Easy to write.
* Suitable for known iterations.
* Reduces code duplication.
* Improves readability.
* Works with all iterable objects.

---

# Difference between while and for

| while Loop                        | for Loop                                |
| --------------------------------- | --------------------------------------- |
| Used when iterations are unknown. | Used when iterations are known.         |
| Condition-based.                  | Sequence-based.                         |
| Manual update required.           | Automatic iteration.                    |
| More chances of infinite loop.    | No infinite loop due to missing update. |

---

# Common Mistakes

## Incorrect range()

❌ Incorrect

```python
for number in range(5, 1):
    print(number)
```

Output

```text
No Output
```

Reason:

Default step is **+1**, but `5` is greater than `1`.

---

✅ Correct

```python
for number in range(5, 0, -1):

    print(number)
```

---

## Forgetting the Colon

❌ Incorrect

```python
for number in range(5)
```

---

✅ Correct

```python
for number in range(5):
```

---

# Interview Questions

## 1. What is a for loop?

### Answer

A `for` loop is an iterative statement used to execute a block of code repeatedly by iterating over a sequence or range.

---

## 2. What is the use of range()?

### Answer

The `range()` function generates a sequence of numbers used for iteration.

---

## 3. Can a for loop iterate over strings?

### Answer

Yes.

Example

```python
for character in "Python":
    print(character)
```

---

## 4. What is the difference between while and for?

### Answer

A `while` loop depends on a condition, whereas a `for` loop iterates over a sequence.

---

## 5. What are the three forms of range()?

### Answer

* `range(stop)`
* `range(start, stop)`
* `range(start, stop, step)`

---

# Quick Revision

* `for` loop is used for known iterations.
* `range()` generates a sequence of numbers.
* Python supports three forms of `range()`.
* `for` loop works with strings, lists, tuples, sets, and dictionaries.
* `for` loop automatically moves to the next element.

---

# Summary

In this chapter, you learned:

* What the `for` loop is.
* Why it is used.
* The `range()` function.
* Three forms of `range()`.
* Practical programs.
* Real-world applications.
* Advantages.
* Common mistakes.
* Interview questions.

