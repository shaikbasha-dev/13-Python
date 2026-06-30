# Object-Oriented Programming (OOPs) in Python

## Learning Objectives

After completing this chapter, you will be able to:

- Understand Object-Oriented Programming (OOP).
- Explain why OOP is required.
- Understand Objects and Classes.
- Learn the advantages of OOP.
- Identify real-world examples of OOP.
- Create simple classes and objects in Python.

---

# Introduction

Object-Oriented Programming (OOP) is one of the most important programming paradigms.

Python supports Object-Oriented Programming, which helps developers build modular, reusable, and maintainable software.

Instead of writing programs as a collection of functions, OOP organizes programs using **objects** and **classes**.

Almost every modern software application uses Object-Oriented Programming.

---

# What is Object-Oriented Programming?

Object-Oriented Programming (OOP) is a programming paradigm in which programs are designed using **objects** and **classes**.

An object contains:

- Data (Attributes)
- Functions (Methods)

---

# Why Do We Need OOP?

Suppose we are developing a Student Management System.

Each student has:

- Roll Number
- Name
- Age
- Marks

Instead of creating separate variables for every student, we can create a **Student class**.

From that class, we can create multiple student objects.

This makes the program:

- Easy to understand
- Easy to maintain
- Reusable
- Scalable

---

# Real-Life Example

Consider a car.

Every car has:

- Brand
- Model
- Color
- Engine Number

And every car performs actions like:

- Start
- Stop
- Accelerate
- Brake

Here,

Car → Class

Individual Car → Object

---

# What is a Class?

A **Class** is a blueprint or template used to create objects.

A class defines:

- Attributes (Data Members)
- Methods (Member Functions)

---

# What is an Object?

An **Object** is an instance of a class.

Objects occupy memory and can access the data and methods defined inside the class.

---

# Relationship Between Class and Object

```text
           Class

             │

             ▼

      Create Object

             │

             ▼

          Object
```

---

# Syntax of a Class

```python
class ClassName:

    # Data Members

    # Methods
```

---

# Creating an Object

```python
object_name = ClassName()
```

---

# Program 1 : Creating a Class and Object

## Problem Statement

Write a Python program to create a class and an object.

---

## Program

```python
# Creating a class
class Student:

    # Creating a method
    def display(self):
        print("Welcome to Python OOP")

# Creating an object
student = Student()

# Calling the method
student.display()
```

---

## Output

```text
Welcome to Python OOP
```

---

## Pseudocode

```text
START

Create a class

Create a method

Create an object

Call the method

STOP
```

---

## Line-by-Line Explanation

### Line 1

```python
class Student:
```

Creates a class named `Student`.

---

### Line 2

```python
def display(self):
```

Defines a method inside the class.

---

### Line 3

```python
print("Welcome to Python OOP")
```

Displays a message.

---

### Line 4

```python
student = Student()
```

Creates an object of the `Student` class.

---

### Line 5

```python
student.display()
```

Calls the method using the object.

---

# Characteristics of OOP

- Programs are object-oriented.
- Supports code reusability.
- Supports modular programming.
- Easy to maintain.
- Easy to extend.

---

# Advantages of OOP

- Code Reusability
- Easy Maintenance
- Better Security
- Easy Debugging
- Modular Programming
- Real-World Modeling

---

# Real-Time Applications

Object-Oriented Programming is used in:

- Banking Applications
- Hospital Management Systems
- Student Management Systems
- E-Commerce Applications
- Airline Reservation Systems
- Library Management Systems

---

# Common Mistakes

## Forgetting to Create an Object

```python
class Student:

    def display(self):
        print("Hello")
```

This only creates a class.

Without creating an object, the method cannot be executed.

---

## Forgetting self

```python
class Student:

    def display():
        print("Hello")
```

This produces an error because instance methods must include the `self` parameter.

---

# Interview Questions

## 1. What is OOP?

### Answer

Object-Oriented Programming is a programming paradigm based on classes and objects.

---

## 2. What is a Class?

### Answer

A class is a blueprint used to create objects.

---

## 3. What is an Object?

### Answer

An object is an instance of a class.

---

## 4. Why is OOP used?

### Answer

OOP improves code reusability, modularity, maintainability, and scalability.

---

## 5. Which keyword is used to create a class in Python?

### Answer

The `class` keyword.

---

# Quick Revision

- OOP stands for Object-Oriented Programming.
- Class is a blueprint.
- Object is an instance of a class.
- Objects access class methods.
- OOP supports reusable and maintainable code.

---

# Summary

In this chapter, you learned:

- What Object-Oriented Programming is.
- Why OOP is required.
- What a Class is.
- What an Object is.
- Creating classes and objects.
- Advantages of OOP.
- Practical program.
- Interview questions.
