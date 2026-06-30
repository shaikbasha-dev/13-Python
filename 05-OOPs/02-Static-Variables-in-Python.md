# Static Variables in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. Variables in Object-Oriented Programming
5. What are Instance Variables?
6. What are Class Variables (Static Variables)?
7. Why are Static Variables Required?
8. Real-World Analogy
9. Instance Variables vs Class Variables
10. Namespace Concepts
11. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand variables used in OOP.
- Differentiate instance variables and class variables.
- Understand static variables.
- Explain namespace concepts.
- Understand memory allocation.
- Write programs using static variables.

---

# Prerequisites

Before learning this chapter, you should know:

- Classes
- Objects
- self keyword
- Methods

---

# Introduction

In the previous chapter, we learned how to create classes and objects.

A class becomes useful only when it stores data.

The data stored inside a class is called **variables**.

Python mainly provides two types of variables inside a class.

- Instance Variables
- Class Variables (Static Variables)

Understanding these variables is very important because they determine how data is stored and shared among objects.

---

# Variables in Object-Oriented Programming

Variables inside a class are used to store the state of an object.

Example

```text
Student

↓

Roll Number

Name

Age

College Name
```

Some values belong to each student individually.

Some values are common to every student.

This is why Python provides different types of variables.

---

# What are Instance Variables?

## Definition

Instance variables are variables whose values are different for every object.

Every object maintains its own separate copy of instance variables.

They are usually initialized inside the constructor (`__init__`) using the `self` keyword.

---

## Example

```python
class Student:

    def __init__(self, name, age):

        self.name = name

        self.age = age
```

Here,

`name`

and

`age`

are instance variables.

Every student object has its own values.

---

# Real-Life Example

Consider two students.

```text
Student 1

Name : Rahul

Age : 21


Student 2

Name : Priya

Age : 20
```

Although both belong to the same class,

their names and ages are different.

Therefore,

they are stored as **instance variables**.

---

# Characteristics of Instance Variables

- Belong to an object.
- Every object has its own copy.
- Created when an object is created.
- Accessed using the object or `self`.
- Stored inside the object's namespace.

---

# What are Class Variables?

## Definition

A **Class Variable** is a variable that belongs to the class itself rather than to individual objects.

Since one copy is shared by all objects, it is commonly called a **Static Variable**.

Unlike instance variables, class variables are declared directly inside the class body, outside all methods.

---

## Syntax

```python
class Student:

    college = "ABC Engineering College"
```

Here,

`college`

is a class variable.

Every object created from the `Student` class shares the same value.

---

# Why are Static Variables Required?

Suppose a college has

```text
500 Students
```

Every student belongs to

```text
ABC Engineering College
```

Should Python store

```text
ABC Engineering College
```

500 times?

No.

Instead,

Python stores it only once as a class variable.

Every object shares it.

This reduces memory usage and keeps the data consistent.

---

# Real-World Analogy

Imagine a company.

Every employee has

- Employee ID
- Name
- Salary

These are different for each employee.

But

Company Name

is the same for everyone.

```text
Employee

↓

Employee ID

Name

Salary

↓

Instance Variables


Company Name

↓

Class Variable
```

---

# Instance Variables vs Class Variables

| Instance Variables | Class Variables (Static Variables) |
|--------------------|------------------------------------|
| Belong to an object | Belong to the class |
| Separate copy for each object | Single shared copy |
| Declared using `self` | Declared inside class body |
| Stored in object namespace | Stored in class namespace |
| Can have different values | Same value shared by all objects |

---

# Namespace Concepts

To understand variables correctly, we must understand **Namespaces**.

A namespace is a container that stores names and their corresponding objects.

Python provides several namespaces.

- Built-in Namespace
- Global Namespace
- Local Namespace
- Class Namespace
- Object (Instance) Namespace

For this chapter, the important namespaces are:

## Class Namespace

Stores

- Class Variables
- Class Methods

There is only one class namespace for a class.

---

## Object Namespace

Every object has its own namespace.

It stores

- Instance Variables

Each object has a separate namespace.

---

# Memory Representation

Suppose

```python
class Student:

    college = "ABC College"
```

Two objects are created.

```python
student1 = Student()

student2 = Student()
```

Internally,

```text
                Student Class

        +--------------------------+

        | college = ABC College    |

        +--------------------------+

             ▲              ▲

             │              │

      student1        student2


Object Namespace     Object Namespace

(name, age)          (name, age)
```

Notice

There is only **one copy** of

```text
college
```

shared by both objects.

---

# Internal Working

When Python executes

```python
student = Student()
```

it performs the following steps.

```text
Load Class

↓

Read Class Variables

↓

Create Object

↓

Allocate Object Namespace

↓

Initialize Instance Variables

↓

Return Object Reference
```

---

# Summary

In this part, we learned:

- Variables in OOP
- Instance Variables
- Class Variables (Static Variables)
- Why Static Variables are needed
- Difference between Instance and Class Variables
- Namespace Concepts
- Memory Representation
- Internal Working

# Program 1 – Instance Variables

## Problem Statement

Write a Python program to demonstrate Instance Variables.

---

## Program

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Rahul", 21)
student2 = Student("Priya", 20)

print(student1.name, student1.age)
print(student2.name, student2.age)
```

---

## Output

```text
Rahul 21
Priya 20
```

---

## Dry Run

```text
Step 1

