# Python Basics Interview Questions and Answers

## Table of Contents

1. Introduction to Python
2. Execution Flow of Python Program
3. Data Types in Python
4. Type Casting in Python
5. Frequently Asked Programs
6. Output-Based Questions
7. Viva Questions
8. Quick Revision

---

# Introduction to Python Interview Questions

## Q1. What is Python?

### Answer

Python is a **high-level**, **interpreted**, **general-purpose**, **object-oriented**, and **dynamically typed** programming language.

It was developed by **Guido van Rossum** and officially released in **1991**.

Python is one of the most popular programming languages because of its simple syntax, readability, and powerful built-in libraries.

It is widely used in:

- Web Development
- Artificial Intelligence
- Machine Learning
- Data Science
- Automation
- Cloud Computing
- Cyber Security
- Software Development

### Key Points

- High-Level Language
- Interpreted Language
- Open Source
- Platform Independent
- Object-Oriented
- Dynamically Typed
- Easy to Learn

---

## Q2. Who developed Python?

### Answer

Python was developed by **Guido van Rossum**.

He started working on Python in the late 1980s at CWI (Centrum Wiskunde & Informatica) in the Netherlands.

Python was officially released in **1991**.

---

## Q3. Why is Python called a High-Level Language?

### Answer

Python is called a **High-Level Language** because it is easy for humans to read and write.

The programmer does not need to worry about low-level memory management or hardware-specific instructions.

Python provides simple English-like syntax, making programming easier.

Example:

```python
print("Hello World")
```

This is much simpler than writing equivalent code in low-level languages.

---

## Q4. Why is Python called an Interpreted Language?

### Answer

Python is called an **interpreted language** because its source code is executed by the Python Interpreter instead of being directly compiled into machine code.

Execution Process:

```text
Python Source Code (.py)

        │

        ▼

Python Interpreter

        │

        ▼

Bytecode (.pyc)

        │

        ▼

Python Virtual Machine (PVM)

        │

        ▼

Machine Code

        │

        ▼

Output
```

### Advantages

- Easier debugging
- Platform independent
- Faster development
- No manual compilation required

---

## Q5. What are the features of Python?

### Answer

Python provides many powerful features.

Some important features are:

- Simple and Easy to Learn
- High-Level Language
- Interpreted Language
- Object-Oriented
- Dynamically Typed
- Platform Independent
- Portable
- Open Source
- Large Standard Library
- Automatic Memory Management
- Extensible
- Embeddable

---

## Q6. What is Dynamic Typing?

### Answer

Dynamic Typing means the programmer does not declare the data type of a variable.

Python automatically determines the data type based on the assigned value.

Example

```python
age = 22

name = "Basha"

percentage = 91.5
```

Python automatically identifies:

- age → int
- name → str
- percentage → float

---

## Q7. What is Platform Independence?

### Answer

Platform Independence means a Python program written on one operating system can also run on another operating system without modifying the source code.

For example,

A Python program written on:

- Windows

can also run on

- Linux
- macOS

provided that Python is installed.

This is possible because Python uses the Python Virtual Machine (PVM).

---

## Q8. What is Portability?

### Answer

Portability means a Python program can be moved from one platform to another platform with little or no modification.

Example:

A Python program developed on Windows can be copied and executed on Linux or macOS.

---

## Q9. What is Open Source Software?

### Answer

Open Source Software is software whose source code is freely available to the public.

Anyone can:

- View the source code
- Modify the source code
- Improve the software
- Distribute the software

Python is an open-source programming language.

---

## Q10. Why is Python popular?

### Answer

Python is popular because:

- Easy syntax
- Easy to learn
- Huge community support
- Rich standard library
- Used in AI and Machine Learning
- Used in Automation
- Used in Web Development
- Used in Data Science
- Cross-platform support

---

## Q11. What are the applications of Python?

### Answer

Python is used in many domains.

Examples include:

- Web Development
- Software Development
- Desktop Applications
- Data Science
- Artificial Intelligence
- Machine Learning
- Automation
- Robotics
- Cloud Computing
- Networking
- Cyber Security
- Game Development

---

## Q12. Is Python compiled or interpreted?

### Answer

Python is generally known as an interpreted language.

However, internally Python first compiles the source code into **Bytecode** (`.pyc` file), and then the **Python Virtual Machine (PVM)** interprets the bytecode and executes it.

