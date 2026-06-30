# Thread Life Cycle in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is a Thread Life Cycle?
5. Thread States
6. State Transitions
7. Thread Scheduler
8. Context Switching
9. Internal Working
10. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the Thread Life Cycle.
- Learn different thread states.
- Understand state transitions.
- Learn how the Thread Scheduler works.
- Understand Context Switching.
- Learn the complete execution flow of a thread.

---

# Prerequisites

Before learning this chapter, you should know:

- Threads
- Multithreading
- Thread Creation
- start()
- run()
- join()

---

# Introduction

A thread does not start executing immediately after it is created.

Instead,

it passes through several states before completing execution.

These states collectively form the **Thread Life Cycle**.

Understanding the Thread Life Cycle helps developers write efficient multithreaded programs and debug thread-related issues.

---

# What is a Thread Life Cycle?

## Definition

The **Thread Life Cycle** is the sequence of states through which a thread passes from its creation until its termination.

---

## Simple Definition

> The Thread Life Cycle represents the journey of a thread from creation to completion.

---

# Thread States

A thread generally passes through the following states.

```text
New

↓

Runnable

↓

Running

↓

Blocked / Waiting

↓

Runnable

↓

Running

↓

Terminated
```

---

# State 1 – New

## Definition

A thread is in the **New** state immediately after the thread object is created.

Example

```python
thread = threading.Thread(target=display)
```

At this stage,

the thread exists,

but it has **not started execution**.

---

# State 2 – Runnable

## Definition

After calling

```python
thread.start()
```

the thread enters the **Runnable** state.

The thread is ready to execute,

but it is waiting for CPU time from the operating system scheduler.

---

# State 3 – Running

## Definition

When the operating system scheduler assigns CPU time,

the thread moves to the **Running** state.

Its task begins executing.

Example

```python
def display():

    print("Running")
```

---

# State 4 – Blocked / Waiting

## Definition

A running thread enters the **Blocked** or **Waiting** state when it cannot continue immediately.

Examples include:

- Waiting for I/O operations.
- Waiting for a lock.
- Waiting for another thread using `join()`.
- Sleeping using `time.sleep()`.

---

# State 5 – Runnable Again

After the required resource becomes available,

the thread moves back to the **Runnable** state,

waiting once again for CPU allocation.

---

# State 6 – Terminated

A thread enters the **Terminated** state after completing its task.

Once terminated,

the thread cannot be restarted.

Attempting to call

```python
start()
```

again raises an error.

---

# Thread State Diagram

```text
New

↓

Runnable

↓

Running

↓

Blocked / Waiting

↓

Runnable

↓

Running

↓

Terminated
```

---

# State Transitions

| Current State | Event | Next State |
|---------------|-------|------------|
| New | `start()` | Runnable |
| Runnable | CPU Allocated | Running |
| Running | Waiting for Resource | Blocked |
| Blocked | Resource Available | Runnable |
| Running | Task Completed | Terminated |

---

# Thread Scheduler

The **Thread Scheduler** is responsible for deciding which runnable thread gets CPU time.

The scheduler is controlled by the operating system.

Python programmers do not directly control thread scheduling.

Therefore,

the execution order of multiple threads is generally **not predictable**.

---

# Context Switching

When multiple threads share a CPU,

the operating system rapidly switches execution between them.

This process is called **Context Switching**.

Example

```text
Thread A

↓

Thread B

↓

Thread C

↓

Thread A

↓

Thread B
```

Rapid switching creates the appearance that threads are executing simultaneously.

---

# Internal Working

```text
Thread Object Created

↓

New State

↓

start()

↓

Runnable

↓

CPU Assigned

↓

Running

↓

Waiting?

↓

Yes

↓

Blocked

↓

Resource Available

↓

Runnable

↓

Running

↓

Task Finished

↓

Terminated
```

---

# Advantages

- Helps understand thread execution.
- Simplifies debugging.
- Makes synchronization easier.
- Improves understanding of scheduler behavior.
- Helps design efficient multithreaded applications.

---

# Best Practices

- Start a thread only once.
- Use `join()` when thread completion is required.
- Avoid unnecessary waiting.
- Keep thread tasks short and efficient.
- Synchronize shared resources properly.

---

# Common Mistakes

## Mistake 1

