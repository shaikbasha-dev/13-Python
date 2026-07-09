# Method Chaining in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is Method Chaining?
5. Why is Method Chaining Required?
6. How Method Chaining Works
7. Returning self
8. Fluent Interface
9. Method Chaining vs Constructor Chaining
10. Internal Working
11. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand Method Chaining.
- Explain why Method Chaining is required.
- Learn how Method Chaining works.
- Understand the importance of returning `self`.
- Create Fluent Interfaces.
- Differentiate Method Chaining and Constructor Chaining.

---

# Prerequisites

Before learning this chapter, you should know:

- Classes
- Objects
- Methods
- Constructors
- Constructor Chaining
- self Keyword

---

# Introduction

In Object-Oriented Programming,

an object usually contains multiple methods.

Normally,

we call methods one after another.

Example

```python
student.set_name("Rahul")

student.set_age(21)

student.display()
```

Although this works correctly,

it can become lengthy when many methods are involved.

Python provides a cleaner approach called **Method Chaining**.

Method Chaining allows multiple methods to be called in a single statement.

---

# What is Method Chaining?

## Definition

**Method Chaining** is the process of calling multiple methods one after another using the same object in a single statement.

This is possible when each method returns the current object using

```python
return self
```

---

# Simple Definition

> Calling multiple methods continuously using the same object is called **Method Chaining**.

---

# Why is Method Chaining Required?

Suppose we are creating a Student object.

Without Method Chaining,

we write

```python
student.set_name("Rahul")

student.set_age(21)

student.set_course("Python")

student.display()
```

Using Method Chaining,

the same code becomes

```python
student.set_name("Rahul")\
       .set_age(21)\
       .set_course("Python")\
       .display()
```

This improves readability and makes the code more expressive.

---

# How Method Chaining Works

Method Chaining works because every method returns

```python
self
```

The returned object immediately calls the next method.

Flow

```text
Method 1

↓

returns self

↓

Method 2

↓

returns self

↓

Method 3

↓

returns self

↓

Next Method
```

---

# Returning self

The most important requirement for Method Chaining is

```python
return self
```

Example

```python
class Student:

    def set_name(self, name):

        self.name = name

        return self
```

Without

```python
return self
```

Method Chaining is not possible.

---

# Fluent Interface

A programming style where methods return the current object to allow continuous method calls is called a **Fluent Interface**.

Many modern frameworks use this design pattern.

Examples include:

- Django ORM
- Pandas
- SQLAlchemy
- PySpark
- Selenium WebDriver

---

# Method Chaining vs Constructor Chaining

| Method Chaining | Constructor Chaining |
|-----------------|----------------------|
| Calls multiple methods | Calls multiple constructors |
| Uses `return self` | Uses `super()` |
| Improves readability | Initializes parent objects |
| Happens after object creation | Happens during object creation |

---

# Real-World Example

Consider Online Shopping.

Instead of writing

```text
Select Product

Add to Cart

Apply Coupon

Proceed to Checkout

Make Payment
```

as separate disconnected actions,

many APIs allow

```text
selectProduct()

↓

addToCart()

↓

applyCoupon()

↓

checkout()

↓

pay()
```

This resembles Method Chaining.

---

# Internal Working

```text
Object Created

↓

Method Called

↓

Method Returns self

↓

Next Method Called

↓

Method Returns self

↓

Next Method Called

↓

Execution Complete
```

---

# Advantages

- Cleaner code.
- Better readability.
- Reduces repeated object references.
- Supports Fluent Interfaces.
- Makes APIs easier to use.

---

# Real-Time Applications

Method Chaining is used in:

- Django ORM
- Pandas
- SQLAlchemy
- Selenium
- PySpark
- Machine Learning Libraries
- REST API Builders

---

# Summary

In this part, we learned:

- Method Chaining
- Need for Method Chaining
- Returning `self`
- Fluent Interface
- Method Chaining vs Constructor Chaining
- Internal Working


# Program 1 – Basic Method Chaining

