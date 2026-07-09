# Thread Methods in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. Common Thread Methods
5. start()
6. run()
7. join()
8. is_alive()
9. name Attribute
10. current_thread()
11. active_count()
12. enumerate()
13. daemon Property
14. Internal Working
15. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand commonly used thread methods.
- Learn the purpose of `start()`.
- Learn the purpose of `run()`.
- Learn how `join()` works.
- Check whether a thread is alive.
- Access and modify thread names.
- Get the current thread.
- Count active threads.
- List active threads.
- Understand daemon threads.

---

# Prerequisites

Before learning this chapter, you should know:

- Multithreading
- Thread Creation
- Thread Life Cycle
- Functions
- Classes

---

# Introduction

Python provides several built-in methods to create, start, monitor, and manage threads.

These methods are available in the

```python
threading
```

module.

Understanding these methods is essential for writing efficient multithreaded applications.

---

# Common Thread Methods

| Method / Attribute | Purpose |
|--------------------|---------|
| `start()` | Starts a new thread |
| `run()` | Contains the thread's task |
| `join()` | Waits for thread completion |
| `is_alive()` | Checks whether a thread is running |
| `name` | Gets or sets the thread name |
| `current_thread()` | Returns the current thread |
| `active_count()` | Returns the number of active threads |
| `enumerate()` | Returns a list of active thread objects |
| `daemon` | Gets or sets daemon thread status |

---

# start()

## Definition

The

```python
start()
```

method starts a new thread.

After calling

```python
start()
```

Python creates a new thread and internally calls the

```python
run()
```

method.

---

## Syntax

```python
thread.start()
```

---

# run()

## Definition

The

```python
run()
```

method contains the code executed by the child thread.

Normally,

developers override this method when extending the `Thread` class.

---

## Syntax

```python
class MyThread(threading.Thread):

    def run(self):

        print("Running")
```

---

# join()

## Definition

The

```python
join()
```

method pauses the calling thread until the specified thread completes execution.

---

## Syntax

```python
thread.join()
```

---

# is_alive()

## Definition

The

```python
is_alive()
```

method returns

- `True` if the thread is still running.
- `False` if the thread has completed.

---

## Syntax

```python
thread.is_alive()
```

---

# name Attribute

Each thread has a name.

It can be read or modified.

Example

```python
thread.name = "DownloadThread"
```

---

# current_thread()

## Definition

Returns the thread object currently executing.

---

## Syntax

```python
threading.current_thread()
```

---

# active_count()

## Definition

Returns the number of currently active threads.

---

## Syntax

```python
threading.active_count()
```

---

# enumerate()

## Definition

Returns a list containing all currently active thread objects.

---

## Syntax

```python
threading.enumerate()
```

---

# daemon Property

A daemon thread runs in the background.

When all non-daemon threads finish,

Python automatically terminates daemon threads.

Example

```python
thread.daemon = True
```

---

# Internal Working

```text
Create Thread

↓

start()

↓

run()

↓

Thread Running

↓

join() (optional)

↓

Thread Completed

↓

is_alive() → False
```

---

# Advantages

- Easy thread management.
- Built-in monitoring support.
- Synchronization using `join()`.
- Simple thread identification.
- Background processing with daemon threads.

---

# Best Practices

- Always use `start()` instead of calling `run()` directly.
- Use `join()` only when synchronization is required.
- Assign meaningful thread names.
- Use daemon threads only for background tasks.
- Check thread status using `is_alive()` when required.

---

# Common Mistakes

## Mistake 1

Calling

```python
run()
```

directly.

This does not create a new thread.

---

## Mistake 2

Restarting a completed thread.

A thread can only be started once.

---

## Mistake 3

Assuming daemon threads always finish their work.

Daemon threads may terminate immediately when all non-daemon threads exit.

---

## Mistake 4

Using `join()` unnecessarily.

Unnecessary joins reduce concurrency.

---

# Interview Questions

## 1. Which method starts a thread?

### Answer

```python
start()
```

---

## 2. What is the purpose of `run()`?

### Answer

It contains the code executed by the child thread.

---

## 3. What does `join()` do?

### Answer

It waits until another thread finishes execution.

---

## 4. What does `is_alive()` return?

### Answer

It returns `True` if the thread is still running; otherwise, `False`.

---

## 5. Which method returns the current thread?

### Answer

```python
threading.current_thread()
```

---

## 6. Which method returns the number of active threads?

### Answer

```python
threading.active_count()
```

---

## 7. What is a daemon thread?

### Answer

A daemon thread is a background thread that automatically terminates when all non-daemon threads finish.

---

# Quick Revision

- `start()`
- `run()`
- `join()`
- `is_alive()`
- `name`
- `current_thread()`
- `active_count()`
- `enumerate()`
- `daemon`

---

# Chapter Summary

In this chapter, we learned:

- Thread Methods
- start()
- run()
- join()
- is_alive()
- name
- current_thread()
- active_count()
- enumerate()
- daemon threads
- Best Practices
- Interview Questions
- Quick Revision


# Program 1 – start() Method

## Problem Statement

Write a Python program to demonstrate the `start()` method.

---

## Program

```python
import threading

def display():

    print("Child Thread Started")


thread = threading.Thread(target=display)

thread.start()

thread.join()
```

---

## Output

```text
Child Thread Started
```

---

## Explanation

The `start()` method creates a new thread.

Internally, Python invokes the `run()` method in the new thread.

---

# Program 2 – run() Method

## Program

```python
import threading

class MyThread(threading.Thread):

    def run(self):

        print("Inside run() Method")


thread = MyThread()

thread.start()

thread.join()
```

---

## Output

```text
Inside run() Method
```

---

## Explanation

The `run()` method contains the task executed by the child thread.

It should not be called directly.

