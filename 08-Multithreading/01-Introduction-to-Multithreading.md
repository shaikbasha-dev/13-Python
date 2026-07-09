# Introduction to Multithreading in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is a Thread?
5. What is Multithreading?
6. Why is Multithreading Required?
7. Process vs Thread
8. Single Threading vs Multithreading
9. Thread Lifecycle
10. Python Threading Module
11. Internal Working
12. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand Threads.
- Understand Multithreading.
- Learn why Multithreading is required.
- Differentiate Process and Thread.
- Compare Single Threading and Multithreading.
- Understand the Thread Lifecycle.
- Learn about Python's `threading` module.

---

# Prerequisites

Before learning this chapter, you should know:

- Functions
- Classes
- Objects
- Exception Handling

---

# Introduction

Modern applications often perform multiple tasks at the same time.

Examples include:

- Downloading files while browsing.
- Playing music while editing documents.
- Processing multiple client requests in a web server.
- Chat applications sending and receiving messages simultaneously.

If all these tasks execute one after another,

the application becomes slow and less responsive.

To perform multiple tasks concurrently,

Python provides **Multithreading**.

---

# What is a Thread?

## Definition

A **Thread** is the smallest unit of execution within a process.

A process may contain one or more threads.

Each thread executes independently,

but threads belonging to the same process share resources such as memory.

---

## Simple Definition

> A Thread is a lightweight execution path inside a process.

---

# What is Multithreading?

## Definition

**Multithreading** is the process of executing multiple threads within a single process.

Multiple threads perform different tasks concurrently,

improving responsiveness and resource utilization.

---

## Simple Definition

> Multithreading allows a program to perform multiple tasks concurrently using multiple threads.

---

# Why is Multithreading Required?

Suppose a web browser needs to:

- Load a web page.
- Download images.
- Play audio.
- Accept user input.

Without multithreading,

each task waits for the previous one to finish.

With multithreading,

all tasks can make progress concurrently,

making the application more responsive.

---

# Real-World Applications

Multithreading is used in:

- Web Browsers
- Chat Applications
- Online Games
- Banking Systems
- Web Servers
- Video Streaming Platforms
- File Download Managers
- IDEs (Integrated Development Environments)

---

# Process vs Thread

| Process | Thread |
|----------|---------|
| Independent program | Smallest execution unit |
| Own memory space | Shares process memory |
| More memory usage | Less memory usage |
| Costly to create | Faster to create |
| Communication is slower | Communication is faster |

---

# Single Threading vs Multithreading

| Single Threading | Multithreading |
|------------------|----------------|
| One execution path | Multiple execution paths |
| Executes one task at a time | Executes multiple tasks concurrently |
| Slower for concurrent workloads | More responsive for concurrent workloads |
| Easier to manage | Requires synchronization in some cases |

---

# Thread Lifecycle

A thread typically passes through the following states:

```text
New

↓

Runnable

↓

Running

↓

Waiting / Blocked

↓

Runnable

↓

Terminated
```

### State Description

- **New** – Thread object is created.
- **Runnable** – Thread is ready to execute.
- **Running** – Thread is executing.
- **Waiting / Blocked** – Thread waits for a resource or event.
- **Terminated** – Thread completes execution.

---

# Python Threading Module

Python provides the built-in

```python
threading
```

module for creating and managing threads.

Example

```python
import threading
```

Commonly used classes and methods include:

| Component | Purpose |
|-----------|---------|
| `Thread` | Creates a thread |
| `start()` | Starts thread execution |
| `run()` | Defines thread task |
| `join()` | Waits for a thread to finish |
| `current_thread()` | Returns the currently executing thread |
| `active_count()` | Returns the number of active threads |

---

# Internal Working

```text
Program Starts

↓

Main Thread Created

↓

Additional Threads Created

↓

Scheduler Allocates CPU Time

↓

Threads Execute Concurrently

↓

Threads Complete

↓

Program Ends
```

---

# Advantages

- Improves responsiveness.
- Better CPU utilization for I/O-bound tasks.
- Allows concurrent task execution.
- Improves user experience.
- Efficient resource sharing.

---

# Limitations

- Requires synchronization when sharing data.
- Debugging can be more difficult.
- Poor thread management may cause deadlocks or race conditions.
- CPU-bound tasks may not speed up due to Python's Global Interpreter Lock (GIL).

