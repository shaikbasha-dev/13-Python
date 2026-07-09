# Abstraction in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is Abstraction?
5. Why is Abstraction Required?
6. Real-World Examples
7. Characteristics of Abstraction
8. Advantages of Abstraction
9. Abstraction vs Encapsulation
10. Achieving Abstraction in Python
11. Abstract Class
12. Abstract Method
13. abc Module
14. ABC Class
15. @abstractmethod Decorator
16. Internal Working
17. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand Abstraction.
- Explain why Abstraction is required.
- Differentiate Abstraction and Encapsulation.
- Understand Abstract Classes and Abstract Methods.
- Learn the `abc` module.
- Create Abstract Classes in Python.
- Implement Abstraction in real-world applications.

---

# Prerequisites

Before learning this chapter, you should know:

- Classes
- Objects
- Methods
- Inheritance
- Encapsulation

---

# Introduction

In the previous chapter, we learned **Encapsulation**, which combines data and methods into a single unit while controlling access to the data.

The second pillar of Object-Oriented Programming is **Abstraction**.

Abstraction focuses on **showing only the essential features** of an object while **hiding unnecessary implementation details**.

This makes programs easier to use, understand, and maintain.

---

# What is Abstraction?

## Definition

**Abstraction** is the process of hiding implementation details and exposing only the essential functionality to the user.

The user knows **what an object does**, but does not need to know **how it does it**.

---

# Simple Definition

> Showing only the required information and hiding the implementation details is called **Abstraction**.

---

# Why is Abstraction Required?

Suppose you are driving a car.

You use:

- Steering Wheel
- Accelerator
- Brake
- Clutch

Do you need to know:

- How the engine works?
- How fuel is injected?
- How the gearbox operates?

**No.**

You only use the controls.

The complex internal implementation remains hidden.

This is Abstraction.

---

# Real-World Examples

## ATM Machine

The user performs:

- Withdraw Money
- Deposit Money
- Check Balance

The user does not know how the bank server processes these operations internally.

---

## Mobile Phone

The user:

- Makes Calls
- Sends Messages
- Opens Applications

The internal processing remains hidden.

---

## Television Remote

The user presses:

- Power
- Volume
- Channel

The internal electronic circuits remain hidden.

---

# Characteristics of Abstraction

- Hides implementation details.
- Shows only essential functionality.
- Reduces complexity.
- Improves code readability.
- Makes software easier to maintain.

---

# Advantages of Abstraction

- Reduces code complexity.
- Improves security.
- Easier maintenance.
- Better code organization.
- Supports modular programming.
- Makes software reusable.

---

# Abstraction vs Encapsulation

| Abstraction | Encapsulation |
|-------------|---------------|
| Hides implementation | Hides data |
| Focuses on what an object does | Focuses on protecting data |
| Achieved using Abstract Classes and Interfaces | Achieved using Classes and Access Control |
| Simplifies usage | Improves security |

---

# Achieving Abstraction in Python

Python provides abstraction using the **abc** module.

Important components are:

- Abstract Class
- Abstract Method
- ABC
- @abstractmethod

---

# What is an Abstract Class?

## Definition

An **Abstract Class** is a class that cannot be instantiated directly.

It is designed to act as a blueprint for other classes.

It may contain:

- Abstract Methods
- Concrete (Normal) Methods

---

# What is an Abstract Method?

## Definition

An **Abstract Method** is a method that is declared but does not contain an implementation.

Every child class must implement the abstract method.

---

# abc Module

Python provides a built-in module named

```python
abc
```

which stands for

```text
Abstract Base Classes
```

It provides support for creating Abstract Classes.

---

# ABC Class

To create an Abstract Class,

inherit from

```python
ABC
```

Example

```python
from abc import ABC

class Vehicle(ABC):
    pass
```

---

# @abstractmethod Decorator

To declare an Abstract Method,

use

```python
@abstractmethod
```

Example

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass
```

Every child class must provide an implementation for `start()`.

---

# Internal Working

```text
Create Abstract Class

↓

Declare Abstract Method

↓

Create Child Class

↓

Override Abstract Method

↓

Create Child Object

↓

Call Implemented Method
```

---

# Summary

In this part, we learned:

- Abstraction
- Need for Abstraction
- Real-World Examples
- Abstract Class
- Abstract Method
- abc Module
- ABC
- @abstractmethod
- Internal Working


# Program 1 – Creating an Abstract Class

## Problem Statement

Write a Python program to create an Abstract Class.

---

## Program

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass
```

---

## Explanation

- `Vehicle` is an Abstract Class.
- `start()` is an Abstract Method.
- Since `Vehicle` contains an Abstract Method, objects of this class cannot be created.

---

# Program 2 – Implementing an Abstract Method

## Problem Statement

Write a Python program to implement an Abstract Method in a child class.

---

## Program

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car Started")


car = Car()