## Problem Statement

Write a Python program to demonstrate Method Chaining.

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

        return self


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

Each method returns

```python
self
```

Therefore,

the returned object immediately calls the next method.

---

# Program 2 – Method Chaining Without return self

## Problem Statement

Write a Python program to demonstrate why `return self` is required.

---

## Program

```python
class Student:

    def set_name(self, name):

        self.name = name

    def set_age(self, age):

        self.age = age


student = Student()

student.set_name("Rahul").set_age(21)
```

---

## Output

```text
AttributeError:
'NoneType' object has no attribute 'set_age'
```

---

## Explanation

`set_name()` returns

```python
None
```

Therefore,

Python tries to execute

```python
None.set_age()
```

which produces an error.

---

# Program 3 – Calculator using Method Chaining

## Program

```python
class Calculator:

    def __init__(self):

        self.result = 0

    def add(self, value):

        self.result += value

        return self

    def subtract(self, value):

        self.result -= value

        return self

    def multiply(self, value):

        self.result *= value

        return self

    def display(self):

        print("Result :", self.result)

        return self


calculator = Calculator()

calculator.add(20).subtract(5).multiply(2).display()
```

---

## Output

```text
Result : 30
```

---

## Explanation

Execution

```text
0

↓

+20

↓

20

↓

-5

↓

15

↓

×2

↓

30
```

---

# Program 4 – Bank Account Example

## Program

```python
class Bank:

    def deposit(self, amount):

        print("Deposited :", amount)

        return self

    def withdraw(self, amount):

        print("Withdrawn :", amount)

        return self

    def balance(self):

        print("Balance Checked")

        return self


bank = Bank()

bank.deposit(5000).withdraw(2000).balance()
```

---

## Output

```text
Deposited : 5000

Withdrawn : 2000

Balance Checked
```

---

# Program 5 – Student Information Example

## Program

```python
class Student:

    def name(self, value):

        self.student_name = value

        return self

    def course(self, value):

        self.student_course = value

        return self

    def marks(self, value):

        self.student_marks = value

        return self

    def display(self):

        print(self.student_name)

        print(self.student_course)

        print(self.student_marks)

        return self


Student().name("Rahul").course("Python").marks(95).display()
```

---

## Output

```text
Rahul

Python

95
```

---

# Program 6 – Employee Example

## Program

```python
class Employee:

    def set_name(self, name):

        self.name = name

        return self

    def set_salary(self, salary):

        self.salary = salary

        return self

    def show(self):

        print(self.name)

        print(self.salary)

        return self


Employee().set_name("Rahul").set_salary(50000).show()
```

---

## Output

```text
Rahul

50000
```

---

# Program 7 – Method Chaining using Object Reference

## Program

```python
class Demo:

    def one(self):

        print("Method One")

        return self

    def two(self):

        print("Method Two")

        return self

    def three(self):

        print("Method Three")

        return self


obj = Demo()

obj.one().two().three()
```

---

## Output

```text
Method One

Method Two

Method Three
```

---

## Explanation

Each method returns the same object,

allowing continuous method calls.

---

# Program 8 – Fluent Interface Example

## Program

```python
class Query:

    def select(self):

        print("SELECT")

        return self

    def where(self):

        print("WHERE")

        return self

    def order_by(self):

        print("ORDER BY")

        return self


Query().select().where().order_by()
```

---

## Output

```text
SELECT

WHERE

ORDER BY
```

---

## Explanation

This resembles the Fluent Interface used in many frameworks such as Django ORM and SQLAlchemy.

---

# Program 9 – Method Chaining with String Operations

## Program

```python
class Message:

    def __init__(self):

        self.text = ""

    def add(self, word):

        self.text += word + " "

        return self

    def display(self):

        print(self.text)

        return self


Message().add("Python").add("is").add("Awesome").display()
```

---

## Output

```text
Python is Awesome
```

---

# Program 10 – Real-Time Builder Pattern Example

## Program

