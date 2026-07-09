# Introduction to File Handling in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is File Handling?
5. Why is File Handling Required?
6. Types of Files
7. File Operations
8. File Handling Life Cycle
9. Internal Working
10. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand File Handling.
- Learn why File Handling is required.
- Understand different file types.
- Learn the basic file operations.
- Understand the File Handling life cycle.
- Prepare for interview questions related to File Handling.

---

# Prerequisites

Before learning this chapter, you should know:

- Variables
- Strings
- Functions
- Lists
- Exception Handling

---

# Introduction

A program stores data in memory while it is running.

However,

when the program terminates,

all data stored in memory is lost.

Sometimes,

we need to store information permanently.

Examples include:

- Student records
- Employee details
- Banking information
- User credentials
- Application logs
- Configuration files

Python provides **File Handling** to store and retrieve data from files.

---

# What is File Handling?

## Definition

**File Handling** is the process of creating, opening, reading, writing, updating, and deleting files using a programming language.

---

## Simple Definition

> File Handling allows programs to store data permanently inside files.

---

# Why is File Handling Required?

Without File Handling,

every time the program closes,

all information stored in memory disappears.

Using files allows us to:

- Store data permanently.
- Retrieve data whenever required.
- Share information between programs.
- Maintain application records.
- Save reports and logs.

---

# Real-World Examples

## Banking System

Stores

- Customer Details
- Transactions
- Account Information

---

## College Management System

Stores

- Student Records
- Attendance
- Marks
- Fee Details

---

## Hospital Management System

Stores

- Patient Details
- Medical Reports
- Billing Information

---

## E-Commerce Website

Stores

- Orders
- Product Information
- Customer Details
- Payment Records

---

# Types of Files

Python mainly works with two categories of files.

## 1. Text Files

These files store human-readable data.

Examples

```text
.txt
.csv
.json
.xml
.html
.py
.md
```

Example

```text
Name : John

Age : 25
```

---

## 2. Binary Files

Binary files store data in binary format.

These files are generally not human-readable.

Examples

```text
.jpg
.png
.mp3
.mp4
.pdf
.exe
.docx
.xlsx
```

---

# File Operations

Python supports several operations on files.

## Create File

Creates a new file if it does not already exist.

---

## Open File

Opens an existing file for processing.

---

## Read File

Retrieves data from a file.

---

## Write File

Writes new data into a file.

---

## Append File

Adds new data to the end of an existing file.

---

## Update File

Modifies existing file content.

---

## Close File

Releases system resources associated with the file.

---

## Delete File

Removes a file from the storage device.

---

# File Handling Life Cycle

```text
Create File

↓

Open File

↓

Read / Write / Append

↓

Save Changes

↓

Close File

↓

File Stored Permanently
```

---

# Advantages of File Handling

- Permanent storage.
- Easy retrieval.
- Data sharing.
- Better application management.
- Supports large amounts of data.
- Useful for backups.
- Improves data persistence.

---

# Limitations

- Reading and writing files is generally slower than accessing data in memory.
- Files can become corrupted.
- Improper handling may cause data loss.
- Permissions may restrict file access.

---

# Best Practices

- Always close files after use.
- Use the `with` statement whenever possible.
- Handle file-related exceptions.
- Use meaningful file names.
- Store files in organized directories.
- Validate file paths before accessing files.

---

# Common Mistakes

## Mistake 1

Forgetting to close files.

---

## Mistake 2

Opening files in the wrong mode.

---

## Mistake 3

Ignoring exceptions such as

```python
FileNotFoundError
```

---

## Mistake 4

Attempting to read from a file opened in write-only mode.

---

## File Handling Architecture

```text
Python Program

↓

open()

↓

Operating System

↓

Storage Device

↓

File

↓

Read / Write / Append

↓

close()
```

---

# Internal Working

```text
Program Starts

↓

Open File

↓

Operating System Locates File

↓

File Handle Created

↓

Perform File Operation

↓

Save Changes

↓

Close File

↓

Program Ends
```

---

# Advantages of Using the with Statement

Instead of manually closing files,

Python provides the `with` statement.

Benefits:

- Automatically closes files.
- Cleaner code.
- Safer resource management.
- Handles exceptions more effectively.

---

# Dry Run

```text
Program Starts

↓

Open File

↓

Read or Write Data

↓

Save Changes

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

├── RAM

│      │

│      └── File Object

│

└── Storage Device

       │

       └── data.txt
```

---

# Interview Questions

## 1. What is File Handling?

### Answer

File Handling is the process of creating, reading, writing, updating, and deleting files using a programming language.

---

## 2. Why is File Handling important?

### Answer

It allows programs to store data permanently instead of keeping it only in memory.

---

## 3. What are the two main types of files?

### Answer

- Text Files
- Binary Files

---

## 4. What is the difference between RAM and File Storage?

### Answer

RAM stores temporary data, while files provide permanent storage on a storage device.

---

## 5. Name some common text file extensions.

### Answer

- `.txt`
- `.csv`
- `.json`
- `.xml`
- `.html`
- `.md`

---

## 6. Name some common binary file extensions.

### Answer

- `.jpg`
- `.png`
- `.pdf`
- `.docx`
- `.xlsx`
- `.exe`

---

## 7. What are the common file operations?

### Answer

- Create
- Open
- Read
- Write
- Append
- Update
- Close
- Delete

---

## 8. Why should files always be closed?

### Answer

Closing a file releases system resources and ensures that all pending data is written properly.

---

## 9. Which statement automatically closes a file?

### Answer

The `with` statement.

---

## 10. Which exception is raised when a file is not found?

### Answer

```python
FileNotFoundError
```

---

# Practice Questions

1. Explain the File Handling life cycle.
2. Differentiate text files and binary files.
3. List all common file operations.
4. Explain why the `with` statement is preferred.
5. Explain the advantages of File Handling.

---

# Quick Revision

- File Handling → Permanent storage.
- Text File → Human-readable.
- Binary File → Machine-readable.
- Common Operations → Open, Read, Write, Append, Close.
- `with` → Automatically closes files.
- `FileNotFoundError` → File does not exist.

---

# Chapter Summary

In this chapter, you learned:

- Introduction to File Handling
- Need for File Handling
- Types of Files
- File Operations
- File Handling Life Cycle
- Advantages
- Limitations
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Questions
- Quick Revision