Therefore, Python uses both compilation (to bytecode) and interpretation (by the PVM).

---

## Q13. What is the latest version of Python?

### Answer

Python is continuously updated with new releases.

Instead of memorizing a specific version number, it is better to answer:

> Python is actively maintained by the Python Software Foundation (PSF), and newer versions are released regularly with performance improvements, new features, and bug fixes.

This answer remains accurate even as new versions are released.

---

## Q14. What is the full form of PVM?

### Answer

**PVM** stands for **Python Virtual Machine**.

It is responsible for executing the bytecode generated by the Python Interpreter.

---

## Q15. What is PSF?

### Answer

**PSF** stands for **Python Software Foundation**.

It is a non-profit organization responsible for maintaining, developing, and promoting the Python programming language.

The PSF also manages Python releases and supports the Python community worldwide.

---

## Quick Revision

- Python was developed by Guido van Rossum.
- First released in 1991.
- Python is high-level and interpreted.
- Python is dynamically typed.
- Python is platform independent.
- Python is portable.
- Python is open source.
- Python uses the Python Virtual Machine (PVM).
- Python is maintained by the Python Software Foundation (PSF).

---

---

# Execution Flow of Python Program Interview Questions

## Q16. Explain the Execution Flow of a Python Program.

### Answer

The execution flow of a Python program describes how Python converts the source code into executable instructions and produces the final output.

The execution process consists of the following steps:

1. Write the Python source code (`.py` file).
2. The Python Interpreter checks the source code for syntax errors.
3. The source code is compiled into **Bytecode**.
4. The generated Bytecode is stored as a **`.pyc`** file.
5. The **Python Virtual Machine (PVM)** executes the Bytecode.
6. The operating system converts the instructions into machine code.
7. The final output is displayed.

### Diagram

```text
Python Program (.py)

        │

        ▼

Python Interpreter

        │

        ▼

Bytecode (.pyc)

        │

        ▼

Python Virtual Machine (PVM)

        │

        ▼

Operating System

        │

        ▼

Hardware

        │

        ▼

Output
```

---

## Q17. What is Source Code?

### Answer

Source code is the program written by the programmer using Python syntax.

A Python source code file is saved with the **`.py`** extension.

Example:

```python
print("Hello World")
```

File Name

```text
hello.py
```

---

## Q18. What is a Python Interpreter?

### Answer

A Python Interpreter is software that reads, checks, compiles, and executes Python programs.

Its responsibilities include:

- Reading the source code.
- Checking for syntax errors.
- Converting the source code into Bytecode.
- Passing the Bytecode to the Python Virtual Machine (PVM).

### Advantages

- Easy debugging.
- Immediate execution.
- Platform independent.
- No separate compilation step required.

---

## Q19. What is Bytecode?

### Answer

Bytecode is the intermediate code generated by the Python Interpreter after compiling the source code.

Bytecode is:

- Platform independent.
- Not machine code.
- Executed by the Python Virtual Machine (PVM).

### Example

```text
Source Code

↓

Bytecode

↓

Machine Code
```

---

## Q20. What is a `.py` File?

### Answer

A `.py` file is a Python source code file.

It contains the program written by the programmer.

Example

```text
student.py

calculator.py

employee.py
```

---

## Q21. What is a `.pyc` File?

### Answer

A `.pyc` file is a compiled Python Bytecode file.

It is automatically generated by Python after successful compilation.

Advantages:

- Faster execution.
- No need to compile the same source code repeatedly.
- Improves program loading time.

---

## Q22. What is the Python Virtual Machine (PVM)?

### Answer

The **Python Virtual Machine (PVM)** is the runtime engine responsible for executing Python Bytecode.

The PVM reads the Bytecode instruction by instruction and executes it.

### Responsibilities

- Executes Bytecode.
- Converts Bytecode into machine-level instructions.
- Produces the final output.

---

## Q23. Is the Python Virtual Machine (PVM) platform dependent?

### Answer

Yes.

The **Bytecode** generated by Python is platform independent, but the **PVM implementation** is available separately for each operating system.

This enables the same Python program to run on Windows, Linux, and macOS.

---

## Q24. Why does Python generate Bytecode?

### Answer

Python generates Bytecode because:

- It improves execution speed.
- It avoids recompiling unchanged source code.
- It provides platform independence.
- It acts as an intermediate representation before execution.

---

## Q25. What happens if there is a syntax error in a Python program?

### Answer

If a syntax error is present:

1. The interpreter detects the error during compilation.
2. Bytecode is **not** generated.
3. The program execution stops.
4. Python displays an appropriate error message.

Example

```python
print("Hello"
```

Output

```text
SyntaxError: '(' was never closed
```

---

## Q26. What is the difference between Source Code and Bytecode?

| Source Code | Bytecode |
|-------------|-----------|
| Written by the programmer | Generated automatically by Python |
| Human-readable | Intermediate code |
| Saved as `.py` | Saved as `.pyc` |
| Editable | Not intended for editing |
| Executed after compilation | Executed by the PVM |

---

## Q27. What is the difference between Bytecode and Machine Code?

| Bytecode | Machine Code |
|-----------|--------------|
| Generated by Python | Generated by the operating system/processor |
| Platform independent | Platform dependent |
| Executed by the PVM | Executed directly by the CPU |
| Intermediate code | Binary instructions |

---

## Q28. Does Python compile the program?

### Answer

Yes.

Python internally compiles the source code into Bytecode before execution.

Therefore, Python uses both:

- Compilation (Source Code → Bytecode)
- Interpretation (Bytecode → Execution by PVM)

---

## Q29. Why is Python called an interpreted language if it compiles the program?

### Answer

Python is commonly called an interpreted language because the **Python Virtual Machine (PVM)** executes the Bytecode.

Although Python first compiles the source code into Bytecode, the Bytecode is interpreted during execution.

Hence, Python follows a hybrid execution model.

---

## Q30. Explain the complete execution architecture of Python.

### Answer

The complete execution architecture is:

```text
Programmer

     │

     ▼

Python Source Code (.py)

     │

     ▼

Python Interpreter

     │

     ▼

Bytecode (.pyc)

     │

     ▼

Python Virtual Machine

     │

     ▼

Operating System

     │

     ▼

Hardware

     │

     ▼

Output
```

---

## Quick Revision

- `.py` → Source Code
- `.pyc` → Bytecode
- Interpreter → Converts source code into Bytecode
- PVM → Executes Bytecode
- Bytecode → Platform Independent
- Machine Code → Platform Dependent
- Python internally compiles before execution
- PVM is responsible for running the Bytecode

---

## Interview Tips

### Tip 1

If the interviewer asks:

**"How does Python execute a program?"**

Always explain the complete execution flow using the architecture diagram.

---

### Tip 2

Remember the execution order:

```text
Source Code

↓

Interpreter

↓

Bytecode

↓

PVM

↓

Operating System

↓

Hardware

↓

Output
```

---


---

# Data Types in Python Interview Questions

## Q31. What are Data Types in Python?

### Answer

A **Data Type** is a classification that specifies the type of value a variable can store.

It tells the Python interpreter:

- What kind of data is stored.
- How the data should be processed.
- What operations can be performed on it.

Every value in Python belongs to a specific data type.

### Example

```python
age = 21          # int

salary = 25000.50 # float

name = "Basha"    # str

status = True     # bool
```

---

## Q32. Why are Data Types Required?

### Answer

Data Types are required because different types of data need to be processed differently.

For example,

- Addition is performed on numbers.
- Concatenation is performed on strings.
- Logical operations are performed on Boolean values.

Without data types, Python cannot determine which operation should be performed.

### Advantages

- Efficient memory allocation.
- Better readability.
- Easy debugging.
- Proper execution of operations.
- Type safety during runtime.

---

## Q33. How are Data Types classified in Python?

### Answer

Python Data Types are classified into two categories.

### 1. Basic Data Types

- int
- float
- bool
- str
- complex

### 2. Advanced Data Types

- list
- tuple
- set
- dictionary

---

## Q34. What is Dynamic Typing?

### Answer

Dynamic Typing means Python automatically determines the data type of a variable based on the assigned value.

The programmer does not need to declare the data type explicitly.

### Example

```python
number = 100

price = 99.99

name = "Python"

status = True
```

Python automatically identifies:

- `number` → int
- `price` → float
- `name` → str
- `status` → bool

---

## Q35. What is the difference between Static Typing and Dynamic Typing?

### Answer

| Static Typing | Dynamic Typing |
|---------------|----------------|
| Data type must be declared. | Data type is determined automatically. |
| Checked during compilation. | Checked during execution. |
| More coding required. | Less coding required. |
| Example: Java, C++ | Example: Python |

---

