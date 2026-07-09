# String (`str`) - Operations

## Introduction

Python provides several operators that can be used with strings. These operators allow programmers to combine strings, repeat strings, compare strings, check the existence of characters or words, and perform many other useful operations.

Understanding string operations is essential because almost every Python application processes textual data.

---

# String Concatenation

Concatenation means joining two or more strings together.

Python uses the **`+`** operator for string concatenation.

---

## Syntax

```python
string1 + string2
```

---

## Example

```python
first_name = "Shaik"

last_name = "Basha"

full_name = first_name + " " + last_name

print(full_name)
```

---

## Output

```text
Shaik Basha
```

---

## Memory Representation

Before Concatenation

```text
first_name ──► "Shaik"

last_name ───► "Basha"
```

After Concatenation

```text
full_name ──► "Shaik Basha"
```

Python creates a **new string object** because strings are immutable.

---

# String Repetition

The `*` operator repeats a string multiple times.

---

## Syntax

```python
string * number
```

---

## Example

```python
text = "Python "

print(text * 3)
```

---

## Output

```text
Python Python Python
```

---

# Membership Operators

Membership operators determine whether a substring exists inside another string.

Python provides two membership operators.

| Operator | Description                                    |
| -------- | ---------------------------------------------- |
| `in`     | Returns `True` if the substring exists         |
| `not in` | Returns `True` if the substring does not exist |

---

## Example

```python
language = "Python Programming"

print("Python" in language)

print("Java" in language)

print("Java" not in language)
```

---

## Output

```text
True

False

True
```

---

# Comparison Operators

Strings can be compared using comparison operators.

Python compares strings **lexicographically** (dictionary order) using Unicode values.

---

## Supported Operators

| Operator | Description              |
| -------- | ------------------------ |
| `==`     | Equal To                 |
| `!=`     | Not Equal To             |
| `>`      | Greater Than             |
| `<`      | Less Than                |
| `>=`     | Greater Than or Equal To |
| `<=`     | Less Than or Equal To    |

---

## Example

```python
print("Apple" == "Apple")

print("Apple" != "Orange")

print("Banana" > "Apple")

print("Cat" < "Dog")
```

---

## Output

```text
True

True

True

True
```

---

# String Length

The `len()` function returns the total number of characters in a string.

---

## Example

```python
text = "Python"

print(len(text))
```

---

## Output

```text
6
```

---

# Iterating Through a String

Strings are sequences, so each character can be accessed one by one using a loop.

---

## Example

```python
language = "Python"

for character in language:
    print(character)
```

---

## Output

```text
P
y
t
h
o
n
```

---

# Escape Characters

Escape characters allow special characters to be included inside strings.

| Escape Sequence | Meaning        |
| --------------- | -------------- |
| `\n`            | New Line       |
| `\t`            | Horizontal Tab |
| `\\`            | Backslash      |
| `\'`            | Single Quote   |
| `\"`            | Double Quote   |

---

## Example

```python
print("Hello\nPython")

print("Name\tAge")

print("C:\\Users\\Admin")
```

---

## Output

```text
Hello
Python

Name    Age

C:\Users\Admin
```

---

# Raw Strings

Raw strings treat backslashes as ordinary characters.

Prefix the string with `r`.

---

## Example

```python
path = r"C:\Users\Admin\Documents"

print(path)
```

---

## Output

```text
C:\Users\Admin\Documents
```

---

# Unicode Support

Python strings support Unicode characters.

---

## Example

```python
print("こんにちは")

print("مرحبا")

print("नमस्ते")
```

---

## Output

```text
こんにちは

مرحبا

नमस्ते
```

---

# Real-World Applications

String operations are used in:

* User registration
* Login systems
* Text editors
* Search engines
* Email validation
* Chat applications
* Report generation
* File processing

---

# Best Practices

* Use concatenation for combining small strings.
* Use formatted strings for complex output.
* Use `len()` instead of manually counting characters.
* Use raw strings for file paths and regular expressions.
* Use meaningful variable names.

---

# Common Mistakes

## 1. Concatenating String and Integer

Incorrect

```python
age = 21

print("Age: " + age)
```

Output

```text
TypeError
```

Correct

```python
age = 21

print("Age: " + str(age))
```

---

## 2. Forgetting Spaces During Concatenation

Incorrect

```python
print("Hello" + "World")
```

Output

```text
HelloWorld
```

Correct

```python
print("Hello " + "World")
```

Output

```text
Hello World
```

---

## 3. Incorrect Escape Characters

Incorrect

```python
print("C:\new")
```

`\n` is interpreted as a newline.

Correct

```python
print(r"C:\new")
```

---

# Frequently Asked Interview Questions

## 1. Which operator is used for string concatenation?

The `+` operator.

---

## 2. Which operator is used for string repetition?

The `*` operator.

---

## 3. Which operators check membership?

* `in`
* `not in`

---

## 4. How are strings compared?

Strings are compared lexicographically using Unicode values.

---

## 5. Which function returns the length of a string?

The `len()` function.

---

## 6. What is a raw string?

A raw string is prefixed with `r` and treats backslashes as ordinary characters.

Example:

```python
path = r"C:\Users\Admin"
```

---

# Summary

In this chapter, you learned:

* String concatenation
* String repetition
* Membership operators
* Comparison operators
* String length
* String iteration
* Escape characters
* Raw strings
* Unicode support
* Best practices
* Common mistakes
* Frequently asked interview questions

In the next chapter, you will learn **String Indexing and Slicing**, including positive indexing, negative indexing, slicing syntax, step values, and practical examples.
