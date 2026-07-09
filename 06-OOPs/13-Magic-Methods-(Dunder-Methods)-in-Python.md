# Magic Methods (Dunder Methods) in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What are Magic Methods?
5. Why are Magic Methods Required?
6. Why are they called Dunder Methods?
7. How Magic Methods Work
8. Common Magic Methods
9. Operator Overloading
10. Object Lifecycle
11. Internal Working
12. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand Magic Methods.
- Understand Dunder Methods.
- Learn Python's built-in special methods.
- Understand Operator Overloading.
- Customize object behavior.
- Use Magic Methods in real-world applications.

---

# Prerequisites

Before learning this chapter, you should know:

- Classes
- Objects
- Constructors
- Methods
- Method Overloading
- Polymorphism

---

# Introduction

Everything in Python is an object.

Whenever we perform operations like

```python
+
-
*
/
len()
print()
str()
```

Python internally calls special methods.

For example,

```python
a = 10

b = 20

print(a + b)
```

Internally,

Python executes

```python
a.__add__(b)
```

Similarly,

```python
print(obj)
```

internally calls

```python
obj.__str__()
```

These special methods are called

**Magic Methods**

or

**Dunder Methods**.

---

# What are Magic Methods?

## Definition

Magic Methods are special predefined methods that begin and end with double underscores (`__`).

Python automatically invokes these methods in response to specific operations.

---

# Simple Definition

> Magic Methods allow Python objects to respond to built-in operations such as addition, printing, comparison, iteration, and object creation.

---

# Why are Magic Methods Required?

Suppose we create a class

```python
Student
```

Without Magic Methods,

Python does not know

- How to print an object
- How to compare two objects
- How to add two objects
- How to calculate object length

Magic Methods define these behaviors.

---

# Why are they called Dunder Methods?

"Dunder" means

```text
Double

↓

Under

↓

Double Underscore
```

Examples

```python
__init__()

__str__()

__len__()

__add__()
```

Because they begin and end with

```text
__
```

they are called

**Dunder Methods**.

---

# How Magic Methods Work

Suppose

```python
print(student)
```

Python internally executes

```python
student.__str__()
```

Similarly,

```python
len(student)
```

becomes

```python
student.__len__()
```

Likewise,

```python
student1 + student2
```

becomes

```python
student1.__add__(student2)
```

Python automatically invokes these methods.

---

# Common Magic Methods

| Magic Method | Purpose |
|--------------|---------|
| `__init__()` | Object Initialization |
| `__str__()` | User-Friendly String Representation |
| `__repr__()` | Official Object Representation |
| `__len__()` | Length of Object |
| `__add__()` | Addition |
| `__sub__()` | Subtraction |
| `__mul__()` | Multiplication |
| `__truediv__()` | Division |
| `__eq__()` | Equality Comparison |
| `__lt__()` | Less Than |
| `__gt__()` | Greater Than |
| `__contains__()` | Membership Test (`in`) |
| `__getitem__()` | Index Access |
| `__setitem__()` | Assign by Index |
| `__call__()` | Make Object Callable |

---

# Operator Overloading

Magic Methods make Operator Overloading possible.

Example

```python
student1 + student2
```

internally becomes

```python
student1.__add__(student2)
```

Instead of only adding integers,

we can define what

```python
+
```

means for our own objects.

---

# Object Lifecycle

When an object is created,

Python follows this sequence

```text
Object Created

↓

__new__()

↓

Memory Allocated

↓

__init__()

↓

Object Initialized

↓

Object Used

↓

Garbage Collected
```

Although `__new__()` exists,

beginners mainly work with

```python
__init__()
```

---

# Internal Working

```text
Operation

↓

Python Searches

↓

Corresponding Magic Method

↓

Method Executes

↓

Result Returned
```

Example

```text
len(obj)

↓

obj.__len__()

↓

Length Returned
```

---

# Advantages

- Customizes object behavior.
- Enables Operator Overloading.
- Improves readability.
- Integrates with Python built-in functions.
- Makes classes behave like built-in types.

---

# Real-Time Applications

Magic Methods are used in:

- Django ORM
- NumPy
- Pandas
- TensorFlow
- SQLAlchemy
- PyTorch
- Data Structures
- Game Development

---

# Summary

In this part, you learned:

- Magic Methods
- Dunder Methods
- Operator Overloading
- Object Lifecycle
- Internal Working
- Common Magic Methods
- Advantages


# Program 1 – __init__() Method

## Problem Statement

Write a Python program to demonstrate the `__init__()` method.

---

## Program

```python
class Student:

    def __init__(self, name):

        self.name = name

student = Student("Rahul")

print(student.name)
```

---

## Output

```text
Rahul
```

