# Object-Oriented Programming (OOP) in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. Programming Paradigms
5. What is Procedural Programming?
6. Limitations of Procedural Programming
7. Why Object-Oriented Programming?
8. What is Object-Oriented Programming?
9. Real-World Analogy
10. Features of OOP
11. Four Pillars of OOP
12. Advantages of OOP
13. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand Object-Oriented Programming.
- Explain why OOP was introduced.
- Differentiate Procedural Programming and OOP.
- Understand the basic principles of OOP.
- Identify real-world examples of OOP.
- Understand the four pillars of OOP.

---

# Prerequisites

Before learning this chapter, you should know:

- Variables
- Data Types
- Functions
- Control Statements
- Operators

---

# Introduction

As software applications become larger and more complex, writing programs using only functions becomes difficult.

Consider applications like:

- Banking System
- Hospital Management System
- Railway Reservation System
- E-Commerce Website
- Social Media Applications

These applications contain thousands or even millions of lines of code.

Managing such large applications using only functions becomes difficult because:

- Code becomes lengthy.
- Code duplication increases.
- Maintenance becomes difficult.
- Debugging becomes time-consuming.
- Reusability becomes limited.

To overcome these problems, **Object-Oriented Programming (OOP)** was introduced.

OOP organizes programs around **objects** rather than functions, making software easier to design, maintain, and extend.

---

# Programming Paradigms

A **Programming Paradigm** is a style or approach used to write programs.

Some common programming paradigms are:

- Procedural Programming
- Object-Oriented Programming
- Functional Programming
- Event-Driven Programming

In this chapter, we focus on **Object-Oriented Programming (OOP)**.

---

# What is Procedural Programming?

Procedural Programming is a programming paradigm in which a program is divided into a collection of functions.

Each function performs a specific task.

Example:

```text
Student Management System

↓

Input Student Details

↓

Calculate Marks

↓

Display Result
```

The focus is on **functions** rather than **objects**.

Examples of procedural programming languages include:

- C
- Pascal

Python also supports procedural programming.

---

# Limitations of Procedural Programming

Although procedural programming is suitable for small programs, it has limitations when building large applications.

Some common limitations are:

- Code reusability is limited.
- Data is less secure because it can be accessed directly.
- Large programs become difficult to maintain.
- Debugging becomes more complex.
- Modifying one function may affect other parts of the program.

These limitations led to the development of Object-Oriented Programming.

---

# Why Object-Oriented Programming?

Object-Oriented Programming helps solve many problems found in procedural programming.

It provides:

- Better code organization.
- Code reusability.
- Data security.
- Easier maintenance.
- Better scalability.
- Modular programming.

Because of these advantages, OOP is widely used in modern software development.

---

# What is Object-Oriented Programming?

Object-Oriented Programming (OOP) is a programming paradigm in which software is designed using **classes** and **objects**.

A class acts as a blueprint, while objects represent real-world entities created from that blueprint.

An object contains:

- Data (Attributes)
- Behavior (Methods)

---

# Real-World Analogy

Consider a mobile phone.

Every mobile phone has:

Attributes:

- Brand
- Model
- Color
- Price

Behaviors:

- Call
- Message
- Camera
- Internet

Similarly, in Python:

```text
Mobile

↓

Class

↓

Samsung Galaxy

↓

Object
```

The class defines the structure, while the object is an actual instance created from that structure.

---

# Features of Object-Oriented Programming

Object-Oriented Programming provides the following features:

- Classes
- Objects
- Encapsulation
- Abstraction
- Inheritance
- Polymorphism
- Reusability
- Modularity

---

# Four Pillars of OOP

Object-Oriented Programming is built on four fundamental principles.

## 1. Encapsulation

Encapsulation is the process of combining data and methods into a single unit called a class.

Example:

A Bank Account stores:

- Account Number
- Balance

and provides methods such as:

- Deposit()
- Withdraw()

The internal data is protected from direct access.

---

## 2. Abstraction

Abstraction means hiding unnecessary implementation details and showing only the essential features.

Example:

While driving a car, the driver uses:

- Steering Wheel
- Brake
- Accelerator

The driver does not need to know how the engine works internally.

---

## 3. Inheritance

Inheritance allows one class to acquire the properties and methods of another class.

Example:

Vehicle

↓

Car

↓

Electric Car

The child class automatically inherits features from the parent class.

---

## 4. Polymorphism

Polymorphism means "many forms."

The same method can perform different actions depending on the object.

Example:

Method:

```text
draw()
```

Objects:

- Circle
- Rectangle
- Triangle

Each object provides its own implementation of the `draw()` method.

---

# Advantages of OOP

Object-Oriented Programming offers several advantages:

- Code Reusability
- Easy Maintenance
- Better Security
- Modular Design
- Scalability
- Easy Testing
- Real-World Modeling
- Improved Readability

---

# Summary

In this part, you learned:

- Programming Paradigms
- Procedural Programming
- Limitations of Procedural Programming
- Why OOP was introduced
- Object-Oriented Programming
- Real-World Analogy
- Features of OOP
- Four Pillars of OOP

# What is a Class?

## Definition

A **Class** is a user-defined blueprint or template used to create objects.

A class defines:

- Attributes (Variables)
- Methods (Functions)

A class itself does not occupy significant memory for data. Memory is allocated only when an object is created.

---

## Syntax

```python
class ClassName:

    # Attributes

    # Methods
```

Example

```python
class Student:
    pass
```

Here,

- `Student` is the class name.
- `pass` is used because the class body is currently empty.

---

# What is an Object?

## Definition

An **Object** is an instance of a class.

It is a real entity created from the blueprint (class).

Each object has its own memory and can access the variables and methods defined inside the class.

---

## Real-World Example

Blueprint

↓

House Plan

↓

Actual House

Similarly,

Class

↓

Student

↓

Student Object

---

## Syntax

```python
object_name = ClassName()
```

Example

```python
student = Student()
```

Here,

- `student` is an object.
- `Student()` creates the object.

---

# Relationship Between Class and Object

```text
              Class

                │

                ▼

        Object Creation

                │

                ▼

             Object

         (Occupies Memory)
```

---

# What are Attributes?

Attributes are variables that belong to a class or an object.

They represent the properties of an object.

Example

```text
Student

↓

Roll Number

Name

Age

Marks
```

These are attributes of the Student object.

---

# What are Methods?

Methods are functions defined inside a class.

They represent the behavior of an object.

Example

```text
Student

↓

study()

writeExam()

displayResult()
```

---

# The self Keyword

## Definition

`self` is a reference to the current object.

It allows an object to access its own attributes and methods.

Whenever an object calls a method, Python automatically passes the object as the first argument.

---

## Example

```python
class Student:

    def display(self):
        print("Welcome")
```

When executed,

```python
student = Student()

student.display()
```

Python internally converts it into

```python
Student.display(student)
```

Therefore,

`self` refers to the object `student`.

---

# Internal Working of Object Creation

Consider

```python
student = Student()
```

Python performs the following steps internally.

```text
Load Class

↓

Allocate Memory

↓

Create Object

↓

Return Object Reference

↓

Store Reference in Variable
```

---

# Memory Representation

```text
student = Student()


student

   │

   ▼

+---------------------+

|  Student Object     |

+---------------------+

```

The variable stores the **reference** to the object, not the object itself.

---

# Program 1 – Creating a Simple Class

## Problem Statement

Write a Python program to create a class and an object.

---

## Program

```python
class Student:

    def display(self):
        print("Welcome to Python OOP")

student = Student()

student.display()
```

---

## Output

```text
Welcome to Python OOP
```

---

## Dry Run

```text
Step 1

Student class created.

↓

Step 2

student object created.

↓

Step 3

display() method called.

↓

Step 4

Message displayed.
```

---

## Algorithm

```text
START

Create class

Create method

Create object

Call method

STOP
```

---

## Pseudocode

```text
BEGIN

Create Student class

Create display() method

Create Student object

Call display()

END
```

---

## Line-by-Line Explanation

### Line 1

```python
class Student:
```

Creates a class named Student.

---

### Line 2

```python
def display(self):
```

Creates a method inside the class.

---

### Line 3

```python
print("Welcome to Python OOP")
```

Displays the message.

---

### Line 4

```python
student = Student()
```

Creates an object of the Student class.

---

### Line 5

```python
student.display()
```

Calls the method using the object.

---

# Program 2 – Student Information

```python
class Student:

    def details(self):

        print("Name : Rahul")

        print("Age  : 21")

student = Student()

student.details()
```

---

## Output

```text
Name : Rahul

Age  : 21
```

---

# Difference Between Class and Object

| Class | Object |
|--------|---------|
| Blueprint | Instance |
| Logical entity | Physical entity |
| No separate data memory | Occupies memory |
| Used to create objects | Created from a class |

---

# Advantages of Classes and Objects

- Better code organization.
- Reusability.
- Easy maintenance.
- Modular programming.
- Real-world modeling.
- Easy debugging.

---

# Real-Time Applications

Classes and objects are used in:

- Banking Systems
- Hospital Management
- Student Management
- Railway Reservation
- Inventory Systems
- E-Commerce Applications
- Library Management Systems

---

# Best Practices

- Use meaningful class names.
- Follow PascalCase for class names.
- Use meaningful method names.
- Keep one responsibility per class.
- Create reusable classes.

---

# Common Mistakes

## Forgetting to Create an Object

```python
class Student:

    def display(self):
        print("Hello")
```

No output will be produced until an object is created.

---

## Forgetting self

```python
class Student:

    def display():
        print("Hello")
```

This raises a `TypeError` because instance methods must include the `self` parameter.

---

## Calling Method Without Object

```python
display()
```

This results in a `NameError` because the method belongs to the class and should be called using an object.

---

# Interview Questions

## 1. What is Object-Oriented Programming?

### Answer

A programming paradigm that organizes programs using classes and objects.

---

## 2. What is a Class?

### Answer

A class is a blueprint used to create objects.

---

## 3. What is an Object?

### Answer

An object is an instance of a class.

---

## 4. What is the purpose of the self keyword?

### Answer

It refers to the current object and allows access to its attributes and methods.

---

## 5. Does a class occupy memory?

### Answer

A class definition exists in memory, but data for instances is allocated when objects are created.

---

## 6. What is the difference between a Class and an Object?

### Answer

A class is a blueprint, while an object is an actual instance created from that blueprint.

---

# Practice Programs

1. Create an Employee class and display employee details.
2. Create a Car class and display car information.
3. Create a Mobile class and print mobile specifications.
4. Create two objects of the same class.
5. Create a Book class with one method to display book details.

---

# Quick Revision

- OOP organizes programs using classes and objects.
- Class → Blueprint.
- Object → Instance of a class.
- Attributes store data.
- Methods define behavior.
- `self` refers to the current object.
- Objects occupy memory.
- OOP supports reusable and maintainable code.

---

# Chapter Summary

In this chapter, you learned:

- Programming Paradigms
- Procedural Programming
- Need for OOP
- Object-Oriented Programming
- Features of OOP
- Four Pillars of OOP
- Class
- Object
- Attributes
- Methods
- self Keyword
- Object Creation
- Memory Representation
- Internal Working
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs

