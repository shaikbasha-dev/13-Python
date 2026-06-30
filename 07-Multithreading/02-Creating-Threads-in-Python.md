# Creating Threads in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. Ways to Create Threads
5. Creating Threads using Target Functions
6. Creating Threads by Extending the Thread Class
7. Passing Arguments to Threads
8. Starting Threads
9. Thread Execution
10. Internal Working
11. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand different ways to create threads.
- Create threads using target functions.
- Create threads by extending the `Thread` class.
- Pass arguments to threads.
- Start and execute threads.
- Understand how Python schedules threads.

---

# Prerequisites

Before learning this chapter, you should know:

- Functions
- Classes
- Objects
- Introduction to Multithreading

---

# Introduction

In the previous chapter,

we learned what Multithreading is and why it is useful.

Now,

we will learn **how to create threads** in Python.

Python provides multiple ways to create threads,

allowing developers to choose the most suitable approach depending on the application.

---

# Ways to Create Threads

Python mainly provides two ways to create threads.

## Method 1

Using the

```python
Thread
```

class with the

```python
target
```

parameter.

---

## Method 2

By inheriting from

```python
threading.Thread
```

and overriding the

```python
run()
```

method.

---

# Creating Threads using Target Functions

A normal Python function can be executed by a thread.

Syntax

```python
import threading

thread = threading.Thread(

    target=function_name
)
```

The thread executes the specified function when

```python
start()
```

is called.

---

# Creating Threads by Extending the Thread Class

Another approach is to inherit from

```python
threading.Thread
```

and override the

```python
run()
```

method.

Syntax

```python
class MyThread(threading.Thread):

    def run(self):

        # Thread Code
```

Calling

```python
start()
```

automatically invokes

```python
run()
```

inside the new thread.

---

# Passing Arguments to Threads

Arguments are supplied using

```python
args
```

Example

```python
thread = threading.Thread(

    target=display,

    args=("Rahul",)
)
```

The arguments are passed to the target function when the thread starts.

---

# Starting Threads

Threads are started using

```python
start()
```

Example

```python
thread.start()
```

The operating system scheduler determines when the thread actually begins execution.

---

# Thread Execution

When

```python
start()
```

is called,

Python performs the following steps:

```text
Thread Object Created

↓

New Thread Created

↓

run() Invoked

↓

Task Executed

↓

Thread Terminates
```

---

# Internal Working

```text
Main Thread

↓

Thread Object Created

↓

start()

↓

Operating System Scheduler

↓

Child Thread Executes

↓

Thread Completes

↓

Program Ends
```

---

# Advantages

- Simple thread creation.
- Supports concurrent execution.
- Flexible design.
- Easy to pass arguments.
- Supports reusable thread classes.

---

# Best Practices

- Prefer target functions for simple tasks.
- Extend `Thread` only when additional customization is required.
- Always start threads using `start()`.
- Wait for important threads using `join()`.
- Keep thread logic independent whenever possible.

---

# Common Mistakes

## Mistake 1

Calling

```python
run()
```

instead of

```python
start()
```

---

## Mistake 2

Forgetting to import

```python
threading
```

---

## Mistake 3

Passing the result of a function instead of the function itself.

❌ Incorrect

```python
threading.Thread(

    target=display()
)
```

✅ Correct

```python
threading.Thread(

    target=display
)
```

---

## Mistake 4

Forgetting the comma in a single-element tuple.

❌ Incorrect

```python
args=("Rahul")
```

✅ Correct

```python
args=("Rahul",)
```

---

# Interview Questions

## 1. How many ways are there to create threads in Python?

### Answer

Two common ways:

- Using a target function.
- Extending the `Thread` class.

---

## 2. Which method is recommended for simple tasks?

### Answer

Using a target function.

---

## 3. Which method allows customization?

### Answer

Extending the `Thread` class.

---

## 4. Which method starts thread execution?

### Answer

```python
start()
```

---

## 5. What is the purpose of the `args` parameter?

### Answer

It passes arguments to the thread function.

---

# Quick Revision

- Two ways to create threads.
- `target`
- `Thread`
- `run()`
- `start()`
- `args`
- `join()`

---

# Chapter Summary

In this chapter, we learned:

- Creating Threads
- Target Functions
- Extending Thread Class
- Passing Arguments
- Thread Execution
- Internal Working
- Best Practices
- Common Mistakes
- Interview Questions
- Quick Revision


# Program 1 – Creating a Thread using a Target Function

## Problem Statement

Write a Python program to create a thread using a target function.

---

## Program

```python
import threading

def display():

    print("Child Thread Executing")


thread = threading.Thread(target=display)

thread.start()

thread.join()
```

---

## Output

```text
Child Thread Executing
```

---

## Explanation

- A thread is created using the `Thread` class.
- The `target` parameter specifies the function to execute.
- `start()` starts the new thread.
- `join()` waits until the thread completes.

---

# Program 2 – Creating Multiple Threads

## Program

```python
import threading

def display():

    print("Executing Child Thread")


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
Executing Child Thread

Executing Child Thread
```

---

## Explanation

Two independent threads execute the same function.