Trying to restart a terminated thread.

❌ Incorrect

```python
thread.start()

thread.start()
```

A thread can be started only once.

---

## Mistake 2

Assuming a thread starts immediately after calling `start()`.

The thread first enters the **Runnable** state and waits for CPU scheduling.

---

## Mistake 3

Assuming execution order is fixed.

The operating system scheduler determines the execution order.

---

## Mistake 4

Ignoring blocked states while designing applications.

Waiting for resources can affect responsiveness.

---

# Interview Questions

## 1. What is the Thread Life Cycle?

### Answer

It is the sequence of states through which a thread passes from creation until termination.

---

## 2. What is the first state of a thread?

### Answer

**New**.

---

## 3. Which method moves a thread from New to Runnable?

### Answer

```python
start()
```

---

## 4. Which component decides thread execution?

### Answer

The operating system's **Thread Scheduler**.

---

## 5. Can a terminated thread be restarted?

### Answer

No.

A thread can be started only once.

---

## 6. What is Context Switching?

### Answer

Context Switching is the process of rapidly switching CPU execution between multiple threads.

---

## 7. Why is the execution order of threads unpredictable?

### Answer

Because thread scheduling is controlled by the operating system.

---

# Quick Revision

- New
- Runnable
- Running
- Blocked / Waiting
- Runnable
- Running
- Terminated
- `start()`
- Scheduler
- Context Switching

---

# Chapter Summary

In this chapter, you learned:

- Thread Life Cycle
- Thread States
- State Transitions
- Thread Scheduler
- Context Switching
- Internal Working
- Advantages
- Best Practices
- Common Mistakes
- Interview Questions
- Quick Revision


# Program 1 – Thread Creation (New State)

## Problem Statement

Write a Python program to demonstrate the New state of a thread.

---

## Program

```python
import threading

def display():

    print("Child Thread")


thread = threading.Thread(target=display)

print("Thread Created")
```

---

## Output

```text
Thread Created
```

---

## Explanation

The thread object has been created,

but `start()` has not been called.

Therefore,

the thread remains in the **New** state.

---

# Program 2 – Runnable State

## Program

```python
import threading

def display():

    print("Thread is Ready to Execute")


thread = threading.Thread(target=display)

thread.start()

thread.join()
```

---

## Output

```text
Thread is Ready to Execute
```

---

## Explanation

After calling

```python
start()
```

the thread enters the **Runnable** state.

The operating system scheduler later selects it for execution.

---

# Program 3 – Running State

## Program

```python
import threading

def display():

    print("Thread is Running")


thread = threading.Thread(target=display)

thread.start()

thread.join()
```

---

## Output

```text
Thread is Running
```

---

## Explanation

When CPU time is assigned,

the thread enters the **Running** state and executes its task.

---

# Program 4 – Waiting State using sleep()

## Program

```python
import threading
import time

def display():

    print("Running")

    time.sleep(3)

    print("Resumed")


thread = threading.Thread(target=display)

thread.start()

thread.join()
```

---

## Sample Output

```text
Running

Resumed
```

---

## Explanation

During

```python
time.sleep(3)
```

the thread enters the **Waiting** state.

After three seconds,

it becomes runnable again.

---

# Program 5 – Waiting using join()

## Program

```python
import threading
import time

def child():

    print("Child Started")

    time.sleep(2)

    print("Child Finished")


thread = threading.Thread(target=child)

thread.start()

thread.join()

print("Main Thread Finished")
```

---

## Output

```text
Child Started

Child Finished

Main Thread Finished
```

---

## Explanation

The main thread waits until the child thread completes.

---

# Program 6 – Multiple Runnable Threads

## Program

```python
import threading

def task():

    print("Executing")


thread1 = threading.Thread(target=task)

thread2 = threading.Thread(target=task)

thread3 = threading.Thread(target=task)

thread1.start()

thread2.start()

thread3.start()

thread1.join()

thread2.join()

thread3.join()
```

---

## Sample Output

```text
Executing

Executing

Executing
```

---

## Explanation

All three threads enter the Runnable state.

The scheduler decides which thread executes first.

---

# Program 7 – Demonstrating Context Switching

## Program

