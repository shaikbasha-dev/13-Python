# Boolean (`bool`) - Operations

## Introduction

Boolean operations form the foundation of decision-making in Python. They are used to compare values, combine conditions, evaluate expressions, and control the flow of program execution.

Almost every Python program uses Boolean operations through conditional statements (`if`, `elif`, `else`), loops (`while`), and logical expressions.

---

# Comparison Operators

Comparison operators compare two values and always return a Boolean value (`True` or `False`).

## Comparison Operators Table

| Operator | Description              | Example    | Result |
| -------- | ------------------------ | ---------- | ------ |
| `==`     | Equal To                 | `10 == 10` | `True` |
| `!=`     | Not Equal To             | `10 != 5`  | `True` |
| `>`      | Greater Than             | `15 > 10`  | `True` |
| `<`      | Less Than                | `5 < 10`   | `True` |
| `>=`     | Greater Than or Equal To | `10 >= 10` | `True` |
| `<=`     | Less Than or Equal To    | `8 <= 12`  | `True` |

---

## Program

```python
a = 15
b = 10

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
```

---

## Output

```text
False
True
True
False
True
False
```

---

# Logical Operators

Logical operators combine two or more Boolean expressions.

Python provides three logical operators.

| Operator | Description                                      |
| -------- | ------------------------------------------------ |
| `and`    | Returns `True` if both conditions are true       |
| `or`     | Returns `True` if at least one condition is true |
| `not`    | Reverses the Boolean value                       |

---

# Logical AND

The `and` operator returns `True` only when both conditions are `True`.

## Example

```python
age = 22
citizen = True

print(age >= 18 and citizen)
```

Output

```text
True
```

---

# Logical OR

The `or` operator returns `True` if at least one condition is `True`.

## Example

```python
is_admin = False
is_manager = True

print(is_admin or is_manager)
```

Output

```text
True
```

---

# Logical NOT

The `not` operator reverses the Boolean value.

## Example

```python
is_logged_in = True

print(not is_logged_in)
```

Output

```text
False
```

---

# Truth Tables

## AND (`and`)

| A     | B     | Result |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | False  |
| False | True  | False  |
| False | False | False  |

---

## OR (`or`)

| A     | B     | Result |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

---

## NOT (`not`)

| A     | Result |
| ----- | ------ |
| True  | False  |
| False | True   |

---

# Truth Value Testing

In Python, many objects can be evaluated as either `True` or `False`.

## Values Evaluated as False

```python
False
None
0
0.0
0j
''
""
[]
()
{}
set()
range(0)
```

---

## Values Evaluated as True

```python
1
-10
3.14
"Python"
[1, 2]
(10,)
{"A": 1}
{5}
range(5)
```

---

# Program

```python
print(bool(0))
print(bool(100))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([1]))
```

---

## Output

```text
False
True
False
True
False
True
```

---

# Boolean Conversion

Python converts values into Boolean objects using the `bool()` function.

## Integer to Boolean

```python
print(bool(1))
print(bool(0))
print(bool(-10))
```

Output

```text
True
False
True
```

---

## Float to Boolean

```python
print(bool(10.5))
print(bool(0.0))
```

Output

```text
True
False
```

---

## String to Boolean

```python
print(bool(""))
print(bool("Python"))
print(bool(" "))
```

Output

```text
False
True
True
```

A string containing a space is **not** empty, so it evaluates to `True`.

---

## List to Boolean

```python
print(bool([]))
print(bool([10]))
```

Output

```text
False
True
```

---

# Short-Circuit Evaluation

Python uses short-circuit evaluation with logical operators.

## AND Example

```python
print(False and (10 / 0))
```

Output

```text
False
```

The second expression is never evaluated because the first operand is already `False`.

---

## OR Example

```python
print(True or (10 / 0))
```

Output

```text
True
```

The second expression is skipped because the first operand is already `True`.

---

# Real-World Applications

Boolean operations are widely used in:

* Login systems
* Online payment verification
* Age validation
* Access control
* User authentication
* Form validation
* Search filtering
* Business rule evaluation

---

# Best Practices

* Write clear Boolean expressions.
* Avoid unnecessary comparisons such as `if value == True`.
* Prefer direct expressions:

Correct

```python
if is_logged_in:
    print("Welcome")
```

Instead of

```python
if is_logged_in == True:
    print("Welcome")
```

* Use parentheses for complex logical expressions to improve readability.

---

# Common Mistakes

## 1. Using Assignment Instead of Comparison

Incorrect

```python
if age = 18:
    print("Eligible")
```

Correct

```python
if age == 18:
    print("Eligible")
```

---

## 2. Confusing Empty and Non-Empty Strings

```python
bool("")
```

Result

```text
False
```

```python
bool(" ")
```

Result

```text
True
```

---

## 3. Forgetting Short-Circuit Behavior

Remember that `and` and `or` may skip evaluating the second operand.

---

# Frequently Asked Interview Questions

## 1. What are the logical operators in Python?

* `and`
* `or`
* `not`

---

## 2. Which values evaluate to `False`?

* False
* None
* Numeric zero (`0`, `0.0`, `0j`)
* Empty string
* Empty list
* Empty tuple
* Empty dictionary
* Empty set
* `range(0)`

---

## 3. What is short-circuit evaluation?

Python stops evaluating an expression as soon as the final result is determined.

---

## 4. What does `bool(" ")` return?

`True`

Because the string contains one space and is therefore not empty.

---

## 5. What is the output?

```python
print(bool([]))
```

Output

```text
False
```

---

# Summary

In this chapter, you learned:

* Comparison operators
* Logical operators
* Truth tables
* Truth value testing
* Boolean conversion
* Short-circuit evaluation
* Real-world applications
* Best practices
* Common mistakes
* Frequently asked interview questions

In the next chapter, you will learn advanced concepts of the `bool` data type, including Python's internal implementation, memory management, singleton objects, the relationship between `bool` and `int`, object identity, and advanced interview topics.
