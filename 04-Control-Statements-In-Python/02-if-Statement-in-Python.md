# If Statement in Python

## Learning Objectives

After completing this chapter, you will be able to:

* Understand the `if` statement.
* Explain why the `if` statement is used.
* Write simple decision-making programs.
* Understand the flow of an `if` statement.
* Develop basic logical thinking for problem-solving.

---

# Introduction

In programming, we often need to execute a block of code only when a specific condition is **True**.

For example:

* If the student has passed, display **"Pass"**.
* If the password is correct, allow login.
* If the age is 18 or above, allow voting.

To perform such decision-making operations, Python provides the **`if` statement**.

---

# Definition

The **`if` statement** is a decision-making statement that executes a block of code only when the specified condition evaluates to **True**.

If the condition is **False**, the block of code is skipped.

---

# Why do we use the if Statement?

The `if` statement is used whenever a program needs to make a decision.

Examples include:

* Login Validation
* ATM PIN Verification
* Student Result Processing
* Online Payment Verification
* Age Verification
* Employee Eligibility Check

---

# Syntax

```python
if condition:
    statement1
    statement2
```

> **Note:** The statements inside the `if` block must be indented.

---

# Flow Diagram

```text
            Condition

               │

        ┌──────┴──────┐

      True         False

        │              │

 Execute Block     Skip Block

        │              │

        └──────┬───────┘

               │

            Next Statement
```

---

# Working of the if Statement

1. Python evaluates the condition.
2. If the condition is **True**, the statements inside the `if` block are executed.
3. If the condition is **False**, the `if` block is skipped.
4. Control moves to the next statement after the `if` block.

---

# Program 1: Check Eligible for Voting

## Problem Statement

Write a Python program to check whether a person is eligible to vote.

---

## Program

```python
# Age of the person
age = 20

# Check voting eligibility
if age >= 18:
    print("Eligible for Voting")
```

---

## Output

```text
Eligible for Voting
```

---

## Pseudocode

```text
START

Create variable age

Assign value 20

Check age >= 18

If True
    Display "Eligible for Voting"

STOP
```

---

## Line-by-Line Explanation

### Line 1

```python
age = 20
```

Creates a variable named `age` and stores the value `20`.

---

### Line 2

```python
if age >= 18:
```

Checks whether the age is greater than or equal to `18`.

The condition evaluates to **True**.

---

### Line 3

```python
print("Eligible for Voting")
```

Since the condition is `True`, the message is displayed.

---

# Program 2: Check Positive Number

## Problem Statement

Write a Python program to check whether a number is positive.

---

## Program

```python
# Store a number
number = 15

# Check whether the number is positive
if number > 0:
    print("Positive Number")
```

---

## Output

```text
Positive Number
```

---

## Pseudocode

```text
START

Create variable number

Assign value 15

Check number > 0

If True
    Display "Positive Number"

STOP
```

---

# Program 3: Student Pass Check

## Problem Statement

Write a Python program to check whether a student has passed.

---

## Program

```python
# Store marks
marks = 65

# Check pass condition
if marks >= 35:
    print("Student Passed")
```

---

## Output

```text
Student Passed
```

---

## Real-Time Applications

The `if` statement is commonly used in:

* ATM Machines
* Login Systems
* Banking Applications
* Hospital Management Systems
* Online Shopping Websites
* Online Examination Systems

---

# Advantages of if Statement

* Simple decision making.
* Improves program logic.
* Easy to understand.
* Widely used in real-world applications.
* Forms the foundation for advanced control statements.

---

# Common Mistakes

### Missing Colon

❌ Incorrect

```python
if age >= 18
    print("Eligible")
```

✅ Correct

```python
if age >= 18:
    print("Eligible")
```

---

### Incorrect Indentation

❌ Incorrect

```python
if age >= 18:
print("Eligible")
```

✅ Correct

```python
if age >= 18:
    print("Eligible")
```

---

# Interview Questions

### 1. What is an `if` statement?

### Answer

The `if` statement is a decision-making statement used to execute a block of code only when a specified condition is `True`.

---

### 2. When is the `if` block executed?

### Answer

The `if` block is executed only when the condition evaluates to `True`.

---

### 3. What happens when the condition is `False`?

### Answer

The statements inside the `if` block are skipped, and execution continues with the next statement after the block.

---

### 4. Why is indentation important in Python?

### Answer

Indentation defines the block of code that belongs to the `if` statement. Without proper indentation, Python raises an `IndentationError`.

---

### 5. Can an `if` statement exist without an `else` statement?

### Answer

Yes. An `if` statement can be used independently without an `else` statement.

---

# Quick Revision

* `if` is a decision-making statement.
* It executes only when the condition is `True`.
* A colon (`:`) is mandatory after the condition.
* Indentation is mandatory for the block of code.
* If the condition is `False`, the block is skipped.

---

# Summary

In this chapter, you learned:

* What the `if` statement is.
* Why it is used.
* Syntax of the `if` statement.
* Flow of execution.
* Practical programs.
* Flow diagram.
* Interview questions.
* Common mistakes.
* Quick revision.

