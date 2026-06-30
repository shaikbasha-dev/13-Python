# Polymorphism in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is Polymorphism?
5. Why is Polymorphism Required?
6. Real-World Examples
7. Types of Polymorphism
8. Compile-Time Polymorphism
9. Run-Time Polymorphism
10. Method Overriding
11. Duck Typing
12. Operator Overloading
13. Method Overloading in Python
14. Internal Working
15. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand Polymorphism.
- Explain why Polymorphism is required.
- Differentiate Compile-Time and Run-Time Polymorphism.
- Understand Method Overriding.
- Learn Duck Typing.
- Understand Operator Overloading.
- Learn how Python achieves Polymorphism.

---

# Prerequisites

Before learning this chapter, you should know:

- Classes
- Objects
- Inheritance
- Methods
- Constructors

---

# Introduction

Object-Oriented Programming consists of four pillars.

- Encapsulation
- Abstraction
- Inheritance
- Polymorphism

The fourth pillar is **Polymorphism**.

The word **Polymorphism** comes from two Greek words.

```text
Poly

↓

Many

Morph

↓

Forms
```

Therefore,

**Polymorphism** means

> **One interface, many forms.**

The same method or operation behaves differently depending on the object that uses it.

---

# What is Polymorphism?

## Definition

**Polymorphism** is the ability of an object, method, or operator to perform different actions depending on the context.

The same method name can produce different behavior for different objects.

---

# Simple Definition

> One method behaving differently for different objects is called **Polymorphism**.

---

# Why is Polymorphism Required?

Suppose we have different animals.

Each animal makes a different sound.

```text
Dog

↓

Bark

Cat

↓

Meow

Cow

↓

Moo
```

Instead of creating different method names

```text
dogSound()

catSound()

cowSound()
```

we create one common method

```text
sound()
```

Each object provides its own implementation.

This makes the code easier to maintain and extend.

---

# Real-World Examples

## Example 1

Vehicle

```text
Start()
```

Car

↓

Starts using Key

Bike

↓

Starts using Self Start

Electric Car

↓

Starts using Push Button

---

## Example 2

Payment

```text
pay()
```

Credit Card

↓

Credit Card Payment

UPI

↓

UPI Payment

Net Banking

↓

Internet Banking Payment

The same method performs different actions.

---

# Types of Polymorphism

There are two major types of Polymorphism.

## 1. Compile-Time Polymorphism

Also called

- Static Binding
- Early Binding

Usually achieved through

- Method Overloading
- Operator Overloading

---

## 2. Run-Time Polymorphism

Also called

- Dynamic Binding
- Late Binding

Achieved through

- Method Overriding

Python mainly supports **Run-Time Polymorphism**.

---

# Compile-Time Polymorphism

In languages like Java and C++,

Compile-Time Polymorphism is achieved using

- Method Overloading

Python does not support true Method Overloading.

Instead,

Python achieves similar behavior using

- Default Arguments
- *args
- **kwargs

---

# Run-Time Polymorphism

Run-Time Polymorphism occurs when the method to execute is decided while the program is running.

This is achieved using

- Inheritance
- Method Overriding

Python strongly supports Run-Time Polymorphism.

---

# Method Overriding

Method Overriding occurs when a Child Class provides its own implementation of a Parent Class method.

Example

```python
class Animal:

    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog Barks")
```

The child class overrides the parent implementation.

---

# Duck Typing

Python follows the concept of **Duck Typing**.

Rule

```text
"If it walks like a duck
and
quacks like a duck,

it is treated as a duck."
```

Python focuses on an object's behavior instead of its type.

If an object provides the required method,

Python allows it to be used.

---

# Operator Overloading

Python allows existing operators to behave differently for user-defined objects.

Example

```python
+
```

Normally,

```python
10 + 20
```

adds integers.

Using

```python
__add__()
```

the same operator can work with custom objects.

---

# Method Overloading in Python

Python does not support true Method Overloading.

Instead,

similar behavior is achieved using

- Default Arguments
- *args
- **kwargs

