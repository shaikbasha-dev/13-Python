# Logical Operators in Python

## Learning Objectives

After completing this chapter, you will be able to:

- Understand Logical Operators.
- Explain why logical operators are used.
- Learn different logical operators.
- Evaluate multiple conditions.
- Understand truth tables.
- Write programs using logical operators.

---

# Introduction

Logical Operators are used to combine two or more conditions.

These operators return either **True** or **False** depending on the result of the logical expression.

Logical operators are mainly used in:

- Decision Making
- Login Systems
- Eligibility Checking
- User Authentication
- Banking Applications

Without logical operators, checking multiple conditions would be difficult.

---

# Definition

A **Logical Operator** is an operator used to combine or modify Boolean expressions.

Python provides three logical operators:

- `and`
- `or`
- `not`

---

# Why do we use Logical Operators?

Logical operators help to:

- Combine multiple conditions.
- Make complex decisions.
- Validate user input.
- Improve program logic.
- Control program execution.

---

# Types of Logical Operators

| Operator | Description |
|----------|-------------|
| and | Returns True if both conditions are True |
| or | Returns True if at least one condition is True |
| not | Reverses the Boolean value |

---

# 1. AND Operator

## Definition

The **and** operator returns **True** only when **both conditions are True**.

---

## Truth Table

| Condition 1 | Condition 2 | Result |
|-------------|-------------|--------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

---

## Program

```python
age = 22
citizen = True

print(age >= 18 and citizen)
```

### Output

```text
True
```

---

# 2. OR Operator

## Definition

The **or** operator returns **True** if **at least one condition is True**.

---

## Truth Table

| Condition 1 | Condition 2 | Result |
|-------------|-------------|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

---

## Program

```python
marks = 80
sports_quota = False

print(marks >= 75 or sports_quota)
```

### Output

```text
True
```

---

# 3. NOT Operator

## Definition

The **not** operator reverses the Boolean result.

---

## Truth Table

| Condition | Result |
|-----------|--------|
| True | False |
| False | True |

---

## Program

```python
is_logged_in = False

print(not is_logged_in)
```

### Output

```text
True
```

---

# Program 1: Check Voting Eligibility

## Problem Statement

Write a Python program to check whether a person is eligible to vote.

Conditions:

- Age should be at least 18.
- Person should be a citizen.

---

## Program

```python
age = 20
citizen = True

if age >= 18 and citizen:
    print("Eligible to Vote")
```

---

## Output

```text
Eligible to Vote
```

---

# Program 2: Scholarship Eligibility

## Problem Statement

A student is eligible if:

- Marks are at least 75 OR
- The student belongs to the sports quota.

---

## Program

```python
marks = 60
sports_quota = True

if marks >= 75 or sports_quota:
    print("Scholarship Approved")
```

---

## Output

```text
Scholarship Approved
```

---

# Program 3: Login Status

## Program

```python
logged_in = False

if not logged_in:
    print("Please Login")
```

---

## Output

```text
Please Login
```

---

# Real-Time Applications

Logical operators are used in:

- Login Authentication
- ATM Applications
- Banking Systems
- Student Management Systems
- Hospital Software
- Online Shopping Websites
- Employee Management Systems

---

# Advantages

- Combines multiple conditions.
- Simplifies decision making.
- Improves code readability.
- Reduces nested if statements.

---

# Difference between and, or, and not

| Operator | Meaning |
|----------|---------|
| and | Both conditions must be True |
| or | At least one condition must be True |
| not | Reverses the Boolean value |

---

# Common Mistakes

## Using and instead of or

Example

```python
marks = 80
sports = False

print(marks >= 75 and sports)
```

Output

```text
False
```

Reason:

Both conditions are not True.

---

## Forgetting not Reverses the Result

```python
status = True

print(not status)
```

Output

```text
False
```

---

# Interview Questions

## 1. What are Logical Operators?

### Answer

Logical operators combine or modify Boolean expressions and return either `True` or `False`.

---

## 2. How many Logical Operators are available in Python?

### Answer

Three:

- `and`
- `or`
- `not`

---

## 3. When does the and operator return True?

### Answer

Only when both conditions are True.

---

## 4. When does the or operator return True?

### Answer

When at least one condition is True.

---

## 5. What is the purpose of the not operator?

### Answer

It reverses the Boolean value.

---

# Quick Revision

- `and` → Both conditions must be True.
- `or` → At least one condition must be True.
- `not` → Reverses the Boolean result.
- Logical operators return `True` or `False`.
- Used in decision-making and conditional statements.

---

# Summary

In this chapter, you learned:

- What Logical Operators are.
- Types of Logical Operators.
- Truth tables.
- Practical programs.
- Real-world applications.
- Common mistakes.
- Interview questions.
