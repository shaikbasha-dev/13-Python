# while Loop in Python

## Learning Objectives

After completing this chapter, you will be able to:

* Understand the `while` loop.
* Explain why the `while` loop is used.
* Write programs using the `while` loop.
* Understand the execution flow of a loop.
* Differentiate between `while` and `if` statements.

---

# Introduction

In programming, there are situations where a block of code needs to be executed repeatedly.

For example:

* Printing numbers from 1 to 10.
* Displaying multiplication tables.
* Reading user input until a valid value is entered.
* Processing records repeatedly.

Writing the same statement multiple times is inefficient.

To solve this problem, Python provides the **`while` loop**.

---

# Definition

A **`while` loop** is an iterative control statement that repeatedly executes a block of code as long as the given condition is **True**.

When the condition becomes **False**, the loop terminates.

---

# Why do we use the while Loop?

The `while` loop is used when:

* The number of iterations is not known in advance.
* A condition controls the repetition.
* Continuous execution is required until a condition becomes false.

### Examples

* ATM PIN Verification
* Password Validation
* Menu-Driven Programs
* Game Loops
* Reading User Input

---

# Syntax

```python
while condition:
    statements
```

---

# Flow Diagram

```text
           Start

             │

             ▼

        Initialize

             │

             ▼

         Condition

        /         \

     True        False

      │             │

      ▼             ▼

 Execute Block     Stop

      │

      ▼

 Update Variable

      │

      └──────────────► Condition
```

---

# Working of while Loop

1. Initialize the loop variable.
2. Check the condition.
3. If the condition is **True**, execute the loop body.
4. Update the loop variable.
5. Repeat the process.
6. When the condition becomes **False**, exit the loop.

---

# Program 1: Print Numbers from 1 to 5

## Problem Statement

Write a Python program to print numbers from **1 to 5** using a `while` loop.

---

## Program

```python
# Initialize variable
number = 1

# Loop until number becomes greater than 5
while number <= 5:

    # Display the current number
    print(number)

    # Increment the value
    number = number + 1
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

Initialize number = 1

WHILE number <= 5

    Display number

    Increment number

END WHILE

STOP
```

---

## Line-by-Line Explanation

### Line 1

```python
number = 1
```

Initializes the loop control variable.

---

### Line 2

```python
while number <= 5:
```

Checks whether the value of `number` is less than or equal to `5`.

---

### Line 3

```python
print(number)
```

Displays the current value of `number`.

---

### Line 4

```python
number = number + 1
```

Increments the value of `number` by `1`.

---

# Program 2: Print Even Numbers from 2 to 10

## Program

```python
number = 2

while number <= 10:

    print(number)

    number = number + 2
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
count = 1

while count <= 10:

    print("5 x", count, "=", 5 * count)

    count = count + 1
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

# Infinite while Loop

## Definition

An **Infinite Loop** is a loop that never terminates because its condition always remains **True**.

---

## Example

```python
while True:

    print("Welcome")
```

> Press **Ctrl + C** to stop the program manually.

---

# Real-Time Applications

The `while` loop is used in:

* ATM Machines
* Login Systems
* Password Verification
* Online Games
* Chat Applications
* Menu-Driven Programs

---

# Advantages

* Executes code repeatedly.
* Reduces code duplication.
* Suitable when the number of iterations is unknown.
* Makes programs efficient and readable.

---

# Difference between if and while

| if Statement                            | while Loop                                       |
| --------------------------------------- | ------------------------------------------------ |
| Executes once if the condition is True. | Executes repeatedly while the condition is True. |
| Used for decision making.               | Used for repetition.                             |
| No iteration.                           | Supports iteration.                              |

---

# Common Mistakes

## Forgetting to Update the Loop Variable

❌ Incorrect

```python
number = 1

while number <= 5:
    print(number)
```

This creates an infinite loop because `number` never changes.

---

✅ Correct

```python
number = 1

while number <= 5:
    print(number)
    number = number + 1
```

---

## Incorrect Condition

Always ensure the loop condition eventually becomes `False`.

---

# Interview Questions

## 1. What is a while loop?

### Answer

A `while` loop is a looping statement that repeatedly executes a block of code as long as the given condition is `True`.

---

## 2. When should we use a while loop?

### Answer

A `while` loop should be used when the number of iterations is not known beforehand and execution depends on a condition.

---

## 3. What is an Infinite Loop?

### Answer

An Infinite Loop is a loop whose condition never becomes `False`, causing it to execute continuously.

---

## 4. How can you stop an Infinite Loop?

### Answer

An Infinite Loop can be stopped by:

* Updating the loop variable correctly.
* Changing the loop condition.
* Pressing **Ctrl + C** during execution.

---

## 5. What is the difference between while and for loops?

### Answer

A `while` loop is condition-based and is used when the number of iterations is unknown.

A `for` loop is generally used when the number of iterations is known.

---

# Quick Revision

* `while` is a looping statement.
* It executes while the condition is `True`.
* Initialization, condition, and update are important.
* Forgetting the update may create an infinite loop.
* Used when the number of iterations is unknown.

---

# Summary

In this chapter, you learned:

* What a `while` loop is.
* Why it is used.
* Syntax and execution flow.
* Practical programs.
* Infinite loop.
* Real-world applications.
* Advantages.
* Common mistakes.
* Interview questions.

