# Control Constructs in Python

## Learning Objectives

After completing this chapter, you will be able to:

* Understand what control constructs are.
* Explain why control constructs are required.
* Identify different types of control statements.
* Understand the flow of program execution.
* Differentiate between sequential, selection, and iterative execution.
* Build a strong foundation for decision-making and looping concepts.

---

# Introduction

By default, a Python program executes statements **one after another** from top to bottom. This is called **sequential execution**.

However, in real-world applications, programs often need to:

* Make decisions.
* Repeat a set of statements.
* Skip certain statements.
* Execute different blocks of code based on conditions.

To perform these tasks, Python provides **Control Constructs**.

---

# Definition

**Control Constructs** are programming statements that control the flow of execution of a program.

They determine:

* Which statement should execute.
* When a statement should execute.
* How many times a statement should execute.

---

# Why are Control Constructs Required?

Without control constructs, every statement would execute sequentially.

Real-world applications require decision-making and repetition.

### Examples

* ATM Machine

  * If PIN is correct → Allow transaction.
  * Otherwise → Display "Invalid PIN".

* Login System

  * If username and password are correct → Login successful.
  * Otherwise → Access denied.

* Student Result

  * If marks are greater than or equal to the pass mark → Pass.
  * Otherwise → Fail.

---

# Types of Control Constructs

Python provides three major types of control constructs.

```text
Control Constructs

│

├── Sequential Control

├── Selection (Decision Making)

└── Iteration (Looping)
```

---

# 1. Sequential Control

## Definition

Sequential control means statements execute one after another in the order they are written.

### Flow Diagram

```text
Start

↓

Statement 1

↓

Statement 2

↓

Statement 3

↓

Stop
```

### Example

```python
print("Python")

print("Java")

print("C++")
```

### Output

```text
Python
Java
C++
```

---

# 2. Selection (Decision Making)

## Definition

Selection control executes different blocks of code depending on whether a condition is **True** or **False**.

Python provides:

* if
* if-else
* if-elif-else
* Nested if

### Flow Diagram

```text
           Condition

          /        \

      True         False

       |              |

Statement 1     Statement 2

        \        /

           Continue
```

### Real-Time Example

* Online Payment
* Login Authentication
* Student Result
* Eligibility Check

---

# 3. Iteration (Looping)

## Definition

Iteration repeatedly executes a block of code until a condition becomes false.

Python provides:

* while loop
* for loop

### Flow Diagram

```text
Start

↓

Condition

↓

True

↓

Statements

↓

Condition Again

↓

False

↓

Stop
```

### Real-Time Example

* Printing numbers from 1 to 100.
* Displaying employee records.
* Reading data from a file.
* Processing student marks.

---

# Comparison of Control Constructs

| Type       | Purpose                      | Examples          |
| ---------- | ---------------------------- | ----------------- |
| Sequential | Executes statements in order | Normal statements |
| Selection  | Makes decisions              | if, if-else       |
| Iteration  | Repeats statements           | for, while        |

---

# Advantages of Control Constructs

* Makes programs intelligent.
* Reduces code duplication.
* Improves readability.
* Supports decision-making.
* Supports repetition.
* Improves program efficiency.

---

# Real-World Applications

Control constructs are used in almost every software application.

Examples include:

* Banking Systems
* E-Commerce Applications
* Hospital Management Systems
* Student Management Systems
* Online Examination Systems
* Railway Reservation Systems
* Payroll Systems

---

# Summary

In this chapter, you learned:

* What Control Constructs are.
* Why they are required.
* Types of Control Constructs.
* Sequential execution.
* Selection (Decision Making).
* Iteration (Looping).
* Flow diagrams.
* Real-world applications.