## Q36. What is the Integer (`int`) Data Type?

### Answer

The **Integer (`int`)** data type stores whole numbers without a decimal point.

Integers may be:

- Positive
- Negative
- Zero

### Example

```python
age = 22

marks = 95

temperature = -10
```

---

## Q37. What is the Float (`float`) Data Type?

### Answer

The **Float (`float`)** data type stores numbers containing a decimal point.

### Example

```python
percentage = 92.5

price = 499.99

height = 175.8
```

---

## Q38. What is the Boolean (`bool`) Data Type?

### Answer

The **Boolean (`bool`)** data type stores only two values.

- True
- False

It is mainly used in:

- Decision making
- Conditional statements
- Loops
- Comparisons

### Example

```python
is_logged_in = True

is_admin = False
```

---

## Q39. What is the String (`str`) Data Type?

### Answer

A **String (`str`)** is a sequence of Unicode characters enclosed within quotes.

Python supports:

- Single Quotes
- Double Quotes
- Triple Single Quotes
- Triple Double Quotes

### Example

```python
name = "Basha"

city = 'Hyderabad'
```

---

## Q40. What is the Complex (`complex`) Data Type?

### Answer

The **Complex (`complex`)** data type stores numbers having both a real part and an imaginary part.

General Form

```text
a + bj
```

Where:

- `a` → Real Part
- `b` → Imaginary Part
- `j` → Imaginary Unit

### Example

```python
number = 5 + 3j
```

---

## Q41. How can you check the Data Type of a variable?

### Answer

Python provides the `type()` function.

### Example

```python
age = 22

print(type(age))
```

### Output

```text
<class 'int'>
```

---

## Q42. Are Python variables declared with a data type?

### Answer

No.

Python variables are **not declared with a data type**.

The interpreter automatically assigns the appropriate data type based on the assigned value.

### Example

```python
number = 10

number = "Python"
```

Python allows the same variable to store different types of values.

---

## Q43. Are Data Types mutable or immutable?

### Answer

Some Python data types are mutable, while others are immutable.

### Immutable Data Types

- int
- float
- bool
- str
- complex
- tuple

### Mutable Data Types

- list
- set
- dictionary

---

## Q44. What is the difference between Mutable and Immutable Objects?

### Answer

| Mutable | Immutable |
|----------|-----------|
| Can be modified after creation | Cannot be modified after creation |
| Memory remains the same | New object is created after modification |
| Examples: list, set, dictionary | Examples: int, float, str, tuple |

---

## Q45. Explain Memory Representation in Python.

### Answer

In Python, variables do **not store values directly**.

Instead, they store a **reference** to an object.

Example

```python
age = 21
```

Memory Representation

```text
      age

       │

       ▼

+----------------+

|      21        |

|   int Object   |

+----------------+
```

---

## Q46. Can a variable change its Data Type?

### Answer

Yes.

Since Python is dynamically typed, a variable can store different data types during program execution.

Example

```python
value = 100

print(type(value))

value = "Python"

print(type(value))
```

### Output

```text
<class 'int'>

<class 'str'>
```

---

## Q47. What are the advantages of Dynamic Typing?

### Answer

Advantages include:

- Less code.
- Easy to learn.
- Flexible programming.
- Faster development.
- Improved readability.
- Suitable for rapid application development.

---

## Q48. Which data type is used to store multiple values?

### Answer

Python provides Advanced Data Types to store multiple values.

They are:

- list
- tuple
- set
- dictionary

Example

```python
marks = [80, 85, 90]
```

---

## Q49. What is the default Data Type of a decimal number?

### Answer

The default data type of a decimal number in Python is **float**.

Example

```python
number = 25.75

print(type(number))
```

Output

```text
<class 'float'>
```

---

## Q50. Can Integer and Float values be used together?

### Answer

Yes.

Python automatically performs **Implicit Type Casting**.

Example

```python
number1 = 10

number2 = 5.5

result = number1 + number2

print(result)

print(type(result))
```

### Output

```text
15.5

<class 'float'>
```

---

## Quick Revision

- Every value belongs to a data type.
- Python supports Basic and Advanced Data Types.
- Python is dynamically typed.
- Variables store references to objects.
- `int` stores whole numbers.
- `float` stores decimal numbers.
- `bool` stores logical values.
- `str` stores text.
- `complex` stores complex numbers.
- Mutable objects can be modified.
- Immutable objects cannot be modified.
- `type()` returns the data type of a variable.

