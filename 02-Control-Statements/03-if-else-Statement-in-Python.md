# if...else Statement in Python

## Learning Objectives

After completing this chapter, you will be able to:

* Understand the `if...else` statement.
* Explain why the `if...else` statement is used.
* Differentiate between `if` and `if...else`.
* Write programs using `if...else`.
* Understand the execution flow of decision-making programs.

---

# Introduction

In many situations, a program must execute one block of code when a condition is **True** and another block when the condition is **False**.

For example:

* If a student passes, display **"Pass"**; otherwise, display **"Fail"**.
* If the password is correct, allow login; otherwise, display **"Invalid Password"**.
* If the account balance is sufficient, allow withdrawal; otherwise, display **"Insufficient Balance"**.

To perform such operations, Python provides the **`if...else` statement**.

---

# Definition

The **`if...else` statement** is a decision-making statement that executes one block of code when the condition is **True** and another block when the condition is **False**.

---

# Why do we use the if...else Statement?

The `if...else` statement is used when there are two possible outcomes.

Examples:

* Pass / Fail
* Login Success / Login Failed
* Eligible / Not Eligible
* Even / Odd
* Positive / Negative

---

# Syntax

```python
if condition:
    statements_if_true
else:
    statements_if_false
```

---

# Flow Diagram

```text
               Condition

            /            \

         True           False

          |                |

   if Block Executes   else Block Executes

          \              /

           \            /

            Next Statement
```

---

# Working of if...else

1. Python evaluates the condition.
2. If the condition is **True**, the `if` block executes.
3. If the condition is **False**, the `else` block executes.
4. Program execution continues with the next statement.

---

# Program 1: Check Pass or Fail

## Problem Statement

Write a Python program to check whether a student has passed or failed.

---

## Program

```python
# Student marks
marks = 65

# Check result
if marks >= 35:
    print("Student Passed")
else:
    print("Student Failed")
```

---

## Output

```text
Student Passed
```

---

## Pseudocode

```text
START

Create variable marks

Assign value 65

Check marks >= 35

If True
    Display "Student Passed"

Else
    Display "Student Failed"

STOP
```

---

## Line-by-Line Explanation

### Line 1

```python
marks = 65
```

Stores the student's marks.

---

### Line 2

```python
if marks >= 35:
```

Checks whether the marks are greater than or equal to 35.

---

### Line 3

```python
print("Student Passed")
```

Executes when the condition is `True`.

---

### Line 4

```python
else:
```

Executes when the condition is `False`.

---

### Line 5

```python
print("Student Failed")
```

Displays the failure message.

---

# Program 2: Check Even or Odd

## Problem Statement

Write a Python program to check whether a number is even or odd.

---

## Program

```python
number = 18

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
```

---

## Output

```text
Even Number
```

---

# Program 3: Voting Eligibility

## Problem Statement

Write a Python program to check whether a person is eligible for voting.

---

## Program

```python
age = 16

if age >= 18:
    print("Eligible for Voting")
else:
    print("Not Eligible for Voting")
```

---

## Output

```text
Not Eligible for Voting
```

---

# Difference between if and if...else

| if                                        | if...else                   |
| ----------------------------------------- | --------------------------- |
| Executes only when the condition is True. | Executes one of two blocks. |
| May skip execution completely.            | Always executes one block.  |
| Used for single decision.                 | Used for two-way decision.  |

---

# Real-Time Applications

The `if...else` statement is used in:

* Login Systems
* ATM Applications
* Banking Software
* Student Result Processing
* Online Payment Systems
* Hospital Management Systems
* Railway Reservation Systems

---

# Advantages

* Handles two possible outcomes.
* Improves decision-making.
* Makes programs more readable.
* Reduces unnecessary code.

---

# Common Mistakes

## Missing Colon

❌ Incorrect

```python
if age >= 18
    print("Eligible")
else
    print("Not Eligible")
```

✅ Correct

```python
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

---

## Incorrect Indentation

❌ Incorrect

```python
if age >= 18:
print("Eligible")
else:
print("Not Eligible")
```

✅ Correct

```python
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

---

# Interview Questions

## 1. What is an if...else statement?

### Answer

An `if...else` statement is a decision-making statement that executes one block of code when the condition is `True` and another block when the condition is `False`.

---

## 2. What is the difference between if and if...else?

### Answer

The `if` statement executes code only when the condition is `True`, whereas `if...else` always executes one of the two blocks.

---

## 3. Can an else block exist without an if statement?

### Answer

No. An `else` block must always be associated with an `if` statement.

---

## 4. Is indentation mandatory in if...else?

### Answer

Yes. Python uses indentation to define the code blocks.

---

## 5. How many else blocks can an if statement have?

### Answer

Only one `else` block can be associated with an `if` statement.

---

# Quick Revision

* `if...else` handles two-way decisions.
* One block executes when the condition is `True`.
* The other block executes when the condition is `False`.
* A colon (`:`) is mandatory after both `if` and `else`.
* Proper indentation is required.

---

# Summary

In this chapter, you learned:

* What the `if...else` statement is.
* Why it is used.
* Syntax and execution flow.
* Practical programs.
* Difference between `if` and `if...else`.
* Real-world applications.
* Common mistakes.
* Interview questions.

