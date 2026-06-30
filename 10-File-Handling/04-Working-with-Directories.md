# Working with Directories in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is a Directory?
5. Why are Directories Required?
6. The os Module
7. The pathlib Module
8. Common Directory Operations
9. Current Working Directory
10. Internal Working
11. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand directories.
- Work with the os module.
- Work with the pathlib module.
- Create directories.
- Rename directories.
- Delete directories.
- Navigate between directories.
- List files and folders.

---

# Prerequisites

Before learning this chapter, you should know:

- File Handling
- File Modes
- Python Modules
- Basic Operating System Concepts

---

# Introduction

A computer stores files inside folders.

In programming,

these folders are called **directories**.

Directories help organize files in a structured manner.

Example

```text
Project

│

├── main.py

├── README.md

├── data

│      ├── students.txt

│      └── employees.txt

└── images

       └── logo.png
```

Python provides modules such as

- os
- pathlib

to work with directories.

---

# What is a Directory?

## Definition

A directory is a container that stores files and other directories.

---

## Simple Definition

> A directory is a folder used to organize files.

---

# Why are Directories Required?

Directories help:

- Organize files.
- Separate project resources.
- Improve maintainability.
- Reduce file management complexity.
- Simplify backups.

---

# The os Module

Python provides the

```python
os
```

module

for interacting with the operating system.

Import

```python
import os
```

Common operations include:

- Create directories
- Remove directories
- Rename directories
- Change directories
- List directory contents
- Get current directory

---

# The pathlib Module

Python also provides

```python
pathlib
```

which offers an object-oriented approach to working with files and directories.

Import

```python
from pathlib import Path
```

Advantages

- Cleaner syntax
- Cross-platform compatibility
- Easier path manipulation

---

# Common Directory Operations

| Operation | Function |
|-----------|----------|
| Get Current Directory | `os.getcwd()` |
| Change Directory | `os.chdir()` |
| List Files | `os.listdir()` |
| Create Directory | `os.mkdir()` |
| Create Nested Directories | `os.makedirs()` |
| Remove Empty Directory | `os.rmdir()` |
| Remove Nested Directories | `os.removedirs()` |
| Rename Directory | `os.rename()` |
| Check Existence | `os.path.exists()` |

---

# Current Working Directory

The Current Working Directory (CWD) is the directory in which the Python program is currently executing.

Example

```python
import os

print(os.getcwd())
```

---

# Changing Directory

```python
import os

os.chdir("Projects")
```

---

# Listing Files

```python
import os

print(os.listdir())
```

---

# Creating a Directory

```python
import os

os.mkdir("PythonFiles")
```

---

# Creating Nested Directories

```python
import os

os.makedirs("Project/Data/Students")
```

---

# Removing a Directory

```python
import os

os.rmdir("PythonFiles")
```

The directory must be empty.

---

# Removing Nested Directories

```python
import os

os.removedirs("Project/Data/Students")
```

Removes empty directories recursively.

---

# Renaming a Directory

```python
import os

os.rename("OldFolder","NewFolder")
```

---

# Checking Directory Existence

```python
import os

print(os.path.exists("Project"))
```

---

# Using pathlib

Creating a directory

```python
from pathlib import Path

Path("Students").mkdir()
```

Checking existence

```python
from pathlib import Path

print(Path("Students").exists())
```

---

# Internal Working

```text
Python Program

↓

OS Module

↓

Operating System

↓

Storage Device

↓

Directory Operations

↓

Result Returned
```

---

# Advantages

- Organizes files.
- Simplifies navigation.
- Supports automation.
- Cross-platform support.
- Easy project management.

---

# Best Practices

- Use meaningful directory names.
- Check if a directory exists before creating it.
- Prefer `pathlib` for new projects.
- Handle exceptions.
- Avoid hard-coded file paths.

---

# Common Mistakes

## Mistake 1

Creating a directory that already exists.