---


---

# Type Casting in Python Interview Questions

## Q51. What is Type Casting?

### Answer

**Type Casting** is the process of converting a value from one data type into another data type.

Python provides built-in functions to perform type conversion whenever required.

### Example

```python
number = 100

result = float(number)

print(result)
```

### Output

```text
100.0
```

---

## Q52. Why is Type Casting Required?

### Answer

Type Casting is required to:

- Convert one data type into another.
- Perform arithmetic operations between different data types.
- Accept and process user input.
- Avoid type mismatch errors.
- Improve code flexibility and readability.

### Example

```python
number = "100"

print(int(number) + 50)
```

### Output

```text
150
```

---

## Q53. How many types of Type Casting are available in Python?

### Answer

Python supports two types of Type Casting.

1. **Implicit Type Casting**
2. **Explicit Type Casting**

```text
Type Casting

│

├── Implicit Type Casting

└── Explicit Type Casting
```

---

## Q54. What is Implicit Type Casting?

### Answer

**Implicit Type Casting** is the automatic conversion of one data type into another by the Python Interpreter.

The programmer does not perform the conversion manually.

### Example

```python
number1 = 10

number2 = 2.5

result = number1 + number2

print(result)

print(type(result))
```

### Output

```text
12.5

<class 'float'>
```

### Explanation

- `number1` is an integer.
- `number2` is a float.
- Python automatically converts the integer into a float.
- The final result becomes a float.

---

## Q55. What is Explicit Type Casting?

### Answer

**Explicit Type Casting** is the manual conversion of one data type into another using Python's built-in conversion functions.

### Example

```python
number = 25.99

result = int(number)

print(result)
```

### Output

```text
25
```

---

## Q56. What is the difference between Implicit and Explicit Type Casting?

### Answer

| Implicit Type Casting | Explicit Type Casting |
|------------------------|----------------------|
| Done automatically by Python | Done manually by the programmer |
| No conversion function is required | Uses conversion functions |
| Safer for compatible types | Programmer has full control |
| Example: `10 + 2.5` | Example: `int(25.8)` |

---

## Q57. Which built-in functions are used for Type Casting?

### Answer

Python provides the following built-in conversion functions.

| Function | Converts To |
|----------|-------------|
| `int()` | Integer |
| `float()` | Float |
| `str()` | String |
| `bool()` | Boolean |
| `complex()` | Complex |

---

## Q58. Explain the int() Function.

### Answer

The `int()` function converts a compatible value into an integer.

### Example

```python
print(int(25.99))

print(int(True))

print(int(False))
```

### Output

```text
25

1

0
```

---

## Q59. Explain the float() Function.

### Answer

The `float()` function converts a compatible value into a floating-point number.

### Example

```python
print(float(10))

print(float(True))
```

### Output

```text
10.0

1.0
```

---

## Q60. Explain the str() Function.

### Answer

The `str()` function converts any compatible value into a string.

### Example

```python
number = 500

text = str(number)

print(text)

print(type(text))
```

### Output

```text
500

<class 'str'>
```

---

## Q61. Explain the bool() Function.

### Answer

The `bool()` function converts a value into either `True` or `False`.

### Common Boolean Conversions

| Value | Result |
|--------|--------|
| `0` | False |
| `1` | True |
| `""` | False |
| `"Python"` | True |
| `[]` | False |
| `[10]` | True |
| `None` | False |

### Example

```python
print(bool(0))

print(bool(10))

print(bool(""))

print(bool("Python"))
```

### Output

```text
False

True

False

True
```

---

## Q62. Explain the complex() Function.

### Answer

The `complex()` function converts a number into a complex number.

### Example

```python
number = complex(10)

print(number)
```

### Output

```text
(10+0j)
```

---

## Q63. Can every String be converted into an Integer?

### Answer

No.

Only strings containing valid numeric values can be converted.

### Valid Example

```python
print(int("150"))
```

Output

```text
150
```

### Invalid Example

```python
print(int("Python"))
```

Output

```text
ValueError: invalid literal for int()
```

---

## Q64. What happens when float is converted into int?

### Answer

The decimal part is removed.

It is **not rounded**.

### Example

```python
print(int(45.98))
```

### Output

```text
45
```

---

## Q65. Can Python automatically convert int into float?

### Answer

Yes.

Python performs **Implicit Type Casting** automatically.

### Example

