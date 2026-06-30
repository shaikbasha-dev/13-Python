# CSV and JSON Files in Python

## Table of Contents

1. Learning Objectives
2. Prerequisites
3. Introduction
4. What is a CSV File?
5. What is a JSON File?
6. Why are CSV and JSON Files Required?
7. Working with the csv Module
8. Working with the json Module
9. Serialization and Deserialization
10. Internal Working
11. Summary

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand CSV files.
- Understand JSON files.
- Read CSV files.
- Write CSV files.
- Read JSON files.
- Write JSON files.
- Understand serialization and deserialization.
- Work with structured data.

---

# Prerequisites

Before learning this chapter, you should know:

- File Handling
- Lists
- Dictionaries
- Functions
- Modules

---

# Introduction

Modern applications exchange and store structured data using standard file formats.

The two most commonly used formats are:

- CSV
- JSON

Examples

- Student records
- Employee information
- Product details
- API responses
- Configuration files
- Reports

Python provides built-in modules to work with both formats.

---

# What is a CSV File?

## Definition

CSV stands for **Comma-Separated Values**.

It stores data in rows and columns where each value is separated by a comma.

Example

```text
ID,Name,Marks

101,Alice,92

102,Bob,85

103,Charlie,90
```

---

## Characteristics of CSV

- Human-readable
- Lightweight
- Easy to edit
- Tabular structure
- Widely supported

---

# What is a JSON File?

## Definition

JSON stands for **JavaScript Object Notation**.

It stores structured data using key-value pairs.

Example

```json
{
    "id":101,
    "name":"Alice",
    "marks":92
}
```

---

## Characteristics of JSON

- Human-readable
- Platform-independent
- Supports nested structures
- Commonly used in APIs
- Easy to exchange data

---

# Why are CSV and JSON Files Required?

CSV is useful for

- Reports
- Excel data
- Databases
- Data analysis

JSON is useful for

- APIs
- Web applications
- Configuration files
- Data exchange
- Cloud applications

---

# CSV Module

Python provides

```python
csv
```

module.

Import

```python
import csv
```

Common Functions

- csv.reader()
- csv.writer()
- csv.DictReader()
- csv.DictWriter()

---

# Reading CSV File

Example

```python
import csv

with open("students.csv","r") as file:

    reader = csv.reader(file)

    for row in reader:

        print(row)
```

---

# Writing CSV File

Example

```python
import csv

with open("students.csv","w",newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["ID","Name","Marks"])

    writer.writerow([101,"Alice",92])
```

---

# Reading CSV using DictReader

Example

```python
import csv

with open("students.csv","r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        print(row)
```

---

# Writing CSV using DictWriter

Example

```python
import csv

with open("students.csv","w",newline="") as file:

    fieldnames=["ID","Name","Marks"]

    writer=csv.DictWriter(file,fieldnames=fieldnames)

    writer.writeheader()

    writer.writerow(

        {"ID":101,"Name":"Alice","Marks":92}

    )
```

---

# JSON Module

Python provides

```python
json
```

module.

Import

```python
import json
```

Common Functions

- json.dump()
- json.dumps()
- json.load()
- json.loads()

---

# Writing JSON File

Example

```python
import json

student = {

    "id":101,

    "name":"Alice",

    "marks":92

}

with open("student.json","w") as file:

    json.dump(student,file,indent=4)
```

---

# Reading JSON File

Example

```python
import json

with open("student.json","r") as file:

    data=json.load(file)

print(data)
```

---

# Serialization

## Definition

Serialization is the process of converting a Python object into JSON format.

Example

```python
json.dumps(dictionary)
```

---

# Deserialization

## Definition

Deserialization is the process of converting JSON data back into Python objects.

Example

```python
json.loads(json_string)
```

---

# CSV vs JSON

| CSV | JSON |
|------|------|
| Tabular Data | Key-Value Data |
| Rows and Columns | Objects and Arrays |
| Simpler Structure | More Flexible Structure |
| Best for Spreadsheet Data | Best for APIs and Web Applications |

---

# Internal Working

```text
Python Program

↓

CSV / JSON Module

↓

Open File

↓

Read / Write Data

↓

Close File

↓

Storage Device
```

---

# Advantages

## CSV

- Simple format.
- Lightweight.
- Easy to edit.
- Excellent for tabular data.

---

## JSON

- Supports nested data.
- Human-readable.
- Easy data exchange.
- Widely used by APIs.

---

# Best Practices

- Use `with` while opening files.
- Validate JSON before processing.
- Use `DictReader` for meaningful CSV column access.
- Use `indent` while writing JSON for better readability.
- Handle exceptions when reading files.

---

# Common Mistakes

## Mistake 1

Forgetting

```python
newline=""
```

while writing CSV on some platforms, which can result in extra blank lines.

---

## Mistake 2

Writing invalid JSON syntax manually.

---

## Mistake 3

Using

```python
json.load()
```

instead of

```python
json.loads()
```

Remember

- `load()` → File
- `loads()` → String

---

## Mistake 4

Confusing

```python
dump()
```

and

```python
dumps()
```

Remember

- `dump()` → Writes to a file.
- `dumps()` → Returns a JSON string.

---

# Program 1 – Read CSV File

```python
import csv

with open("students.csv","r") as file:

    reader = csv.reader(file)

    for row in reader:

        print(row)
```

---

# Program 2 – Write CSV File

```python
import csv

with open("students.csv","w",newline="") as file:

    writer=csv.writer(file)

    writer.writerow(["ID","Name","Marks"])

    writer.writerow([101,"Alice",95])
```

---

# Program 3 – Read CSV using DictReader

```python
import csv

with open("students.csv","r") as file:

    reader=csv.DictReader(file)

    for row in reader:

        print(row["Name"])
```

---

# Program 4 – Write CSV using DictWriter

```python
import csv

with open("students.csv","w",newline="") as file:

    fields=["ID","Name","Marks"]

    writer=csv.DictWriter(file,fieldnames=fields)

    writer.writeheader()

    writer.writerow(

        {"ID":102,"Name":"Bob","Marks":88}

    )
```

---

# Program 5 – Write JSON File

```python
import json

student={

    "id":101,

    "name":"Alice",

    "marks":92

}

with open("student.json","w") as file:

    json.dump(student,file,indent=4)
```

---

# Program 6 – Read JSON File

```python
import json

with open("student.json","r") as file:

    student=json.load(file)

print(student)
```

---

# Program 7 – JSON Serialization

```python
import json

student={

    "id":101,

    "name":"Alice"

}

result=json.dumps(student)

print(result)
```

---

# Program 8 – JSON Deserialization

```python
import json

text='{"name":"Alice","marks":90}'

student=json.loads(text)

print(student)
```

---

# Program 9 – Multiple JSON Objects

```python
import json

students=[

    {"id":1,"name":"Alice"},

    {"id":2,"name":"Bob"}

]

print(json.dumps(students,indent=4))
```

---

# Program 10 – Pretty Print JSON

```python
import json

data={

    "course":"Python",

    "duration":"3 Months"

}

print(json.dumps(data,indent=4))
```

---

# Dry Run

```text
Program Starts

↓

Import csv/json

↓

Open File

↓

Read / Write Data

↓

Convert Objects

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

├── csv Module

│

├── json Module

│

├── CSV File

│

└── JSON File
```

---

# Interview Questions

## 1. What is a CSV file?

### Answer

A CSV file stores tabular data using comma-separated values.

---

## 2. What is JSON?

### Answer

JSON (JavaScript Object Notation) is a lightweight format for storing and exchanging structured data.

---

## 3. Which module is used to work with CSV files?

### Answer

```python
csv
```

---

## 4. Which module is used to work with JSON files?

### Answer

```python
json
```

---

## 5. What is the difference between `csv.reader()` and `csv.DictReader()`?

### Answer

- `csv.reader()` returns each row as a list.
- `csv.DictReader()` returns each row as a dictionary using column names as keys.

---

## 6. What is the difference between `json.dump()` and `json.dumps()`?

### Answer

- `json.dump()` writes JSON data to a file.
- `json.dumps()` converts a Python object into a JSON string.

---

## 7. What is the difference between `json.load()` and `json.loads()`?

### Answer

- `json.load()` reads JSON from a file.
- `json.loads()` parses JSON from a string.

---

## 8. What is serialization?

### Answer

Serialization converts a Python object into JSON format.

---

## 9. What is deserialization?

### Answer

Deserialization converts JSON data back into Python objects.

---

## 10. Which format is more suitable for APIs?

### Answer

JSON.

---

# Practice Programs

1. Read student records from a CSV file.
2. Write employee details to a CSV file.
3. Read data using `DictReader`.
4. Write JSON data to a file.
5. Read JSON from a file.
6. Serialize a Python dictionary.
7. Deserialize a JSON string.

---

# Quick Revision

- CSV → Comma-Separated Values
- JSON → JavaScript Object Notation
- `csv.reader()` → Read CSV
- `csv.writer()` → Write CSV
- `json.dump()` → Write JSON to file
- `json.dumps()` → Python object → JSON string
- `json.load()` → Read JSON from file
- `json.loads()` → JSON string → Python object
- Serialization → Python → JSON
- Deserialization → JSON → Python

---

# Chapter Summary

In this chapter, you learned:

- CSV Files
- JSON Files
- csv Module
- json Module
- Reading CSV
- Writing CSV
- Reading JSON
- Writing JSON
- Serialization
- Deserialization
- Practical Programs
- Best Practices
- Common Mistakes
- Interview Questions
- Practice Programs
- Quick Revision
