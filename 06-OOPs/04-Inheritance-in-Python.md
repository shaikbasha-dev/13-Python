# Inheritance in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is Inheritance?
5. Why is Inheritance Required?
6. Parent Class
7. Child Class
8. Terminologies Used in Inheritance
9. Types of Inheritance
10. Method Resolution Order (MRO)
11. super() Function
12. Advantages of Inheritance
13. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand Inheritance.
- Explain why Inheritance is required.
- Differentiate Parent and Child classes.
- Learn all types of Inheritance supported in Python.
- Understand Method Resolution Order (MRO).
- Learn the purpose of the super() function.
- Implement Inheritance in real-world applications.

---

# Prerequisites

Before learning this chapter, you should know:

- Classes
- Objects
- Constructors
- Encapsulation
- Abstraction

---

# Introduction

One of the biggest advantages of Object-Oriented Programming is **Code Reusability**.

Suppose we already have a class that contains common properties and methods.

Instead of creating another class from scratch, we can reuse the existing class.

This concept is known as **Inheritance**.

Inheritance allows one class to acquire the properties and methods of another class.

This reduces duplicate code and makes programs easier to maintain.

---

# What is Inheritance?

## Definition

**Inheritance** is the process by which one class acquires the properties and methods of another class.

The existing class is called the **Parent Class** (Base Class or Superclass).

The new class is called the **Child Class** (Derived Class or Subclass).

---

# Simple Definition

> Acquiring the properties and methods of one class into another class is called **Inheritance**.

---

# Why is Inheritance Required?

Imagine a company that has different types of employees.

Every employee has:

- Employee ID
- Employee Name
- Salary

Managers have additional information:

- Department

Developers have additional information:

- Programming Language

Instead of rewriting the common employee details in every class, we create a parent class called **Employee** and inherit it.

This avoids code duplication.

---

# Real-World Example

Consider a Vehicle.

Common properties:

- Brand
- Color
- Engine Number

Different vehicles have their own additional features.

Car

- Number of Doors

Bike

- Helmet Type

Bus

- Seating Capacity

Instead of rewriting the common properties, each class inherits them from the Vehicle class.

---

# Parent Class

A **Parent Class** is the class whose properties and methods are inherited.

It is also called:

- Base Class
- Super Class

Example

```python
class Person:
    pass
```

---

# Child Class

A **Child Class** is the class that inherits from another class.

It is also called:

- Derived Class
- Sub Class

Example

```python
class Student(Person):
    pass
```

Here,

- `Person` → Parent Class
- `Student` → Child Class

---

# Syntax of Inheritance

```python
class Parent:

    # Parent Members

class Child(Parent):

    # Child Members
```

---

# Terminologies Used in Inheritance

### Parent Class

The class whose members are inherited.

---

### Child Class

The class that inherits members.

---

### Inheritance Hierarchy

A relationship between Parent and Child classes.

---

### Code Reusability

Using existing code instead of writing it again.

---

### IS-A Relationship

Inheritance represents an **IS-A** relationship.

Examples:

```text
Car IS-A Vehicle

Dog IS-An Animal

Student IS-A Person
```

---

# Types of Inheritance

Python supports the following types of inheritance.

## 1. Single Inheritance

One Parent

↓

One Child

```text
Parent

↓

Child
```

---

## 2. Multiple Inheritance

One Child inherits from multiple Parent classes.

```text
Parent1

      ↘

       Child

      ↗

Parent2
```

---

## 3. Multilevel Inheritance

Inheritance continues through multiple levels.

```text
GrandParent

↓

Parent

↓

Child
```

---

## 4. Hierarchical Inheritance

Multiple Child classes inherit from the same Parent.

```text
        Parent

      ↙      ↘

 Child1      Child2
```

---

## 5. Hybrid Inheritance

A combination of multiple inheritance types.

Python supports Hybrid Inheritance because it supports Multiple Inheritance.

---

# Method Resolution Order (MRO)

When multiple inheritance is used,

Python must decide which method should execute first.

Python follows the **Method Resolution Order (MRO)**.

You can check the MRO using:

```python
ClassName.mro()
```

or

```python
help(ClassName)
```

Python follows the **C3 Linearization Algorithm** to determine the MRO.

