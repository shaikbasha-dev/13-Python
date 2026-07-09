# File Modes in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What are File Modes?
5. Why are File Modes Required?
6. Types of File Modes
7. Text Modes
8. Binary Modes
9. File Pointer Behavior
10. File Mode Comparison
11. Internal Working
12. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand file modes.
- Differentiate read, write, append, and create modes.
- Work with update modes.
- Understand binary file modes.
- Learn file pointer behavior.
- Select the correct mode for different scenarios.

---

# Prerequisites

Before learning this chapter, you should know:

- File Handling Basics
- open() Function
- Reading and Writing Files

---

# Introduction

When opening a file,

Python needs to know **how the file will be used**.

For example,

- Read existing data
- Write new data
- Append data
- Create a new file
- Read and write together

This is specified using **File Modes**.

---

# What are File Modes?

## Definition

A **File Mode** specifies the purpose for which a file is opened.

It tells Python what operations are allowed on the file.

---

## Simple Definition

> File modes tell Python how to open and use a file.

---

# Why are File Modes Required?

Different operations require different permissions.

For example:

- Reading requires read permission.
- Writing requires write permission.
- Appending requires append permission.

Using the wrong mode can lead to errors or accidental data loss.

---

# Types of File Modes

| Mode | Description |
|------|-------------|
| `r` | Read |
| `w` | Write |
| `a` | Append |
| `x` | Create |
| `r+` | Read and Write |
| `w+` | Write and Read |
| `a+` | Append and Read |
| `rb` | Read Binary |
| `wb` | Write Binary |
| `ab` | Append Binary |

---

# Read Mode (`r`)

Used for reading an existing file.

If the file does not exist,

Python raises

```python
FileNotFoundError
```

Example

```python
file = open("student.txt", "r")
```

---

# Write Mode (`w`)

Used for writing data.

If the file exists,

its previous contents are removed.

If it does not exist,

Python creates a new file.

Example

```python
file = open("student.txt", "w")
```

---

# Append Mode (`a`)

Adds new data to the end of the file.

Existing data remains unchanged.

Example

```python
file = open("student.txt", "a")
```

---

# Create Mode (`x`)

Creates a new file.

If the file already exists,

Python raises

```python
FileExistsError
```

Example

```python
file = open("student.txt", "x")
```

---

# Read and Write Mode (`r+`)

Allows both reading and writing.

The file must already exist.

Example

```python
file = open("student.txt", "r+")
```

---

# Write and Read Mode (`w+`)

Allows reading and writing.

Existing content is erased before writing.

Example

```python
file = open("student.txt", "w+")
```

---

# Append and Read Mode (`a+`)

Allows appending and reading.

Existing content is preserved.

Example

```python
file = open("student.txt", "a+")
```

---

# Binary Modes

Binary files contain non-text data.

Examples

- Images
- Videos
- Audio
- PDF Documents
- Executables

Binary modes include:

```text
rb

wb

ab
```

Example

```python
file = open("photo.jpg", "rb")
```

---

# File Pointer Behavior

Whenever a file is opened,

Python maintains a **file pointer**.

The file pointer indicates the current reading or writing position.

Example

```text
Python

↓

File Opened

↓

Pointer at Beginning

↓

Read()

↓

Pointer Moves Forward
```

---

# File Mode Comparison

| Mode | Read | Write | Create File | Overwrite | Append |
|------|------|-------|-------------|-----------|--------|
| r | ✅ | ❌ | ❌ | ❌ | ❌ |
| w | ❌ | ✅ | ✅ | ✅ | ❌ |
| a | ❌ | ✅ | ✅ | ❌ | ✅ |
| x | ❌ | ✅ | ✅ (New Only) | ❌ | ❌ |
| r+ | ✅ | ✅ | ❌ | ❌ | ❌ |
| w+ | ✅ | ✅ | ✅ | ✅ | ❌ |
| a+ | ✅ | ✅ | ✅ | ❌ | ✅ |

---

# Internal Working

```text
Program Starts

↓

open(file, mode)

↓

Operating System Checks Mode

↓

Permission Granted

↓

File Object Created

↓

Operation Performed

↓

close()

↓

Program Ends
```

---

# Advantages

- Controls file access.
- Prevents accidental operations.
- Supports different use cases.
- Works with text and binary files.
- Improves application safety.

