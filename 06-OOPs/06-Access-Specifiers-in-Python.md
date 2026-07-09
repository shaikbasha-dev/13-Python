# Access Specifiers in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What are Access Specifiers?
5. Why are Access Specifiers Required?
6. Types of Access Specifiers
7. Public Members
8. Protected Members
9. Private Members
10. Name Mangling
11. Comparison of Access Specifiers
12. Internal Working
13. Advantages
14. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand Access Specifiers.
- Explain the need for Access Specifiers.
- Learn Public, Protected, and Private members.
- Understand Name Mangling.
- Apply Access Specifiers in real-world applications.
- Differentiate Python and Java access control.

---

# Prerequisites

Before learning this chapter, you should know:

- Classes
- Objects
- Encapsulation
- Instance Variables
- Methods
- Inheritance

---

# Introduction

In the previous chapter, we learned **Encapsulation**, which combines data and methods into a single unit while protecting data from unauthorized access.

One important concept used to implement Encapsulation is **Access Specifiers**.

Access Specifiers determine **who can access class variables and methods**.

Unlike Java or C++, Python does not enforce strict access modifiers. Instead, it uses **naming conventions** that developers follow to indicate how members should be accessed.

---

# What are Access Specifiers?

## Definition

Access Specifiers are mechanisms used to control the visibility and accessibility of class members (variables and methods).

They help protect data and support Encapsulation.

---

# Simple Definition

> Access Specifiers decide who can access the members of a class.

---

# Why are Access Specifiers Required?

Consider a Banking Application.

A Bank Account contains:

- Account Number
- Customer Name
- Balance
- ATM PIN

Can every user directly modify the balance or PIN?

**No.**

Instead,

the application should allow access only through methods such as

- Deposit()
- Withdraw()
- ChangePIN()

This prevents unauthorized modifications.

---

# Real-World Example

Consider a Hospital Management System.

Doctor Information

```text
Doctor Name

Department

Salary

Password
```

Everyone can know the doctor's name and department.

However,

Salary and Password should be protected.

Access Specifiers help implement this restriction.

---

# Types of Access Specifiers

Python provides three types of Access Specifiers.

- Public
- Protected
- Private

---

# 1. Public Members

## Definition

Public members can be accessed from anywhere.

They can be accessed:

- Inside the class
- Outside the class
- Inside child classes

No special symbol is required.

---

## Syntax

```python
variable

method()
```

Example

```python
class Student:

    def __init__(self):

        self.name = "Rahul"
```

Here,

```python
name
```

is a Public Variable.

---

# 2. Protected Members

## Definition

Protected members are intended to be accessed only inside the class and its child classes.

Python represents Protected members using a single underscore.

---

## Syntax

```python
_variable
```

Example

```python
self._marks = 95
```

Although accessible from outside the class, doing so is discouraged by convention.

---

# 3. Private Members

## Definition

Private members are intended to be accessed only inside the class where they are declared.

Python represents Private members using two underscores.

---

## Syntax

```python
__variable
```

Example

```python
self.__password = "Python123"
```

Python internally changes the variable name.

This process is called **Name Mangling**.

---

# Name Mangling

Python does not completely hide private members.

Instead,

it changes

```python
__password
```

into

```python
_Student__password
```

This prevents accidental access.

It is **not** a security mechanism.

---

# Comparison of Access Specifiers

| Access Specifier | Symbol | Same Class | Child Class | Outside Class |
|-----------------|---------|------------|-------------|---------------|
| Public | None | ✅ | ✅ | ✅ |
| Protected | `_` | ✅ | ✅ | ⚠️ Discouraged |
| Private | `__` | ✅ | ❌ Direct Access | ❌ Direct Access |

---

# Python vs Java

| Java | Python |
|------|--------|
| Compiler Enforced | Naming Convention |
| Strict Access Control | Flexible Access Control |
| public | Public |
| protected | _Protected |
| private | __Private |

---

# Internal Working

Suppose

```python
self.__salary
```

Python internally converts it into

```python
_Employee__salary
```

When accessed outside,

Python searches

```python
__salary
```