```python
class Pizza:

    def size(self, value):

        print("Size :", value)

        return self

    def cheese(self):

        print("Extra Cheese")

        return self

    def toppings(self, value):

        print("Toppings :", value)

        return self

    def order(self):

        print("Order Confirmed")

        return self


Pizza().size("Large").cheese().toppings("Mushroom").order()
```

---

## Output

```text
Size : Large

Extra Cheese

Toppings : Mushroom

Order Confirmed
```

---

## Explanation

Builder-style APIs commonly use Method Chaining.

Each method configures the object and returns the same object.

---

# Dry Run

```text
Object Created

↓

Method 1 Called

↓

Returns self

↓

Method 2 Called

↓

Returns self

↓

Method 3 Called

↓

Execution Completed
```

---

# Memory Representation

```text
Student Object

        │

        ▼

+----------------------------+

name

↓

Rahul

age

↓

21

----------------------------

set_name()

set_age()

display()

↓

return self

+----------------------------+
```

---

# Advantages

- Improves readability.
- Produces cleaner code.
- Reduces repeated object references.
- Supports Fluent Interfaces.
- Makes APIs intuitive.
- Encourages reusable code.

---

# Best Practices

- Always return `self` if chaining is required.
- Keep methods focused on a single task.
- Use meaningful method names.
- Avoid overly long chains that reduce readability.
- Validate input before returning `self`.

---

# Common Mistakes

## Mistake 1

Forgetting to return `self`.

```python
def set_name(self, name):

    self.name = name
```

Method Chaining will fail.

---

## Mistake 2

Returning another object instead of `self`.

If another object is returned,

subsequent methods may not exist.

---

## Mistake 3

Performing unrelated operations inside chained methods.

Each method should perform one logical task.

---

## Mistake 4

Creating excessively long chains.

Break long chains into multiple statements if readability suffers.

---

# Interview Questions

## 1. What is Method Chaining?

### Answer

Method Chaining is the technique of calling multiple methods on the same object in a single statement by returning `self` from each method.

---

## 2. Why is `return self` required?

### Answer

It returns the current object so that the next method can be called immediately.

---

## 3. What happens if `return self` is omitted?

### Answer

The method returns `None` by default, causing the next chained method call to fail with an `AttributeError`.

---

## 4. What is a Fluent Interface?

### Answer

A Fluent Interface is a design style where methods return the current object, enabling readable chained method calls.

---

## 5. What is the difference between Method Chaining and Constructor Chaining?

### Answer

Method Chaining links multiple method calls using `return self`.

Constructor Chaining links constructors using `super()` during object initialization.

---

## 6. Which frameworks commonly use Method Chaining?

### Answer

- Django ORM
- Pandas
- SQLAlchemy
- Selenium
- PySpark

---

## 7. Can Method Chaining improve code readability?

### Answer

Yes. It reduces repeated object references and makes related operations appear together.

---

## 8. Is Method Chaining compulsory?

### Answer

No. It is a design choice used to improve readability and API usability.

---

## 9. Can Method Chaining be used without inheritance?

### Answer

Yes. It only requires methods to return `self`.

---

## 10. What is the most important requirement for Method Chaining?

### Answer

Every chained method must return the current object using:

```python
return self
```

---

# Practice Programs

1. Create a Calculator using Method Chaining.
2. Create a Student class using chained setter methods.
3. Create a BankAccount class using Method Chaining.
4. Create a Builder-style Pizza class.
5. Demonstrate why Method Chaining fails without `return self`.

---

# Quick Revision

- Method Chaining calls multiple methods in one statement.
- Each method returns `self`.
- `return self` is mandatory for chaining.
- Method Chaining improves readability.
- Fluent Interfaces are based on Method Chaining.
- Commonly used in Django ORM, Pandas, SQLAlchemy, and Selenium.

---

# Chapter Summary

In this chapter, you learned:

- Method Chaining
- Returning `self`
- Fluent Interface
- Method Chaining vs Constructor Chaining
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