---

# Program 3 – join() Method

## Program

```python
import threading

def display():

    print("Child Thread Completed")


thread = threading.Thread(target=display)

thread.start()

thread.join()

print("Main Thread Completed")
```

---

## Output

```text
Child Thread Completed

Main Thread Completed
```

---

## Explanation

`join()` pauses the main thread until the child thread completes execution.

---

# Program 4 – is_alive() Method

## Program

```python
import threading
import time

def display():

    time.sleep(2)


thread = threading.Thread(target=display)

thread.start()

print(thread.is_alive())

thread.join()

print(thread.is_alive())
```

---

## Sample Output

```text
True

False
```

---

## Explanation

While the thread is executing,

`is_alive()` returns

```python
True
```

After completion,

it returns

```python
False
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

returns the currently executing thread.

---

# Program 6 – active_count()

## Program

```python
import threading

print(

    "Active Threads :",

    threading.active_count()

)
```

---

## Sample Output

```text
Active Threads : 1
```

---

## Explanation

Returns the total number of active threads.

---

# Program 7 – enumerate()

## Program

```python
import threading

print(

    threading.enumerate()

)
```

---

## Sample Output

```text
[<_MainThread(MainThread, started ...)>]
```

---

## Explanation

`enumerate()`

returns a list containing all active thread objects.

---

# Program 8 – Thread Name

## Program

```python
import threading

def display():

    print(

        threading.current_thread().name

    )


thread = threading.Thread(

    target=display,

    name="DownloadThread"

)

thread.start()

thread.join()
```

---

## Output

```text
DownloadThread
```

---

## Explanation

The thread name can be assigned using the

```python
name
```

parameter.

Meaningful names simplify debugging.

---

# Program 9 – Daemon Thread

## Program

```python
import threading
import time

def task():

    while True:

        print("Running...")

        time.sleep(1)


thread = threading.Thread(

    target=task,

    daemon=True

)

thread.start()

time.sleep(3)

print("Main Thread Finished")
```

---

## Sample Output

```text
Running...

Running...

Running...

Main Thread Finished
```

---

## Explanation

The child thread is a daemon thread.

When the main thread exits,

the daemon thread is automatically terminated.

---

# Program 10 – Combining Multiple Thread Methods

## Program

```python
import threading

def display():

    print(

        "Current Thread :",

        threading.current_thread().name

    )


thread = threading.Thread(

    target=display,

    name="WorkerThread"

)

print(

    "Before Start :",

    thread.is_alive()

)

thread.start()

thread.join()

print(

    "After Completion :",

    thread.is_alive()

)
```

---

## Sample Output

```text
Before Start : False

Current Thread : WorkerThread

After Completion : False
```

---

## Explanation

This example demonstrates:

- Thread Naming
- `start()`
- `current_thread()`
- `join()`
- `is_alive()`

---

# Dry Run

```text
Program Starts

↓

Thread Object Created

↓

start()

↓

run()

↓

Thread Executes

↓

join()

↓

Thread Ends

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

└── Worker Thread

      │

      ├── start()

      ├── run()

      ├── Executing

      └── Terminated
```

---

# Advantages

- Easy thread management.
- Supports synchronization.
- Allows thread monitoring.
- Enables background processing.
- Improves application responsiveness.

---

# Best Practices

- Always call `start()` instead of `run()`.
- Use `join()` only when synchronization is required.
- Assign meaningful thread names.
- Use daemon threads for background services only.
- Monitor thread status using `is_alive()` when needed.

---

# Common Mistakes

## Mistake 1

Calling

```python
thread.run()
```

instead of

```python
thread.start()
```

---

## Mistake 2

Starting the same thread twice.

A thread can only be started once.

---

## Mistake 3

Assuming daemon threads always complete.

Daemon threads terminate when all non-daemon threads finish.

---

## Mistake 4

Using `join()` for every thread unnecessarily.

This reduces concurrency.

---

# Interview Questions

## 1. Which method starts a new thread?

### Answer

```python
start()
```

---

## 2. What is the purpose of `run()`?

### Answer

It contains the code executed by the child thread.

---

## 3. What does `join()` do?

### Answer

It waits until the specified thread completes execution.

---

## 4. What does `is_alive()` return?

### Answer

It returns `True` while the thread is running and `False` after it terminates.

---

## 5. Which method returns the currently executing thread?

### Answer

```python
threading.current_thread()
```

---

## 6. What does `active_count()` return?

### Answer

The number of active threads currently running.

---

## 7. What does `enumerate()` return?

### Answer

A list of all active thread objects.

---

## 8. What is a daemon thread?

### Answer

A background thread that automatically terminates when all non-daemon threads finish.

---

## 9. Can a thread name be changed?

### Answer

Yes.

A thread name can be assigned using the `name` parameter or modified through the `name` attribute.

---

## 10. Should `run()` be called directly?

### Answer

No.

Always use `start()`, which creates a new thread and then invokes `run()` internally.

---

# Practice Programs

1. Demonstrate `start()` and `run()`.
2. Demonstrate `join()`.
3. Check thread status using `is_alive()`.
4. Display active threads using `active_count()`.
5. Create and execute a daemon thread.

---

# Quick Revision

- `start()` → Starts a new thread.
- `run()` → Thread task.
- `join()` → Waits for completion.
- `is_alive()` → Checks thread status.
- `current_thread()` → Returns current thread.
- `active_count()` → Number of active threads.
- `enumerate()` → List of active threads.
- `name` → Thread name.
- `daemon` → Background thread.

---

# Chapter Summary

In this chapter, we learned:

- `start()`
- `run()`
- `join()`
- `is_alive()`
- `current_thread()`
- `active_count()`
- `enumerate()`
- Thread Names
- Daemon Threads
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
