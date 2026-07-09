# Static Variables (Class Variables) in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What are Variables in Python OOP?
5. Types of Variables
6. What is an Instance Variable?
7. What is a Static Variable (Class Variable)?
8. Why are Static Variables Required?
9. Instance Variables vs Static Variables
10. Namespace Concepts
11. Accessing Static Variables
12. Modifying Static Variables
13. Internal Working
14. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand Variables in OOP.
- Differentiate Instance Variables and Static Variables.
- Learn Class Variables.
- Understand Namespace Concepts.
- Learn how Python stores variables in memory.
- Access and modify Static Variables correctly.

---

# Prerequisites

Before learning this chapter, you should know:

- Classes
- Objects
- Methods
- Constructors
- Access Specifiers

---

# Introduction

When we create objects in Python,

every object stores its own data.

Sometimes,

certain data should be shared by every object.

For example,

consider a College.

Every Student has

- Name
- Roll Number
- Marks

These values differ for every student.

However,

the

```text
College Name

College Address

University Name
```

remain the same for every student.

Instead of storing identical information inside every object,

Python stores it only once.

This is called a **Static Variable** or **Class Variable**.

---

# What are Variables in Python OOP?

Variables are used to store data.

In Object-Oriented Programming,

variables are mainly divided into two types.

- Instance Variables
- Static Variables (Class Variables)

---

# Types of Variables

## 1. Instance Variables

Belong to an individual object.

Every object has its own copy.

Example

```text
Student1

Name → Rahul

Age → 21

-------------------

Student2

Name → Priya

Age → 20
```

Each object stores different values.

---

## 2. Static Variables (Class Variables)

Belong to the class.

Only one copy exists.

Every object shares that copy.

Example

```text
College Name

↓

KodNest
```

Every Student object uses the same value.

---

# What is an Instance Variable?

## Definition

An Instance Variable belongs to an object.

A separate copy is created for every object.

Instance Variables are declared using

```python
self
```

Example

```python
class Student:

    def __init__(self):

        self.name = "Rahul"
```

---

# What is a Static Variable?

## Definition

A Static Variable is a variable that belongs to the class rather than individual objects.

Only one copy exists,

and every object shares it.

Static Variables are also called

- Class Variables

---

## Syntax

```python
class Student:

    college = "KodNest"
```

Here,

```python
college
```

is a Static Variable.

---

# Why are Static Variables Required?

Suppose there are

```text
1000 Students
```

Should every object store

```text
College Name

University Name

Country
```

1000 times?

**No.**

Only one copy is sufficient.

This reduces memory usage.

---

# Real-World Example

Employee

Instance Variables

```text
Employee ID

Employee Name

Salary
```

Static Variables

```text
Company Name

Company Address

CEO Name
```

Every employee belongs to the same company.

---

# Instance Variables vs Static Variables

| Instance Variable | Static Variable |
|-------------------|-----------------|
| Belongs to Object | Belongs to Class |
| Separate Copy for Every Object | One Copy Shared by All Objects |
| Created during Object Creation | Created when the Class is Loaded |
| Accessed using Object | Accessed using Class or Object |
| Uses `self` | Declared inside Class Body |

---

# Namespace Concepts

Python maintains different namespaces.

## Local Namespace

Variables inside a function.

---

## Global Namespace

Variables declared outside functions and classes.

---

## Class Namespace

Contains

- Static Variables
- Class Methods

---

## Object Namespace

Contains

- Instance Variables

Every object has its own namespace.

---

# Accessing Static Variables

Static Variables can be accessed using

## 1. Class Name

```python
Student.college
```

---

## 2. Object Reference

```python
student.college
```

Although both work,

using the **Class Name** is recommended because it clearly indicates that the variable belongs to the class.

---

# Modifying Static Variables

Static Variables should normally be modified using the Class Name.

Example

```python
Student.college = "OpenAI University"
```

This updates the value for all objects.

---

# Internal Working

```text
Class Loaded

↓

Static Variables Created

↓

Object Created

↓

Instance Variables Created

↓

Object Accesses Static Variable

↓

Shared Copy Returned
```

---

# Memory Representation

```text
                Student Class

        +------------------------+

        college

        ↓

      "KodNest"

        +------------------------+

             ▲          ▲

             │          │

      Student1      Student2

         │              │

       name          name

       age           age
```

