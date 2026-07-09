# Method Overloading in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is a Method?
5. What is Method Overloading?
6. Does Python Support Method Overloading?
7. Why Python Does Not Support Method Overloading
8. How Python Achieves Method Overloading
9. Using Default Arguments
10. Using *args
11. Using **kwargs
12. Method Overloading vs Method Overriding
13. Internal Working
14. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand Method Overloading.
- Explain why Python does not support true Method Overloading.
- Simulate Method Overloading using Python techniques.
- Differentiate Method Overloading and Method Overriding.
- Implement flexible methods using default arguments, *args, and **kwargs.

---

# Prerequisites

Before learning this chapter, you should know:

- Classes
- Objects
- Methods
- Constructors
- Constructor Overloading
- Polymorphism

---

# Introduction

Methods define the behavior of objects.

Sometimes,

we want the same method to perform different tasks depending on the number or type of arguments supplied.

For example,

a Calculator may perform addition using

```text
add()

add(a)

add(a, b)

add(a, b, c)
```

In Java,

this is called **Method Overloading**.

Python follows a different approach.

Instead of supporting multiple methods with the same name,

Python provides flexible programming features such as

- Default Arguments
- Variable-Length Arguments (`*args`)
- Keyword Arguments (`**kwargs`)

These features make Method Overloading unnecessary.

---

# What is a Method?

## Definition

A Method is a function defined inside a class that performs a specific operation on an object.

Example

```python
class Student:

    def display(self):

        print("Student Details")
```

Methods define the behavior of objects.

---

# What is Method Overloading?

## Definition

Method Overloading is the process of defining multiple methods with the **same name** but **different parameter lists** within the same class.

The appropriate method is selected based on the arguments supplied during the method call.

---

# Example (Java)

```java
class Calculator {

    void add() {}

    void add(int a) {}

    void add(int a, int b) {}

    void add(int a, int b, int c) {}

}
```

The compiler automatically selects the appropriate method.

---

# Does Python Support Method Overloading?

## Answer

**No.**

Python does **not support true Method Overloading**.

A class can have only one method with a particular name.

If multiple methods with the same name are declared,

the last definition replaces all previous definitions.

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

It does not differentiate methods based on

- Number of Parameters
- Type of Parameters

Instead,

Python encourages writing flexible methods using

- Default Arguments
- `*args`
- `**kwargs`

This makes separate overloaded methods unnecessary.

---

# How Python Achieves Method Overloading

Although Python does not support true Method Overloading,

similar behavior is achieved using:

- Default Arguments
- Variable-Length Arguments (`*args`)
- Keyword Arguments (`**kwargs`)

---

# Using Default Arguments

Default arguments make parameters optional.

Example

```python
class Calculator:

    def add(self, a, b=0):

        return a + b
```

Method Calls

```python
calculator.add(10)

calculator.add(10, 20)
```

---

# Using *args

`*args` accepts any number of positional arguments.

Example

```python
class Calculator:

    def add(self, *numbers):

        print(numbers)
```

Example Calls

```python
calculator.add()

calculator.add(10)

calculator.add(10, 20)

calculator.add(10, 20, 30)
```

---

# Using **kwargs

`**kwargs` accepts any number of keyword arguments.

Example

```python
class Student:

    def details(self, **kwargs):

        print(kwargs)
```

Example Calls

```python
student.details(name="Rahul")

student.details(name="Rahul", age=21)

student.details(name="Rahul", age=21, course="Python")
```

---

# Method Overloading vs Method Overriding

| Method Overloading | Method Overriding |
|--------------------|-------------------|
| Same Class | Parent and Child Classes |
| Same Method Name | Same Method Name |
| Different Parameter Lists | Same Parameter List |
| Compile-Time Concept | Run-Time Concept |
| Not directly supported in Python | Fully supported in Python |

---

# Internal Working

```text
Method Called

↓

Python Searches Method Name

↓

Last Method Definition Found

↓

Method Executes
```

If duplicate method names exist,

Python keeps only the last definition.

---

# Advantages of Python's Approach

- Flexible programming.
- Less code duplication.
- Easy maintenance.
- Cleaner class design.
- Supports dynamic argument handling.

---

# Real-Time Applications