> **Note:** In CPython, the **Global Interpreter Lock (GIL)** allows only one thread to execute Python bytecode at a time. Multithreading is therefore most beneficial for **I/O-bound tasks** (such as file operations, network requests, and database access) rather than CPU-intensive computations.

---

# Best Practices

- Create threads only when concurrency is beneficial.
- Keep thread tasks independent whenever possible.
- Synchronize shared resources properly.
- Wait for threads using `join()` when required.
- Avoid creating unnecessary threads.

---

# Common Mistakes

## Mistake 1

Assuming multithreading always improves performance.

For CPU-bound tasks in CPython, the GIL may limit performance gains.

---

## Mistake 2

Sharing data without synchronization.

This can lead to inconsistent results.

---

## Mistake 3

Creating too many threads.

Too many threads increase memory usage and scheduling overhead.

---

# Interview Questions

## 1. What is a Thread?

### Answer

A Thread is the smallest unit of execution within a process.

---

## 2. What is Multithreading?

### Answer

Multithreading is the execution of multiple threads concurrently within a single process.

---

## 3. What is the difference between a Process and a Thread?

### Answer

A process has its own memory space, while threads within the same process share memory and resources.

---

## 4. Which module is used for Multithreading in Python?

### Answer

```python
threading
```

---

## 5. What is the GIL?

### Answer

The Global Interpreter Lock (GIL) is a mechanism in CPython that allows only one thread to execute Python bytecode at a time, making multithreading most effective for I/O-bound tasks.

---

# Quick Revision

- Thread → Smallest execution unit
- Multithreading → Multiple threads in one process
- Threads share memory
- `threading` module → Used for thread management
- `Thread`, `start()`, `join()`
- GIL affects CPU-bound multithreading in CPython

---

# Chapter Summary

In this chapter, we learned:

- Thread
- Multithreading
- Process vs Thread
- Single Threading vs Multithreading
- Thread Lifecycle
- Python `threading` Module
- GIL (Introduction)
- Advantages
- Limitations
- Best Practices
- Interview Questions
- Quick Revision


# Program 1 – Creating a Thread using a Function

## Problem Statement

Write a Python program to create a thread using a target function.

---

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

- A thread is created using the `Thread` class.
- The `target` parameter specifies the function to execute.
- `start()` begins thread execution.
- `join()` waits for the thread to finish.

---

# Program 2 – Creating Multiple Threads

## Program

```python
import threading

def display():

    print("Child Thread")


thread1 = threading.Thread(target=display)

thread2 = threading.Thread(target=display)

thread1.start()

thread2.start()

thread1.join()

thread2.join()
```

---

## Sample Output

```text
Child Thread

Child Thread
```

---

## Explanation

Two independent threads execute the same function concurrently.

The execution order may vary.

---

# Program 3 – Extending the Thread Class

## Program

```python
import threading

class MyThread(threading.Thread):

    def run(self):

        print("Thread Executing")


thread = MyThread()

thread.start()

thread.join()
```

---

## Output

```text
Thread Executing
```

---

## Explanation

Instead of using the `target` parameter,

the `run()` method is overridden.

When `start()` is called,

Python automatically invokes `run()`.

---

# Program 4 – Multiple Threads using Thread Class

## Program

```python
import threading

class MyThread(threading.Thread):

    def run(self):

        print("Executing Child Thread")


thread1 = MyThread()

thread2 = MyThread()

thread1.start()

thread2.start()

thread1.join()

thread2.join()
```

---

## Sample Output

```text
Executing Child Thread

Executing Child Thread
```

---

# Program 5 – current_thread()

## Program

```python
import threading

def display():

    print(threading.current_thread().name)


thread = threading.Thread(target=display)

thread.start()

thread.join()
```

---

## Sample Output

```text
Thread-1
```

---

## Explanation

`current_thread()`

returns the thread currently executing the function.

---

# Program 6 – active_count()

## Program

```python
import threading

print("Active Threads :",

threading.active_count())
```

---

## Sample Output

```text
Active Threads : 1
```

---

## Explanation

`active_count()`

returns the number of currently active threads.

---

# Program 7 – Main Thread

## Program

```python
import threading

print(threading.current_thread().name)
```

---

## Output

```text
MainThread
```

---

## Explanation

Every Python program begins execution in the

```text
MainThread
```

---

# Program 8 – Thread with Arguments

## Program

```python
import threading

def display(name):

    print("Welcome", name)


thread = threading.Thread(

    target=display,

    args=("Rahul",)

)

thread.start()

thread.join()
```

---

## Output

```text
Welcome Rahul
```

---

## Explanation

Arguments are passed to the thread function using the

```python
args
```

parameter.

---

# Program 9 – Multiple Tasks

## Program

```python
import threading

def task1():

    print("Downloading File")


def task2():

    print("Playing Music")


thread1 = threading.Thread(target=task1)

thread2 = threading.Thread(target=task2)

thread1.start()

thread2.start()

thread1.join()

thread2.join()
```

---

## Sample Output

```text
Downloading File

Playing Music
```

---

## Explanation

Two independent tasks execute concurrently.

The output order may differ between executions.

---

# Program 10 – Main Thread Waits using join()

## Program

```python
import threading

def display():

    print("Child Thread Finished")


thread = threading.Thread(target=display)

thread.start()

thread.join()

print("Main Thread Finished")
```

---

## Output

```text
Child Thread Finished

Main Thread Finished
```

---

## Explanation

`join()` blocks the main thread until the child thread completes.

Without `join()`, the order of output is not guaranteed.

---

# Dry Run

```text
Program Starts

↓

Main Thread Created

↓

Child Thread Created

↓

start()

↓

Scheduler Executes Thread

↓

Thread Completes

↓

join()

↓

Program Ends
```

---

# Memory Representation

```text
Process

│

├── Main Thread

│

├── Child Thread 1

│

└── Child Thread 2

↓

Shared Memory

↓

Program Ends
```

---

# Advantages

- Executes multiple tasks concurrently.
- Improves application responsiveness.
- Efficient for I/O-bound operations.
- Shares process resources efficiently.
- Supports background processing.

---

# Best Practices

- Use the `threading` module for thread creation.
- Prefer creating threads using target functions unless subclassing is necessary.
- Always call `join()` when the main thread depends on child threads.
- Minimize shared mutable data between threads.
- Synchronize shared resources when required.

---

# Common Mistakes

## Mistake 1

Calling `run()` directly.

❌ Incorrect

```python
thread.run()
```

This executes the method in the current thread.

✅ Correct

```python
thread.start()
```

`start()` creates a new thread and then calls `run()` internally.

---

## Mistake 2

Forgetting `join()`.

The main thread may finish before child threads complete.

---

## Mistake 3

Assuming thread execution order is fixed.

The operating system scheduler determines execution order.

---

## Mistake 4

Creating unnecessary threads.

Too many threads increase scheduling overhead and memory usage.

---

# Interview Questions

## 1. Which module is used for Multithreading in Python?

### Answer

```python
threading
```

---

## 2. What is the difference between `start()` and `run()`?

### Answer

`start()` creates a new thread and internally invokes `run()`.

Calling `run()` directly executes the method in the current thread without creating a new thread.

---

## 3. Why is `join()` used?

### Answer

`join()` makes the calling thread wait until the specified thread finishes execution.

---

## 4. What does `current_thread()` return?

### Answer

It returns the currently executing thread object.

---

## 5. What does `active_count()` return?

### Answer

It returns the number of currently active threads.

---

## 6. Can multiple threads share memory?

### Answer

Yes.

Threads within the same process share memory and resources.

---

## 7. Does Python guarantee thread execution order?

### Answer

No.

The operating system scheduler determines the execution order.

---

# Practice Programs

1. Create a thread using a target function.
2. Create a thread by extending the `Thread` class.
3. Display the current thread name.
4. Display the number of active threads.
5. Execute multiple tasks using multiple threads.

---

# Quick Revision

- `threading.Thread()` → Creates a thread.
- `start()` → Starts execution.
- `run()` → Contains thread logic.
- `join()` → Waits for thread completion.
- `current_thread()` → Returns current thread.
- `active_count()` → Returns active thread count.
- Threads share process memory.

---

# Chapter Summary

In this chapter, we learned:

- Creating Threads
- Target Functions
- Extending the Thread Class
- `start()`
- `run()`
- `join()`
- `current_thread()`
- `active_count()`
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
