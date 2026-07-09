# Type Casting in Python

## Introduction

In Python, sometimes we need to convert one data type into another data type.

For example:

- Convert an integer into a float.
- Convert a float into an integer.
- Convert a number into a string.
- Convert a string into an integer.

This process is called **Type Casting** or **Type Conversion**.

## Definition

**Type Casting** is the process of converting a value from one data type to another data type.

Python provides built-in functions to perform type conversion.

## Why do we use Type Casting?

Type casting is used to:

- Perform mathematical calculations.
- Accept user input.
- Convert one data type into another.
- Avoid type mismatch errors.
- Improve program flexibility.

## Types of Type Casting

Python supports two types of type casting.

```text
Type Casting

│

├── Implicit Type Casting
│
└── Explicit Type Casting
```

# Implicit Type Casting

## Definition

**Implicit Type Casting** is the automatic conversion of one data type into another by the Python interpreter.

The programmer does not perform the conversion manually.

Python automatically converts the smaller data type into a larger compatible data type.

## Example

```python
number1 = 10

number2 = 5.5

result = number1 + number2

print(result)

print(type(result))
```

## Output

```text
15.5

<class 'float'>
```

## Explanation

- `number1` is an integer.
- `number2` is a float.
- Python automatically converts the integer into a float.
- The result becomes a float.

## Memory Representation

```text
10 (int)

        +

5.5 (float)

        │

        ▼

15.5 (float)
```

# Explicit Type Casting

## Definition

**Explicit Type Casting** is the process of converting one data type into another manually using Python's built-in functions.

The programmer performs the conversion.

## Syntax

```python
new_variable = datatype(value)
```

## Example

```python
number = 25.75

result = int(number)

print(result)

print(type(result))
```

## Output

```text
25

<class 'int'>
```

## Explanation

The `int()` function converts the float value into an integer.

The decimal part is removed.

# Built-in Type Conversion Functions

Python provides several built-in functions for type conversion.

| Function | Description |
|----------|-------------|
| `int()` | Converts a value into an integer |
| `float()` | Converts a value into a float |
| `str()` | Converts a value into a string |
| `bool()` | Converts a value into a Boolean |
| `complex()` | Converts a value into a complex number |

# int()

## Example

```python
number = 99.99

print(int(number))
```

### Output

```text
99
```

# float()

## Example

```python
number = 50

print(float(number))
```

### Output

```text
50.0
```

# str()

## Example

```python
number = 100

print(str(number))

print(type(str(number)))
```

### Output

```text
100

<class 'str'>
```

# bool()

## Example

```python
print(bool(1))

print(bool(0))

print(bool("Python"))

print(bool(""))
```

### Output

```text
True

False

True

False
```

# complex()

## Example

```python
number = complex(10)

print(number)
```

### Output

```text
(10+0j)
```

# Complete Type Conversion Program

```python
# Integer to Float
number1 = 100
print(float(number1))

# Float to Integer
number2 = 55.75
print(int(number2))

# Integer to String
number3 = 250
print(str(number3))

# Integer to Boolean
number4 = 1
print(bool(number4))

# Integer to Complex
number5 = 15
print(complex(number5))
```

## Output

```text
100.0

55

250

True

(15+0j)
```

## Pseudocode

```text
START

Create integer value

Convert into float

Display result

Create float value

Convert into integer

Display result

Convert integer into string

Display result

Convert integer into Boolean

Display result

Convert integer into complex

Display result

STOP
```

## Line-by-Line Explanation

### Line 1

Creates an integer variable.

### Line 2

Converts the integer into a float.

### Line 3

Displays the float value.

### Line 4

Creates a float variable.

### Line 5

Converts the float into an integer.

### Line 6

Displays the integer value.

### Line 7

Converts the integer into a string.

### Line 8

Displays the string.

### Line 9

Converts the integer into a Boolean.

### Line 10

Displays the Boolean value.

### Line 11

Converts the integer into a complex number.

### Line 12

Displays the complex number.

## Comparison

| Implicit Type Casting | Explicit Type Casting |
|------------------------|----------------------|
| Automatic conversion | Manual conversion |
| Done by Python | Done by Programmer |
| No built-in function required | Uses built-in functions |
| Safe conversion | Programmer controls conversion |

## Characteristics of Type Casting

- Converts one data type into another.
- Improves compatibility between data types.
- Uses built-in conversion functions.
- Reduces type mismatch errors.
- Makes programs more flexible.

## Summary

- Type Casting means converting one data type into another.
- Python supports **Implicit** and **Explicit** type casting.
- Implicit conversion is done automatically by Python.
- Explicit conversion is done manually using built-in functions.
- Common conversion functions are `int()`, `float()`, `str()`, `bool()`, and `complex()`.