Student class is loaded.

↓

Step 2

student1 object is created.

↓

Object Namespace

name = Rahul

age = 21

↓

Step 3

student2 object is created.

↓

Object Namespace

name = Priya

age = 20

↓

Step 4

Both objects display their own data.
```

---

## Memory Representation

```text
                Student Class

             +--------------+

             | __init__()   |

             +--------------+

                 ▲      ▲

                 │      │

      ----------------------------

      student1

      name = Rahul

      age  = 21

      ----------------------------

      student2

      name = Priya

      age  = 20
```

---

## Line-by-Line Explanation

### Line 1

```python
class Student:
```

Creates the Student class.

---

### Line 2

```python
def __init__(self, name, age):
```

Defines the constructor.

---

### Line 3

```python
self.name = name
```

Creates an instance variable called `name`.

---

### Line 4

```python
self.age = age
```

Creates another instance variable called `age`.

---

### Line 5

```python
student1 = Student("Rahul", 21)
```

Creates the first object.

---

### Line 6

```python
student2 = Student("Priya", 20)
```

Creates the second object.

Each object stores different values.

---

# Program 2 – Static (Class) Variable

## Problem Statement

Write a Python program to demonstrate Static Variables.

---

## Program

```python
class Student:

    college = "ABC Engineering College"

student1 = Student()
student2 = Student()

print(student1.college)
print(student2.college)
```

---

## Output

```text
ABC Engineering College

ABC Engineering College
```

---

## Dry Run

```text
Student class loaded

↓

Class Variable created

↓

college

↓

ABC Engineering College

↓

student1 created

↓

student2 created

↓

Both objects access the same variable.
```

---

## Memory Representation

```text
               Student Class

+------------------------------------+

college

↓

ABC Engineering College

+------------------------------------+

        ▲                    ▲

        │                    │

   student1             student2
```

Notice that only **one copy** of `college` exists.

---

# Program 3 – Modifying Static Variable

```python
class Student:

    college = "ABC College"

student1 = Student()
student2 = Student()

Student.college = "XYZ University"

print(student1.college)
print(student2.college)
```

---

## Output

```text
XYZ University

XYZ University
```

---

## Explanation

The class variable belongs to the class.

Changing it using the class name updates the value for every object.

---

# Program 4 – Instance Variable vs Static Variable

```python
class Student:

    college = "ABC College"

    def __init__(self, name):
        self.name = name

student1 = Student("Rahul")
student2 = Student("Priya")

print(student1.name)
print(student2.name)

print(student1.college)
print(student2.college)
```

---

## Output

```text
Rahul

Priya

ABC College

ABC College
```

---

## Explanation

Instance Variable

```text
name
```

Different for every object.

Static Variable

```text
college
```

Same for every object.

---

# Program 5 – Accessing Static Variable

```python
class Student:

    college = "ABC College"

print(Student.college)
```

---

## Output

```text
ABC College
```

---

## Explanation

Static variables can be accessed directly using the class name.

This is the recommended approach.

---

# Best Practices

- Use instance variables for object-specific data.
- Use class variables only for common data.
- Access class variables using the class name.
- Avoid modifying class variables through objects unless necessary.
- Use meaningful variable names.

---

# Common Mistakes

## Mistake 1

Creating common data as an instance variable.

❌ Incorrect

```python
class Student:

    def __init__(self):
        self.college = "ABC College"
```

Every object stores its own copy.

---

✅ Correct

```python
class Student:

    college = "ABC College"
```

Only one copy is stored.

---

## Mistake 2

Modifying a class variable through an object.

```python
student.college = "XYZ"
```

This creates an **instance variable** named `college` for that object instead of modifying the class variable.

Prefer:

```python
Student.college = "XYZ"
```

---

# Real-Time Applications

Static Variables are used in:

- Company Name
- College Name
- Bank Name
- GST Percentage
- Currency Symbol
- Application Version
- Tax Rate
- Organization Details

---

# Interview Questions

## 1. What is an Instance Variable?

### Answer

An instance variable belongs to an object. Every object has its own separate copy.

---

## 2. What is a Static Variable?

### Answer

A static variable (class variable) belongs to the class and is shared by all objects.

---

## 3. Where are Instance Variables stored?

### Answer

Inside the object (instance) namespace.

---

## 4. Where are Class Variables stored?

### Answer

Inside the class namespace.

---

## 5. Which variable saves memory?

### Answer

Static (Class) Variables because only one copy is created.

---

## 6. Can a Static Variable be modified?

### Answer

Yes.

It is recommended to modify it using the class name.

---

## Practice Programs

1. Create an Employee class with employee name as an instance variable and company name as a class variable.
2. Create three Student objects and display a common college name.
3. Change the class variable and observe the output.
4. Print a class variable using both the class name and an object.
5. Demonstrate the difference between instance and class variables.

---

# Quick Revision

- Instance Variables belong to objects.
- Class Variables belong to the class.
- Class Variables are also called Static Variables.
- Every object has its own instance namespace.
- The class has one class namespace.
- Class variables reduce memory usage.
- Access static variables using the class name.
- Modify static variables using the class name.

---

# Chapter Summary

In this chapter, we learned:

- Variables in OOP
- Instance Variables
- Static (Class) Variables
- Why Static Variables are required
- Instance Variables vs Static Variables
- Namespace Concepts
- Memory Representation
- Internal Working
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision

