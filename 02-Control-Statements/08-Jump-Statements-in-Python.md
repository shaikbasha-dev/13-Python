# Jump Statements in Python

## Learning Objectives

After completing this chapter, you will be able to:

* Understand Jump Statements in Python.
* Explain why Jump Statements are used.
* Learn the `break`, `continue`, and `pass` statements.
* Understand the execution flow of each jump statement.
* Write programs using Jump Statements.
* Differentiate between `break`, `continue`, and `pass`.

---

# Introduction

During the execution of loops, there are situations where we need to:

* Stop the loop immediately.
* Skip the current iteration.
* Keep a placeholder for future implementation.

Python provides **Jump Statements** to perform these tasks.

The three Jump Statements in Python are:

* `break`
* `continue`
* `pass`

---

# Definition

**Jump Statements** are control statements that alter the normal flow of program execution by terminating a loop, skipping an iteration, or acting as a placeholder.

---

# Types of Jump Statements

```text
Jump Statements

│

├── break

├── continue

└── pass
```

---

# 1. break Statement

## Definition

The **`break`** statement immediately terminates the loop and transfers control to the first statement after the loop.

---

## Why do we use break?

The `break` statement is used when:

* The required result is found.
* An error condition occurs.
* No further iterations are required.

---

## Syntax

```python
for variable in sequence:

    if condition:
        break
```

---

## Flow Diagram

```text
Loop Starts

     │

     ▼

Condition

     │

 True ─────► break

     │

 False

     │

 Continue Loop

     │

 Loop Ends
```

---

## Program 1: break Statement

### Problem Statement

Write a Python program to print numbers from 1 to 10 and stop when the number becomes 6.

---

### Program

```python
# Print numbers using for loop
for number in range(1, 11):

    # Check the condition
    if number == 6:
        break

    # Display number
    print(number)
```

---

### Output

```text
1
2
3
4
5
```

---

### Explanation

* The loop starts from 1.
* Numbers 1 to 5 are printed.
* When the value becomes 6, the `break` statement terminates the loop.

---

# 2. continue Statement

## Definition

The **`continue`** statement skips the current iteration and transfers control to the next iteration of the loop.

---

## Why do we use continue?

The `continue` statement is used when:

* A particular value should be skipped.
* Certain conditions should be ignored.
* Processing should continue with the remaining values.

---

## Syntax

```python
for variable in sequence:

    if condition:
        continue
```

---

## Flow Diagram

```text
Loop Starts

     │

     ▼

Condition

     │

 True

     │

continue

     │

Next Iteration

     │

 False

     │

Execute Statements
```

---

## Program 2: continue Statement

### Problem Statement

Write a Python program to print numbers from 1 to 10 except 6.

---

### Program

```python
# Print numbers using for loop
for number in range(1, 11):

    # Skip number 6
    if number == 6:
        continue

    # Display number
    print(number)
```

---

### Output

```text
1
2
3
4
5
7
8
9
10
```

---

### Explanation

* Numbers 1 to 10 are processed.
* When the value becomes 6, `continue` skips that iteration.
* Remaining numbers are printed.

---

# 3. pass Statement

## Definition

The **`pass`** statement is a null statement.

It does nothing when executed.

It is used as a placeholder where code will be added later.

---

## Why do we use pass?

The `pass` statement is used:

* During program development.
* When writing empty functions.
* When creating empty classes.
* When writing empty loops.

---

## Syntax

```python
if condition:
    pass
```

---

## Program 3: pass Statement

### Problem Statement

Write a Python program demonstrating the use of the `pass` statement.

---

### Program

```python
# Check a condition
number = 10

if number > 5:
    pass

print("Program Executed Successfully")
```

---

### Output

```text
Program Executed Successfully
```

---

### Explanation

* The `pass` statement performs no action.
* Program execution continues normally.

---

# Difference between break, continue, and pass

| Statement  | Purpose                     | Effect                            |
| ---------- | --------------------------- | --------------------------------- |
| `break`    | Terminates the loop         | Exits the loop completely         |
| `continue` | Skips the current iteration | Continues with the next iteration |
| `pass`     | Placeholder statement       | Performs no action                |

---

# Real-Time Applications

### break

* Search Operations
* Menu Exit
* Game Over Condition

### continue

* Skip Invalid Records
* Ignore Empty Input
* Skip Specific Values

### pass

* Empty Functions
* Empty Classes
* Future Code Implementation

---

# Advantages

* Improves control over loop execution.
* Reduces unnecessary processing.
* Simplifies program logic.
* Improves readability.
* Supports structured program development.

---

# Common Mistakes

## Using break outside a loop

❌ Incorrect

```python
break
```

This produces a `SyntaxError`.

---

## Using continue outside a loop

❌ Incorrect

```python
continue
```

This also produces a `SyntaxError`.

---

## Confusing pass with continue

Remember:

* `pass` → Does nothing.
* `continue` → Skips the current iteration.

---

# Interview Questions

## 1. What are Jump Statements?

### Answer

Jump Statements are control statements that alter the normal flow of execution.

---

## 2. What is the purpose of break?

### Answer

The `break` statement immediately terminates the loop.

---

## 3. What is the purpose of continue?

### Answer

The `continue` statement skips the current iteration and continues with the next iteration.

---

## 4. What is the purpose of pass?

### Answer

The `pass` statement is a placeholder that performs no operation.

---

## 5. Can break be used outside a loop?

### Answer

No.

Using `break` outside a loop results in a `SyntaxError`.

---

## 6. Can continue be used outside a loop?

### Answer

No.

Using `continue` outside a loop also results in a `SyntaxError`.

---

## 7. Does pass terminate a loop?

### Answer

No.

The `pass` statement does not affect program execution.

---

# Quick Revision

* `break` terminates the loop.
* `continue` skips the current iteration.
* `pass` performs no action.
* `break` and `continue` are used only inside loops.
* `pass` is commonly used as a placeholder.

---

# Summary

In this chapter, you learned:

* What Jump Statements are.
* The `break` statement.
* The `continue` statement.
* The `pass` statement.
* Syntax and execution flow.
* Practical programs.
* Real-world applications.
* Differences between `break`, `continue`, and `pass`.
* Common mistakes.
* Interview questions.

