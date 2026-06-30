# Method Chaining in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is Method Chaining?
5. Why is Method Chaining Required?
6. How Method Chaining Works
7. Returning self
8. Internal Working
9. Real-World Examples
10. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand Method Chaining.
- Explain why Method Chaining is used.
- Learn how methods return objects.
- Understand the use of the `self` keyword in Method Chaining.
- Write programs using Method Chaining.
- Understand Fluent Interface Design.

---

# Prerequisites

Before learning this chapter, you should know:

- Classes and Objects
- Methods
- self Keyword
- Constructors
- return Statement

---

# Introduction

In Python, one method can call another method by returning the current object.

This technique is known as **Method Chaining**.

Instead of calling methods one by one,

```python
obj.method1()
obj.method2()
obj.method3()
```

we can write

```python
obj.method1().method2().method3()
```

This makes the code shorter, cleaner, and easier to read.

---

# What is Method Chaining?

## Definition

**Method Chaining** is the process of calling multiple methods continuously using a single object.

Each method returns the current object (`self`), allowing the next method to be called immediately.

---

# Why is Method Chaining Required?

Suppose we are configuring a Mobile object.

Without Method Chaining

```python
mobile.set_brand("Samsung")
mobile.set_model("S25")
mobile.set_price(85000)
```

Using Method Chaining

```python
mobile.set_brand("Samsung")\
      .set_model("S25")\
      .set_price(85000)
```

The second approach is:

- More readable
- Easier to maintain
- Cleaner
- Professional

---

# How Method Chaining Works

Method chaining works because every method returns the current object.

Example

```python
return self
```

When a method returns `self`,

Python allows another method to be called immediately.

---

# Returning self

The `self` keyword refers to the current object.

Returning `self` means:

```python
return self
```

returns the current object reference.

Example

```python
class Demo:

    def show(self):

        print("Hello")

        return self
```

Now another method can be called immediately.

---

# Internal Working

Consider

```python
obj.method1().method2().method3()
```

Python internally performs

```text
method1()

↓

Returns self

↓

method2()

↓

Returns self

↓

method3()

↓

Program Ends
```

---

# Real-World Examples

Method Chaining is commonly used in

- Database Query Builders
- Web Frameworks
- Data Processing Libraries
- Configuration APIs
- Builder Design Pattern

Example

```python
query.select()\
     .where()\
     .order_by()
```

---

# Advantages

- Improves readability.
- Reduces code length.
- Supports Fluent Interface Design.
- Easy to maintain.
- Professional coding style.

---

# Summary

In this part, we learned:

- Method Chaining
- Why Method Chaining is required
- Returning `self`
- Internal Working
- Real-world applications


# Program 1 – Basic Method Chaining

## Problem Statement

Write a Python program to demonstrate Method Chaining.

---

## Program

```python
class Student:

    def display(self):

        print("Display Method")

        return self

    def show(self):

        print("Show Method")

        return self

    def finish(self):

        print("Finish Method")

student = Student()

student.display().show().finish()
```

---

## Output

```text
Display Method
Show Method
Finish Method
```

---

## Explanation

- `display()` executes first.
- It returns the current object using `return self`.
- The returned object calls `show()`.
- `show()` again returns the same object.
- Finally, `finish()` executes.

---

## Dry Run

```text
Student Object Created

↓

display()

↓

return self

↓

show()

↓

return self

↓

finish()

↓

Program Ends
```

---

# Program 2 – Method Chaining Using Student Details

## Problem Statement

Write a Python program to set and display student details using Method Chaining.

---

## Program

```python
class Student:

    def set_name(self, name):

        self.name = name

        return self

    def set_age(self, age):

        self.age = age

        return self

    def display(self):

        print("Name :", self.name)

        print("Age  :", self.age)

student = Student()

student.set_name("Rahul").set_age(21).display()
```

---

## Output

```text
Name : Rahul
Age  : 21
```

---

## Explanation

Each setter method returns the current object.

Therefore, another method can be called immediately.

---

# Program 3 – Method Chaining in Calculator

