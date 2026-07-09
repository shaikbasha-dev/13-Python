# Introduction to Data Types

## Introduction

A **data type** specifies the type of value that can be stored in a variable. Every value in a Python program belongs to a particular data type. Python automatically identifies the type of a value when it is assigned to a variable, so explicit type declarations are not required.

Data types help Python understand:

* What kind of data is being stored
* How much memory should be allocated
* Which operations are valid for that data
* How the value should be processed during program execution

Python supports several built-in data types for storing numeric values, text, collections of data, binary data, and special values.

---

# What is a Data Type?

A **data type** is a classification that defines the nature of a value and the operations that can be performed on it.

In simple words, a data type tells Python what kind of information a variable contains.

---

# Why are Data Types Required?

Data types are essential because they enable Python to:

* Store different kinds of information efficiently.
* Allocate memory appropriately.
* Perform valid operations on values.
* Prevent invalid operations between incompatible data.
* Improve program readability and reliability.

Without data types, Python would not know whether a value represents a number, text, a collection of items, or another kind of object.

---

# Real-World Examples

| Data                | Data Type           |
| ------------------- | ------------------- |
| Student Age         | Integer (`int`)     |
| Product Price       | Float (`float`)     |
| Student Name        | String (`str`)      |
| Login Status        | Boolean (`bool`)    |
| Shopping Cart       | List (`list`)       |
| Student Marks       | Tuple (`tuple`)     |
| Unique Roll Numbers | Set (`set`)         |
| Employee Details    | Dictionary (`dict`) |

---

# Syntax

Python automatically determines the data type.

```python
variable_name = value
```

### Example

```python
age = 21
price = 499.99
name = "Basha"
is_student = True
```

---

# Program

```python
age = 21
price = 499.99
name = "Basha"
is_student = True

print(age)
print(price)
print(name)
print(is_student)
```

---

# Output

```text
21
499.99
Basha
True
```

---

# Checking the Data Type

Python provides the built-in `type()` function to determine the data type of a variable or value.

### Example

```python
age = 21
price = 499.99
name = "Python"
status = True

print(type(age))
print(type(price))
print(type(name))
print(type(status))
```

### Output

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

---

# Internal Working

When Python executes the following statement:

```python
age = 21
```

Internally, the interpreter performs these steps:

```text
Interpreter Reads Statement

↓

Creates Integer Object

↓

Allocates Memory

↓

Stores Value

↓

Variable References the Object

↓

Execution Continues
```

---

# Memory Representation

```text
          age
           │
           ▼
+--------------------+
|     21 (int)       |
+--------------------+

        price
           │
           ▼
+--------------------+
|   499.99 (float)   |
+--------------------+

         name
           │
           ▼
+--------------------+
|   "Basha" (str)    |
+--------------------+

      is_student
           │
           ▼
+--------------------+
|    True (bool)     |
+--------------------+
```

---

# Pseudocode

```text
START

Create variables

Assign different types of values

Display the values

Display their data types

STOP
```

---

# Line-by-Line Explanation

### Line 1

```python
age = 21
```

Creates an integer variable named `age`.

---

### Line 2

```python
price = 499.99
```

Creates a float variable named `price`.

---

### Line 3

```python
name = "Basha"
```

Creates a string variable named `name`.

---

### Line 4

```python
is_student = True
```

Creates a Boolean variable named `is_student`.

---

### Remaining Lines

The `print()` function displays the stored values, while the `type()` function returns the data type of each variable.

---

# Advantages of Data Types

* Organize data efficiently.
* Improve code readability.
* Help Python perform appropriate operations.
* Simplify memory management.
* Reduce programming errors.

---

# Limitations

* Some data types are immutable and cannot be modified after creation.
* Using an inappropriate data type may require unnecessary type conversions.

---

# Real-World Applications

* Student Management Systems
* Banking Applications
* E-Commerce Platforms
* Hospital Management Systems
* Inventory Management
* Payroll Systems
* Online Examination Systems
* Social Media Applications

---

# Best Practices

* Select the most appropriate data type for each value.
* Use meaningful variable names.
* Verify data types using `type()` while debugging.
* Avoid unnecessary type conversions.

---

# Summary

In this chapter, you learned:

* What a data type is
* Why data types are important
* How Python identifies data types automatically
* How to create variables with different data types
* How to use the `type()` function
* Internal working of data types
* Memory representation
* Advantages, applications, and best practices

In the next chapter, you will learn about the **Categories of Data Types in Python**.
