# Daemon Threads in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is a Daemon Thread?
5. What is a Non-Daemon Thread?
6. Why are Daemon Threads Required?
7. Daemon vs Non-Daemon Threads
8. Creating Daemon Threads
9. Checking Daemon Status
10. Changing Daemon Status
11. Internal Working
12. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand Daemon Threads.
- Understand Non-Daemon Threads.
- Learn when daemon threads should be used.
- Create daemon threads.
- Check daemon thread status.
- Change daemon status.
- Compare daemon and non-daemon threads.
- Understand daemon thread execution.

---

# Prerequisites

Before learning this chapter, you should know:

- Multithreading
- Thread Creation
- Thread Life Cycle
- Thread Methods
- Thread Synchronization

---

# Introduction

Not every thread performs an important task.

Some threads work in the background and provide supporting services.

Examples include:

- Monitoring system resources
- Cleaning temporary files
- Sending heartbeat signals
- Logging application activity
- Background cache cleanup

These background threads should automatically stop when the main application exits.

Python provides **Daemon Threads** for this purpose.

---

# What is a Daemon Thread?

## Definition

A **Daemon Thread** is a background thread that automatically terminates when all non-daemon threads have finished execution.

Daemon threads support the main application,

but they do not prevent the program from exiting.

---

## Simple Definition

> A Daemon Thread is a background thread that automatically stops when the main program finishes.

---

# What is a Non-Daemon Thread?

## Definition

A **Non-Daemon Thread** is a normal thread that keeps the Python program running until it completes its execution.

By default,

every new thread created in Python is a **non-daemon thread** unless specified otherwise.

---

## Simple Definition

> A Non-Daemon Thread is a regular thread that must complete before the program exits.

---

# Why are Daemon Threads Required?

Suppose an application creates a background thread that continuously monitors system memory.

When the user closes the application,

there is no need for the monitoring thread to continue running.

Daemon threads automatically terminate,

preventing unnecessary resource usage.

---

# Real-World Applications

Daemon threads are commonly used in:

- Background Logging
- Cache Cleanup
- Monitoring CPU Usage
- Memory Monitoring
- Heartbeat Services
- Background File Synchronization
- Periodic Health Checks
- Server Maintenance Tasks

---

# Daemon vs Non-Daemon Threads

| Daemon Thread | Non-Daemon Thread |
|---------------|-------------------|
| Background thread | Regular thread |
| Automatically terminates | Must complete execution |
| Does not keep program alive | Keeps program alive |
| Used for support tasks | Used for main application tasks |
| Suitable for monitoring | Suitable for business logic |

---

# Creating a Daemon Thread

A daemon thread is created by setting the

```python
daemon
```

property to

```python
True
```

before calling

```python
start()
```

Example

```python
thread.daemon = True
```

or

```python
thread = threading.Thread(

    target=task,

    daemon=True

)
```

---

# Checking Daemon Status

The daemon status can be checked using

```python
thread.daemon
```

Example

```python
print(thread.daemon)
```

Output

```text
True
```

or

```text
False
```

---

# Changing Daemon Status

Daemon status must be changed **before**

calling

```python
start()
```

Example

```python
thread.daemon = True

thread.start()
```

Changing the daemon property after the thread starts raises a

```python
RuntimeError
```

---

# Internal Working

```text
Program Starts

↓

Main Thread

↓

Create Child Thread

↓

Daemon = True

↓

start()

↓

Background Task

↓

Main Thread Ends

↓

Daemon Thread Automatically Stops

↓

Program Ends
```

---

# Advantages

- Automatically terminates.
- Suitable for background services.
- Reduces manual thread management.
- Saves system resources.
- Improves application design.

---

# Best Practices

- Use daemon threads only for background tasks.
- Never store important business logic in daemon threads.
- Set the daemon property before calling `start()`.
- Use non-daemon threads for tasks that must complete.
- Keep daemon tasks lightweight.

---

# Common Mistakes

## Mistake 1

Changing daemon status after calling

```python
start()
```

This raises a

```python
RuntimeError
```

---

## Mistake 2

Using daemon threads for important business operations.

Daemon threads may terminate before completing their work.

---

## Mistake 3

Assuming daemon threads execute forever.

They stop automatically when all non-daemon threads finish.

---

## Mistake 4

Confusing daemon threads with background processes.

Daemon threads belong to the current Python process.

---

# Interview Questions