```python
import threading
import time

def task(name):

    for i in range(3):

        print(name, i)

        time.sleep(1)


thread1 = threading.Thread(target=task, args=("A",))

thread2 = threading.Thread(target=task, args=("B",))

thread1.start()

thread2.start()

thread1.join()

thread2.join()
```

---

## Sample Output

```text
A 0

B 0

A 1

B 1

A 2

B 2
```

---

## Explanation

The operating system rapidly switches between threads.

This process is called **Context Switching**.

The exact output order may vary.

---

# Program 8 – Thread Termination

## Program

```python
import threading

def task():

    print("Task Completed")


thread = threading.Thread(target=task)

thread.start()

thread.join()

print("Thread Terminated")
```

---

## Output

```text
Task Completed

Thread Terminated
```

---

## Explanation

After completing its task,

the thread enters the **Terminated** state.

---

# Program 9 – Starting a Thread Twice

## Program

```python
import threading

def task():

    print("Executing")


thread = threading.Thread(target=task)

thread.start()

thread.join()

thread.start()
```

---

## Output

```text
RuntimeError:
threads can only be started once
```

---

## Explanation

A thread can be started only once.

After termination,

it cannot be restarted.

---

# Program 10 – Complete Thread Life Cycle

## Program

```python
import threading
import time

def task():

    print("Running")

    time.sleep(2)

    print("Completed")


thread = threading.Thread(target=task)

print("New State")

thread.start()

thread.join()

print("Terminated")
```

---

## Sample Output

```text
New State

Running

Completed

Terminated
```

---

## Explanation

The thread progresses through the following states:

```text
New

↓

Runnable

↓

Running

↓

Waiting

↓

Running

↓

Terminated
```

---

# Dry Run

```text
Thread Object Created

↓

New

↓

start()

↓

Runnable

↓

Scheduler

↓

Running

↓

sleep()

↓

Waiting

↓

Runnable

↓

Running

↓

Completed

↓

Terminated
```

---

# Memory Representation

```text
Process

│

├── Main Thread

│

└── Child Thread

      │

      ├── New

      ├── Runnable

      ├── Running

      ├── Waiting

      └── Terminated
```

---

# Advantages

- Helps understand thread execution.
- Makes debugging easier.
- Improves synchronization design.
- Explains scheduler behavior.
- Useful for interview preparation.

---

# Best Practices

- Start each thread only once.
- Use `join()` whenever synchronization is required.
- Avoid long blocking operations inside threads.
- Minimize unnecessary waiting.
- Design thread tasks to be independent.

---

# Common Mistakes

## Mistake 1

Restarting a completed thread.

❌ Incorrect

```python
thread.start()

thread.start()
```

---

## Mistake 2

Assuming `start()` immediately executes the thread.

The thread first enters the Runnable state and waits for the scheduler.

---

## Mistake 3

Expecting a fixed execution order.

Thread scheduling depends on the operating system.

---

## Mistake 4

Ignoring waiting states.

Operations such as `sleep()` and `join()` temporarily block thread execution.

---

# Interview Questions

## 1. What are the different thread states?

### Answer

- New
- Runnable
- Running
- Blocked / Waiting
- Terminated

---

## 2. Which method moves a thread from New to Runnable?

### Answer

```python
start()
```

---

## 3. Which component decides thread execution?

### Answer

The operating system's Thread Scheduler.

---

## 4. What is Context Switching?

### Answer

Context Switching is the process of switching CPU execution between multiple threads.

---

## 5. Can a terminated thread be restarted?

### Answer

No.

A thread can only be started once.

---

## 6. Which function commonly moves a thread to the Waiting state?

### Answer

```python
time.sleep()
```

---

## 7. What is the purpose of `join()`?

### Answer

It makes one thread wait until another thread completes execution.

---

# Practice Programs

1. Demonstrate all thread lifecycle states.
2. Create multiple runnable threads.
3. Demonstrate `sleep()`.
4. Demonstrate `join()`.
5. Show that restarting a thread raises an error.

---

# Quick Revision

- New
- Runnable
- Running
- Waiting
- Terminated
- Scheduler
- Context Switching
- `sleep()`
- `join()`

---

# Chapter Summary

In this chapter, we learned:

- Thread Life Cycle
- Thread States
- Scheduler
- Context Switching
- Waiting State
- Thread Termination
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