Flexible methods are commonly used in:

- Calculator Applications
- Banking Systems
- Employee Management Systems
- Inventory Systems
- Data Processing Libraries
- Web Frameworks

---

# Summary

In this part, we learned:

- Methods
- Method Overloading
- Why Python does not support true Method Overloading
- Default Arguments
- `*args`
- `**kwargs`
- Method Overloading vs Method Overriding
- Internal Working


# Program 1 – Demonstrating That Python Does Not Support True Method Overloading

## Problem Statement

Write a Python program to demonstrate that Python does not support true Method Overloading.

---

## Program

```python
class Calculator:

    def add(self):
        print("First Method")

    def add(self, a):
        print("Second Method")
        print("Value :", a)


calculator = Calculator()

calculator.add(10)
```

---

## Output

```text
Second Method
Value : 10
```

---

## Explanation

Although two methods with the same name are declared,

Python keeps only the last method definition.

The first method is overwritten.

---

# Program 2 – Method Overloading using Default Arguments

## Problem Statement

Write a Python program to simulate Method Overloading using default arguments.

---

## Program

```python
class Calculator:

    def add(self, a, b=0):

        return a + b


calculator = Calculator()

print(calculator.add(10))

print(calculator.add(10, 20))
```

---

## Output

```text
10

30
```

---

## Explanation

When only one argument is supplied,

the default value of

```python
b = 0
```

is used.

---

# Program 3 – Method Overloading using *args

## Problem Statement

Write a Python program using *args.

---

## Program

```python
class Calculator:

    def add(self, *numbers):

        print(sum(numbers))


calculator = Calculator()

calculator.add()

calculator.add(10)

calculator.add(10, 20)

calculator.add(10, 20, 30)
```

---

## Output

```text
0

10

30

60
```

---

## Explanation

`*numbers` stores all positional arguments inside a tuple.

The built-in

```python
sum()
```

function calculates the total.

---

# Program 4 – Method Overloading using **kwargs

## Program

```python
class Student:

    def details(self, **kwargs):

        for key, value in kwargs.items():

            print(key, ":", value)


student = Student()

student.details(name="Rahul")

student.details(name="Rahul", age=21)

student.details(name="Rahul", age=21, course="Python")
```

---

## Output

```text
name : Rahul

name : Rahul
age : 21

name : Rahul
age : 21
course : Python
```

---

## Explanation

`**kwargs` stores keyword arguments inside a dictionary.

---

# Program 5 – Using Default Arguments and *args Together

## Program

```python
class Calculator:

    def add(self, a=0, *numbers):

        total = a + sum(numbers)

        print(total)


calculator = Calculator()

calculator.add()

calculator.add(10)

calculator.add(10, 20)

calculator.add(10, 20, 30)
```

---

## Output

```text
0

10

30

60
```

---

## Explanation

The first parameter has a default value.

Remaining values are stored inside `numbers`.

---

# Program 6 – Student Information Example

## Program

```python
class Student:

    def details(self, name, age=18, course="Python"):

        print("Name   :", name)

        print("Age    :", age)

        print("Course :", course)


student = Student()

student.details("Rahul")

student.details("Priya", 21)

student.details("Akhil", 22, "Java")
```

---

## Output

```text
Name   : Rahul
Age    : 18
Course : Python

Name   : Priya
Age    : 21
Course : Python

Name   : Akhil
Age    : 22
Course : Java
```

---

## Explanation

Default arguments provide flexibility without creating multiple methods.

---

# Program 7 – Employee Details using **kwargs

## Program

```python
class Employee:

    def display(self, **details):

        for key, value in details.items():

            print(key, ":", value)


employee = Employee()

employee.display(name="Rahul", salary=50000, department="HR")
```

---

## Output

```text
name : Rahul
salary : 50000
department : HR
```

---

## Explanation

Keyword arguments are useful when different objects contain different information.

---

# Program 8 – Calculator using Variable Number of Arguments

## Program

```python
class Calculator:

    def multiply(self, *numbers):

        result = 1

        for number in numbers:

            result *= number

        print(result)


calculator = Calculator()

calculator.multiply(2, 3)

calculator.multiply(2, 3, 4)
```

---

## Output

```text
6

24
```

