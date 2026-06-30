# Reading and Writing Files in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. Opening a File
5. The open() Function
6. Syntax
7. Parameters of open()
8. File Modes
9. Reading Methods
10. Writing Methods
11. The with Statement
12. Internal Working
13. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Open files using the open() function.
- Read file contents using different methods.
- Write data into files.
- Understand file modes.
- Use the with statement.
- Handle files safely.

---

# Prerequisites

Before learning this chapter, you should know:

- File Handling Basics
- Strings
- Variables
- Functions
- Exception Handling

---

# Introduction

Before reading or writing data,

a file must first be opened.

Python provides the built-in

```python
open()
```

function to access files.

After opening a file,

we can

- Read data
- Write data
- Append data
- Close the file

---

# Opening a File

The first step in File Handling is opening the file.

Python uses

```python
open()
```

to create a connection between the program and the file.

---

# The open() Function

## Definition

The `open()` function opens a file and returns a file object.

The returned file object is used to perform all file operations.

---

# Syntax

```python
open(file_name, mode)
```

---

# Parameters

## file_name

Specifies the name or path of the file.

Example

```python
"student.txt"
```

---

## mode

Specifies how the file will be opened.

Examples

```text
r
w
a
x
```

---

# File Modes

| Mode | Description |
|------|-------------|
| `r` | Read existing file (default) |
| `w` | Write (creates new file or overwrites existing file) |
| `a` | Append data to the end of an existing file |
| `x` | Create a new file. Raises an error if the file already exists |
| `r+` | Read and write |
| `w+` | Read and write (overwrites existing content) |
| `a+` | Read and append |
| `rb` | Read binary file |
| `wb` | Write binary file |
| `ab` | Append binary file |

---

# Reading Methods

Python provides several methods for reading data.

## read()

Reads the entire file or a specified number of characters.

Example

```python
file = open("student.txt","r")

print(file.read())

file.close()
```

---

## readline()

Reads one line at a time.

Example

```python
file = open("student.txt","r")

print(file.readline())

file.close()
```

---

## readlines()

Reads all lines and returns a list.

Example

```python
file = open("student.txt","r")

print(file.readlines())

file.close()
```

---

# Writing Methods

## write()

Writes a string into the file.

Example

```python
file = open("student.txt","w")

file.write("Hello Python")

file.close()
```

---

## writelines()

Writes multiple lines.

Example

```python
file = open("student.txt","w")

file.writelines([

"Java\n",

"Python\n",

"SQL\n"

])

file.close()
```

---

# The with Statement

Instead of writing

```python
file = open(...)

...

file.close()
```

Python recommends

```python
with open("student.txt","r") as file:

    print(file.read())
```

Advantages

- Automatically closes the file.
- Cleaner code.
- Better exception handling.
- Prevents resource leaks.

---

# Internal Working

```text
Program Starts

↓

open()

↓

Operating System Opens File

↓

File Object Created

↓

Read / Write Operation

↓

close()

↓

Program Ends
```

---

# Advantages

- Easy file access.
- Supports different file modes.
- Safe resource management using `with`.
- Supports both text and binary files.

---

# Best Practices

- Always use the `with` statement when possible.
- Open files in the correct mode.
- Close files after use if not using `with`.
- Handle file-related exceptions.
- Use descriptive file names.

---

# Common Mistakes

## Mistake 1

Opening a non-existent file in read mode.

Raises

```python
FileNotFoundError
```

---

## Mistake 2

Using write mode unintentionally.

`w` deletes existing content before writing.

---

## Mistake 3

Forgetting to close files when not using `with`.

---

## Mistake 4

Trying to read from a file opened in write mode.

---

# Program 1 – Open a File

```python
file = open("student.txt", "r")

print(file)

file.close()
```

---

## Output

```text
<_io.TextIOWrapper ...>
```

---

# Program 2 – Read Entire File

```python
file = open("student.txt", "r")

print(file.read())

file.close()
```

---

## Sample Output

```text
Welcome to Python
File Handling Example
```

---

# Program 3 – Read One Line

```python
file = open("student.txt", "r")

print(file.readline())

file.close()
```

---

## Sample Output

```text
Welcome to Python
```

---

# Program 4 – Read All Lines

```python
file = open("student.txt", "r")

print(file.readlines())

file.close()
```

---

## Sample Output

```text
['Welcome to Python\n', 'File Handling Example']
```

---

# Program 5 – Write to a File

```python
file = open("student.txt", "w")

file.write("Python Programming")

file.close()
```

---

## Explanation

Creates the file if it does not exist.

If it exists,

its previous content is overwritten.

---

# Program 6 – Append to a File

```python
file = open("student.txt", "a")

file.write("\nAdvanced Python")

file.close()
```

---

## Explanation

Adds data to the end of the file without removing existing content.

---

# Program 7 – Write Multiple Lines

```python
file = open("courses.txt", "w")

file.writelines([

"Java\n",

"Python\n",

"SQL\n"

])

file.close()
```

---

# Program 8 – Using the with Statement

```python
with open("student.txt", "r") as file:

    print(file.read())
```

---

## Explanation

The file is automatically closed after the block finishes.

---

# Program 9 – Create a New File

```python
file = open("newfile.txt", "x")

file.write("New File Created")

file.close()
```

---

## Explanation

Raises

```python
FileExistsError
```

if the file already exists.

---

# Program 10 – Read Limited Characters

```python
file = open("student.txt", "r")

print(file.read(10))

file.close()
```

---

## Sample Output

```text
Welcome t
```

---

# Dry Run

```text
Program Starts

↓

open()

↓

File Object Created

↓

Read / Write Method

↓

Data Processed

↓

close()

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

│      ├── read()

│      ├── write()

│      ├── readline()

│      └── close()

│

└── student.txt
```

---

# Interview Questions

## 1. What is the purpose of the open() function?

### Answer

It opens a file and returns a file object.

---

## 2. What is the default file mode?

### Answer

```python
r
```

(Read Mode)

---

## 3. What is the difference between `read()` and `readline()`?

### Answer

- `read()` reads the entire file or a specified number of characters.
- `readline()` reads one line at a time.

---

## 4. What does `readlines()` return?

### Answer

A list containing all lines in the file.

---

## 5. What is the difference between `write()` and `writelines()`?

### Answer

- `write()` writes a single string.
- `writelines()` writes multiple strings from an iterable. It does **not** automatically add newline characters.

---

## 6. What is the advantage of the `with` statement?

### Answer

It automatically closes the file after the block finishes, even if an exception occurs.

---

## 7. What happens if a file is opened in `w` mode?

### Answer

If the file exists, its contents are overwritten.

If it does not exist, a new file is created.

---

## 8. Which mode is used to append data?

### Answer

```python
a
```

---

## 9. Which mode creates a file only if it does not already exist?

### Answer

```python
x
```

---

## 10. Which exception is raised when opening a non-existent file in read mode?

### Answer

```python
FileNotFoundError
```

---

# Practice Programs

1. Read the complete contents of a file.
2. Read one line at a time.
3. Read only the first 20 characters.
4. Write student details to a file.
5. Append new records to an existing file.
6. Create a new file using `x` mode.
7. Read a file using the `with` statement.

---

# Quick Revision

- `open()` → Opens a file.
- `read()` → Reads complete file or specified characters.
- `readline()` → Reads one line.
- `readlines()` → Returns a list of lines.
- `write()` → Writes one string.
- `writelines()` → Writes multiple strings.
- `with` → Automatically closes the file.
- `r` → Read
- `w` → Write
- `a` → Append
- `x` → Create

---

# Chapter Summary

In this chapter, you learned:

- open() Function
- File Modes
- Reading Methods
- Writing Methods
- The with Statement
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