---

## Explanation

`__init__()` is automatically called whenever an object is created.

It initializes the object.

---

# Program 2 – __str__() Method

## Problem Statement

Write a Python program to demonstrate the `__str__()` method.

---

## Program

```python
class Student:

    def __init__(self, name):

        self.name = name

    def __str__(self):

        return f"Student(Name = {self.name})"


student = Student("Rahul")

print(student)
```

---

## Output

```text
Student(Name = Rahul)
```

---

## Explanation

When

```python
print(student)
```

is executed,

Python internally calls

```python
student.__str__()
```

It returns a user-friendly string representation.

---

# Program 3 – __repr__() Method

## Problem Statement

Write a Python program to demonstrate the `__repr__()` method.

---

## Program

```python
class Student:

    def __init__(self, name):

        self.name = name

    def __repr__(self):

        return f"Student('{self.name}')"


student = Student("Rahul")

print(repr(student))
```

---

## Output

```text
Student('Rahul')
```

---

## Explanation

`__repr__()` returns the official string representation of an object.

It is mainly used for debugging and development.

---

# Program 4 – __len__() Method

## Problem Statement

Write a Python program to demonstrate the `__len__()` method.

---

## Program

```python
class Team:

    def __init__(self):

        self.players = ["Rahul", "Priya", "Kiran"]

    def __len__(self):

        return len(self.players)


team = Team()

print(len(team))
```

---

## Output

```text
3
```

---

## Explanation

When

```python
len(team)
```

is executed,

Python internally calls

```python
team.__len__()
```

---

# Program 5 – __add__() Method (Operator Overloading)

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

# Program 6 – __sub__() Method

## Program

```python
class Number:

    def __init__(self, value):

        self.value = value

    def __sub__(self, other):

        return Number(self.value - other.value)


num1 = Number(50)

num2 = Number(20)

result = num1 - num2

print(result.value)
```

---

## Output

```text
30
```

---

## Explanation

Python internally calls

```python
num1.__sub__(num2)
```

when the `-` operator is used.

---

# Program 7 – __eq__() Method

## Program

```python
class Student:

    def __init__(self, marks):

        self.marks = marks

    def __eq__(self, other):

        return self.marks == other.marks


student1 = Student(90)

student2 = Student(90)

print(student1 == student2)
```

---

## Output

```text
True
```

---

## Explanation

The `==` operator internally invokes

```python
__eq__()
```

---

# Program 8 – __lt__() Method

## Program

```python
class Student:

    def __init__(self, marks):

        self.marks = marks

    def __lt__(self, other):

        return self.marks < other.marks


student1 = Student(80)

student2 = Student(90)

print(student1 < student2)
```

---

## Output

```text
True
```

---

## Explanation

The `<` operator calls

```python
__lt__()
```

---

# Program 9 – __gt__() Method

## Program

```python
class Student:

    def __init__(self, marks):

        self.marks = marks

    def __gt__(self, other):

        return self.marks > other.marks


student1 = Student(95)

student2 = Student(90)

print(student1 > student2)
```

---

## Output

```text
True
```

---

## Explanation

The `>` operator internally calls

```python
__gt__()
```

---

# Program 10 – __contains__() Method

## Program

```python
class Team:

    def __init__(self):

        self.players = ["Rahul", "Priya", "Kiran"]

    def __contains__(self, player):

        return player in self.players


team = Team()

print("Rahul" in team)
```

---

## Output

```text
True
```

---

## Explanation

The `in` operator internally calls

```python
__contains__()
```

---

# Program 11 – __getitem__() Method

## Program

```python
class Numbers:

    def __init__(self):

        self.data = [10, 20, 30, 40]

    def __getitem__(self, index):

        return self.data[index]


numbers = Numbers()

print(numbers[2])
```

---

## Output

```text
30
```

---

## Explanation

Indexing

```python
numbers[2]
```

internally calls

```python
numbers.__getitem__(2)
```

---

# Program 12 – __setitem__() Method

## Program

```python
class Numbers:

    def __init__(self):

        self.data = [10, 20, 30]

    def __setitem__(self, index, value):

        self.data[index] = value


numbers = Numbers()

numbers[1] = 100

print(numbers.data)
```

---

## Output

```text
[10, 100, 30]
```

---

## Explanation

Assignment using an index internally invokes

```python
__setitem__()
```

---

# Program 13 – __call__() Method

## Program

```python
class Greeting:

    def __call__(self):

        print("Hello, Welcome!")


greet = Greeting()

greet()
```

---

## Output

```text
Hello, Welcome!
```

---

## Explanation

Objects become callable when the

```python
__call__()
```

method is implemented.

---

# Program 14 – __str__() vs __repr__()

