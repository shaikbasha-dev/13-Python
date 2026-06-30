# Inter-Thread Communication in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is Inter-Thread Communication?
5. Why is Inter-Thread Communication Required?
6. Thread-Safe Communication
7. Queue Module
8. Queue Operations
9. Producer-Consumer Pattern
10. Internal Working
11. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand Inter-Thread Communication.
- Learn why threads communicate.
- Understand thread-safe communication.
- Learn the Queue module.
- Perform queue operations.
- Understand the Producer-Consumer pattern.
- Write thread-safe multithreaded programs.

---

# Prerequisites

Before learning this chapter, you should know:

- Multithreading
- Thread Synchronization
- Lock
- RLock
- Thread Methods

---

# Introduction

In many multithreaded applications,

threads work together instead of independently.

For example,

one thread downloads data,

while another thread processes the downloaded data.

Instead of using shared variables,

Python provides a safer communication mechanism using the

```python
queue
```

module.

The Queue module automatically handles synchronization,

making communication between threads safe and reliable.

---

# What is Inter-Thread Communication?

## Definition

Inter-Thread Communication is the process of exchanging data between multiple threads safely.

---

## Simple Definition

> Inter-Thread Communication allows threads to exchange information without causing data corruption.

---

# Why is Inter-Thread Communication Required?

Suppose one thread reads customer orders from a website.

Another thread prepares invoices.

Another thread updates the inventory.

Instead of sharing variables directly,

the threads exchange data through a thread-safe queue.

This avoids race conditions and keeps data consistent.

---

# Real-World Applications

Inter-thread communication is used in:

- Web Servers
- Chat Applications
- Banking Systems
- File Processing
- Video Streaming
- Online Shopping
- Producer-Consumer Systems
- Background Task Processing

---

# Thread-Safe Communication

A communication mechanism is called **thread-safe**

when multiple threads can access it without causing data inconsistency.

Python's

```python
Queue
```

class is thread-safe.

Therefore,

additional locking is usually unnecessary.

---

# Queue Module

Python provides the

```python
queue
```

module.

Example

```python
import queue
```

The most commonly used class is

```python
queue.Queue
```

---

# Creating a Queue

```python
import queue

q = queue.Queue()
```

---

# Queue Operations

## put()

Adds an item to the queue.

```python
q.put("Laptop")
```

---

## get()

Removes and returns an item.

```python
item = q.get()
```

---

## empty()

Returns

```python
True
```

if the queue is empty.

---

## full()

Returns

```python
True
```

if the queue is full.

---

## qsize()

Returns the number of items currently stored.

---

## task_done()

Indicates that a retrieved task has been completed.

---

## join()

Blocks until all queued tasks have been processed.

---

# Producer-Consumer Pattern

The Producer-Consumer pattern is one of the most common applications of inter-thread communication.

Producer

```text
Creates Data

↓

Places Data into Queue
```

Consumer

```text
Retrieves Data

↓

Processes Data
```

The queue acts as the communication bridge between the two threads.

---

# Internal Working

```text
Producer Thread

↓

Queue

↓

Consumer Thread

↓

Task Completed
```

---

# Advantages

- Thread-safe communication.
- Eliminates most race conditions.
- Simplifies synchronization.
- Improves reliability.
- Easy to use.

---

# Best Practices

- Prefer Queue over shared variables.
- Use `task_done()` after processing each item.
- Use `join()` when waiting for all tasks.
- Keep producer and consumer logic separate.
- Avoid unnecessary manual locking with queues.

---

# Common Mistakes

## Mistake 1

Sharing mutable variables instead of using a queue.

---

## Mistake 2

Forgetting to call

```python
task_done()
```

after processing an item.

---

## Mistake 3

Using a queue when simple local variables are sufficient.

---

## Mistake 4

Confusing

```python
queue.Queue
```

with the built-in Python list.

Lists are **not** inherently thread-safe.

---

# Interview Questions

## 1. What is Inter-Thread Communication?

### Answer

It is the process of exchanging data safely between multiple threads.

---

## 2. Which module provides thread-safe communication?

### Answer

```python
queue
```

---

## 3. Which class is commonly used?

### Answer

```python
queue.Queue
```

---

## 4. Why is Queue preferred over shared variables?

