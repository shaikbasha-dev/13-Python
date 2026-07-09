# Complex (`complex`) - Advanced Concepts

## Introduction

After learning the fundamentals and operations of complex numbers, it is important to understand how Python internally stores and manages complex objects.

This chapter explains the internal working of the `complex` data type, memory management, object immutability, implementation details, performance considerations, advantages, limitations, common mistakes, and interview-oriented concepts.

---

# Internal Working of Complex Numbers

Whenever a complex number is created, Python performs several internal operations.

Example

```python
number = 5 + 3j
```

Internally, Python performs the following steps.

```text
Interpreter Reads Statement

↓

Recognizes Complex Number

↓

Creates Complex Object

↓

Stores Real Part

↓

Stores Imaginary Part

↓

Allocates Memory

↓

Variable References the Object

↓

Execution Continues
```

Python variables do not store values directly.

Instead, they store **references** to objects created in memory.

---

# Internal Structure of a Complex Object

A complex object internally contains two floating-point values.

```text
Complex Object

+----------------------------+

| Real Part      : 5.0       |

| Imaginary Part : 3.0       |

+----------------------------+
```

Both components are stored as floating-point numbers.

---

# Memory Representation

Example

```python
number = 5 + 3j
```

```text
        number
           │
           ▼
+----------------------------+
|      5 + 3j (complex)      |
+----------------------------+
```

When another variable references the same object:

```python
a = 5 + 3j

b = a
```

```text
        a             b
        │             │
        └──────┬──────┘
               ▼
+----------------------------+
|      5 + 3j (complex)      |
+----------------------------+
```

Both variables reference the same complex object until one of them is reassigned.

---

# Memory Management

Python automatically manages memory for complex objects.

Memory management includes:

* Object creation
* Reference counting
* Garbage collection

Example

```python
x = 4 + 2j

y = x
```

Both variables point to the same object.

When one variable changes,

```python
y = 8 + 6j
```

Python creates a new complex object instead of modifying the existing one.

---

# Complex Immutability

Complex numbers are **immutable**.

Once created, the value of a complex object cannot be changed.

Whenever a complex number appears to change, Python creates a completely new object.

Example

```python
number = 2 + 3j

number = number + (4 + 5j)
```

Python creates a new object rather than modifying the existing object.

Memory Representation

Before

```text
number

   │

   ▼

+---------------+

|    2 + 3j     |

+---------------+
```

After

```text
number

   │

   ▼

+---------------+

|    6 + 8j     |

+---------------+
```

---

# Arithmetic Processing

Whenever arithmetic operations are performed,

```python
a = 2 + 3j

b = 4 + 5j

c = a + b
```

Python performs the following internally.

```text
Read Operands

↓

Extract Real Parts

↓

Extract Imaginary Parts

↓

Perform Addition

↓

Create New Complex Object

↓

Store Result

↓

Assign Reference to c
```

---

# Performance Considerations

Complex arithmetic is generally slower than integer and floating-point arithmetic because every operation involves two floating-point components.

Approximate comparison:

```text
Integer Operations

↓

Fastest

↓

Float Operations

↓

Complex Operations

↓

More Computational Work
```

Complex numbers should be used only when mathematical models require imaginary values.

---

# Advantages of Complex Numbers

* Represents real and imaginary values together.
* Simplifies mathematical expressions.
* Supports direct arithmetic operations.
* Useful for engineering and scientific applications.
* Immutable and thread-safe.
* Built into Python without requiring additional libraries.

---

# Limitations of Complex Numbers

* Cannot be ordered using `<`, `>`, `<=`, or `>=`.
* Consumes more memory than integers and floats.
* Slower than integer arithmetic.
* Not commonly required in general business applications.

---

# Best Practices

* Use complex numbers only when imaginary values are required.
* Access individual components using `.real` and `.imag`.
* Use `abs()` to calculate magnitude.
* Use `conjugate()` instead of implementing conjugation manually.
* Avoid ordering comparisons.
* Use meaningful variable names in mathematical programs.

---

# Common Mistakes

## 1. Forgetting the Imaginary Suffix

Incorrect

```python
number = 5 + 3
```

Correct

```python
number = 5 + 3j
```

---

## 2. Using Ordering Operators

```python
print((2+3j) > (4+5j))
```

Output

```text
TypeError
```

---

## 3. Assuming Complex Numbers Can Be Modified

Incorrect thinking

```python
number = 5 + 3j

number.real = 10
```

Output

```text
AttributeError
```

The `.real` and `.imag` attributes are read-only because complex numbers are immutable.

---

# Frequently Asked Interview Questions

## 1. What is a complex number?

A complex number is a numeric value containing both a real part and an imaginary part.

---

## 2. Which data type stores complex numbers?

The built-in `complex` data type.

---

## 3. Which symbol represents the imaginary part?

Python uses **`j`** as the imaginary unit.

---

## 4. Are complex numbers mutable?

No.

Complex numbers are immutable.

---

## 5. Can complex numbers be compared using `<` or `>`?

No.

Python raises a `TypeError`.

---

## 6. How do you obtain the magnitude?

Using the built-in `abs()` function.

---

## 7. How do you access the real part?

Using `.real`.

---

## 8. How do you access the imaginary part?

Using `.imag`.

---

## 9. How do you obtain the conjugate?

Using the `conjugate()` method.

---

# Summary

In this chapter, you learned:

* Internal working of complex numbers
* Internal object structure
* Memory representation
* Automatic memory management
* Object immutability
* Arithmetic processing
* Performance considerations
* Advantages and limitations
* Best practices
* Common mistakes
* Frequently asked interview questions

You now have a complete understanding of Python's **Complex (`complex`)** data type, from basic concepts to advanced implementation details.

In the next chapter, you will learn about the **Boolean (`bool`)** data type, including logical values, Boolean operations, truth values, internal working, and practical applications.