---

# super() Function

The `super()` function allows a child class to access the members of its parent class.

It is commonly used to:

- Call Parent Constructors
- Call Parent Methods
- Avoid duplicate code

Example

```python
super().__init__()
```

---

# Advantages of Inheritance

- Code Reusability
- Reduced Code Duplication
- Easy Maintenance
- Easy Extension
- Better Code Organization
- Faster Development
- Supports Hierarchical Design

---

# Disadvantages of Inheritance

- Tight coupling between classes.
- Changes in the parent class may affect child classes.
- Incorrect hierarchy can make code difficult to maintain.

---

# Real-Time Applications

Inheritance is used in:

- Banking Systems
- Employee Management Systems
- Hospital Management Systems
- School Management Systems
- Game Development
- GUI Frameworks
- Django Framework
- Machine Learning Libraries

---

# Internal Working

```text
Parent Class Created

↓

Child Class Inherits Parent

↓

Child Object Created

↓

Search Child Members

↓

If Not Found

↓

Search Parent Members

↓

Execute Method
```

---

# Summary

In this part, we learned:

- Inheritance
- Need for Inheritance
- Parent Class
- Child Class
- Types of Inheritance
- IS-A Relationship
- Method Resolution Order (MRO)
- super() Function
- Advantages
- Internal Working


# Program 1 – Single Inheritance

## Problem Statement

Write a Python program to demonstrate Single Inheritance.

---

## Program

```python
class Person:

    def display(self):
        print("I am a Person")


class Student(Person):

    def study(self):
        print("Student is Studying")


student = Student()

student.display()

student.study()
```

---

## Output

```text
I am a Person
Student is Studying
```

---

## Explanation

- `Person` is the Parent Class.
- `Student` is the Child Class.
- The child class inherits the `display()` method from the parent class.

---

# Program 2 – Multiple Inheritance

## Problem Statement

Write a Python program to demonstrate Multiple Inheritance.

---

## Program

```python
class Father:

    def father_property(self):
        print("Father Property")


class Mother:

    def mother_property(self):
        print("Mother Property")


class Child(Father, Mother):

    def child_property(self):
        print("Child Property")


child = Child()

child.father_property()

child.mother_property()

child.child_property()
```

---

## Output

```text
Father Property
Mother Property
Child Property
```

---

## Explanation

The `Child` class inherits from both `Father` and `Mother`.

This is called **Multiple Inheritance**.

---

# Program 3 – Multilevel Inheritance

## Problem Statement

Write a Python program to demonstrate Multilevel Inheritance.

---

## Program

```python
class GrandParent:

    def grandparent(self):
        print("Grand Parent")


class Parent(GrandParent):

    def parent(self):
        print("Parent")


class Child(Parent):

    def child(self):
        print("Child")


obj = Child()

obj.grandparent()

obj.parent()

obj.child()
```

---

## Output

```text
Grand Parent
Parent
Child
```

---

## Explanation

The inheritance chain is

```text
GrandParent

↓

Parent

↓

Child
```

The child class inherits members from both its parent and grandparent.

---

# Program 4 – Hierarchical Inheritance

## Problem Statement

Write a Python program to demonstrate Hierarchical Inheritance.

---

## Program

```python
class Animal:

    def eat(self):
        print("Animal Eats")


class Dog(Animal):

    def bark(self):
        print("Dog Barks")


class Cat(Animal):

    def meow(self):
        print("Cat Meows")


dog = Dog()

cat = Cat()

dog.eat()

dog.bark()

cat.eat()

cat.meow()
```

---

## Output

```text
Animal Eats
Dog Barks
Animal Eats
Cat Meows
```

---

## Explanation

Both `Dog` and `Cat` inherit from the same parent class `Animal`.

---

# Program 5 – Using super()

## Problem Statement

Write a Python program to demonstrate the `super()` function.

---

## Program

```python
class Person:

    def display(self):
        print("Person Class")


class Student(Person):

    def display(self):

        super().display()

        print("Student Class")


student = Student()

student.display()
```

---

## Output

```text
Person Class
Student Class
```

---

## Explanation

`super()` calls the parent class method before executing the child class method.

---

# Program 6 – Method Resolution Order (MRO)

