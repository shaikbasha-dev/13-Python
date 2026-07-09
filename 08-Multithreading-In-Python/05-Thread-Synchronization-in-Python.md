# Thread Synchronization in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is Thread Synchronization?
5. Why Synchronization is Required?
6. Race Condition
7. Critical Section
8. Lock (Mutex)
9. RLock (Reentrant Lock)
10. Lock vs RLock
11. Internal Working
12. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand Thread Synchronization.
- Learn why synchronization is required.
- Understand Race Conditions.
- Learn about Critical Sections.
- Use Lock objects.
- Use Reentrant Locks (RLock).
- Prevent data inconsistency in multithreaded programs.

---

# Prerequisites

Before learning this chapter, you should know:

- Threads
- Thread Creation
- Thread Life Cycle
- Thread Methods

---

# Introduction

Multiple threads often share the same resources such as:

- Variables
- Objects
- Files
- Database Connections

If two or more threads modify the same data simultaneously,

unexpected results may occur.

To avoid this,

Python provides **Thread Synchronization**.

Synchronization ensures that only one thread accesses a shared resource at a time.

---

# What is Thread Synchronization?

## Definition

Thread Synchronization is the process of controlling access to shared resources so that only one thread can execute a critical section at a time.

---

## Simple Definition

> Thread Synchronization prevents multiple threads from accessing shared resources simultaneously.

---

# Why Synchronization is Required?

Suppose two ATM machines access the same bank account.

Initial Balance

```text
₹10,000
```

Customer A withdraws

```text
₹5,000
```

Customer B also withdraws

```text
₹7,000
```

If both transactions occur simultaneously,

the balance may become incorrect.

Synchronization ensures that one transaction completes before another begins.

---

# Real-World Applications

Synchronization is used in:

- Banking Systems
- Railway Reservation Systems
- Online Shopping
- Hospital Management Systems
- Payment Gateways
- Inventory Systems
- Airline Reservation Systems
- Database Applications

---

# Race Condition

## Definition

A **Race Condition** occurs when multiple threads access and modify shared data simultaneously,

leading to unpredictable or incorrect results.

---

## Example

Two threads increment the same counter.

Expected Result

```text
Counter = 2
```

Actual Result

```text
Counter = 1
```

because both threads read the same value before either writes the updated value.

---

# Critical Section

## Definition

A **Critical Section** is the part of a program where shared resources are accessed or modified.

Only one thread should execute a critical section at a time.

Example

```python
balance = balance - amount
```

If multiple threads execute this statement simultaneously,

data corruption may occur.

---

# Lock (Mutex)

## Definition

A **Lock** (also called a **Mutex**) ensures that only one thread can execute a critical section at a time.

Python provides the

```python
threading.Lock
```

class.

---

## Syntax

```python
lock = threading.Lock()
```

---

## Acquiring a Lock

```python
lock.acquire()
```

The calling thread waits until the lock becomes available.

---

## Releasing a Lock

```python
lock.release()
```

After completing the critical section,

the lock should be released.

---

# Using Lock with Context Manager

Python recommends using a context manager.

```python
with lock:

    # Critical Section
```

The lock is automatically acquired and released,

making the code safer and easier to read.

---

# RLock (Reentrant Lock)

## Definition

An **RLock** (Reentrant Lock) allows the same thread to acquire the same lock multiple times.

This is useful when a function holding a lock calls another function that also needs the same lock.

Python provides

```python
threading.RLock()
```

---

## Syntax

```python
lock = threading.RLock()
```

---

# Lock vs RLock

| Lock | RLock |
|------|--------|
| Can be acquired once by the same thread | Can be acquired multiple times by the same thread |
| Simpler | More flexible |
| Lower overhead | Slightly higher overhead |
| Used for simple synchronization | Used for nested locking |

---

# Internal Working

```text
Thread A

↓

Requests Lock

↓

Lock Available?

↓

Yes

↓

Acquire Lock

↓

Critical Section

↓

Release Lock

↓

Next Waiting Thread

↓

Acquire Lock

↓

Continue Execution
```

---

# Advantages

- Prevents race conditions.
- Protects shared resources.
- Ensures data consistency.
- Improves application reliability.
- Simplifies concurrent programming.

---

# Best Practices

- Lock only the critical section.
- Release locks as quickly as possible.
- Prefer `with lock:` over manual `acquire()` and `release()`.
- Use `RLock` only when reentrant behavior is required.
- Keep critical sections short.

---

# Common Mistakes

## Mistake 1

Forgetting to release a lock.

This can cause other threads to wait indefinitely.

---

## Mistake 2

Locking large portions of code.

This reduces concurrency.

---

## Mistake 3

Using `Lock` when recursive or nested locking is required.

Use `RLock` instead.

---

## Mistake 4

Accessing shared variables without synchronization.