---

# Internal Working

```text
Object Created

↓

Method Called

↓

Python Finds Object Type

↓

Corresponding Method Executes

↓

Output Produced
```

---

# Advantages of Polymorphism

- Improves flexibility.
- Reduces duplicate code.
- Supports code reusability.
- Easy maintenance.
- Easy extension.
- Cleaner program design.

---

# Real-Time Applications

Polymorphism is used in

- Banking Systems
- Payment Gateways
- GUI Frameworks
- Game Development
- Machine Learning Libraries
- Web Frameworks
- Database Drivers

---

# Summary

In this part, we learned:

- Polymorphism
- Need for Polymorphism
- Types of Polymorphism
- Compile-Time Polymorphism
- Run-Time Polymorphism
- Method Overriding
- Duck Typing
- Operator Overloading
- Internal Working


# Program 1 – Method Overriding

## Problem Statement

Write a Python program to demonstrate Method Overriding.

---

## Program

```python
class Animal:

    def sound(self):
        print("Animals make different sounds")


class Dog(Animal):

    def sound(self):
        print("Dog Barks")


dog = Dog()

dog.sound()
```

---

## Output

```text
Dog Barks
```

---

## Explanation

- `Animal` is the Parent Class.
- `Dog` is the Child Class.
- The `sound()` method in the child class overrides the parent's `sound()` method.
- Since the object belongs to `Dog`, the child method executes.

---

# Program 2 – Method Overriding using super()

## Problem Statement

Write a Python program to call both Parent and Child methods.

---

## Program

```python
class Animal:

    def sound(self):
        print("Animals make sounds")


class Dog(Animal):

    def sound(self):

        super().sound()

        print("Dog Barks")


dog = Dog()

dog.sound()
```

---

## Output

```text
Animals make sounds

Dog Barks
```

---

## Explanation

`super()` calls the parent class method first.

After the parent method completes,

the child method executes.

---

# Program 3 – Runtime Polymorphism

## Problem Statement

Write a Python program to demonstrate Runtime Polymorphism.

---

## Program

```python
class Bird:

    def fly(self):
        print("Bird Flies")


class Eagle(Bird):

    def fly(self):
        print("Eagle Flies High")


class Sparrow(Bird):

    def fly(self):
        print("Sparrow Flies Low")


birds = [Eagle(), Sparrow()]

for bird in birds:

    bird.fly()
```

---

## Output

```text
Eagle Flies High

Sparrow Flies Low
```

---

## Explanation

The same method

```python
fly()
```

behaves differently for different objects.

Python decides which method to execute at runtime.

---

# Program 4 – Duck Typing

## Problem Statement

Write a Python program to demonstrate Duck Typing.

---

## Program

```python
class Duck:

    def speak(self):
        print("Quack Quack")


class Human:

    def speak(self):
        print("Hello")


def call_speak(obj):

    obj.speak()


duck = Duck()

human = Human()

call_speak(duck)

call_speak(human)
```

---

## Output

```text
Quack Quack

Hello
```

---

## Explanation

The function

```python
call_speak()
```

does not check the object's type.

It simply calls

```python
speak()
```

If the object has a `speak()` method,

Python executes it.

This is Duck Typing.

---

# Program 5 – Operator Overloading

## Problem Statement

Write a Python program to overload the `+` operator.

---

## Program

```python
class Number:

    def __init__(self, value):

        self.value = value

    def __add__(self, other):

        return Number(self.value + other.value)


num1 = Number(10)

num2 = Number(20)

result = num1 + num2

print(result.value)
```

---

## Output

```text
30
```

---

## Explanation

Python converts

```python
num1 + num2
```

into

```python
num1.__add__(num2)
```

This is called **Operator Overloading**.

---

# Program 6 – Polymorphism without Inheritance

## Program

```python
class Car:

    def start(self):
        print("Car Started")


class Bike:

    def start(self):
        print("Bike Started")


def vehicle_start(vehicle):

    vehicle.start()


vehicle_start(Car())

vehicle_start(Bike())
```

