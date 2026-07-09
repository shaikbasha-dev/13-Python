# File Handling Interview Questions and Answers in Python

## Table of Contents

1. Introduction
2. File Handling Basics
3. File Operations
4. File Modes
5. Reading and Writing Files
6. Directories
7. CSV Files
8. JSON Files
9. Scenario-Based Questions
10. Comparison Questions
11. Quick Revision
12. Final Notes

---

# Introduction

This document contains the most frequently asked interview questions related to Python File Handling.

It is useful for:

- Freshers
- Python Developers
- Technical Interviews
- Placement Preparation
- Revision Before Interviews

---

# File Handling Basics

## 1. What is File Handling?

### Answer

File Handling is the process of creating, opening, reading, writing, updating, and deleting files using a programming language.

---

## 2. Why is File Handling important?

### Answer

File Handling allows programs to store data permanently instead of keeping it only in memory.

---

## 3. What are the two main types of files?

### Answer

- Text Files
- Binary Files

---

## 4. What is the difference between RAM and File Storage?

### Answer

RAM stores temporary data that is lost when the program ends, whereas file storage preserves data permanently.

---

## 5. What are some examples of text files?

### Answer

- .txt
- .csv
- .json
- .xml
- .html
- .md

---

## 6. What are some examples of binary files?

### Answer

- .jpg
- .png
- .pdf
- .docx
- .xlsx
- .mp3
- .mp4

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

Closing files releases system resources and ensures that buffered data is written properly.

---

# open() Function

## 9. What is the purpose of the open() function?

### Answer

The `open()` function opens a file and returns a file object that can be used for reading, writing, or updating the file.

---

## 10. What is the syntax of open()?

### Answer

```python
open(file_name, mode)
```

---

## 11. What is the default file mode?

### Answer

```python
r
```

(Read Mode)

---

## 12. What are the parameters of open()?

### Answer

- File Name (or File Path)
- File Mode

---

# File Modes

## 13. What is a file mode?

### Answer

A file mode specifies how a file should be opened and what operations are allowed.

---

## 14. What does `r` mode do?

### Answer

Opens an existing file for reading.

---

## 15. What does `w` mode do?

### Answer

Opens a file for writing.

If the file already exists, its contents are overwritten.

---

## 16. What does `a` mode do?

### Answer

Appends data to the end of the file.

---

## 17. What does `x` mode do?

### Answer

Creates a new file.

If the file already exists,

Python raises

```python
FileExistsError
```

---

## 18. What is the purpose of `r+`?

### Answer

Allows both reading and writing.

---

## 19. What is the purpose of `w+`?

### Answer

Allows reading and writing.

Existing contents are overwritten.

---

## 20. What is the purpose of `a+`?

### Answer

Allows appending and reading.

---

## 21. Which modes are used for binary files?

### Answer

- rb
- wb
- ab

---

# Reading and Writing

## 22. What does `read()` do?

### Answer

Reads the entire file or a specified number of characters.

---

## 23. What does `readline()` do?

### Answer

Reads one line at a time.

---

## 24. What does `readlines()` return?

### Answer

A list containing all lines in the file.

---

## 25. What does `write()` do?

### Answer

Writes a string to a file.

---

## 26. What does `writelines()` do?

### Answer

Writes multiple strings from an iterable to a file.

It does not automatically add newline characters.

---

## 27. What is the advantage of using the `with` statement?

### Answer

It automatically closes the file after the block finishes, even if an exception occurs.

---

## 28. What exception occurs when a file does not exist in read mode?

### Answer

```python
FileNotFoundError
```

---

## 29. What exception occurs when creating an existing file using `x` mode?

### Answer

```python
FileExistsError
```

---

# Directories

## 30. What is a directory?

### Answer

A directory is a folder used to organize files and other directories.

---

## 31. Which module is used for directory operations?

### Answer

```python
os
```

---

## 32. Which module provides an object-oriented interface for paths?

### Answer

```python
pathlib
```

---

## 33. Which function returns the current working directory?

### Answer

```python
os.getcwd()
```

---

## 34. Which function changes the current directory?

### Answer

```python
os.chdir()
```

---