## Problem Statement

Write a Python program to demonstrate Method Resolution Order.

---

## Program

```python
class A:

    def show(self):
        print("Class A")


class B(A):

    def show(self):
        print("Class B")


class C(A):

    def show(self):
        print("Class C")


class D(B, C):
    pass


obj = D()

obj.show()

print(D.mro())
```

---

## Output

```text
Class B

[<class '__main__.D'>,
<class '__main__.B'>,
<class '__main__.C'>,
<class '__main__.A'>,
<class 'object'>]
```

---

## Explanation

Python follows the **Method Resolution Order (MRO)** to determine which method should execute first.

The search order is

```text
D

↓

B

↓

C

↓

A

↓

object
```

Since `B` appears before `C`, Python executes `B.show()`.

---

# Memory Representation

```text
        Parent Class

             ▲

             │

      Child Class

             ▲

             │

        Child Object
```

The child object can access:

- Child Members
- Parent Members

---

# Dry Run

```text
Create Parent Class

↓

Create Child Class

↓

Child inherits Parent

↓

Create Child Object

↓

Search Child Method

↓

If not found

↓

Search Parent Method

↓

Execute Method
```

---

# Advantages

- Code Reusability
- Reduced Code Duplication
- Easy Maintenance
- Better Organization
- Faster Development
- Extensible Design

---

# Best Practices

- Keep Parent Classes generic.
- Child Classes should extend, not duplicate.
- Prefer `super()` over direct parent method calls.
- Use inheritance only when an **IS-A** relationship exists.
- Avoid unnecessary deep inheritance hierarchies.

---

# Common Mistakes

## Mistake 1

Using inheritance where there is no IS-A relationship.

❌ Incorrect

```text
Car IS-A Engine
```

---

✅ Correct

```text
Car HAS-A Engine
```

This is composition, not inheritance.

---

## Mistake 2

Forgetting to call the parent constructor.

Always use

```python
super().__init__()
```

when the parent constructor performs important initialization.

---

## Mistake 3

Ignoring Method Resolution Order (MRO) in Multiple Inheritance.

Understanding MRO helps avoid unexpected behavior.

---

# Real-Time Applications

Inheritance is widely used in:

- Banking Systems
- Hospital Management Systems
- School Management Systems
- E-Commerce Applications
- Game Development
- GUI Applications
- Django Framework
- Machine Learning Libraries

---

# Interview Questions

## 1. What is Inheritance?

### Answer

Inheritance is the process of acquiring the properties and methods of one class into another class.

---

## 2. What are the different types of Inheritance?

### Answer

- Single Inheritance
- Multiple Inheritance
- Multilevel Inheritance
- Hierarchical Inheritance
- Hybrid Inheritance

---

## 3. What is a Parent Class?

### Answer

A Parent Class is the class whose members are inherited by another class.

---

## 4. What is a Child Class?

### Answer

A Child Class is the class that inherits the members of a Parent Class.

---

## 5. What is the purpose of `super()`?

### Answer

`super()` is used to access the parent class's methods and constructors without directly referring to the parent class name.

---

## 6. What is Method Resolution Order (MRO)?

### Answer

Method Resolution Order (MRO) is the order in which Python searches classes for methods and attributes during inheritance.

---

## 7. Which algorithm does Python use for MRO?

### Answer

Python uses the **C3 Linearization Algorithm**.

---

# Practice Programs

1. Create a Person and Student class using Single Inheritance.
2. Create Father, Mother, and Child classes using Multiple Inheritance.
3. Demonstrate Multilevel Inheritance using three classes.
4. Demonstrate Hierarchical Inheritance.
5. Use `super()` to call the parent method.
6. Display the MRO of a class using `mro()`.

---

# Quick Revision

- Inheritance enables code reuse.
- Parent Class → Base Class / Superclass.
- Child Class → Derived Class / Subclass.
- Inheritance represents an **IS-A** relationship.
- Python supports five types of inheritance.
- `super()` accesses parent class members.
- MRO determines the method lookup order.

---

# Chapter Summary

In this chapter, you learned:

- Inheritance
- Parent and Child Classes
- Types of Inheritance
- IS-A Relationship
- Method Resolution Order (MRO)
- `super()` Function
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