### Answer

Because Queue is thread-safe and automatically handles synchronization.

---

## 5. What is the Producer-Consumer pattern?

### Answer

A design pattern in which one thread produces data and another thread consumes it using a shared queue.

---

## 6. Which method inserts data into the queue?

### Answer

```python
put()
```

---

## 7. Which method removes data from the queue?

### Answer

```python
get()
```

---

# Quick Revision

- Inter-Thread Communication
- Queue
- put()
- get()
- empty()
- full()
- qsize()
- task_done()
- join()
- Producer-Consumer Pattern

---

# Chapter Summary

In this chapter, we learned:

- Inter-Thread Communication
- Queue Module
- Queue Operations
- Thread-Safe Communication
- Producer-Consumer Pattern
- Internal Working
- Best Practices
- Common Mistakes
- Interview Questions
- Quick Revision


# Program 1 – Creating a Queue

## Problem Statement

Write a Python program to create a queue and insert elements.

---

## Program

```python
import queue

q = queue.Queue()

q.put("Laptop")

q.put("Mobile")

q.put("Keyboard")

print(q.qsize())
```

---

## Output

```text
3
```

---

## Explanation

A queue is created using

```python
queue.Queue()
```

Three items are inserted using

```python
put()
```

The

```python
qsize()
```

method returns the total number of elements in the queue.

---

# Program 2 – Retrieving Data using get()

## Program

```python
import queue

q = queue.Queue()

q.put("Python")

q.put("Java")

print(q.get())

print(q.get())
```

---

## Output

```text
Python

Java
```

---

## Explanation

The queue follows the

**FIFO (First In, First Out)** principle.

The first inserted element is removed first.

---

# Program 3 – Checking Whether Queue is Empty

## Program

```python
import queue

q = queue.Queue()

print(q.empty())

q.put(100)

print(q.empty())
```

---

## Output

```text
True

False
```

---

## Explanation

Before inserting data,

the queue is empty.

After inserting one item,

the queue is no longer empty.

---

# Program 4 – Checking Queue Size

## Program

```python
import queue

q = queue.Queue()

for i in range(5):

    q.put(i)

print("Queue Size :", q.qsize())
```

---

## Output

```text
Queue Size : 5
```

---

## Explanation

The

```python
qsize()
```

method returns the current number of elements in the queue.

---

# Program 5 – Queue with Maximum Size

## Program

```python
import queue

q = queue.Queue(maxsize=2)

q.put("A")

q.put("B")

print(q.full())
```

---

## Output

```text
True
```

---

## Explanation

The queue can store only two elements.

After inserting two elements,

the queue becomes full.

---

# Program 6 – Producer Thread

## Program

```python
import threading
import queue

q = queue.Queue()

def producer():

    for item in ["Pen", "Book", "Bag"]:

        q.put(item)

        print("Produced :", item)


thread = threading.Thread(target=producer)

thread.start()

thread.join()
```

---

## Sample Output

```text
Produced : Pen

Produced : Book

Produced : Bag
```

---

## Explanation

The producer thread inserts items into the queue.

---

# Program 7 – Consumer Thread

## Program

```python
import threading
import queue

q = queue.Queue()

q.put("Laptop")

q.put("Mouse")

def consumer():

    while not q.empty():

        print("Consumed :", q.get())


thread = threading.Thread(target=consumer)

thread.start()

thread.join()
```

---

## Sample Output

```text
Consumed : Laptop

Consumed : Mouse
```

---

## Explanation

The consumer removes elements from the queue in FIFO order.

---

# Program 8 – Producer-Consumer Pattern

## Program

```python
import threading
import queue

q = queue.Queue()

def producer():

    for i in range(1, 6):

        q.put(i)

        print("Produced :", i)

def consumer():

    while not q.empty():

        print("Consumed :", q.get())


producer_thread = threading.Thread(target=producer)

producer_thread.start()

producer_thread.join()

consumer_thread = threading.Thread(target=consumer)

consumer_thread.start()

consumer_thread.join()
```

---

## Sample Output

```text
Produced : 1

Produced : 2

Produced : 3

Produced : 4

Produced : 5

Consumed : 1

Consumed : 2

Consumed : 3

Consumed : 4

Consumed : 5
```