---

# Best Practices

- Use the least permissive mode required.
- Avoid `w` unless overwriting is intended.
- Use `a` for logs and reports.
- Use `x` when creating new files safely.
- Use binary modes for non-text files.

---

# Common Mistakes

## Mistake 1

Using `w` instead of `a`.

This removes existing content.

---

## Mistake 2

Opening a binary file using text mode.

---

## Mistake 3

Using `r` when the file does not exist.

Raises

```python
FileNotFoundError
```

---

## Mistake 4

Using `x` when the file already exists.

Raises

```python
FileExistsError
```

---

# Program 1 – Read Mode

```python
file = open("student.txt", "r")

print(file.read())

file.close()
```

---

# Program 2 – Write Mode

```python
file = open("student.txt", "w")

file.write("Python")

file.close()
```

---

# Program 3 – Append Mode

```python
file = open("student.txt", "a")

file.write("\nAdvanced Python")

file.close()
```

---

# Program 4 – Create Mode

```python
file = open("newfile.txt", "x")

file.close()
```

---

# Program 5 – Read and Write Mode

```python
file = open("student.txt", "r+")

print(file.read())

file.write("\nNew Record")

file.close()
```

---

# Program 6 – Write and Read Mode

```python
file = open("student.txt", "w+")

file.write("Python")

file.seek(0)

print(file.read())

file.close()
```

---

## Explanation

`seek(0)` moves the file pointer back to the beginning before reading.

---

# Program 7 – Append and Read Mode

```python
file = open("student.txt", "a+")

file.write("\nNew Line")

file.seek(0)

print(file.read())

file.close()
```

---

# Program 8 – Read Binary File

```python
file = open("photo.jpg", "rb")

data = file.read()

print(type(data))

file.close()
```

---

## Sample Output

```text
<class 'bytes'>
```

---

# Program 9 – Write Binary File

```python
file = open("sample.bin", "wb")

file.write(b"Python")

file.close()
```

---

# Program 10 – Append Binary File

```python
file = open("sample.bin", "ab")

file.write(b"123")

file.close()
```

---

# Dry Run

```text
Program Starts

↓

Choose File Mode

↓

Open File

↓

File Pointer Created

↓

Perform Operation

↓

Close File

↓

Program Ends
```

---

# Memory Representation

```text
Python Program

│

├── File Object

│      │

│      ├── Mode : r

│      ├── Pointer

│      └── Data

│

└── student.txt
```

---

# Interview Questions

## 1. What is a file mode?

### Answer

A file mode specifies how a file is opened and what operations are permitted.

---

## 2. Which is the default file mode?

### Answer

```python
r
```

---

## 3. What happens in `w` mode?

### Answer

The file is opened for writing.

If it exists, its contents are overwritten.

If it does not exist, a new file is created.

---

## 4. What is the difference between `w` and `a`?

### Answer

- `w` overwrites existing data.
- `a` preserves existing data and appends new data.

---

## 5. Which mode creates a new file only if it does not exist?

### Answer

```python
x
```

---

## 6. What is the purpose of `r+`?

### Answer

It allows both reading and writing without automatically overwriting the file.

---

## 7. What is the purpose of `seek(0)`?

### Answer

It moves the file pointer to the beginning of the file.

---

## 8. Which modes are used for binary files?

### Answer

- `rb`
- `wb`
- `ab`

---

## 9. Which exception is raised when using `x` on an existing file?

### Answer

```python
FileExistsError
```

---

## 10. Which exception is raised when opening a missing file in `r` mode?

### Answer

```python
FileNotFoundError
```

---

# Practice Programs

1. Open a file using every file mode.
2. Compare `w` and `a`.
3. Read and write using `r+`.
4. Use `seek()` after writing.
5. Read a binary file.

---

# Quick Revision

- `r` → Read
- `w` → Write (Overwrite)
- `a` → Append
- `x` → Create New File
- `r+` → Read + Write
- `w+` → Write + Read
- `a+` → Append + Read
- `rb` → Read Binary
- `wb` → Write Binary
- `ab` → Append Binary

---

# Chapter Summary

In this chapter, we learned:

- File Modes
- Text Modes
- Binary Modes
- File Pointer
- File Mode Comparison
- Practical Programs
- Advantages
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