## 1. What is a Daemon Thread?

### Answer

A daemon thread is a background thread that automatically terminates when all non-daemon threads finish execution.

---

## 2. What is a Non-Daemon Thread?

### Answer

A normal thread that keeps the program running until it completes.

---

## 3. Are threads daemon by default?

### Answer

No.

Threads are non-daemon by default.

---

## 4. When should daemon threads be used?

### Answer

For background tasks such as logging, monitoring, and cleanup operations.

---

## 5. Can daemon status be changed after starting a thread?

### Answer

No.

It must be changed before calling `start()`.

---

## 6. What happens to daemon threads when the main program exits?

### Answer

They are automatically terminated.

---

## 7. Should important business logic run inside daemon threads?

### Answer

No.

Business-critical tasks should use non-daemon threads.

---

# Quick Revision

- Daemon Thread
- Non-Daemon Thread
- `daemon=True`
- `thread.daemon`
- Background Services
- Automatic Termination

---

# Chapter Summary

In this chapter, we learned:

- Daemon Threads
- Non-Daemon Threads
- Daemon Property
- Creating Daemon Threads
- Checking Daemon Status
- Daemon vs Non-Daemon Threads
- Internal Working
- Best Practices
- Common Mistakes
- Interview Questions
- Quick Revision


# Program 1 – Creating a Daemon Thread

## Problem Statement

Write a Python program to create a daemon thread.

---

## Program

```python
import threading
import time

def background_task():

    while True:

        print("Daemon Thread Running")

        time.sleep(1)


thread = threading.Thread(

    target=background_task,

    daemon=True

)

thread.start()

time.sleep(3)

print("Main Thread Finished")
```

---

## Sample Output

```text
Daemon Thread Running

Daemon Thread Running

Daemon Thread Running

Main Thread Finished
```

---

## Explanation

The daemon thread executes in the background.

When the main thread finishes,

Python automatically terminates the daemon thread.

---

# Program 2 – Creating a Non-Daemon Thread

## Program

```python
import threading
import time

def task():

    for i in range(3):

        print("Working...", i)

        time.sleep(1)


thread = threading.Thread(target=task)

thread.start()

thread.join()

print("Main Thread Finished")
```

---

## Output

```text
Working... 0

Working... 1

Working... 2

Main Thread Finished
```

---

## Explanation

A non-daemon thread completes its task before the program exits.

---

# Program 3 – Checking Daemon Status

## Program

```python
import threading

def display():

    pass


thread = threading.Thread(target=display)

print(thread.daemon)
```

---

## Output

```text
False
```

---

## Explanation

Threads are non-daemon by default.

---

# Program 4 – Setting Daemon Property

## Program

```python
import threading

def display():

    print("Background Task")


thread = threading.Thread(target=display)

thread.daemon = True

print(thread.daemon)
```

---

## Output

```text
True
```

---

## Explanation

The daemon property is changed before calling `start()`.

---

# Program 5 – Daemon Thread with Background Monitoring

## Program

```python
import threading
import time

def monitor():

    while True:

        print("Monitoring System...")

        time.sleep(2)


thread = threading.Thread(

    target=monitor,

    daemon=True

)

thread.start()

time.sleep(5)

print("Application Closed")
```

---

## Sample Output

```text
Monitoring System...

Monitoring System...

Monitoring System...

Application Closed
```

---

## Explanation

The monitoring thread runs in the background.

It automatically stops when the application exits.

---

# Program 6 – Attempting to Change Daemon Status After start()

## Program

```python
import threading

def display():

    print("Running")


thread = threading.Thread(target=display)

thread.start()

thread.daemon = True
```

---

## Output

```text
RuntimeError:
cannot set daemon status of active thread
```

---

## Explanation

The daemon property must be set **before** calling `start()`.

---

# Program 7 – Daemon vs Non-Daemon Threads

## Program

```python
import threading

def task():

    print("Thread Executing")


daemon_thread = threading.Thread(

    target=task,

    daemon=True

)

normal_thread = threading.Thread(

    target=task

)

print("Daemon :", daemon_thread.daemon)

print("Non-Daemon :", normal_thread.daemon)
```

---

## Output

```text
Daemon : True

Non-Daemon : False
```

---

## Explanation

The daemon thread has its `daemon` property set to `True`.

The normal thread remains a non-daemon thread.

---

# Program 8 – Multiple Daemon Threads