```python
result = 50 + 25.5

print(result)

print(type(result))
```

### Output

```text
75.5

<class 'float'>
```

---

## Q66. What happens when an invalid conversion is performed?

### Answer

Python raises an exception.

Example

```python
print(int("Hello"))
```

Output

```text
ValueError: invalid literal for int()
```

---

## Q67. What is Type Mismatch?

### Answer

A **Type Mismatch** occurs when an operation is performed between incompatible data types.

### Example

```python
print("100" + 50)
```

Output

```text
TypeError
```

Correct Approach

```python
print(int("100") + 50)
```

Output

```text
150
```

---

## Q68. Which Type Casting functions are most frequently used?

### Answer

The most commonly used functions are:

- `int()`
- `float()`
- `str()`
- `bool()`

These functions are frequently used while processing user input and performing calculations.

---

## Q69. What are the advantages of Type Casting?

### Answer

Advantages include:

- Easy data conversion.
- Better program flexibility.
- Reduces type mismatch errors.
- Improves compatibility between data types.
- Simplifies user input handling.

---

## Q70. Explain Type Casting with a Real-Time Example.

### Answer

Consider a calculator application.

The user enters two numbers using the keyboard.

```python
number1 = "50"

number2 = "25"
```

Both values are stored as strings.

Before performing addition, they must be converted into integers.

```python
result = int(number1) + int(number2)

print(result)
```

### Output

```text
75
```

Without type casting, Python would treat the values as strings instead of numbers.

---

## Quick Revision

- Type Casting converts one data type into another.
- Python supports Implicit and Explicit Type Casting.
- Implicit conversion is automatic.
- Explicit conversion uses built-in functions.
- Common conversion functions are:
  - `int()`
  - `float()`
  - `str()`
  - `bool()`
  - `complex()`
- Invalid conversions raise exceptions such as `ValueError`.

---


---

# Frequently Asked Python Basic Interview Programs

These programs are commonly asked in **Python Fresher Interviews**, **Technical Interviews**, **Campus Placements**, and **Viva Examinations**.

Each program includes:

- Problem Statement
- Program
- Output
- Explanation
- Interview Questions

---

# Program 1: Print Hello World

## Problem Statement

Write a Python program to display **Hello World**.

### Program

```python
# Displaying a message
print("Hello World")
```

### Output

```text
Hello World
```

### Explanation

- `print()` is a built-in function.
- It displays the given message on the console.
- `"Hello World"` is a string literal.

### Interview Questions

**Q1. Is `print` a keyword?**

No. It is a built-in function.

---

**Q2. Can `print()` display variables?**

Yes.

Example

```python
name = "Basha"
print(name)
```

---

**Q3. Can `print()` display multiple values?**

Yes.

Example

```python
name = "Basha"
age = 22

print(name, age)
```

---

# Program 2: Declare Variables of Different Data Types

## Problem Statement

Write a program to declare variables of different data types and display them.

### Program

```python
# Integer
age = 22

# Float
percentage = 92.5

# String
name = "Basha"

# Boolean
is_student = True

# Complex
number = 5 + 3j

# Displaying values
print(age)
print(percentage)
print(name)
print(is_student)
print(number)
```

### Output

```text
22
92.5
Basha
True
(5+3j)
```

### Explanation

The program demonstrates the five basic Python data types.

### Interview Questions

- What are the basic data types?
- Which data type stores decimal values?
- Which data type stores logical values?
- What is a complex number?

---

# Program 3: Display the Data Type of Variables

## Problem Statement

Write a program to display the data type of different variables.

### Program

```python
age = 22

salary = 35000.50

name = "Python"

status = True

print(type(age))
print(type(salary))
print(type(name))
print(type(status))
```

### Output

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

### Explanation

The `type()` function returns the data type of an object.

### Interview Questions

- What is the purpose of the `type()` function?
- Does `type()` return a string?
- Can `type()` be used with all Python objects?

---

# Program 4: Demonstrate Dynamic Typing

## Problem Statement

Write a program to demonstrate Dynamic Typing.

### Program

```python
value = 100

print(value)
print(type(value))

value = "Python"

print(value)
print(type(value))
```

### Output

```text
100
<class 'int'>
Python
<class 'str'>
```

### Explanation

The same variable stores different data types.

This demonstrates Dynamic Typing.

### Interview Questions

- What is Dynamic Typing?
- Can a variable change its data type?
- Is Dynamic Typing available in Java?