## 35. Which function creates a directory?

### Answer

```python
os.mkdir()
```

---

## 36. Which function creates nested directories?

### Answer

```python
os.makedirs()
```

---

## 37. Which function removes an empty directory?

### Answer

```python
os.rmdir()
```

---

## 38. Which function renames a directory?

### Answer

```python
os.rename()
```

---

## 39. Which function lists all files and folders?

### Answer

```python
os.listdir()
```

---

## 40. How do you check whether a directory exists?

### Answer

```python
os.path.exists(path)
```

or

```python
Path(path).exists()
```

---

# CSV Files

## 41. What does CSV stand for?

### Answer

Comma-Separated Values.

---

## 42. Which module is used for CSV files?

### Answer

```python
csv
```

---

## 43. What does `csv.reader()` return?

### Answer

Each row as a list.

---

## 44. What does `csv.DictReader()` return?

### Answer

Each row as a dictionary using column names as keys.

---

## 45. What does `csv.writer()` do?

### Answer

Writes rows to a CSV file.

---

## 46. What does `csv.DictWriter()` do?

### Answer

Writes dictionary data to a CSV file.

---

# JSON Files

## 47. What does JSON stand for?

### Answer

JavaScript Object Notation.

---

## 48. Which module is used for JSON?

### Answer

```python
json
```

---

## 49. What does `json.dump()` do?

### Answer

Writes a Python object to a JSON file.

---

## 50. What does `json.dumps()` do?

### Answer

Converts a Python object into a JSON string.

---

## 51. What does `json.load()` do?

### Answer

Reads JSON data from a file.

---

## 52. What does `json.loads()` do?

### Answer

Converts a JSON string into a Python object.

---

## 53. What is Serialization?

### Answer

Serialization is the process of converting a Python object into JSON format.

---

## 54. What is Deserialization?

### Answer

Deserialization is the process of converting JSON data back into Python objects.

---

# Comparison Questions

## 55. Difference between `read()` and `readline()`

| read() | readline() |
|---------|------------|
| Reads entire file or specified characters | Reads one line |

---

## 56. Difference between `write()` and `append()`

| Write (`w`) | Append (`a`) |
|--------------|--------------|
| Overwrites existing data | Preserves existing data and adds new data |

---

## 57. Difference between CSV and JSON

| CSV | JSON |
|------|------|
| Tabular data | Key-value structured data |
| Rows and columns | Objects and arrays |
| Best for spreadsheets | Best for APIs |

---

## 58. Difference between `dump()` and `dumps()`

| dump() | dumps() |
|---------|----------|
| Writes to a file | Returns a JSON string |

---

## 59. Difference between `load()` and `loads()`

| load() | loads() |
|---------|-----------|
| Reads from a file | Reads from a string |

---

# Scenario-Based Questions

## 60. Which file mode should be used to preserve existing data?

### Answer

```python
a
```

---

## 61. Which mode should be used to create a file only if it does not exist?

### Answer

```python
x
```

---

## 62. Which file format is commonly used for API responses?

### Answer

JSON.

---

## 63. Which file format is suitable for spreadsheet data?

### Answer

CSV.

---

## 64. Which module should be used to navigate directories?

### Answer

```python
os
```

or

```python
pathlib
```

---

## 65. Which function should be preferred to automatically close files?

### Answer

The `with` statement.

---

# Quick Revision

Remember:

- `open()` → Opens file
- `r` → Read
- `w` → Write
- `a` → Append
- `x` → Create
- `read()` → Entire file
- `readline()` → One line
- `readlines()` → List of lines
- `write()` → Write string
- `writelines()` → Write multiple strings
- `with` → Automatic close
- `os` → Directory operations
- `pathlib` → Object-oriented paths
- CSV → Tabular data
- JSON → Structured data
- Serialization → Python → JSON
- Deserialization → JSON → Python

---

# Final Notes

After completing this chapter, you should be able to:

- Work confidently with Python File Handling.
- Choose the correct file mode for different tasks.
- Read and write text, CSV, and JSON files.
- Perform directory operations.
- Understand serialization and deserialization.
- Answer common File Handling interview questions with confidence.