which does not exist.

Therefore,

an

```text
AttributeError
```

is generated.

---

# Advantages

- Supports Encapsulation.
- Protects sensitive information.
- Prevents accidental modification.
- Makes programs easier to maintain.
- Improves code organization.
- Encourages better software design.

---

# Real-Time Applications

Access Specifiers are used in:

- Banking Systems
- ATM Applications
- Employee Management Systems
- Hospital Management Systems
- E-Commerce Applications
- School Management Systems

---

# Summary

In this part, we learned:

- Access Specifiers
- Public Members
- Protected Members
- Private Members
- Name Mangling
- Python vs Java Access Control
- Internal Working
- Advantages


# Program 1 – Public Access Specifier

## Problem Statement

Write a Python program to demonstrate Public Members.

---

## Program

```python
class Student:

    def __init__(self):

        self.name = "Rahul"

student = Student()

print(student.name)
```

---

## Output

```text
Rahul
```

---

## Explanation

The variable

```python
name
```

is a Public Variable.

It can be accessed

- Inside the class
- Outside the class
- Inside child classes

without any restrictions.

---

# Program 2 – Protected Access Specifier

## Problem Statement

Write a Python program to demonstrate Protected Members.

---

## Program

```python
class Student:

    def __init__(self):

        self._marks = 95

student = Student()

print(student._marks)
```

---

## Output

```text
95
```

---

## Explanation

The variable

```python
_marks
```

is a Protected Variable.

Python allows access outside the class,

but according to Python conventions,

Protected members should only be used

- Inside the class
- Inside child classes

---

# Program 3 – Private Access Specifier

## Problem Statement

Write a Python program to demonstrate Private Members.

---

## Program

```python
class Student:

    def __init__(self):

        self.__password = "Python123"

student = Student()

print(student.__password)
```

---

## Output

```text
AttributeError:
'Student' object has no attribute '__password'
```

---

## Explanation

Python performs **Name Mangling**.

Internally,

```python
__password
```

becomes

```python
_Student__password
```

Therefore,

direct access fails.

---

# Program 4 – Accessing Private Members using Name Mangling

## Problem Statement

Write a Python program to access a private member using Name Mangling.

---

## Program

```python
class Student:

    def __init__(self):

        self.__password = "Python123"

student = Student()

print(student._Student__password)
```

---

## Output

```text
Python123
```

---

## Explanation

Python internally renames

```python
__password
```

to

```python
_Student__password
```

Although this is possible,

it should generally be avoided because it breaks encapsulation.

---

# Program 5 – Protected Members in Inheritance

## Problem Statement

Write a Python program to demonstrate Protected Members in Inheritance.

---

## Program

```python
class Person:

    def __init__(self):

        self._name = "Rahul"


class Student(Person):

    def display(self):

        print(self._name)

student = Student()

student.display()
```

---

## Output

```text
Rahul
```

---

## Explanation

Protected members are intended to be inherited.

The child class can directly access

```python
_name
```

---

# Program 6 – Private Members in Inheritance

## Problem Statement

Write a Python program to demonstrate Private Members in Inheritance.

---

## Program

```python
class Person:

    def __init__(self):

        self.__salary = 50000


class Employee(Person):

    def display(self):

        print(self.__salary)

employee = Employee()

employee.display()
```

---

## Output

```text
AttributeError:
'Employee' object has no attribute '_Employee__salary'
```

---

## Explanation

Private members are **not directly inherited**.

Python internally converts

```python
__salary
```

into

```python
_Person__salary
```

Inside the child class,

Python searches for

```python
_Employee__salary
```

which does not exist.

Hence,

an `AttributeError` occurs.

---

# Program 7 – Accessing Private Members using Getter Method

## Program

```python
class Employee:

    def __init__(self):

        self.__salary = 50000

    def get_salary(self):

        return self.__salary

employee = Employee()

print(employee.get_salary())
```

---

## Output

```text
50000
```

---

## Explanation

Instead of directly accessing the private variable,

the Getter Method provides controlled access.

This is the recommended approach.

---

# Program 8 – Updating Private Members using Setter Method

## Program

```python
class Employee:

    def __init__(self):

        self.__salary = 0

    def set_salary(self, salary):

        if salary > 0:

            self.__salary = salary

    def get_salary(self):

        return self.__salary

employee = Employee()

employee.set_salary(60000)

print(employee.get_salary())
```

---

## Output

```text
60000
```

---

## Explanation

The Setter Method validates the data before storing it.

This prevents invalid values from being assigned.

---

# Dry Run

```text
Create Employee Object

↓

Private Variable Created

↓

Getter Called

↓

Private Variable Returned

↓

Output Displayed
```

---

# Memory Representation

```text
Employee Object

        │

        ▼

+------------------------------+

__salary

↓

_Person__salary

↓

50000

------------------------------

get_salary()

set_salary()

+------------------------------+
```

---

# Advantages

- Protects sensitive data.
- Prevents accidental modification.
- Supports Encapsulation.
- Improves maintainability.
- Improves code readability.
- Encourages secure programming.

---

# Best Practices

- Use Public members for general-purpose data.
- Use Protected members for inheritance-related data.
- Use Private members for confidential information.
- Prefer Getter and Setter methods instead of Name Mangling.
- Validate data before updating private variables.

---

# Common Mistakes

## Mistake 1

Trying to access Private Variables directly.

❌ Incorrect

```python
employee.__salary
```

Produces

```text
AttributeError
```

---

## Mistake 2

Confusing Protected and Private Members.

```python
_marks
```

is Protected.

```python
__marks
```

is Private.

---

## Mistake 3

Using Name Mangling in normal applications.

```python
employee._Employee__salary
```

Although possible,

this should be avoided.

Use Getter methods instead.

---

## Mistake 4

Assuming Python provides complete data security.

Python uses naming conventions and Name Mangling.

It is **not** intended as a strict security mechanism like Java's access modifiers.

---

# Interview Questions

## 1. What are Access Specifiers?

### Answer

Access Specifiers determine the visibility and accessibility of class members.

---

## 2. Which Access Specifiers are available in Python?

### Answer

- Public
- Protected
- Private

---

## 3. Does Python support strict Access Specifiers?

### Answer

No.

Python follows naming conventions instead of compiler-enforced access control.

---

## 4. What is a Public Member?

### Answer

A member that can be accessed from anywhere.

---

## 5. What is a Protected Member?

### Answer

A member prefixed with a single underscore (`_`), intended for use within the class and its subclasses.

---

## 6. What is a Private Member?

### Answer

A member prefixed with a double underscore (`__`), intended for use only within its own class.

---

## 7. What is Name Mangling?

### Answer

Name Mangling is the process of internally renaming private members to reduce accidental access.

Example:

```python
__salary
```

becomes

```python
_Employee__salary
```

---

## 8. Can a Child Class access Private Members directly?

### Answer

No.

Private members are not directly accessible in child classes.

---

## 9. What is the recommended way to access Private Members?

### Answer

Using Getter and Setter methods or Python Properties.

---

## 10. What is the difference between Public, Protected, and Private Members?

| Public | Protected | Private |
|---------|-----------|----------|
| Accessible everywhere | Intended for class and subclasses | Intended only for the defining class |

---

# Practice Programs

1. Create a Student class with Public variables.
2. Create an Employee class with Protected variables.
3. Create a BankAccount class with Private variables.
4. Demonstrate Name Mangling.
5. Create Getter and Setter methods.
6. Demonstrate Protected Members in Inheritance.
7. Demonstrate why Private Members cannot be directly inherited.

---

# Quick Revision

- Public → No Prefix
- Protected → `_variable`
- Private → `__variable`
- Python follows naming conventions.
- Name Mangling changes the internal name of private members.
- Use Getter and Setter methods for controlled access.
- Access Specifiers help implement Encapsulation.

---

# Chapter Summary

In this chapter, you learned:

- Access Specifiers
- Public Members
- Protected Members
- Private Members
- Name Mangling
- Inheritance with Access Specifiers
- Getter and Setter Methods
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision

