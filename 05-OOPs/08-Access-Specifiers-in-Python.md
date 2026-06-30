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
12. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand Access Specifiers.
- Explain why Access Specifiers are used.
- Learn Public, Protected, and Private members.
- Understand Python's naming conventions.
- Learn Name Mangling.
- Write programs using Access Specifiers.

---

# Prerequisites

Before learning this chapter, you should know:

- Classes
- Objects
- Instance Variables
- Methods
- Inheritance

---

# Introduction

In Object-Oriented Programming, every class contains data and methods.

Sometimes we want every object to access the data.

Sometimes we want access to be restricted.

For example,

In a Banking Application,

```text
Account Number

Balance

PIN Number
```

The balance and PIN should not be modified directly by anyone.

To control access to class members, Python provides **Access Specifiers**.

Unlike Java or C++, Python does not have strict access control.

Instead, it follows **naming conventions** that indicate how members should be accessed.

---

# What are Access Specifiers?

## Definition

Access Specifiers are mechanisms used to control the visibility and accessibility of class members (variables and methods).

They help protect data and improve code organization.

---

# Why are Access Specifiers Required?

Access Specifiers help to:

- Protect sensitive data.
- Prevent accidental modification.
- Improve code security.
- Support Encapsulation.
- Improve maintainability.

---

# Types of Access Specifiers

Python provides three types of access specifiers.

- Public
- Protected
- Private

---

# 1. Public Members

## Definition

Public members can be accessed from anywhere.

They can be accessed:

- Inside the class.
- Outside the class.
- Inside child classes.

Public members do not use any special prefix.

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

is a public instance variable.

---

# 2. Protected Members

## Definition

Protected members are intended to be accessed only inside the class and its child classes.

Python indicates protected members using a **single underscore (`_`)** prefix.

Although they can still be accessed from outside the class, it is discouraged by convention.

---

## Syntax

```python
_variable

_method()
```

Example

```python
class Student:

    def __init__(self):

        self._marks = 95
```

---

# 3. Private Members

## Definition

Private members are intended to be accessed only within the class where they are defined.

Python indicates private members using **double underscores (`__`)**.

Python performs **Name Mangling** to reduce accidental access from outside the class.

---

## Syntax

```python
__variable

__method()
```

Example

```python
class Student:

    def __init__(self):

        self.__password = "Python123"
```

---

# Name Mangling

Python does not completely hide private members.

Instead,

it changes their names internally.

Example

```python
__password
```

becomes

```python
_Student__password
```

This process is called **Name Mangling**.

It helps prevent accidental access but does not provide absolute security.

---

# Access Specifiers Comparison

| Access Specifier | Prefix | Same Class | Child Class | Outside Class |
|------------------|--------|------------|-------------|---------------|
| Public | None | ✅ | ✅ | ✅ |
| Protected | `_` | ✅ | ✅ | ⚠️ Discouraged |
| Private | `__` | ✅ | ❌ Direct Access | ❌ Direct Access |

> **Note:** Protected and private members can still be accessed in Python through conventions or name mangling, but doing so should generally be avoided unless necessary.

---

# Python vs Java

| Java | Python |
|------|--------|
| Strict access modifiers | Naming conventions |
| Compiler enforces access | Developer discipline |
| public, protected, private | public, `_protected`, `__private` |

---

# Summary

In this part, we learned:

- Access Specifiers
- Need for Access Specifiers
- Public Members
- Protected Members
- Private Members
- Name Mangling
- Difference between Python and Java Access Control


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

`name` is a public variable.

It can be accessed:

- Inside the class
- Outside the class
- Inside a child class

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

Although `_marks` can be accessed outside the class, it is considered **protected by convention**.

The single underscore (`_`) indicates that it is intended for internal use within the class and its subclasses.

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

Python performs **Name Mangling** on private members.

The actual variable name becomes

```python
_Student__password
```

Therefore,

```python
student.__password
```

cannot access the variable directly.

---

# Program 4 – Accessing Private Members using Name Mangling

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

This mechanism is called **Name Mangling**.

Although possible, accessing private members this way should generally be avoided.

---

# Program 5 – Protected Members in Inheritance

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

Protected members are intended to be used inside child classes.

The child class successfully accesses the protected variable.

---

# Program 6 – Private Members in Inheritance

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

Private members are not directly inherited.

The child class cannot access the parent's private members directly because of Name Mangling.

---

# Internal Working

Suppose

```python
self.__salary
```

Python internally converts it into

```python
_Person__salary
```

When the child class tries

```python
self.__salary
```

Python looks for

```python
_Employee__salary
```

Since that variable does not exist,

an `AttributeError` occurs.

---

# Memory Representation

```text
Student Object

        │

        ▼

+---------------------------+

name

↓

Rahul

_marks

↓

95

__password

↓

_Student__password

+---------------------------+
```

---

# Advantages

- Supports Encapsulation.
- Protects sensitive data.
- Improves code readability.
- Prevents accidental modification.
- Makes programs easier to maintain.

---

# Best Practices

- Use **public** members for general data.
- Use **protected** members for data intended for subclasses.
- Use **private** members for sensitive information.
- Do not rely on Name Mangling as a security mechanism.
- Access private members through public methods (getters/setters or properties) when appropriate.

---

# Common Mistakes

## Mistake 1

Trying to access private members directly.

❌ Incorrect

```python
student.__password
```

Produces

```text
AttributeError
```

---

## Mistake 2

Confusing Protected with Private

```python
_marks
```

is **Protected**

```python
__marks
```

is **Private**

---

## Mistake 3

Assuming Python completely hides private members.

Python only performs **Name Mangling**.

Private members can still be accessed if necessary using the mangled name.

---

# Real-Time Applications

Access Specifiers are used in:

- Banking Applications
- ATM Systems
- Hospital Management Systems
- Employee Payroll Systems
- Student Management Systems
- E-Commerce Applications

Sensitive data such as:

- Passwords
- PIN Numbers
- Account Balance
- Salary
- Personal Information

should not be modified directly from outside the class.

---

# Interview Questions

## 1. What are Access Specifiers?

### Answer

Access Specifiers control the visibility and accessibility of class members.

---

## 2. Which Access Specifiers are available in Python?

### Answer

- Public
- Protected
- Private

---

## 3. Does Python have strict Access Specifiers like Java?

### Answer

No.

Python follows naming conventions rather than enforcing strict access control.

---

## 4. What is Name Mangling?

### Answer

Name Mangling is the process of internally renaming private members to reduce accidental access.

Example

```python
__salary
```

becomes

```python
_Person__salary
```

---

## 5. What is the difference between Protected and Private members?

### Answer

- Protected members use a single underscore (`_`) and are intended for use within the class and its subclasses.
- Private members use a double underscore (`__`) and are intended for use only within the defining class.

---

## 6. Can private members be accessed outside the class?

### Answer

Not directly.

They can be accessed using the mangled name, but this is generally discouraged.

---

# Practice Programs

1. Create a Student class with a public variable.
2. Create an Employee class with a protected variable.
3. Create a BankAccount class with a private PIN.
4. Access a private variable using Name Mangling.
5. Demonstrate protected member access in inheritance.
6. Demonstrate why private members cannot be accessed directly by child classes.

---

# Quick Revision

- Public → No prefix
- Protected → `_variable`
- Private → `__variable`
- Python uses naming conventions.
- Name Mangling changes private member names internally.
- Use `super()` and proper methods instead of directly accessing private data.
- Prefer controlled access using methods or properties.

---

# Chapter Summary

In this chapter, you learned:

- Access Specifiers
- Public Members
- Protected Members
- Private Members
- Name Mangling
- Access Specifiers in Inheritance
- Python vs Java Access Control
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
