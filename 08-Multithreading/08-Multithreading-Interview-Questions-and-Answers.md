# Multithreading Interview Questions and Answers in Python

## Table of Contents

1. Introduction
2. Thread Basics
3. Thread Creation
4. Thread Life Cycle
5. Thread Methods
6. Thread Synchronization
7. Daemon Threads
8. Inter-Thread Communication
9. Python GIL
10. Scenario-Based Questions
11. Quick Revision

---

# Introduction

This document contains the most frequently asked Python Multithreading interview questions.

The questions are suitable for:

- Freshers
- Entry-Level Python Developers
- Technical Interviews
- Coding Assessments
- Revision Before Interviews

---

# Thread Basics

## 1. What is a Thread?

### Answer

A thread is the smallest unit of execution within a process.

---

## 2. What is Multithreading?

### Answer

Multithreading is the execution of multiple threads concurrently within a single process.

---

## 3. Why is Multithreading used?

### Answer

To improve application responsiveness and efficiently perform multiple tasks concurrently.

---

## 4. What is the difference between a Process and a Thread?

### Answer

| Process | Thread |
|----------|---------|
| Independent program | Smallest execution unit |
| Own memory | Shared process memory |
| More resource usage | Less resource usage |

---

## 5. Do threads share memory?

### Answer

Yes.

Threads within the same process share memory and resources.

---

# Thread Creation

## 6. How can threads be created in Python?

### Answer

- Using a target function.
- By extending the `threading.Thread` class.

---

## 7. Which module is used for Multithreading?

### Answer

```python
threading
```

---

## 8. Which method starts a thread?

### Answer

```python
start()
```

---

## 9. What is the purpose of the `run()` method?

### Answer

It contains the code executed by the child thread.

---

## 10. Should `run()` be called directly?

### Answer

No.

Always call `start()`, which internally invokes `run()`.

---

# Thread Life Cycle

## 11. What are the states of a thread?

### Answer

- New
- Runnable
- Running
- Waiting / Blocked
- Terminated

---

## 12. What is the Runnable state?

### Answer

The thread is ready to execute and is waiting for CPU time.

---

## 13. What is Context Switching?

### Answer

It is the process of switching CPU execution between multiple threads.

---

## 14. Can a terminated thread be restarted?

### Answer

No.

A thread can only be started once.

---

## 15. Who decides thread execution order?

### Answer

The operating system's thread scheduler.

---

# Thread Methods

## 16. What is `join()`?

### Answer

It waits until another thread finishes execution.

---

## 17. What does `is_alive()` return?

### Answer

`True` if the thread is still running; otherwise `False`.

---

## 18. What does `current_thread()` return?

### Answer

The currently executing thread object.

---

## 19. What does `active_count()` return?

### Answer

The number of active threads.

---

## 20. What does `enumerate()` return?

### Answer

A list of all active thread objects.

---

## 21. What is the purpose of the `name` attribute?

### Answer

It gets or sets the name of a thread.

---

# Thread Synchronization

## 22. What is Thread Synchronization?

### Answer

The process of controlling access to shared resources so only one thread executes the critical section at a time.

---

## 23. What is a Race Condition?

### Answer

A race condition occurs when multiple threads modify shared data simultaneously, producing unpredictable results.

---

## 24. What is a Critical Section?

### Answer

The part of a program where shared resources are accessed or modified.

---

## 25. What is a Lock?

### Answer

A synchronization mechanism that allows only one thread to access a critical section at a time.

---

## 26. What is an RLock?

### Answer

A reentrant lock that allows the same thread to acquire the same lock multiple times.

---

## 27. What is the difference between Lock and RLock?

### Answer

| Lock | RLock |
|------|--------|
| Acquired once | Acquired multiple times by the same thread |
| Simpler | Supports nested locking |

---

## 28. Why is `with lock:` recommended?

### Answer

Because it automatically acquires and releases the lock.

---

# Daemon Threads

## 29. What is a Daemon Thread?

### Answer

A background thread that automatically terminates when all non-daemon threads finish execution.

---

## 30. Are threads daemon by default?

### Answer

No.

Threads are non-daemon by default.

---

## 31. When should daemon threads be used?

### Answer

For background tasks such as monitoring, logging, and cleanup.

---

## 32. Can daemon status be changed after `start()`?

### Answer

No.

It must be changed before calling `start()`.

---

# Inter-Thread Communication

## 33. What is Inter-Thread Communication?

### Answer

It is the process of exchanging data safely between multiple threads.

---

## 34. Which module provides thread-safe communication?

### Answer

```python
queue
```

---

## 35. Which class is commonly used?

### Answer

```python
queue.Queue
```

---

## 36. What does `put()` do?

### Answer

It inserts an item into the queue.

---

## 37. What does `get()` do?

### Answer

It removes and returns an item from the queue.

---

## 38. What is the Producer-Consumer pattern?

### Answer

A design pattern where producer threads generate data and consumer threads process it using a shared queue.

---

## 39. Why is Queue preferred over shared variables?

### Answer

Because Queue is thread-safe and handles synchronization internally.

---

## 40. Why is `task_done()` used?

### Answer

It informs the queue that a retrieved task has been processed successfully.

---

## 41. What does `join()` do in Queue?

### Answer

It blocks until all queued tasks have been processed.

---

# Python GIL

## 42. What is the GIL?

### Answer

The Global Interpreter Lock (GIL) is a mechanism in CPython that allows only one thread to execute Python bytecode at a time.

---

## 43. Does the GIL prevent all concurrency?

### Answer

No.

Threads can still make progress concurrently, especially for I/O-bound tasks. The GIL mainly limits parallel execution of Python bytecode in CPU-bound workloads.

---

## 44. Is multithreading useful for CPU-bound tasks in CPython?

### Answer

Generally, no.

For CPU-intensive work, the `multiprocessing` module is often a better choice because it uses separate processes.

---

## 45. When is multithreading most beneficial?

### Answer

For I/O-bound operations such as file handling, database access, and network communication.

---

# Scenario-Based Questions

## 46. How would you prevent race conditions?

### Answer

By using synchronization mechanisms such as `Lock` or `RLock`.

---

## 47. Which synchronization mechanism would you use for nested locking?

### Answer

`RLock`.

---

## 48. Which data structure is recommended for communication between threads?

### Answer

`queue.Queue`.

---

## 49. Which type of thread is suitable for background logging?

### Answer

A daemon thread.

---

## 50. What are some common mistakes in multithreading?

### Answer

- Calling `run()` directly instead of `start()`.
- Restarting a completed thread.
- Accessing shared data without synchronization.
- Forgetting to release locks.
- Using daemon threads for business-critical tasks.

---

# Quick Revision

Remember:

- Thread → Smallest execution unit
- Multithreading → Multiple threads in one process
- `start()` → Starts a thread
- `run()` → Thread task
- `join()` → Waits for completion
- `Lock` → Mutual exclusion
- `RLock` → Reentrant lock
- `daemon=True` → Background thread
- `Queue` → Thread-safe communication
- GIL → Limits parallel execution of Python bytecode in CPython
- Multithreading → Best for I/O-bound tasks

---

# Final Notes

After completing this chapter, you should be able to:

- Explain Python Multithreading confidently.
- Create and manage threads.
- Understand the thread life cycle.
- Use thread methods effectively.
- Synchronize shared resources using `Lock` and `RLock`.
- Work with daemon threads.
- Implement inter-thread communication using `Queue`.
- Explain the Producer-Consumer pattern.
- Describe the impact of the GIL.
- Answer common Python Multithreading interview questions confidently.
