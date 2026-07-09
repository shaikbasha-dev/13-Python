# Categories of Data Types

## Introduction

Python provides several built-in data types to store different kinds of information. Every value in Python belongs to a specific data type.

To organize these data types and make them easier to understand, Python classifies them into different categories based on the type of data they store and their purpose.

Understanding these categories helps programmers choose the appropriate data type for different programming scenarios.

---

# What are Categories of Data Types?

A **category of data types** is a group of related data types that share similar characteristics and are designed to store a specific kind of data.

For example:

* Numbers are grouped under **Numeric Data Types**.
* Text and ordered collections are grouped under **Sequence Data Types**.
* Key-value pairs are grouped under **Mapping Data Types**.

---

# Why are Categories of Data Types Required?

Categories of data types help us to:

* Understand Python data types easily.
* Select the correct data type for a program.
* Write readable and maintainable code.
* Improve memory utilization.
* Organize data efficiently.
* Perform operations specific to each type of data.

---

# Categories of Python Data Types

Python provides the following built-in categories of data types.

```text
Python Data Types

│

├── Numeric Data Types
│      ├── int
│      ├── float
│      └── complex
│
├── Boolean Data Type
│      └── bool
│
├── Sequence Data Types
│      ├── str
│      ├── list
│      ├── tuple
│      └── range
│
├── Set Data Types
│      ├── set
│      └── frozenset
│
├── Mapping Data Type
│      └── dict
│
├── Binary Data Types
│      ├── bytes
│      ├── bytearray
│      └── memoryview
│
└── None Type
       └── None
```

---

# 1. Numeric Data Types

Numeric data types are used to store numbers.

Python provides three numeric data types.

| Data Type | Description            | Example  |
| --------- | ---------------------- | -------- |
| `int`     | Stores whole numbers   | `100`    |
| `float`   | Stores decimal numbers | `45.75`  |
| `complex` | Stores complex numbers | `5 + 3j` |

### Example

```python
age = 22
price = 499.99
number = 5 + 2j

print(type(age))
print(type(price))
print(type(number))
```

### Output

```text
<class 'int'>
<class 'float'>
<class 'complex'>
```

---

# 2. Boolean Data Type

The Boolean data type stores logical values.

It contains only two possible values.

* True
* False

### Example

```python
is_logged_in = True
is_admin = False

print(type(is_logged_in))
print(type(is_admin))
```

### Output

```text
<class 'bool'>
<class 'bool'>
```

---

# 3. Sequence Data Types

Sequence data types store an ordered collection of elements.

Python provides four sequence data types.

| Data Type | Description                          |
| --------- | ------------------------------------ |
| `str`     | Stores text                          |
| `list`    | Stores ordered mutable collections   |
| `tuple`   | Stores ordered immutable collections |
| `range`   | Represents a sequence of numbers     |

### Example

```python
name = "Python"

languages = ["Python", "Java", "C"]

numbers = (10, 20, 30)

values = range(5)
```

---

# 4. Set Data Types

Set data types store unique values.

Duplicate values are automatically removed.

Python provides two set data types.

| Data Type   | Description                           |
| ----------- | ------------------------------------- |
| `set`       | Mutable collection of unique values   |
| `frozenset` | Immutable collection of unique values |

### Example

```python
numbers = {10, 20, 30}

colors = frozenset({"Red", "Green", "Blue"})
```

---

# 5. Mapping Data Type

Mapping data types store information in the form of **key-value pairs**.

Python provides one mapping data type.

| Data Type | Description            |
| --------- | ---------------------- |
| `dict`    | Stores key-value pairs |

### Example

```python
student = {
    "Name": "Basha",
    "Age": 22,
    "Course": "Python"
}
```

---

# 6. Binary Data Types

Binary data types are used to store binary (byte) data.

Python provides three binary data types.

| Data Type    | Description                          |
| ------------ | ------------------------------------ |
| `bytes`      | Immutable sequence of bytes          |
| `bytearray`  | Mutable sequence of bytes            |
| `memoryview` | Memory-efficient view of binary data |

### Example

```python
data1 = bytes([65, 66, 67])

data2 = bytearray([68, 69, 70])

data3 = memoryview(data2)
```

---

# 7. None Type

The `None` type represents the absence of a value.

Python has only one value of this type.

```python
result = None

print(result)

print(type(result))
```

### Output

```text
None
<class 'NoneType'>
```

---

# Summary Table

| Category  | Data Types                         |
| --------- | ---------------------------------- |
| Numeric   | `int`, `float`, `complex`          |
| Boolean   | `bool`                             |
| Sequence  | `str`, `list`, `tuple`, `range`    |
| Set       | `set`, `frozenset`                 |
| Mapping   | `dict`                             |
| Binary    | `bytes`, `bytearray`, `memoryview` |
| None Type | `None`                             |

---

# Mutable and Immutable Data Types

Understanding mutability is important because it determines whether an object can be modified after it is created.

## Mutable Data Types

These data types can be modified after creation.

* list
* set
* dict
* bytearray

### Example

```python
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
```

Output

```text
[10, 20, 30, 40]
```

---

## Immutable Data Types

These data types cannot be modified after creation.

* int
* float
* complex
* bool
* str
* tuple
* range
* frozenset
* bytes
* NoneType

### Example

```python
name = "Python"

# name[0] = "J"   # Error
```

---

# Memory Classification

```text
Python Data Types

↓

Numeric
    int
    float
    complex

↓

Boolean
    bool

↓

Sequence
    str
    list
    tuple
    range

↓

Set
    set
    frozenset

↓

Mapping
    dict

↓

Binary
    bytes
    bytearray
    memoryview

↓

None
    NoneType
```

---

# Characteristics

* Every value in Python belongs to a specific data type.
* Python automatically determines the data type during execution.
* Some data types are mutable, while others are immutable.
* Different data types support different operations.
* Each category is designed for a specific purpose.

---

# Real-World Applications

| Category   | Example Applications                              |
| ---------- | ------------------------------------------------- |
| Numeric    | Banking, Billing Systems, Scientific Calculations |
| Boolean    | Login Systems, Authentication, Decision Making    |
| String     | Names, Addresses, Emails, Messages                |
| List       | Shopping Cart, Employee Records                   |
| Tuple      | Coordinates, Fixed Configuration Values           |
| Set        | Unique User IDs, Tags, Permissions                |
| Dictionary | Student Records, Product Details                  |
| Binary     | Images, Audio Files, Video Files                  |
| None       | Default Values, Function Return Values            |

---

# Best Practices

* Select the appropriate data type based on the requirement.
* Use immutable data types whenever data should remain unchanged.
* Use mutable data types only when modification is required.
* Use dictionaries for related key-value information.
* Learn the characteristics of each category before using it.

---

# Interview Questions

## 1. What is a data type category in Python?

A data type category is a group of related data types that are used to store similar kinds of data.

---

## 2. How many categories of built-in data types are available in Python?

Python provides seven built-in categories:

* Numeric
* Boolean
* Sequence
* Set
* Mapping
* Binary
* None Type

---

## 3. Which data types are mutable?

* list
* set
* dict
* bytearray

---

## 4. Which data types are immutable?

* int
* float
* complex
* bool
* str
* tuple
* range
* frozenset
* bytes
* NoneType

---

## Summary

In this chapter, you learned:

* What data type categories are.
* Why Python groups data types into categories.
* The seven built-in categories of data types.
* The data types available in each category.
* Mutable and immutable data types.
* Characteristics, best practices, and real-world applications.

In the next chapter, you will learn the first numeric data type: **Integer (`int`)**, including its syntax, memory representation, built-in functions, arithmetic operations, and practical applications.
