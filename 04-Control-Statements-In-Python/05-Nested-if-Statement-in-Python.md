# Nested if Statement in Python

## Learning Objectives

After completing this chapter, you will be able to:

* Understand the Nested `if` statement.
* Explain why Nested `if` statements are used.
* Write programs using Nested `if`.
* Understand the execution flow of Nested `if`.
* Solve real-world problems involving multiple dependent conditions.

---

# Introduction

Sometimes, a single condition is not enough to make a decision.

A program may need to check another condition only if the first condition is **True**.

In such situations, Python provides the **Nested `if` Statement**.

A Nested `if` means placing one `if` statement inside another `if` statement.

---

# Definition

A **Nested `if` Statement** is an `if` statement placed inside another `if` statement.

The inner `if` statement is executed only when the outer `if` condition evaluates to **True**.

---

# Why do we use Nested if?

Nested `if` statements are used when one condition depends on another condition.

### Examples

* ATM Transaction
* Online Banking
* Employee Verification
* Student Scholarship Eligibility
* Login Authentication
* College Admission

---

# Syntax

```python
if condition1:
    if condition2:
        statements
```

---

# Flow Diagram

```text
             Condition 1

            /          \

         True         False

          |

     Condition 2

      /        \

   True       False

    |

 Execute Block

    |

 Next Statement
```

---

# Working of Nested if

1. Python checks the outer `if` condition.
2. If it is **False**, the inner `if` statement is skipped.
3. If it is **True**, Python checks the inner `if` condition.
4. If the inner condition is **True**, the nested block executes.
5. Control moves to the next statement after the Nested `if`.

---

# Program 1: Student Scholarship Eligibility

## Problem Statement

Write a Python program to check whether a student is eligible for a scholarship.

Conditions:

* Marks should be greater than or equal to 75.
* Attendance should be greater than or equal to 80%.

---

## Program

```python
# Student details
marks = 82
attendance = 90

# Check scholarship eligibility
if marks >= 75:

    if attendance >= 80:
        print("Eligible for Scholarship")
```

---

## Output

```text
Eligible for Scholarship
```

---

## Pseudocode

```text
START

Create variable marks

Create variable attendance

Check marks >= 75

If True

    Check attendance >= 80

    If True

        Display "Eligible for Scholarship"

STOP
```

---

## Line-by-Line Explanation

### Line 1

```python
marks = 82
```

Stores the student's marks.

---

### Line 2

```python
attendance = 90
```

Stores the student's attendance percentage.

---

### Line 3

```python
if marks >= 75:
```

Checks whether the student has scored at least 75 marks.

---

### Line 4

```python
if attendance >= 80:
```

This condition is checked only if the first condition is `True`.

---

### Line 5

```python
print("Eligible for Scholarship")
```

Displays the eligibility message.

---

# Program 2: ATM Cash Withdrawal

## Problem Statement

Write a Python program to verify the ATM PIN and account balance before allowing cash withdrawal.

---

## Program

```python
pin = 1234
balance = 15000

if pin == 1234:

    if balance >= 5000:
        print("Transaction Successful")
```

---

## Output

```text
Transaction Successful
```

---

# Program 3: Employee Bonus Eligibility

## Problem Statement

Write a Python program to determine whether an employee is eligible for a bonus.

Conditions:

* Experience must be at least 5 years.
* Performance rating must be at least 4.

---

## Program

```python
experience = 6
rating = 4

if experience >= 5:

    if rating >= 4:
        print("Bonus Approved")
```

---

## Output

```text
Bonus Approved
```

---

# Real-Time Applications

Nested `if` statements are used in:

* Banking Applications
* Login Authentication
* College Admission Systems
* Scholarship Verification
* Employee Promotion Systems
* Online Examination Systems

---

# Advantages

* Handles dependent conditions efficiently.
* Improves logical decision-making.
* Suitable for complex validation.
* Easy to implement for multiple-level checks.

---

# Difference between if and Nested if

| if Statement                | Nested if Statement                        |
| --------------------------- | ------------------------------------------ |
| Checks a single condition.  | Checks multiple dependent conditions.      |
| Simple decision-making.     | Multi-level decision-making.               |
| One condition is evaluated. | One condition is evaluated inside another. |

---

# Common Mistakes

## Incorrect Indentation

❌ Incorrect

```python
if marks >= 75:
if attendance >= 80:
    print("Eligible")
```

---

✅ Correct

```python
if marks >= 75:
    if attendance >= 80:
        print("Eligible")
```

---

## Unnecessary Nesting

Avoid using Nested `if` statements when a logical operator (`and`, `or`) can solve the problem more simply.

Example:

Instead of

```python
if marks >= 75:
    if attendance >= 80:
        print("Eligible")
```

You can also write

```python
if marks >= 75 and attendance >= 80:
    print("Eligible")
```

Choose the approach that makes the program easier to understand.

---

# Interview Questions

## 1. What is a Nested if statement?

### Answer

A Nested `if` statement is an `if` statement placed inside another `if` statement. It is used to evaluate dependent conditions.

---

## 2. When should Nested if be used?

### Answer

Nested `if` should be used when one condition depends on another condition being true.

---

## 3. Can multiple Nested if statements be used?

### Answer

Yes. Python allows multiple levels of nesting, but excessive nesting should be avoided to maintain readability.

---

## 4. What is the disadvantage of excessive nesting?

### Answer

Deeply nested code becomes difficult to read, understand, debug, and maintain.

---

## 5. Can Nested if be replaced using logical operators?

### Answer

Yes. In many situations, logical operators such as `and` and `or` can simplify the code.

---

# Quick Revision

* Nested `if` means placing one `if` inside another `if`.
* The inner `if` executes only when the outer condition is `True`.
* Used for dependent conditions.
* Indentation is mandatory.
* Avoid unnecessary nesting when simpler alternatives exist.

---

# Summary

In this chapter, you learned:

* What a Nested `if` statement is.
* Why it is used.
* Syntax and execution flow.
* Practical programs.
* Flow diagram.
* Real-world applications.
* Advantages.
* Common mistakes.
* Interview questions.

