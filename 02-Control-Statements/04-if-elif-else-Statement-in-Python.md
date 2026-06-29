# if...elif...else Statement in Python

## Learning Objectives

After completing this chapter, you will be able to:

* Understand the `if...elif...else` statement.
* Explain why the `if...elif...else` statement is used.
* Write programs involving multiple conditions.
* Understand the execution flow of multi-way decision making.
* Apply the `if...elif...else` statement in real-world applications.

---

# Introduction

Sometimes a program needs to evaluate **more than two conditions**.

For example:

* Student Grade Calculation
* Employee Salary Classification
* Traffic Signal System
* Menu-Driven Programs
* Online Shopping Discounts

In such situations, using only `if` or `if...else` becomes difficult.

Python provides the **`if...elif...else` statement** to handle multiple conditions efficiently.

---

# Definition

The **`if...elif...else` statement** is a multi-way decision-making statement that evaluates multiple conditions one by one.

* If a condition is **True**, its corresponding block executes.
* The remaining conditions are skipped.
* If none of the conditions are `True`, the `else` block executes.

---

# Why do we use if...elif...else?

It is used whenever a program has multiple possible outcomes.

### Examples

* Grade Calculation
* ATM Transaction Menu
* Employee Bonus Calculation
* Income Tax Calculation
* Electricity Bill Calculation
* Weather Prediction

---

# Syntax

```python
if condition1:
    statements

elif condition2:
    statements

elif condition3:
    statements

else:
    statements
```

---

# Flow Diagram

```text
                 Condition 1

               /            \

            True          False

             |               |

       Execute Block     Condition 2

                             |

                     True         False

                      |             |

                Execute Block   Condition 3

                                    |

                            True         False

                             |             |

                      Execute Block    else Block

                                    |

                               Next Statement
```

---

# Working of if...elif...else

1. Python checks the first condition.
2. If it is `True`, that block executes.
3. Otherwise, Python checks the next `elif` condition.
4. This process continues until a condition becomes `True`.
5. If no condition is `True`, the `else` block executes.
6. Only **one block** executes.

---

# Program 1: Grade Calculator

## Problem Statement

Write a Python program to display the student's grade based on marks.

---

## Program

```python
# Student marks
marks = 82

# Grade calculation
if marks >= 90:
    print("Grade A+")

elif marks >= 75:
    print("Grade A")

elif marks >= 60:
    print("Grade B")

elif marks >= 35:
    print("Grade C")

else:
    print("Fail")
```

---

## Output

```text
Grade A
```

---

## Pseudocode

```text
START

Create variable marks

Assign marks

If marks >= 90
    Display Grade A+

Else if marks >= 75
    Display Grade A

Else if marks >= 60
    Display Grade B

Else if marks >= 35
    Display Grade C

Else
    Display Fail

STOP
```

---

# Program 2: Largest of Three Numbers

## Problem Statement

Write a Python program to find the largest among three numbers.

---

## Program

```python
# Store three numbers
a = 25
b = 40
c = 18

# Find the largest
if a >= b and a >= c:
    print("A is Largest")

elif b >= a and b >= c:
    print("B is Largest")

else:
    print("C is Largest")
```

---

## Output

```text
B is Largest
```

---

# Program 3: Traffic Signal System

## Problem Statement

Write a Python program to display an action based on the traffic signal color.

---

## Program

```python
# Traffic signal
signal = "Green"

if signal == "Red":
    print("Stop")

elif signal == "Yellow":
    print("Get Ready")

elif signal == "Green":
    print("Go")

else:
    print("Invalid Signal")
```

---

## Output

```text
Go
```

---

# Real-Time Applications

The `if...elif...else` statement is widely used in:

* Student Grade Calculation
* Salary Processing
* Income Tax Calculation
* Banking Applications
* Online Shopping Discounts
* Menu-Driven Programs
* Railway Reservation Systems

---

# Advantages

* Handles multiple conditions efficiently.
* Improves readability.
* Avoids deeply nested `if` statements.
* Makes programs easier to maintain.
* Executes only one matching block.

---

# Difference between if, if...else, and if...elif...else

| Statement          | Purpose                                             |
| ------------------ | --------------------------------------------------- |
| `if`               | Executes a block only when the condition is `True`. |
| `if...else`        | Handles two possible outcomes.                      |
| `if...elif...else` | Handles multiple conditions.                        |

---

# Common Mistakes

## Incorrect Order of Conditions

❌ Incorrect

```python
marks = 85

if marks >= 35:
    print("Pass")

elif marks >= 75:
    print("Grade A")
```

Since `marks >= 35` is already `True`, the `elif` block will never execute.

---

✅ Correct

```python
marks = 85

if marks >= 90:
    print("Grade A+")

elif marks >= 75:
    print("Grade A")

elif marks >= 35:
    print("Pass")
```

Always write conditions from **highest priority to lowest priority**.

---

# Interview Questions

## 1. What is an if...elif...else statement?

### Answer

It is a decision-making statement used to evaluate multiple conditions and execute only one matching block of code.

---

## 2. Why do we use elif?

### Answer

The `elif` keyword allows us to check another condition when the previous condition is `False`.

---

## 3. How many elif blocks can be used?

### Answer

There is no fixed limit. A program can have any number of `elif` blocks.

---

## 4. Is the else block mandatory?

### Answer

No. The `else` block is optional.

---

## 5. How many blocks execute in an if...elif...else statement?

### Answer

Only **one block** executes.

---

# Quick Revision

* Used for multiple conditions.
* Conditions are checked from top to bottom.
* The first matching condition executes.
* Remaining conditions are skipped.
* `else` executes only when no condition is `True`.

---

# Summary

In this chapter, you learned:

* What the `if...elif...else` statement is.
* Why it is used.
* Syntax and execution flow.
* Practical programs.
* Flow diagram.
* Real-world applications.
* Advantages.
* Common mistakes.
* Interview questions.