The order of execution depends on the operating system scheduler.

---

# Program 3 – Creating a Thread by Extending Thread Class

## Program

```python
import threading

class MyThread(threading.Thread):

    def run(self):

        print("Thread Executed")


thread = MyThread()

thread.start()

thread.join()
```

---

## Output

```text
Thread Executed
```

---

## Explanation

The `run()` method contains the task to be executed.

Calling `start()` automatically invokes `run()`.

---

# Program 4 – Multiple Objects of Thread Class

## Program

```python
import threading

class MyThread(threading.Thread):

    def run(self):

        print("Running Child Thread")


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
Running Child Thread

Running Child Thread
```

---

# Program 5 – Passing Arguments to a Thread

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

Arguments are passed through the `args` parameter.

A single argument must be enclosed in a tuple.

---

# Program 6 – Passing Multiple Arguments

## Program

```python
import threading

def add(a, b):

    print("Sum :", a + b)


thread = threading.Thread(

    target=add,

    args=(10, 20)

)

thread.start()

thread.join()
```

---

## Output

```text
Sum : 30
```

---

## Explanation

Multiple arguments are supplied as a tuple.

---

# Program 7 – Using Lambda Function

## Program

```python
import threading

thread = threading.Thread(

    target=lambda: print("Lambda Thread")

)

thread.start()

thread.join()
```

---

## Output

```text
Lambda Thread
```

---

## Explanation

A lambda function can also be used as the thread's target.

This approach is suitable for small tasks.

---

# Program 8 – Main Thread and Child Thread

## Program

```python
import threading

def display():

    print("Child Thread")


print("Main Thread Started")

thread = threading.Thread(target=display)

thread.start()

thread.join()

print("Main Thread Finished")
```

---

## Output

```text
Main Thread Started

Child Thread

Main Thread Finished
```

---

## Explanation

The main thread waits until the child thread finishes because of `join()`.

---

# Program 9 – Creating Three Threads

## Program

```python
import threading

def task():

    print("Executing Task")


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
Executing Task

Executing Task

Executing Task
```

---

## Explanation

Three child threads execute the same task concurrently.

---

# Program 10 – Demonstrating join()

## Program

```python
import threading

def task():

    print("Child Thread Completed")


thread = threading.Thread(target=task)

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

The `join()` method ensures that the main thread waits until the child thread completes execution.

---

# Dry Run

```text
Program Starts

↓

Main Thread

↓

Thread Object Created

↓

start()

↓

Operating System Scheduler

↓

Child Thread Executes

↓

join()

↓

Main Thread Continues

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

├── Child Thread 2

│

└── Child Thread 3

↓

Shared Memory

↓

Program Ends
```

---

# Advantages

- Easy thread creation.
- Supports concurrent execution.
- Improves responsiveness.
- Reusable thread objects.
- Simple argument passing.

---

# Best Practices

- Use target functions for simple thread tasks.
- Extend the `Thread` class only when customization is needed.
- Always start threads using `start()`.
- Use `join()` when the main thread depends on child threads.
- Avoid creating unnecessary threads.

---

# Common Mistakes

## Mistake 1

Calling `run()` directly.

❌ Incorrect

```python
thread.run()
```

✅ Correct

```python
thread.start()
```

---

## Mistake 2

Passing a function call instead of a function reference.

❌ Incorrect

```python
threading.Thread(

    target=display()
)
```

✅ Correct

```python
threading.Thread(

    target=display
)
```

---

## Mistake 3

Forgetting the comma in a single-element tuple.

❌ Incorrect

```python
args=("Rahul")
```

✅ Correct

```python
args=("Rahul",)
```

---

## Mistake 4

Not calling `join()` when synchronization is required.

The main thread may complete before child threads finish.

---

# Interview Questions

## 1. What are the two common ways to create threads in Python?

### Answer

- Using a target function.
- Extending the `Thread` class.

---

## 2. Which method actually starts a new thread?

### Answer

```python
start()
```

---

## 3. What is the purpose of `run()`?

### Answer

It contains the code executed by the child thread.

---

## 4. Why is `join()` used?

### Answer

It makes the calling thread wait until the specified thread finishes execution.

---

## 5. How are arguments passed to a thread?

### Answer

Using the `args` parameter.

---

## 6. Can lambda functions be used as thread targets?

### Answer

Yes.

A lambda function can be supplied to the `target` parameter for simple tasks.

---

## 7. Does `start()` call `run()` automatically?

### Answer

Yes.

Calling `start()` creates a new thread and then internally invokes the `run()` method.

---

# Practice Programs

1. Create a thread using a target function.
2. Create three child threads.
3. Create a thread by extending the `Thread` class.
4. Pass multiple arguments to a thread.
5. Demonstrate the use of `join()`.

---

# Quick Revision

- Two ways to create threads.
- `Thread()`
- `target`
- `run()`
- `start()`
- `args`
- `join()`
- Lambda thread

---

# Chapter Summary

In this chapter, we learned:

- Creating Threads
- Target Functions
- Thread Class
- Passing Arguments
- Lambda Threads
- `start()`
- `run()`
- `join()`
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