---

## Explanation

The producer adds items to the queue.

The consumer removes and processes them.

---

# Program 9 – task_done() and join()

## Program

```python
import queue

q = queue.Queue()

for i in range(3):

    q.put(i)

while not q.empty():

    item = q.get()

    print(item)

    q.task_done()

q.join()

print("All Tasks Completed")
```

---

## Output

```text
0

1

2

All Tasks Completed
```

---

## Explanation

After processing each item,

`task_done()` informs the queue that the task is complete.

`join()` waits until all queued tasks have been marked as done.

---

# Program 10 – Multiple Producers and Consumers

## Program

```python
import threading
import queue

q = queue.Queue()

def producer(name):

    for i in range(3):

        item = f"{name}-{i}"

        q.put(item)

        print("Produced :", item)

def consumer():

    while not q.empty():

        print("Consumed :", q.get())


producer1 = threading.Thread(

    target=producer,

    args=("Producer1",)

)

producer2 = threading.Thread(

    target=producer,

    args=("Producer2",)

)

producer1.start()

producer2.start()

producer1.join()

producer2.join()

consumer = threading.Thread(target=consumer)

consumer.start()

consumer.join()
```

---

## Sample Output

```text
Produced : Producer1-0

Produced : Producer1-1

Produced : Producer2-0

Produced : Producer2-1

...

Consumed : Producer1-0

Consumed : Producer1-1

Consumed : Producer2-0

Consumed : Producer2-1
```

---

## Explanation

Multiple producer threads place data into the same queue.

The consumer thread retrieves the items safely.

---

# Dry Run

```text
Producer Thread

↓

put()

↓

Queue

↓

Consumer Thread

↓

get()

↓

task_done()

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

├── Producer Thread

│

├── Queue

│

└── Consumer Thread

↓

Thread-Safe Data Exchange
```

---

# Advantages

- Thread-safe communication.
- Eliminates most race conditions.
- Supports FIFO processing.
- Simplifies producer-consumer implementations.
- Improves scalability.

---

# Best Practices

- Use `queue.Queue` for communication between threads.
- Call `task_done()` after processing each retrieved item.
- Use `join()` when waiting for all queued tasks.
- Avoid shared variables when a queue is sufficient.
- Keep producer and consumer logic independent.

---

# Common Mistakes

## Mistake 1

Using a normal list instead of a queue for thread communication.

---

## Mistake 2

Forgetting to call `task_done()`.

This may cause `join()` to wait indefinitely.

---

## Mistake 3

Assuming queue operations require manual locking.

`queue.Queue` already provides thread-safe operations.

---

## Mistake 4

Ignoring queue size limits when using bounded queues.

---

# Interview Questions

## 1. What is Inter-Thread Communication?

### Answer

It is the process of exchanging data safely between multiple threads.

---

## 2. Which module provides thread-safe queues?

### Answer

```python
queue
```

---

## 3. Which class is commonly used for thread communication?

### Answer

```python
queue.Queue
```

---

## 4. Which method inserts an item into the queue?

### Answer

```python
put()
```

---

## 5. Which method removes an item from the queue?

### Answer

```python
get()
```

---

## 6. Why is `task_done()` used?

### Answer

It informs the queue that a retrieved task has been completely processed.

---

## 7. What does `join()` do?

### Answer

It blocks until all items placed into the queue have been processed.

---

## 8. What is the Producer-Consumer pattern?

### Answer

A design pattern in which producer threads generate data and consumer threads process it using a shared queue.

---

# Practice Programs

1. Create a queue and insert five elements.
2. Retrieve all elements from a queue.
3. Implement a producer thread.
4. Implement a consumer thread.
5. Implement a producer-consumer system using `queue.Queue`.

---

# Quick Revision

- Queue → Thread-safe communication.
- `put()` → Insert item.
- `get()` → Retrieve item.
- `empty()`
- `full()`
- `qsize()`
- `task_done()`
- `join()`
- Producer-Consumer Pattern.

---

# Chapter Summary

In this chapter, we learned:

- Inter-Thread Communication
- Queue Module
- Queue Operations
- Producer Thread
- Consumer Thread
- Producer-Consumer Pattern
- `task_done()`
- `join()`
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