This may lead to race conditions.

---

# Interview Questions

## 1. What is Thread Synchronization?

### Answer

Thread Synchronization is the process of controlling access to shared resources so that only one thread executes the critical section at a time.

---

## 2. What is a Race Condition?

### Answer

A race condition occurs when multiple threads simultaneously access and modify shared data, causing unpredictable results.

---

## 3. What is a Critical Section?

### Answer

A critical section is the part of a program where shared resources are accessed or modified.

---

## 4. What is a Lock?

### Answer

A Lock ensures that only one thread accesses a critical section at a time.

---

## 5. What is an RLock?

### Answer

An RLock allows the same thread to acquire the same lock multiple times.

---

## 6. What is the difference between Lock and RLock?

### Answer

A Lock can be acquired once by the same thread, whereas an RLock can be acquired multiple times by the same thread.

---

## 7. Which approach is recommended for lock management?

### Answer

Using

```python
with lock:
```

because it automatically acquires and releases the lock.

---

# Quick Revision

- Synchronization
- Race Condition
- Critical Section
- Lock
- acquire()
- release()
- `with lock:`
- RLock

---

# Chapter Summary

In this chapter, we learned:

- Thread Synchronization
- Race Condition
- Critical Section
- Lock
- RLock
- Lock vs RLock
- Internal Working
- Best Practices
- Common Mistakes
- Interview Questions
- Quick Revision


# Program 1 – Race Condition without Synchronization

## Problem Statement

Write a Python program to demonstrate a race condition.

---

## Program

```python
import threading

counter = 0

def increment():

    global counter

    for _ in range(100000):

        counter += 1


thread1 = threading.Thread(target=increment)

thread2 = threading.Thread(target=increment)

thread1.start()

thread2.start()

thread1.join()

thread2.join()

print("Counter :", counter)
```

---

## Sample Output

```text
Counter : 186452
```

> **Note:** The output may vary on different executions and systems.

---

## Explanation

Both threads update the shared variable simultaneously.

Since access is not synchronized,

a **Race Condition** may occur.

---

# Program 2 – Synchronization using Lock

## Program

```python
import threading

counter = 0

lock = threading.Lock()

def increment():

    global counter

    for _ in range(100000):

        lock.acquire()

        counter += 1

        lock.release()


thread1 = threading.Thread(target=increment)

thread2 = threading.Thread(target=increment)

thread1.start()

thread2.start()

thread1.join()

thread2.join()

print("Counter :", counter)
```

---

## Sample Output

```text
Counter : 200000
```

---

## Explanation

Only one thread can update the counter at a time,

preventing the race condition.

---

# Program 3 – Using Lock with Context Manager

## Program

```python
import threading

counter = 0

lock = threading.Lock()

def increment():

    global counter

    for _ in range(100000):

        with lock:

            counter += 1


thread1 = threading.Thread(target=increment)

thread2 = threading.Thread(target=increment)

thread1.start()

thread2.start()

thread1.join()

thread2.join()

print("Counter :", counter)
```

---

## Output

```text
Counter : 200000
```

---

## Explanation

The `with` statement automatically acquires and releases the lock.

This is the recommended approach.

---

# Program 4 – Bank Account Synchronization

## Program

```python
import threading

balance = 10000

lock = threading.Lock()

def withdraw(amount):

    global balance

    with lock:

        if balance >= amount:

            balance -= amount

            print("Withdraw :", amount)

        else:

            print("Insufficient Balance")


thread1 = threading.Thread(target=withdraw, args=(4000,))

thread2 = threading.Thread(target=withdraw, args=(7000,))

thread1.start()

thread2.start()

thread1.join()

thread2.join()

print("Remaining Balance :", balance)
```

---

## Sample Output

```text
Withdraw : 4000

Insufficient Balance

Remaining Balance : 6000
```

---

## Explanation

Synchronization ensures that account balance remains consistent.

---

# Program 5 – acquire() and release()

## Program

```python
import threading

lock = threading.Lock()

def task():

    lock.acquire()

    print("Critical Section")

    lock.release()


thread = threading.Thread(target=task)

thread.start()

thread.join()
```

---

## Output

```text
Critical Section
```

---

## Explanation

The lock is acquired before entering the critical section

and released afterward.

---

# Program 6 – RLock Example

## Program

```python
import threading

lock = threading.RLock()

def outer():

    with lock:

        print("Outer Function")

        inner()

def inner():

    with lock:

        print("Inner Function")


thread = threading.Thread(target=outer)

thread.start()

thread.join()
```

---

## Output

```text
Outer Function

Inner Function
```

---

## Explanation

The same thread acquires the same `RLock` multiple times.

This is not possible with a normal `Lock`.

---

# Program 7 – Multiple Threads Waiting for Lock

## Program