car.start()
```

---

## Output

```text
Car Started
```

---

## Explanation

The child class `Car` provides an implementation for the abstract method `start()`.

Since all abstract methods are implemented, an object of `Car` can be created.

---

# Program 3 – Creating an Object of an Abstract Class

## Problem Statement

Write a Python program to demonstrate that an Abstract Class cannot be instantiated.

---

## Program

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


vehicle = Vehicle()
```

---

## Output

```text
TypeError:
Can't instantiate abstract class Vehicle
with abstract method start
```

---

## Explanation

Python prevents creating objects of Abstract Classes.

Only child classes that implement all abstract methods can be instantiated.

---

# Program 4 – Multiple Abstract Methods

## Program

```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):

    def area(self):
        print("Area Calculated")

    def perimeter(self):
        print("Perimeter Calculated")


rectangle = Rectangle()

rectangle.area()

rectangle.perimeter()
```

---

## Output

```text
Area Calculated

Perimeter Calculated
```

---

## Explanation

An Abstract Class may contain multiple Abstract Methods.

The child class must implement **all** abstract methods.

---

# Program 5 – Abstract Class with Normal Methods

## Program

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("Animal is Sleeping")


class Dog(Animal):

    def sound(self):
        print("Dog Barks")


dog = Dog()

dog.sound()

dog.sleep()
```

---

## Output

```text
Dog Barks

Animal is Sleeping
```

---

## Explanation

An Abstract Class can contain:

- Abstract Methods
- Normal (Concrete) Methods

The child class inherits the normal methods.

---

# Dry Run

```text
Create Abstract Class

↓

Declare Abstract Method

↓

Create Child Class

↓

Override Abstract Method

↓

Create Child Object

↓

Call Method
```

---

# Memory Representation

```text
                Animal (ABC)

         +----------------------+

         | sound()              |

         | sleep()              |

         +----------------------+

                    ▲

                    │

              Dog Object

                    │

                    ▼

         +----------------------+

         | sound()              |

         +----------------------+
```

---

# Advantages of Abstraction

- Hides implementation details.
- Reduces code complexity.
- Improves maintainability.
- Encourages code reusability.
- Supports modular programming.
- Defines a common structure for child classes.

---

# Best Practices

- Use Abstract Classes when multiple child classes share common behavior.
- Declare only essential methods as abstract.
- Avoid unnecessary abstraction in small programs.
- Use meaningful method names.
- Keep common functionality in concrete methods.

---

# Common Mistakes

## Mistake 1

Creating an object of an Abstract Class.

❌ Incorrect

```python
vehicle = Vehicle()
```

Produces

```text
TypeError
```

---

## Mistake 2

Not implementing Abstract Methods.

```python
class Car(Vehicle):
    pass
```

The child class remains abstract and cannot be instantiated.

---

## Mistake 3

Forgetting to inherit from `ABC`.

```python
class Vehicle:
```

Without inheriting from `ABC`, Python will not treat the class as an Abstract Class.

---

## Mistake 4

Forgetting the `@abstractmethod` decorator.

Without the decorator, the method becomes a normal method instead of an abstract one.

---

# Real-Time Applications

Abstraction is used in:

- Payment Gateway Systems
- Banking Applications
- Vehicle Management Systems
- Hospital Management Systems
- GUI Frameworks
- Game Development
- Enterprise Software

---

# Interview Questions

## 1. What is Abstraction?

### Answer

Abstraction is the process of hiding implementation details while exposing only the essential functionality.

---

## 2. What is an Abstract Class?

### Answer

An Abstract Class is a class that cannot be instantiated directly and serves as a blueprint for child classes.

---

## 3. What is an Abstract Method?

### Answer

An Abstract Method is a method declared without implementation. Every child class must implement it.

---

## 4. Which module is used for Abstraction in Python?

### Answer

The built-in `abc` module.

---

## 5. What does `ABC` stand for?

### Answer

**Abstract Base Class**.

---

## 6. What is the purpose of the `@abstractmethod` decorator?

### Answer

It marks a method as abstract, requiring all child classes to provide an implementation.

---

## 7. Can an Abstract Class contain normal methods?

### Answer

Yes.

An Abstract Class can contain both abstract methods and normal (concrete) methods.

---

# Practice Programs

1. Create an Abstract Class named `Employee`.
2. Create an Abstract Class with two Abstract Methods.
3. Create a `Shape` Abstract Class and implement it using `Circle`.
4. Demonstrate that an Abstract Class cannot be instantiated.
5. Create an `Animal` Abstract Class with one abstract method and one normal method.

---

# Quick Revision

- Abstraction hides implementation details.
- Use the `abc` module for abstraction.
- Inherit from `ABC` to create an Abstract Class.
- Use `@abstractmethod` to declare Abstract Methods.
- Abstract Classes cannot be instantiated.
- Child classes must implement all Abstract Methods.

---

# Chapter Summary

In this chapter, you learned:

- Abstraction
- Need for Abstraction
- Abstract Classes
- Abstract Methods
- `abc` Module
- `ABC`
- `@abstractmethod`
- Internal Working
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