---

# Program 5: Implicit Type Casting

## Problem Statement

Write a program to demonstrate Implicit Type Casting.

### Program

```python
number1 = 20

number2 = 5.5

result = number1 + number2

print(result)

print(type(result))
```

### Output

```text
25.5

<class 'float'>
```

### Explanation

Python automatically converts the integer into a float before performing addition.

---

# Program 6: Explicit Type Casting

## Problem Statement

Write a program to convert a float into an integer.

### Program

```python
number = 25.99

result = int(number)

print(result)
```

### Output

```text
25
```

### Explanation

The `int()` function removes the decimal part and returns the integer value.

### Interview Questions

- What is Explicit Type Casting?
- Which function converts float to int?
- Does `int()` round the value?

Answer:

No.

It simply removes the decimal part.

---

# Program 7: Convert Integer into Float

## Program

```python
number = 100

result = float(number)

print(result)
```

### Output

```text
100.0
```

### Explanation

The `float()` function converts an integer into a floating-point number.

---

# Program 8: Convert Integer into String

## Program

```python
number = 150

text = str(number)

print(text)

print(type(text))
```

### Output

```text
150

<class 'str'>
```

---

# Program 9: Convert Integer into Boolean

## Program

```python
number = 1

print(bool(number))

number = 0

print(bool(number))
```

### Output

```text
True

False
```

### Explanation

- Zero becomes False.
- Non-zero becomes True.

---

# Program 10: Display Real and Imaginary Parts of a Complex Number

## Program

```python
number = 5 + 3j

print(number.real)

print(number.imag)
```

### Output

```text
5.0

3.0
```

### Explanation

- `.real` returns the real part.
- `.imag` returns the imaginary part.

---

# Output-Based Questions

## Q1. Predict the Output

```python
print(type(100))
```

### Answer

```text
<class 'int'>
```

---

## Q2. Predict the Output

```python
print(type(100.5))
```

### Answer

```text
<class 'float'>
```

---

## Q3. Predict the Output

```python
print(type(True))
```

### Answer

```text
<class 'bool'>
```

---

## Q4. Predict the Output

```python
print(type("Python"))
```

### Answer

```text
<class 'str'>
```

---

## Q5. Predict the Output

```python
print(int(25.99))
```

### Answer

```text
25
```

---

## Q6. Predict the Output

```python
print(float(100))
```

### Answer

```text
100.0
```

---

## Q7. Predict the Output

```python
print(bool(0))
```

### Answer

```text
False
```

---

## Q8. Predict the Output

```python
print(bool(25))
```

### Answer

```text
True
```

---

## Q9. Predict the Output

```python
print(type(5 + 3j))
```

### Answer

```text
<class 'complex'>
```

---

## Q10. Predict the Output

```python
print(str(100))
```

### Answer

```text
100
```

---

# Viva Questions

### What is Python?

### Why is Python called an interpreted language?

### Explain Dynamic Typing.

### What are Data Types?

### Explain Integer.

### Explain Float.

### Explain Boolean.

### Explain String.

### Explain Complex.

### What is Type Casting?

### Explain Implicit Type Casting.

### Explain Explicit Type Casting.

### Difference between int() and float().

### Explain bool().

### Explain type().

### What is PVM?

### What is Bytecode?

### Difference between .py and .pyc.

### Who developed Python?

### What is the latest version of Python?

---

# Final Quick Revision

- Python is a High-Level Programming Language.
- Python is an Interpreted Language.
- Python supports Dynamic Typing.
- Variables do not require explicit data type declarations.
- Python has five basic data types:
  - int
  - float
  - bool
  - str
  - complex
- Python supports Implicit and Explicit Type Casting.
- `type()` returns the data type.
- `print()` displays output.
- `bool(0)` returns `False`.
- `bool(1)` returns `True`.
- `.real` returns the real part of a complex number.
- `.imag` returns the imaginary part of a complex number.

---

# File Summary

This interview guide covered:

- Introduction to Python
- Execution Flow of Python Program
- Python Data Types
- Type Casting
- 70 Interview Questions with Answers
- 10 Frequently Asked Interview Programs
- 10 Output-Based Questions
- Viva Questions
- Quick Revision Notes

This document serves as a complete interview preparation guide for the **01-Python-Basics** folder and is suitable for freshers preparing for technical interviews, campus placements, and Python viva examinations.