```python
import threading
import time

lock = threading.Lock()

def task(name):

    with lock:

        print(name, "Entered")

        time.sleep(2)

        print(name, "Exited")


thread1 = threading.Thread(target=task, args=("Thread-1",))

thread2 = threading.Thread(target=task, args=("Thread-2",))

thread1.start()

thread2.start()

thread1.join()

thread2.join()
```

---

## Sample Output

```text
Thread-1 Entered

Thread-1 Exited

Thread-2 Entered

Thread-2 Exited
```

---

## Explanation

Only one thread enters the critical section at a time.

The second thread waits until the lock is released.

---

# Program 8 – Shared List Synchronization

## Program

```python
import threading

numbers = []

lock = threading.Lock()

def add_number(value):

    with lock:

        numbers.append(value)


thread1 = threading.Thread(target=add_number, args=(10,))

thread2 = threading.Thread(target=add_number, args=(20,))

thread1.start()

thread2.start()

thread1.join()

thread2.join()

print(numbers)
```

---

## Sample Output

```text
[10, 20]
```

---

## Explanation

The shared list is updated safely using synchronization.

---

# Program 9 – Producer Simulation

## Program

```python
import threading

items = []

lock = threading.Lock()

def produce():

    with lock:

        items.append("Laptop")

        print("Item Produced")


thread = threading.Thread(target=produce)

thread.start()

thread.join()

print(items)
```

---

## Output

```text
Item Produced

['Laptop']
```

---

## Explanation

The shared resource is protected using a lock.

---

# Program 10 – Complete Synchronization Example

## Program

```python
import threading

counter = 0

lock = threading.Lock()

def task():

    global counter

    for _ in range(50000):

        with lock:

            counter += 1


thread1 = threading.Thread(target=task)

thread2 = threading.Thread(target=task)

thread1.start()

thread2.start()

thread1.join()

thread2.join()

print("Final Counter :", counter)
```

---

## Output

```text
Final Counter : 100000
```

---

## Explanation

Synchronization guarantees that every increment operation is completed correctly.

---

# Dry Run

```text
Thread A

↓

Requests Lock

↓

Lock Available

↓

Critical Section

↓

Release Lock

↓

Thread B

↓

Acquire Lock

↓

Critical Section

↓

Release Lock

↓

Program Ends
```

---

# Memory Representation

```text
Process

│

├── Thread A

│

├── Thread B

│

└── Shared Variable

        │

        ├── Lock

        │

        └── Critical Section
```

---

# Advantages

- Prevents race conditions.
- Protects shared resources.
- Ensures data consistency.
- Improves reliability.
- Simplifies concurrent programming.

---

# Best Practices

- Lock only the critical section.
- Prefer `with lock:` over `acquire()` and `release()`.
- Always release manually acquired locks.
- Keep critical sections as short as possible.
- Use `RLock` only when nested locking is required.

---

# Common Mistakes

## Mistake 1

Forgetting to release a lock.

This may block other threads indefinitely.

---

## Mistake 2

Locking the entire function instead of only the shared resource.

---

## Mistake 3

Using `Lock` when nested locking is required.

Use `RLock` instead.

---

## Mistake 4

Accessing shared variables without synchronization.

This can lead to race conditions.

---

# Interview Questions

## 1. What is Thread Synchronization?

### Answer

It is the process of controlling access to shared resources so that only one thread executes the critical section at a time.

---

## 2. What is a Race Condition?

### Answer

A race condition occurs when multiple threads modify shared data simultaneously, resulting in unpredictable outcomes.

---

## 3. What is a Critical Section?

### Answer

The part of a program where shared resources are accessed or modified.

---

## 4. What is a Lock?

### Answer

A synchronization mechanism that allows only one thread to enter a critical section at a time.

---

## 5. What is the difference between `Lock` and `RLock`?

### Answer

`Lock` can be acquired only once by the same thread, whereas `RLock` allows the same thread to acquire it multiple times.

---

## 6. Why is `with lock:` recommended?

### Answer

Because it automatically acquires and releases the lock, reducing the chance of programming errors.

---

## 7. Which problem does synchronization solve?

### Answer

Race conditions and data inconsistency.

---

# Practice Programs

1. Demonstrate a race condition.
2. Synchronize a shared counter using `Lock`.
3. Synchronize a bank account withdrawal.
4. Demonstrate `RLock`.
5. Synchronize updates to a shared list.

---

# Quick Revision

- Synchronization → Controls shared resource access.
- Race Condition → Simultaneous unsafe updates.
- Critical Section → Shared code region.
- `Lock` → Mutual exclusion.
- `RLock` → Reentrant lock.
- `acquire()`
- `release()`
- `with lock:`

---

# Chapter Summary

In this chapter, we learned:

- Thread Synchronization
- Race Condition
- Critical Section
- Lock
- RLock
- `acquire()`
- `release()`
- `with lock:`
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