## Program

```python
class Calculator:

    def add(self, value):

        self.result = value

        return self

    def multiply(self, value):

        self.result *= value

        return self

    def display(self):

        print("Result :", self.result)

calculator = Calculator()

calculator.add(10).multiply(5).display()
```

---

## Output

```text
Result : 50
```

---

## Explanation

Execution Flow

```text
add()

↓

Result = 10

↓

multiply()

↓

Result = 50

↓

display()
```

---

# Program 4 – Method Chaining Without Returning self

## Program

```python
class Demo:

    def show(self):

        print("Hello")

demo = Demo()

demo.show().show()
```

---

## Output

```text
Hello

AttributeError:
'NoneType' object has no attribute 'show'
```

---

## Explanation

The `show()` method does not return `self`.

By default, every Python function returns `None`.

Therefore,

```python
demo.show()
```

returns

```python
None
```

Then Python tries

```python
None.show()
```

which produces an `AttributeError`.

---

# Memory Representation

```text
Student Object

        │

        ▼

+---------------------------+

display()

↓

return self

↓

show()

↓

return self

↓

finish()

+---------------------------+
```

---

# Internal Working

```text
Object Created

↓

Method Executes

↓

return self

↓

Current Object Returned

↓

Next Method Executes

↓

Chain Continues
```

---

# Fluent Interface

Method Chaining is the foundation of the **Fluent Interface Design Pattern**.

A Fluent Interface allows multiple methods to be called in a readable and expressive manner.

Example

```python
query.select()\
     .where()\
     .order_by()\
     .limit()
```

Many popular Python libraries use this approach.

---

# Advantages

- Cleaner code.
- Better readability.
- Professional coding style.
- Easy configuration.
- Supports reusable APIs.
- Reduces repeated object references.

---

# Best Practices

- Always return `self` when chaining is required.
- Keep methods focused on a single responsibility.
- Avoid creating very long chains that reduce readability.
- Use meaningful method names.
- Use chaining only where it improves clarity.

---

# Common Mistakes

## Mistake 1

Forgetting `return self`

❌ Incorrect

```python
class Demo:

    def show(self):

        print("Hello")
```

---

✅ Correct

```python
class Demo:

    def show(self):

        print("Hello")

        return self
```

---

## Mistake 2

Returning another object instead of `self`

Method chaining requires returning the current object.

---

## Mistake 3

Creating excessively long chains

```python
obj.a().b().c().d().e().f().g()
```

Although valid, very long chains may reduce readability.

---

# Real-Time Applications

Method Chaining is used in:

- Pandas Data Analysis
- SQL Query Builders
- Django ORM
- Flask Extensions
- Builder Design Pattern
- Machine Learning Pipelines
- Configuration APIs

---

# Interview Questions

## 1. What is Method Chaining?

### Answer

Method Chaining is the process of calling multiple methods continuously using the same object.

---

## 2. How is Method Chaining achieved?

### Answer

By returning the current object using:

```python
return self
```

---

## 3. Why is `return self` required?

### Answer

It returns the current object so that another method can be called immediately.

---

## 4. What happens if a method does not return `self`?

### Answer

The method returns `None` by default, causing an `AttributeError` if another method is chained.

---

## 5. What is a Fluent Interface?

### Answer

A Fluent Interface is a design pattern that uses Method Chaining to create readable and expressive APIs.

---

# Practice Programs

1. Create a Student class using Method Chaining.
2. Create a Calculator using Method Chaining.
3. Create an Employee class with chained setter methods.
4. Demonstrate the error caused by omitting `return self`.
5. Create a Product class using Fluent Interface style.

---

# Quick Revision

- Method Chaining calls multiple methods using one object.
- `return self` is essential.
- `self` returns the current object.
- Without `return self`, chaining fails.
- Method Chaining improves readability and code organization.
- Widely used in modern Python libraries.

---

# Chapter Summary

In this chapter, we learned:

- Method Chaining
- Why Method Chaining is used
- Returning `self`
- Internal Working
- Fluent Interface
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