---

# Advantages of Static Variables

- Saves memory.
- Reduces duplicate data.
- Easy to maintain.
- Shared among all objects.
- Faster access.
- Improves consistency.

---

# Disadvantages of Static Variables

- Shared modifications affect every object.
- Should not be used for object-specific data.

---

# Real-Time Applications

Static Variables are used in:

- Company Information
- College Information
- Bank Information
- Tax Rates
- Currency Symbols
- Application Configuration
- Database Connection Settings

---

# Summary

In this part, you learned:

- Variables in OOP
- Instance Variables
- Static Variables
- Namespace Concepts
- Memory Representation
- Accessing Static Variables
- Modifying Static Variables
- Advantages
- Real-Time Applications


# Program 1 – Creating a Static Variable

## Problem Statement

Write a Python program to create and access a Static Variable.

---

## Program

```python
class Student:

    college = "KodNest"

student1 = Student()

student2 = Student()

print(student1.college)

print(student2.college)
```

---

## Output

```text
KodNest

KodNest
```

---

## Explanation

`college` is a Static Variable.

Only one copy exists.

Both objects access the same variable.

---

# Program 2 – Creating Instance Variables

## Problem Statement

Write a Python program to create Instance Variables.

---

## Program

```python
class Student:

    college = "KodNest"

    def __init__(self, name):

        self.name = name

student1 = Student("Rahul")

student2 = Student("Priya")

print(student1.name)

print(student2.name)
```

---

## Output

```text
Rahul

Priya
```

---

## Explanation

`name` is an Instance Variable.

Each object stores its own copy.

---

# Program 3 – Static Variable and Instance Variable Together

## Program

```python
class Student:

    college = "KodNest"

    def __init__(self, name):

        self.name = name

student1 = Student("Rahul")

student2 = Student("Priya")

print(student1.name, student1.college)

print(student2.name, student2.college)
```

---

## Output

```text
Rahul KodNest

Priya KodNest
```

---

## Explanation

Every object has its own

```python
name
```

but both objects share

```python
college
```

---

# Program 4 – Accessing Static Variables using Class Name

## Program

```python
class Student:

    college = "KodNest"

print(Student.college)
```

---

## Output

```text
KodNest
```

---

## Explanation

This is the recommended way to access Static Variables.

---

# Program 5 – Modifying Static Variable using Class Name

## Program

```python
class Student:

    college = "KodNest"

student1 = Student()

student2 = Student()

Student.college = "OpenAI University"

print(student1.college)

print(student2.college)

print(Student.college)
```

---

## Output

```text
OpenAI University

OpenAI University

OpenAI University
```

---

## Explanation

Changing the Static Variable using the class updates the shared value for all objects.

---

# Program 6 – Modifying Static Variable using an Object

## Program

```python
class Student:

    college = "KodNest"

student1 = Student()

student2 = Student()

student1.college = "ABC College"

print(student1.college)

print(student2.college)

print(Student.college)
```

---

## Output

```text
ABC College

KodNest

KodNest
```

---

## Explanation

This is one of the most confusing interview questions.

When we write

```python
student1.college = "ABC College"
```

Python **does not modify the Static Variable**.

Instead,

Python creates a new **Instance Variable** named

```python
college
```

inside `student1`.

Now,

```text
student1

↓

Instance Variable

↓

college = ABC College
```

while

```text
Student Class

↓

Static Variable

↓

college = KodNest
```

and

```text
student2

↓

Uses Static Variable
```

remain unchanged.

---

# Program 7 – Checking Namespaces

## Program

```python
class Student:

    college = "KodNest"

    def __init__(self, name):

        self.name = name

student = Student("Rahul")

print(Student.__dict__)

print(student.__dict__)
```

---

## Output (Simplified)

```text
Class Namespace

{

'college': 'KodNest'

...
}

Object Namespace

{

'name': 'Rahul'

}
```

---

## Explanation

`__dict__` displays the namespace.

Class Namespace stores

- Static Variables
- Methods

Object Namespace stores

- Instance Variables

---

# Program 8 – Counting Objects using Static Variable

## Program

```python
class Student:

    count = 0

    def __init__(self):

        Student.count += 1

Student()

Student()

Student()

print(Student.count)
```