## Program

```python
class Student:

    def __str__(self):

        return "Readable Output"

    def __repr__(self):

        return "Official Representation"


student = Student()

print(student)

print(repr(student))
```

---

## Output

```text
Readable Output

Official Representation
```

---

## Explanation

- `__str__()` → User-friendly representation
- `__repr__()` → Developer/debug representation

---

# Program 15 – Real-Time Operator Overloading Example

## Program

```python
class Money:

    def __init__(self, amount):

        self.amount = amount

    def __add__(self, other):

        return Money(self.amount + other.amount)

    def __str__(self):

        return f"₹{self.amount}"


wallet1 = Money(500)

wallet2 = Money(1500)

print(wallet1 + wallet2)
```

---

## Output

```text
₹2000
```

---

## Explanation

Two `Money` objects are added using the overloaded `+` operator.

Python internally executes

```python
wallet1.__add__(wallet2)
```

and then displays the result using

```python
__str__()
```

---

# Dry Run

```text
Object Created

↓

Operator Used

↓

Python Finds Matching Magic Method

↓

Magic Method Executes

↓

Result Returned
```

---

# Memory Representation

```text
Money Object

        │

        ▼

+---------------------------+

amount

↓

500

---------------------------

__add__()

__str__()

+---------------------------+
```

---

# Advantages

- Customizes object behavior.
- Enables Operator Overloading.
- Integrates with Python built-in functions.
- Improves code readability.
- Makes user-defined classes behave like built-in types.

---

# Best Practices

- Override only the Magic Methods your class needs.
- Keep Magic Methods simple and predictable.
- Ensure overloaded operators behave naturally.
- Implement both `__str__()` and `__repr__()` when appropriate.
- Return the correct data types from Magic Methods.

---

# Common Mistakes

## Mistake 1

Returning a non-string from `__str__()`.

❌ Incorrect

```python
def __str__(self):

    return 100
```

`__str__()` must return a string.

---

## Mistake 2

Assuming Magic Methods are called directly.

Normally, use operators or built-in functions instead of calling methods like `__add__()` manually.

---

## Mistake 3

Overloading operators with unexpected behavior.

For example, `+` should generally represent addition or combination, not an unrelated action.

---

## Mistake 4

Confusing `__str__()` and `__repr__()`.

`__str__()` is for end users.

`__repr__()` is for developers and debugging.

---

# Interview Questions

## 1. What are Magic Methods?

### Answer

Magic Methods are predefined special methods surrounded by double underscores that Python automatically invokes for built-in operations.

---

## 2. Why are they called Dunder Methods?

### Answer

Because they begin and end with double underscores (`__`), which stands for **Double Under**.

---

## 3. What is the purpose of `__init__()`?

### Answer

It initializes an object immediately after it is created.

---

## 4. What is the difference between `__str__()` and `__repr__()`?

### Answer

- `__str__()` provides a readable string for users.
- `__repr__()` provides an unambiguous representation for developers.

---

## 5. What is Operator Overloading?

### Answer

Operator Overloading allows built-in operators such as `+`, `-`, and `==` to work with user-defined objects.

---

## 6. Which Magic Method overloads the `+` operator?

### Answer

`__add__()`.

---

## 7. Which Magic Method is used by `len()`?

### Answer

`__len__()`.

---

## 8. Which Magic Method makes an object callable?

### Answer

`__call__()`.

---

## 9. Which Magic Method supports indexing?

### Answer

`__getitem__()`.

---

## 10. Can we create our own Magic Method names?

### Answer

No.

Only Python's predefined special method names have special behavior.

---

# Practice Programs

1. Implement `__str__()` in a Student class.
2. Overload the `+` operator using `__add__()`.
3. Implement `__len__()` for a custom collection.
4. Create a callable object using `__call__()`.
5. Implement `__getitem__()` and `__setitem__()` for a custom list class.

---

# Quick Revision

- Magic Methods are also called Dunder Methods.
- Python automatically invokes them.
- `__init__()` initializes objects.
- `__str__()` returns a readable string.
- `__repr__()` returns a developer representation.
- `__len__()` supports `len()`.
- `__add__()` overloads `+`.
- `__call__()` makes objects callable.
- `__getitem__()` supports indexing.
- `__contains__()` supports the `in` operator.

---

# Chapter Summary

In this chapter, we learned:

- Magic Methods
- Dunder Methods
- `__init__()`
- `__str__()`
- `__repr__()`
- `__len__()`
- `__add__()`
- `__sub__()`
- `__eq__()`
- `__lt__()`
- `__gt__()`
- `__contains__()`
- `__getitem__()`
- `__setitem__()`
- `__call__()`
- Operator Overloading
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