---

## Output

```text
Car Started

Bike Started
```

---

## Explanation

Neither `Car` nor `Bike` inherits from a common parent.

However,

both provide the

```python
start()
```

method.

Python allows this because it focuses on an object's behavior rather than its type.

---

# Dry Run

```text
Create Object

↓

Call Method

↓

Python Identifies Object

↓

Corresponding Method Executes

↓

Output Displayed
```

---

# Memory Representation

```text
Animal

   ▲

   │

Dog

   │

Dog Object

↓

sound()

↓

Dog Barks
```

---

# Advantages

- Improves code flexibility.
- Promotes code reuse.
- Makes programs easier to extend.
- Reduces duplicate code.
- Supports dynamic behavior.
- Improves maintainability.

---

# Best Practices

- Use Method Overriding when child classes require different behavior.
- Prefer polymorphism over multiple conditional statements.
- Use meaningful method names.
- Use Duck Typing only when objects share common behavior.
- Avoid unnecessary inheritance.

---

# Common Mistakes

## Mistake 1

Changing the method name instead of overriding.

❌ Incorrect

```python
class Dog(Animal):

    def bark(self):
        pass
```

This is **not** Method Overriding.

---

## Mistake 2

Forgetting inheritance.

```python
class Dog:
```

Without inheritance,

Method Overriding cannot occur.

---

## Mistake 3

Confusing Method Overloading with Method Overriding.

| Method Overloading | Method Overriding |
|--------------------|-------------------|
| Same class | Parent and Child |
| Different parameters | Same parameters |
| Not directly supported | Fully supported |

---

## Mistake 4

Assuming Duck Typing requires inheritance.

Duck Typing depends on the presence of the required methods, not on inheritance.

---

# Real-Time Applications

Polymorphism is used in:

- Payment Gateway Systems
- Banking Applications
- GUI Frameworks
- Machine Learning Libraries
- Django Framework
- Flask Applications
- Game Development
- Data Processing Libraries

---

# Interview Questions

## 1. What is Polymorphism?

### Answer

Polymorphism is the ability of the same method or operation to perform different actions for different objects.

---

## 2. What are the types of Polymorphism?

### Answer

- Compile-Time Polymorphism
- Run-Time Polymorphism

Python mainly supports Runtime Polymorphism.

---

## 3. What is Method Overriding?

### Answer

Method Overriding occurs when a child class provides its own implementation of a parent class method.

---

## 4. What is Duck Typing?

### Answer

Duck Typing allows objects with the required methods to be used, regardless of their class or inheritance hierarchy.

---

## 5. Does Python support Method Overloading?

### Answer

Python does not support true Method Overloading.

Similar behavior is achieved using:

- Default Arguments
- `*args`
- `**kwargs`

---

## 6. What is Operator Overloading?

### Answer

Operator Overloading gives additional meaning to existing operators for user-defined objects using Magic Methods such as `__add__()`.

---

## 7. Why is Polymorphism important?

### Answer

Polymorphism increases flexibility, improves maintainability, reduces duplicate code, and makes applications easier to extend.

---

# Practice Programs

1. Demonstrate Method Overriding using Animal and Dog classes.
2. Create three payment classes implementing a common `pay()` method.
3. Demonstrate Duck Typing using different objects with the same method.
4. Overload the `+` operator using `__add__()`.
5. Create a Vehicle hierarchy demonstrating Runtime Polymorphism.

---

# Quick Revision

- Polymorphism means **One Interface, Many Forms**.
- Python mainly supports Runtime Polymorphism.
- Method Overriding is achieved using inheritance.
- Duck Typing depends on behavior, not type.
- Operator Overloading uses Magic Methods.
- Method Overloading is simulated using default arguments, `*args`, and `**kwargs`.

---

# Chapter Summary

In this chapter, we learned:

- Polymorphism
- Types of Polymorphism
- Compile-Time and Run-Time Polymorphism
- Method Overriding
- Duck Typing
- Operator Overloading
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