---

## Output

```text
3
```

---

## Explanation

Every time an object is created,

the Static Variable

```python
count
```

is incremented.

This is a common real-world use of Static Variables.

---

# Program 9 – Employee Example

## Program

```python
class Employee:

    company = "OpenAI"

    def __init__(self, name):

        self.name = name

employee1 = Employee("Rahul")

employee2 = Employee("Priya")

print(employee1.company)

print(employee2.company)
```

---

## Output

```text
OpenAI

OpenAI
```

---

# Program 10 – Bank Interest Rate

## Program

```python
class Bank:

    interest_rate = 7.5

customer1 = Bank()

customer2 = Bank()

print(customer1.interest_rate)

print(customer2.interest_rate)
```

---

## Output

```text
7.5

7.5
```

---

## Explanation

Interest rate is common to every customer.

Hence,

it is represented using a Static Variable.

---

# Dry Run

```text
Class Loaded

↓

Static Variable Created

↓

Object Created

↓

Instance Variable Created

↓

Object Searches

↓

Object Namespace

↓

If Not Found

↓

Class Namespace

↓

Value Returned
```

---

# Internal Working

```text
Student Object

↓

Search Object Namespace

↓

Found?

↓

Yes → Return Value

↓

No

↓

Search Class Namespace

↓

Return Static Variable
```

---

# Memory Representation

```text
                Student Class

+--------------------------------+

college

↓

KodNest

count

↓

2

+--------------------------------+

      ▲                 ▲

      │                 │

Student1           Student2

│                   │

name                name

↓

Rahul               Priya
```

---

# Advantages

- Saves memory.
- One shared copy.
- Easy maintenance.
- Suitable for common data.
- Improves consistency.
- Faster access.

---

# Best Practices

- Declare Static Variables inside the class body.
- Access Static Variables using the Class Name.
- Use Static Variables only for common data.
- Do not store object-specific information in Static Variables.
- Modify Static Variables using the Class Name.

---

# Common Mistakes

## Mistake 1

Changing Static Variables using an object.

```python
student.college = "ABC"
```

This creates an Instance Variable.

---

## Mistake 2

Using Static Variables for object-specific data.

Incorrect

```python
company

salary

name
```

Only

```python
company
```

should be static.

---

## Mistake 3

Confusing Class Namespace with Object Namespace.

Always remember

```text
Class Namespace

↓

Static Variables

Object Namespace

↓

Instance Variables
```

---

# Interview Questions

## 1. What is a Static Variable?

### Answer

A Static Variable is a variable that belongs to the class and is shared by all objects.

---

## 2. What is another name for a Static Variable?

### Answer

Class Variable.

---

## 3. Where are Static Variables stored?

### Answer

Inside the Class Namespace.

---

## 4. Where are Instance Variables stored?

### Answer

Inside the Object Namespace.

---

## 5. How many copies of a Static Variable exist?

### Answer

Only one copy.

---

## 6. How many copies of an Instance Variable exist?

### Answer

One copy per object.

---

## 7. What happens when a Static Variable is modified using an object?

### Answer

Python creates a new Instance Variable instead of modifying the Class Variable.

---

## 8. What is the recommended way to access Static Variables?

### Answer

Using the Class Name.

---

## 9. Which method displays the namespace?

### Answer

`__dict__`

---

## 10. Give some real-world examples of Static Variables.

### Answer

- Company Name
- College Name
- Bank Name
- Interest Rate
- GST Percentage
- Currency Symbol

---

# Practice Programs

1. Create a Student class with a Static Variable.
2. Count objects using a Static Variable.
3. Demonstrate Class Namespace and Object Namespace.
4. Modify a Static Variable using the Class Name.
5. Show the difference between Instance Variables and Static Variables.

---

# Quick Revision

- Static Variable = Class Variable.
- One copy per class.
- Shared among all objects.
- Declared inside the class body.
- Stored in the Class Namespace.
- Access using the Class Name.
- Instance Variables belong to objects.
- `__dict__` displays namespaces.

---

# Chapter Summary

In this chapter, we learned:

- Static Variables
- Instance Variables
- Class Variables
- Namespace Concepts
- Accessing Static Variables
- Modifying Static Variables
- Class Namespace
- Object Namespace
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