## Program

```python
import threading
import time

def task(name):

    while True:

        print(name)

        time.sleep(1)


thread1 = threading.Thread(

    target=task,

    args=("Daemon-1",),

    daemon=True

)

thread2 = threading.Thread(

    target=task,

    args=("Daemon-2",),

    daemon=True

)

thread1.start()

thread2.start()

time.sleep(3)

print("Program Finished")
```

---

## Sample Output

```text
Daemon-1

Daemon-2

Daemon-1

Daemon-2

Program Finished
```

---

## Explanation

Both daemon threads terminate automatically when the main program exits.

---

# Program 9 – Background Logger

## Program

```python
import threading
import time

def logger():

    while True:

        print("Writing Log...")

        time.sleep(2)


thread = threading.Thread(

    target=logger,

    daemon=True

)

thread.start()

time.sleep(5)

print("Main Program Closed")
```

---

## Sample Output

```text
Writing Log...

Writing Log...

Writing Log...

Main Program Closed
```

---

## Explanation

Background logging is a common use case for daemon threads.

---

# Program 10 – Complete Daemon Thread Example

## Program

```python
import threading
import time

def background():

    while True:

        print("Background Service Running")

        time.sleep(1)


thread = threading.Thread(

    target=background,

    daemon=True

)

thread.start()

print("Main Thread Working")

time.sleep(4)

print("Main Thread Completed")
```

---

## Sample Output

```text
Main Thread Working

Background Service Running

Background Service Running

Background Service Running

Background Service Running

Main Thread Completed
```

---

## Explanation

The daemon thread runs alongside the main thread.

When the main thread finishes,

the daemon thread automatically terminates.

---

# Dry Run

```text
Program Starts

↓

Main Thread

↓

Daemon Thread Created

↓

daemon=True

↓

start()

↓

Background Task Executes

↓

Main Thread Ends

↓

Daemon Thread Stops

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

└── Daemon Thread

      │

      ├── Background Task

      ├── Monitoring

      └── Auto Terminates
```

---

# Advantages

- Suitable for background services.
- Automatically terminates with the program.
- Simplifies resource management.
- Reduces manual cleanup.
- Improves application design.

---

# Best Practices

- Use daemon threads only for background tasks.
- Set the daemon property before calling `start()`.
- Keep daemon tasks lightweight.
- Do not use daemon threads for critical business operations.
- Use non-daemon threads when task completion is mandatory.

---

# Common Mistakes

## Mistake 1

Changing the daemon property after `start()`.

This raises a `RuntimeError`.

---

## Mistake 2

Using daemon threads for important data processing.

Daemon threads may terminate before completing their work.

---

## Mistake 3

Assuming daemon threads continue after the program exits.

They automatically stop when all non-daemon threads finish.

---

## Mistake 4

Forgetting that threads are non-daemon by default.

Explicitly set `daemon=True` when background execution is required.

---

# Interview Questions

## 1. What is a daemon thread?

### Answer

A daemon thread is a background thread that automatically terminates when all non-daemon threads finish execution.

---

## 2. Are threads daemon by default?

### Answer

No.

Threads are non-daemon by default.

---

## 3. How do you create a daemon thread?

### Answer

By setting `daemon=True` when creating the thread or by assigning `thread.daemon = True` before calling `start()`.

---

## 4. Can daemon status be changed after starting a thread?

### Answer

No.

It must be changed before calling `start()`.

---

## 5. When should daemon threads be used?

### Answer

For background tasks such as monitoring, logging, cache cleanup, and maintenance services.

---

## 6. What happens to daemon threads when the main program exits?

### Answer

They are automatically terminated.

---

## 7. Should daemon threads perform business-critical operations?

### Answer

No.

Critical operations should use non-daemon threads to ensure they complete successfully.

---

# Practice Programs

1. Create a daemon thread.
2. Create a non-daemon thread.
3. Display daemon status.
4. Create a background logger using a daemon thread.
5. Compare daemon and non-daemon threads.

---

# Quick Revision

- Daemon Thread → Background thread.
- Non-Daemon Thread → Regular thread.
- `daemon=True`
- `thread.daemon`
- Automatic termination.
- Background services.
- Set daemon before `start()`.

---

# Chapter Summary

In this chapter, we learned:

- Daemon Threads
- Non-Daemon Threads
- Daemon Property
- Background Services
- Automatic Termination
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
