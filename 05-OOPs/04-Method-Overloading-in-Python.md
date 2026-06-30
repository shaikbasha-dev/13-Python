# Method Overloading in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is a Method?
5. What is Method Overloading?
6. Does Python Support Method Overloading?
7. Why Python Does Not Support Method Overloading
8. How to Achieve Method Overloading in Python
9. Default Arguments
10. Variable-Length Arguments (*args)
11. Keyword Arguments (**kwargs)
12. Method Overriding vs Method Overloading
13. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand methods in Python.
- Understand Method Overloading.
- Explain why Python does not support true Method Overloading.
- Simulate Method Overloading using Python features.
- Differentiate Method Overloading and Method Overriding.

---

# Prerequisites

Before learning this chapter, you should know:

- Classes
- Objects
- Methods
- Constructors
- Instance Variables

---

# Introduction

Methods define the behavior of an object.

Sometimes, we want to perform the same operation using different numbers or types of arguments.

For example,

A calculator may perform addition using:

- Two numbers
- Three numbers
- Four numbers

In Java, this is achieved using **Method Overloading**.

Python, however, follows a different approach.

---

# What is a Method?

A method is a function defined inside a class.

It describes the behavior of an object.

Example

```python
class Student:

    def display(self):
        print("Welcome")
```

Here,

`display()` is a method.

---

# What is Method Overloading?

## Definition

Method Overloading is the process of creating multiple methods with the same name but different parameter lists.

Example in Java

```java
add()

add(int a)

add(int a, int b)

add(int a, int b, int c)
```

The compiler automatically calls the appropriate method based on the arguments passed.

---

# Does Python Support Method Overloading?

## Answer

**No.**

Python **does not support true Method Overloading**.

Only one method with a particular name can exist inside a class.

If multiple methods with the same name are defined, the last method replaces the previous ones.

---

# Example

```python
class Demo:

    def show(self):
        print("First Method")

    def show(self, name):
        print("Second Method")
```

Only the second method exists.

The first method is overwritten.

---

# Why Python Does Not Support Method Overloading

Python is a dynamically typed language.

Instead of checking method signatures like Java, Python provides more flexible features such as:

- Default Arguments
- Variable-Length Arguments (`*args`)
- Keyword Arguments (`**kwargs`)

These features remove the need for traditional method overloading.

---

# How to Achieve Method Overloading in Python

Python simulates Method Overloading using:

- Default Arguments
- `*args`
- `**kwargs`

These techniques allow one method to handle different numbers of arguments.

---

# Using Default Arguments

Example

```python
class Calculator:

    def add(self, a, b=0):
        print(a + b)
```

Usage

```python
cal = Calculator()

cal.add(10)

cal.add(10, 20)
```

---

# Using *args

Example

```python
class Calculator:

    def add(self, *numbers):
        print(sum(numbers))
```

Usage

```python
cal = Calculator()

cal.add(10)

cal.add(10,20)

cal.add(10,20,30)
```

---

# Using **kwargs

Example

```python
class Student:

    def details(self, **data):
        print(data)
```

Usage

```python
student = Student()

student.details(name="Rahul")

student.details(name="Rahul", age=21)
```

---

# Method Overloading vs Method Overriding

| Method Overloading | Method Overriding |
|--------------------|-------------------|
| Same class | Parent and Child class |
| Same method name | Same method name |
| Different parameters | Same parameters |
| Not supported directly in Python | Fully supported in Python |

---

# Summary

In this part, you learned:

- Methods
- Method Overloading
- Why Python does not support true Method Overloading
- Default Arguments
- `*args`
- `**kwargs`
- Difference between Method Overloading and Method Overriding


# Program 1 – Demonstrating That Python Does Not Support True Method Overloading

## Problem Statement

Write a Python program to demonstrate that Python does not support true Method Overloading.

---

## Program

```python
class Demo:

    def show(self):
        print("First Method")

    def show(self, name):
        print("Second Method")
        print("Name :", name)

obj = Demo()

obj.show("Rahul")
```

---

## Output

```text
Second Method
Name : Rahul
```

---

## Explanation

Although two methods with the same name are written, Python keeps only the last method.

The first method is overwritten.

---

## Internal Working

```text
Demo Class Loaded

↓

First show() Method Created

↓

Second show() Method Created

↓

First Method Replaced

↓

Only Second Method Exists
```

---

# Program 2 – Method Overloading Using Default Arguments

## Problem Statement

Write a Python program to simulate Method Overloading using default arguments.

---

## Program

```python
class Calculator:

    def add(self, a, b=0):

        print("Result :", a + b)

cal = Calculator()

cal.add(10)

cal.add(10, 20)
```

---

## Output

```text
Result : 10

Result : 30
```

---

## Explanation

If the second argument is not provided, Python automatically uses the default value.

---

# Program 3 – Method Overloading Using *args

## Problem Statement

Write a Python program using `*args`.

---

## Program

```python
class Calculator:

    def add(self, *numbers):

        print("Sum :", sum(numbers))

cal = Calculator()

cal.add(10)

cal.add(10, 20)

cal.add(10, 20, 30)

cal.add(10, 20, 30, 40)
```

---

## Output

```text
Sum : 10

Sum : 30

Sum : 60

Sum : 100
```

---

## Explanation

`*args` accepts any number of positional arguments.

The `sum()` function calculates the total of all arguments.

---

# Program 4 – Method Overloading Using **kwargs

## Program

```python
class Student:

    def details(self, **data):

        print(data)

student = Student()

student.details(name="Rahul")

student.details(name="Rahul", age=21)

student.details(name="Rahul", age=21, course="Python")
```

---

## Output

```text
{'name': 'Rahul'}

{'name': 'Rahul', 'age': 21}

{'name': 'Rahul', 'age': 21, 'course': 'Python'}
```

---

## Explanation

`**kwargs` accepts any number of keyword arguments.

---

# Program 5 – Combining Default Arguments and *args

## Program

```python
class Employee:

    def salary(self, basic=0, *allowances):

        total = basic + sum(allowances)

        print("Total Salary :", total)

emp = Employee()

emp.salary()

emp.salary(25000)

emp.salary(25000, 3000, 2000)
```

---

## Output

```text
Total Salary : 0

Total Salary : 25000

Total Salary : 30000
```

---

# Dry Run

```text
Calculator Class Loaded

↓

Object Created

↓

Arguments Passed

↓

Method Executes

↓

Result Displayed
```

---

# Memory Representation

```text
Calculator Object

        │

        ▼

+-----------------------+

| add()                 |

| Object Reference      |

+-----------------------+
```

---

# Advantages

- Flexible method implementation.
- Reduces duplicate code.
- Handles different argument combinations.
- Improves code readability.
- Easy to maintain.

---

# Best Practices

- Use default arguments when only a few parameters are optional.
- Use `*args` when the number of positional arguments is unknown.
- Use `**kwargs` when keyword arguments vary.
- Avoid writing unnecessary complex methods.
- Use meaningful method names.

---

# Common Mistakes

## Mistake 1

Writing multiple methods with the same name.

❌ Incorrect

```python
class Demo:

    def show(self):
        pass

    def show(self, name):
        pass
```

Only the second method exists.

---

## Mistake 2

Using `*args` when default arguments are sufficient.

Prefer simpler code whenever possible.

---

## Mistake 3

Forgetting that `*args` stores values as a tuple.

```python
def demo(*args):

    print(type(args))
```

Output

```text
<class 'tuple'>
```

---

# Real-Time Applications

Method overloading techniques are used in:

- Calculator Applications
- Banking Software
- Payroll Systems
- Student Management Systems
- Billing Applications
- Data Processing Programs

---

# Interview Questions

## 1. What is Method Overloading?

### Answer

Method Overloading is the process of defining multiple methods with the same name but different parameter lists.

---

## 2. Does Python support true Method Overloading?

### Answer

No.

Python allows only one method with a given name inside a class.

---

## 3. Why doesn't Python support Method Overloading?

### Answer

Python is dynamically typed and provides flexible alternatives such as default arguments, `*args`, and `**kwargs`.

---

## 4. How can Method Overloading be achieved in Python?

### Answer

By using:

- Default Arguments
- `*args`
- `**kwargs`

---

## 5. What is the purpose of `*args`?

### Answer

It accepts any number of positional arguments.

---

## 6. What is the purpose of `**kwargs`?

### Answer

It accepts any number of keyword arguments.

---

## 7. What is the difference between Method Overloading and Method Overriding?

### Answer

Method Overloading uses the same method name with different parameter lists.

Method Overriding redefines a parent class method in a child class using the same method signature.

---

# Practice Programs

1. Create a Calculator class using default arguments.
2. Create a Calculator class using `*args`.
3. Create an Employee class using `**kwargs`.
4. Simulate method overloading using optional parameters.
5. Write a program that accepts any number of integers and displays their sum.

---

# Quick Revision

- Python does not support true Method Overloading.
- Only one method with a given name exists in a class.
- The last method definition replaces previous ones.
- Use default arguments for optional parameters.
- Use `*args` for variable positional arguments.
- Use `**kwargs` for variable keyword arguments.
- Method Overriding is supported in Python.

---

# Chapter Summary

In this chapter, you learned:

- Methods
- Method Overloading
- Why Python does not support true Method Overloading
- Default Arguments
- `*args`
- `**kwargs`
- Difference between Method Overloading and Method Overriding
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