---

## Explanation

`*args` allows the method to work with any number of arguments.

---

# Program 9 – Flexible Method

## Program

```python
class Demo:

    def show(self, *args, **kwargs):

        print("Positional :", args)

        print("Keyword :", kwargs)


demo = Demo()

demo.show(10, 20, name="Rahul", age=21)
```

---

## Output

```text
Positional : (10, 20)

Keyword : {'name': 'Rahul', 'age': 21}
```

---

## Explanation

Methods can accept both positional and keyword arguments together.

---

# Program 10 – Banking Example

## Program

```python
class Bank:

    def deposit(self, amount=0):

        print("Deposited :", amount)


bank = Bank()

bank.deposit()

bank.deposit(5000)
```

---

## Output

```text
Deposited : 0

Deposited : 5000
```

---

## Explanation

Default arguments make methods more flexible and eliminate the need for multiple overloaded methods.

---

# Dry Run

```text
Method Called

↓

Arguments Passed

↓

Method Parameters Matched

↓

Method Executes

↓

Output Produced
```

---

# Memory Representation

```text
Calculator Object

        │

        ▼

+---------------------------+

add()

multiply()

+---------------------------+
```

---

# Advantages

- Flexible methods.
- Cleaner code.
- Less duplication.
- Easy maintenance.
- Supports optional arguments.
- Improves readability.

---

# Best Practices

- Use default arguments when only a few parameters are optional.
- Use `*args` for variable-length positional arguments.
- Use `**kwargs` for optional keyword arguments.
- Keep methods focused on a single responsibility.
- Validate input before processing.

---

# Common Mistakes

## Mistake 1

Writing multiple methods with the same name.

❌ Incorrect

```python
def show():
    pass

def show(name):
    pass
```

Only the last method remains.

---

## Mistake 2

Using `*args` when fixed parameters are sufficient.

Choose the simplest approach that meets the requirement.

---

## Mistake 3

Using `**kwargs` without checking required keys.

Always validate expected keys before using them.

---

## Mistake 4

Confusing Method Overloading with Method Overriding.

Method Overloading

- Same class
- Different parameter lists

Method Overriding

- Parent and Child classes
- Same method signature

---

# Interview Questions

## 1. What is Method Overloading?

### Answer

Method Overloading is the process of creating multiple methods with the same name but different parameter lists.

---

## 2. Does Python support true Method Overloading?

### Answer

No.

Python allows only one method with a given name inside a class.

---

## 3. Why doesn't Python support Method Overloading?

### Answer

Python is dynamically typed and instead provides default arguments, `*args`, and `**kwargs` for flexible method definitions.

---

## 4. How can Method Overloading be simulated in Python?

### Answer

Using:

- Default Arguments
- `*args`
- `**kwargs`

---

## 5. What does `*args` store?

### Answer

A tuple containing positional arguments.

---

## 6. What does `**kwargs` store?

### Answer

A dictionary containing keyword arguments.

---

## 7. What happens if two methods have the same name?

### Answer

The last method definition replaces all previous ones.

---

## 8. What is the difference between Method Overloading and Method Overriding?

### Answer

Method Overloading occurs within the same class using different parameter lists.

Method Overriding occurs between parent and child classes using the same method signature.

---

## 9. When should you use default arguments?

### Answer

When only a few parameters are optional and predictable.

---

## 10. Give a real-world example of Method Overloading in Python.

### Answer

Calculator methods, Student information methods, Banking operations, Product configuration, and Employee management methods that accept optional parameters.

---

# Practice Programs

1. Create a Calculator using default arguments.
2. Create a Student class using `*args`.
3. Create an Employee class using `**kwargs`.
4. Create a Product class using both `*args` and `**kwargs`.
5. Demonstrate why multiple methods with the same name do not work in Python.

---

# Quick Revision

- Python supports only one method with a given name.
- Default arguments simulate optional parameters.
- `*args` stores positional arguments in a tuple.
- `**kwargs` stores keyword arguments in a dictionary.
- Method Overloading is simulated, not directly supported.

---

# Chapter Summary

In this chapter, we learned:

- Method Overloading
- Why Python does not support true Method Overloading
- Default Arguments
- `*args`
- `**kwargs`
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