Raises

```python
FileExistsError
```

---

## Mistake 2

Removing a non-empty directory using

```python
os.rmdir()
```

Raises

```python
OSError
```

---

## Mistake 3

Using incorrect directory paths.

---

## Mistake 4

Changing directories without verifying the target exists.

---

# Program 1 – Display Current Directory

```python
import os

print(os.getcwd())
```

---

## Sample Output

```text
C:\Users\Student\Projects
```

---

# Program 2 – List Files and Folders

```python
import os

print(os.listdir())
```

---

## Sample Output

```text
['main.py', 'README.md', 'data']
```

---

# Program 3 – Create a Directory

```python
import os

os.mkdir("Python")
```

---

# Program 4 – Create Nested Directories

```python
import os

os.makedirs("Project/Data/Students")
```

---

# Program 5 – Rename Directory

```python
import os

os.rename("Python","PythonProject")
```

---

# Program 6 – Remove Empty Directory

```python
import os

os.rmdir("PythonProject")
```

---

# Program 7 – Check Directory Exists

```python
import os

print(os.path.exists("Project"))
```

---

## Sample Output

```text
True
```

---

# Program 8 – Change Directory

```python
import os

os.chdir("Project")

print(os.getcwd())
```

---

# Program 9 – Create Directory using pathlib

```python
from pathlib import Path

Path("Images").mkdir()
```

---

# Program 10 – Check Directory using pathlib

```python
from pathlib import Path

directory = Path("Images")

print(directory.exists())
```

---

## Sample Output

```text
True
```

---

# Dry Run

```text
Program Starts

↓

Import os

↓

Choose Directory Operation

↓

Operating System Executes

↓

Result Returned

↓

Program Ends
```

---

# Memory Representation

```text
Python Program

│

├── os Module

│      │

│      ├── getcwd()

│      ├── mkdir()

│      ├── listdir()

│      ├── rename()

│      └── rmdir()

│

└── Operating System
```

---

# Interview Questions

## 1. What is a directory?

### Answer

A directory is a folder that stores files and other directories.

---

## 2. Which module is commonly used for directory operations?

### Answer

```python
os
```

---

## 3. Which module provides an object-oriented way to work with directories?

### Answer

```python
pathlib
```

---

## 4. Which function returns the current working directory?

### Answer

```python
os.getcwd()
```

---

## 5. Which function changes the current directory?

### Answer

```python
os.chdir()
```

---

## 6. Which function creates a directory?

### Answer

```python
os.mkdir()
```

---

## 7. What is the difference between `os.mkdir()` and `os.makedirs()`?

### Answer

- `os.mkdir()` creates a single directory.
- `os.makedirs()` creates nested directories.

---

## 8. Which function lists directory contents?

### Answer

```python
os.listdir()
```

---

## 9. Can `os.rmdir()` remove a non-empty directory?

### Answer

No.

It removes only empty directories.

---

## 10. How do you check whether a directory exists?

### Answer

```python
os.path.exists(path)
```

or

```python
Path(path).exists()
```

---

# Practice Programs

1. Display the current working directory.
2. Create a new directory.
3. Create nested directories.
4. Rename a directory.
5. Delete an empty directory.
6. Display all files in a directory.
7. Check whether a directory exists.
8. Create a directory using `pathlib`.

---

# Quick Revision

- `os.getcwd()` → Current directory
- `os.chdir()` → Change directory
- `os.listdir()` → List files
- `os.mkdir()` → Create one directory
- `os.makedirs()` → Create nested directories
- `os.rmdir()` → Remove empty directory
- `os.rename()` → Rename directory
- `Path.mkdir()` → Create directory
- `Path.exists()` → Check existence

---

# Chapter Summary

In this chapter, you learned:

- Directories
- os Module
- pathlib Module
- Creating Directories
- Removing Directories
- Renaming Directories
- Changing Directories
- Listing Files
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
