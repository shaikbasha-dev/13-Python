---

# List Methods

## Introduction

Python provides several built-in methods to perform operations on lists.

These methods make it easy to:

- Add elements
- Remove elements
- Search elements
- Count occurrences
- Sort data
- Reverse data
- Copy lists
- Clear list contents

Instead of writing lengthy code, these built-in methods perform common tasks efficiently.

---

# Categories of List Methods

```text
List Methods

│

├── Adding Elements

│      ├── append()

│      ├── extend()

│      └── insert()

│

├── Removing Elements

│      ├── remove()

│      ├── pop()

│      └── clear()

│

├── Searching

│      ├── index()

│      └── count()

│

├── Ordering

│      ├── sort()

│      └── reverse()

│

└── Copying

       └── copy()
```

---

# append()

## Definition

The `append()` method adds a single element to the **end** of the list.

---

## Why is append() Required?

Suppose an online shopping application stores products inside a list.

Whenever a customer adds a new product, the application must store it at the end of the cart.

The `append()` method performs this task efficiently.

---

## Syntax

```python
list.append(element)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| element | Element to be added |

---

## Return Value

Returns **None**.

The original list is modified.

---

## Program

```python
# Creating a list of programming languages
languages = ["Python", "Java"]

# Adding a new language
languages.append("C++")

# Displaying the updated list
print(languages)
```

---

## Output

```text
['Python', 'Java', 'C++']
```

---

## Dry Run

```text
Initial List

['Python', 'Java']

↓

append("C++")

↓

['Python', 'Java', 'C++']
```

---

## Memory Representation

Before

```text
+------------------------+

| Python | Java |

+------------------------+
```

After

```text
+--------------------------------+

| Python | Java | C++ |

+--------------------------------+
```

---

## Pseudocode

```text
BEGIN

Create List

Call append()

Display List

END
```

---

## Line-by-Line Explanation

### Line 1

Creates a list.

---

### Line 2

Calls `append()`.

---

### Line 3

Adds `"C++"` at the end.

---

### Line 4

Displays the updated list.

---

## Real-World Applications

- Shopping Cart
- Student Registration
- Attendance Systems
- Order Management
- Inventory Systems

---

## Best Practices

Use `append()` when adding **one element**.

---

# extend()

## Definition

The `extend()` method adds **multiple elements** from another iterable to the end of the list.

---

## Why is extend() Required?

Suppose one classroom list needs to be merged with another classroom list.

Instead of adding each student individually,

`extend()` adds all elements together.

---

## Syntax

```python
list.extend(iterable)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| iterable | List, Tuple, Set, etc. |

---

## Program

```python
# First list
list1 = ["Python", "Java"]

# Second list
list2 = ["C++", "JavaScript"]

# Extending list1
list1.extend(list2)

# Displaying result
print(list1)
```

---

## Output

```text
['Python', 'Java', 'C++', 'JavaScript']
```

---

## Difference Between append() and extend()

```python
numbers = [10, 20]

numbers.append([30, 40])

print(numbers)
```

Output

```text
[10, 20, [30, 40]]
```

---

```python
numbers = [10, 20]

numbers.extend([30, 40])

print(numbers)
```

Output

```text
[10, 20, 30, 40]
```

---

## Comparison

| append() | extend() |
|-----------|-----------|
| Adds one element | Adds multiple elements |
| Can add nested list | Merges iterable |
| Slower for multiple insertions | Efficient for multiple insertions |

---

# insert()

## Definition

The `insert()` method inserts an element at a specified index.

---

## Syntax

```python
list.insert(index, element)
```

---

## Parameters

| Parameter | Description |
|-----------|-------------|
| index | Position |
| element | Value to insert |

---

## Program

```python
# Creating a list
numbers = [10, 20, 40]

# Inserting 30
numbers.insert(2, 30)

# Displaying result
print(numbers)
```

---

## Output

```text
[10, 20, 30, 40]
```

---

## Dry Run

```text
Original

10 20 40

↓

Insert 30 at Index 2

↓

10 20 30 40
```

---

## Real-World Applications

- Student Ranking
- Priority Queues
- Playlist Management
- Task Scheduling

---

## Internal Working

When Python executes

```python
numbers.insert(2, 30)
```

Internally,

```text
Interpreter Reads Statement

↓

Locate List Object

↓

Shift Existing Elements

↓

Insert New Element

↓

Update List

↓

Execution Complete
```

---

## Best Practices

- Use `insert()` when position matters.
- Use `append()` if inserting at the end.

---

# Summary

In this section, you learned:

- `append()`
- `extend()`
- `insert()`
- Their syntax
- Parameters
- Internal working
- Memory representation
- Practical examples
- Best practices
- Real-world applications


---

# Integer (`int`)

## Introduction

An **Integer** is a built-in numeric data type in Python used to store **whole numbers**.

It does not contain any decimal point.

Integers can be:

- Positive
- Negative
- Zero

---

## Definition

An **Integer (`int`)** is a data type that stores whole numbers without any fractional (decimal) part.

---

## Syntax

```python
variable_name = integer_value
```

### Example

```python
age = 21

marks = 95

temperature = -10

count = 0
```

---

## Integer Examples

```python
100

250

0

-50

99999
```

---

## Why do we use Integer?

The `int` data type is used whenever the value does not contain decimal numbers.

### Real-Time Examples

| Scenario | Example |
|----------|---------|
| Student Age | 21 |
| Roll Number | 101 |
| Number of Employees | 250 |
| Number of Products | 500 |
| Population | 1000000 |

---

## Memory Representation

Example

```python
age = 21
```

```text
        age

         │

         ▼

+----------------------+

|      21 (int)        |

+----------------------+
```

The variable stores the reference to the integer object.

---

## Program

```python
# Integer variables
age = 21

marks = 95

employees = 250

# Display values
print("Age :", age)

print("Marks :", marks)

print("Employees :", employees)
```

---

## Output

```text
Age : 21

Marks : 95

Employees : 250
```

---

## Pseudocode

```text
START

Create integer variable age

Assign value 21

Create integer variable marks

Assign value 95

Create integer variable employees

Assign value 250

Display all values

STOP
```

---

## Line-by-Line Explanation

### Line 1

```python
age = 21
```

Creates an integer variable named `age` and stores the value `21`.

---

### Line 2

```python
marks = 95
```

Creates an integer variable named `marks` and stores the value `95`.

---

### Line 3

```python
employees = 250
```

Creates an integer variable named `employees` and stores the value `250`.

---

### Line 4

```python
print("Age :", age)
```

Displays the value stored in `age`.

---

### Line 5

```python
print("Marks :", marks)
```

Displays the value stored in `marks`.

---

### Line 6

```python
print("Employees :", employees)
```

Displays the value stored in `employees`.

---

## Characteristics of Integer

- Stores whole numbers.
- Can store positive values.
- Can store negative values.
- Can store zero.
- Immutable data type.
- Supports arithmetic operations.

---

## Integer Literals

Python supports different number systems.

| Type | Example |
|------|---------|
| Decimal | `100` |
| Binary | `0b1010` |
| Octal | `0o17` |
| Hexadecimal | `0x2A` |

### Example

```python
decimal_number = 100

binary_number = 0b1010

octal_number = 0o17

hexadecimal_number = 0x2A

print(decimal_number)

print(binary_number)

print(octal_number)

print(hexadecimal_number)
```

### Output

```text
100

10

15

42
```

---

## Built-in Functions

| Function | Description |
|----------|-------------|
| `int()` | Converts a value into an integer |
| `abs()` | Returns the absolute value |
| `bin()` | Converts to binary |
| `oct()` | Converts to octal |
| `hex()` | Converts to hexadecimal |
| `type()` | Returns the data type |

### Example

```python
number = -25

print(abs(number))

print(bin(10))

print(oct(10))

print(hex(255))

print(type(number))
```

### Output

```text
25

0b1010

0o12

0xff

<class 'int'>
```

---

## Summary

- `int` is used to store whole numbers.
- It does not store decimal values.
- Integers may be positive, negative, or zero.
- Python automatically identifies integer values.
- Integer variables support mathematical operations.
- Python provides built-in functions such as `int()`, `abs()`, `bin()`, `oct()`, and `hex()` for working with integers.


---

# Float (`float`)

## Introduction

A **Float** is a built-in numeric data type in Python used to store **decimal (floating-point) numbers**.

A float value always contains a decimal point (`.`).

---

## Definition

A **Float (`float`)** is a data type that stores numbers containing a fractional (decimal) part.

---

## Syntax

```python
variable_name = float_value
```

### Example

```python
percentage = 91.5

price = 499.99

temperature = -10.8
```

---

## Float Examples

```python
10.5

25.75

0.0

-35.8

999.999
```

---

## Why do we use Float?

The `float` data type is used whenever a value contains decimal numbers.

### Real-Time Examples

| Scenario | Example |
|----------|---------|
| Student Percentage | 91.5 |
| Product Price | 499.99 |
| Bank Interest Rate | 7.25 |
| Temperature | 36.8 |
| Height | 175.5 |

---

## Memory Representation

Example

```python
percentage = 91.5
```

```text
     percentage

          │

          ▼

+----------------------+

|    91.5 (float)      |

+----------------------+
```

The variable stores the reference to the float object.

---

## Program

```python
# Float variables
percentage = 91.5

price = 499.99

temperature = 36.8

# Display values
print("Percentage :", percentage)

print("Price :", price)

print("Temperature :", temperature)
```

---

## Output

```text
Percentage : 91.5

Price : 499.99

Temperature : 36.8
```

---

## Pseudocode

```text
START

Create float variable percentage

Assign value 91.5

Create float variable price

Assign value 499.99

Create float variable temperature

Assign value 36.8

Display all values

STOP
```

---

## Line-by-Line Explanation

### Line 1

```python
percentage = 91.5
```

Creates a float variable named `percentage` and stores the value `91.5`.

---

### Line 2

```python
price = 499.99
```

Creates a float variable named `price` and stores the value `499.99`.

---

### Line 3

```python
temperature = 36.8
```

Creates a float variable named `temperature` and stores the value `36.8`.

---

### Line 4

```python
print("Percentage :", percentage)
```

Displays the value stored in `percentage`.

---

### Line 5

```python
print("Price :", price)
```

Displays the value stored in `price`.

---

### Line 6

```python
print("Temperature :", temperature)
```

Displays the value stored in `temperature`.

---

## Characteristics of Float

- Stores decimal numbers.
- Supports positive values.
- Supports negative values.
- Supports zero.
- Immutable data type.
- Supports arithmetic operations.

---

## Built-in Functions

| Function | Description |
|----------|-------------|
| `float()` | Converts a value into a float |
| `round()` | Rounds a float value |
| `abs()` | Returns the absolute value |
| `type()` | Returns the data type |

### Example

```python
number = 25.6789

print(round(number))

print(round(number, 2))

print(abs(-35.75))

print(type(number))
```

### Output

```text
26

25.68

35.75

<class 'float'>
```

---

## Summary

- `float` is used to store decimal numbers.
- Float values always contain a decimal point.
- Python automatically identifies float values.
- Float objects are immutable.
- Built-in functions like `float()`, `round()`, `abs()`, and `type()` are commonly used with float values.



---

# Boolean (`bool`)

## Introduction

A **Boolean** is a built-in data type in Python used to represent **logical values**.

A Boolean data type has only **two possible values**:

- `True`
- `False`

Boolean values are mainly used in:

- Decision making
- Conditional statements
- Comparisons
- Loops
- Logical operations

---

## Definition

A **Boolean (`bool`)** is a data type that stores either `True` or `False`.

---

## Syntax

```python
variable_name = True

variable_name = False
```

### Example

```python
is_student = True

is_logged_in = False

result = True
```

---

## Boolean Examples

```python
True

False
```

---

## Why do we use Boolean?

The `bool` data type is used whenever the result of an operation is either **True** or **False**.

### Real-Time Examples

| Scenario | Boolean Value |
|----------|---------------|
| Student Passed | True |
| User Logged In | True |
| Payment Successful | True |
| Account Blocked | False |
| Email Verified | True |

---

## Memory Representation

Example

```python
is_student = True
```

```text
     is_student

          │

          ▼

+----------------------+

|     True (bool)      |

+----------------------+
```

The variable stores the reference to the Boolean object.

---

## Program

```python
# Boolean variables
is_student = True

is_logged_in = False

result = True

# Display values
print("Is Student :", is_student)

print("Is Logged In :", is_logged_in)

print("Result :", result)
```

---

## Output

```text
Is Student : True

Is Logged In : False

Result : True
```

---

## Pseudocode

```text
START

Create Boolean variable is_student

Assign True

Create Boolean variable is_logged_in

Assign False

Create Boolean variable result

Assign True

Display all values

STOP
```

---

## Line-by-Line Explanation

### Line 1

```python
is_student = True
```

Creates a Boolean variable named `is_student` and stores the value `True`.

---

### Line 2

```python
is_logged_in = False
```

Creates a Boolean variable named `is_logged_in` and stores the value `False`.

---

### Line 3

```python
result = True
```

Creates a Boolean variable named `result` and stores the value `True`.

---

### Line 4

```python
print("Is Student :", is_student)
```

Displays the value stored in `is_student`.

---

### Line 5

```python
print("Is Logged In :", is_logged_in)
```

Displays the value stored in `is_logged_in`.

---

### Line 6

```python
print("Result :", result)
```

Displays the value stored in `result`.

---

## Boolean Values from Comparison Operators

Comparison operators return Boolean values.

### Example

```python
print(10 > 5)

print(10 < 5)

print(20 == 20)

print(15 != 10)
```

### Output

```text
True

False

True

True
```

---

## Built-in Functions

| Function | Description |
|----------|-------------|
| `bool()` | Converts a value into Boolean |
| `type()` | Returns the data type |

### Example

```python
print(bool(1))

print(bool(0))

print(bool("Python"))

print(bool(""))

print(type(True))
```

### Output

```text
True

False

True

False

<class 'bool'>
```

---

## Characteristics of Boolean

- Stores only two values (`True` or `False`).
- Used in decision-making statements.
- Used with comparison operators.
- Used with logical operators.
- Immutable data type.

---

## Summary

- `bool` stores logical values.
- It has only two values: `True` and `False`.
- Boolean values are widely used in conditions and loops.
- Comparison operators always return Boolean values.
- Python provides the `bool()` function to convert values into Boolean.


---

# String (`str`)

## Introduction

A **String** is a built-in data type in Python used to store **textual data**.

A string is a collection of one or more characters enclosed within:

- Single Quotes (`' '`)
- Double Quotes (`" "`)
- Triple Single Quotes (`''' '''`)
- Triple Double Quotes (`""" """`)

Strings are one of the most frequently used data types in Python because almost every application works with text.

Examples:

- Student Name
- Address
- Email ID
- Mobile Number (stored as text)
- City Name
- Password
- Company Name

---

## Definition

A **String (`str`)** is a sequence of Unicode characters enclosed within quotes.

---

## Syntax

```python
variable_name = "Text"

variable_name = 'Text'
```

### Example

```python
name = "Basha"

city = 'Hyderabad'

course = "Python"
```

---

## String Examples

```python
"Python"

"Java"

"Hello"

"ChatGPT"

"Full Stack Development"
```

---

## Why do we use String?

The `str` data type is used whenever we need to store text or characters.

### Real-Time Examples

| Scenario | Example |
|----------|---------|
| Student Name | "Basha" |
| City | "Hyderabad" |
| Email | "abc@gmail.com" |
| Company | "OpenAI" |
| Country | "India" |

---

## Memory Representation

Example

```python
name = "Basha"
```

```text
        name

         │

         ▼

+----------------------+

|   "Basha" (str)      |

+----------------------+
```

The variable stores the reference to the string object.

---

## Program

```python
# String variables
name = "Basha"

city = "Hyderabad"

course = "Python"

# Display values
print("Name :", name)

print("City :", city)

print("Course :", course)
```

---

## Output

```text
Name : Basha

City : Hyderabad

Course : Python
```

---

## Pseudocode

```text
START

Create string variable name

Assign "Basha"

Create string variable city

Assign "Hyderabad"

Create string variable course

Assign "Python"

Display all values

STOP
```

---

## Line-by-Line Explanation

### Line 1

```python
name = "Basha"
```

Creates a string variable named `name` and stores the value `"Basha"`.

---

### Line 2

```python
city = "Hyderabad"
```

Creates a string variable named `city` and stores the value `"Hyderabad"`.

---

### Line 3

```python
course = "Python"
```

Creates a string variable named `course` and stores the value `"Python"`.

---

### Line 4

```python
print("Name :", name)
```

Displays the value stored in `name`.

---

### Line 5

```python
print("City :", city)
```

Displays the value stored in `city`.

---

### Line 6

```python
print("Course :", course)
```

Displays the value stored in `course`.

---

## Ways to Create a String

Python allows strings to be created in different ways.

### Using Single Quotes

```python
language = 'Python'
```

---

### Using Double Quotes

```python
language = "Python"
```

---

### Using Triple Single Quotes

```python
text = '''Welcome to
Python Programming'''
```

---

### Using Triple Double Quotes

```python
text = """Welcome to
Python Programming"""
```

---

## Built-in Functions

| Function | Description |
|----------|-------------|
| `str()` | Converts a value into a string |
| `len()` | Returns the length of a string |
| `type()` | Returns the data type |

### Example

```python
name = "Python"

print(len(name))

print(str(100))

print(type(name))
```

### Output

```text
6

100

<class 'str'>
```

---

## Characteristics of String

- Stores textual data.
- Sequence of Unicode characters.
- Immutable data type.
- Supports indexing.
- Supports slicing.
- Supports concatenation.
- Supports repetition.

---

## Summary

- `str` is used to store text.
- Strings are enclosed within quotes.
- Python supports single, double, and triple quotes.
- Strings are immutable.
- Built-in functions like `str()`, `len()`, and `type()` are commonly used with strings.


---

# Complex (`complex`)

## Introduction

A **Complex** is a built-in numeric data type in Python used to represent **complex numbers**.

A complex number consists of two parts:

- Real Part
- Imaginary Part

The imaginary part is represented using the letter **`j`** in Python.

Complex numbers are mainly used in:

- Scientific Calculations
- Engineering Applications
- Electrical Engineering
- Signal Processing
- Mathematics

---

## Definition

A **Complex (`complex`)** is a data type that stores a number having both a real part and an imaginary part.

General Form:

```text
a + bj
```

Where:

- **a** → Real Part
- **b** → Imaginary Part
- **j** → Imaginary Unit

---

## Syntax

```python
variable_name = real + imaginaryj
```

### Example

```python
number1 = 5 + 3j

number2 = 10 - 2j

number3 = 0 + 7j
```

---

## Complex Number Examples

```python
5 + 3j

10 - 2j

2j

7 + 0j

-8 + 6j
```

---

## Why do we use Complex Numbers?

The `complex` data type is used whenever calculations involve imaginary numbers.

### Real-Time Applications

| Field | Usage |
|--------|-------|
| Electrical Engineering | AC Circuit Analysis |
| Signal Processing | Wave Analysis |
| Physics | Mathematical Calculations |
| Robotics | Control Systems |
| Scientific Computing | Complex Mathematical Operations |

---

## Memory Representation

Example

```python
number = 5 + 3j
```

```text
        number

           │

           ▼

+----------------------+

|     5 + 3j           |

|   (complex object)   |

+----------------------+
```

The variable stores the reference to the complex object.

---

## Program

```python
# Creating complex variables
number1 = 5 + 3j

number2 = 8 - 2j

# Displaying values
print("Number 1 :", number1)

print("Number 2 :", number2)
```

---

## Output

```text
Number 1 : (5+3j)

Number 2 : (8-2j)
```

---

## Pseudocode

```text
START

Create complex variable number1

Assign 5 + 3j

Create complex variable number2

Assign 8 - 2j

Display both variables

STOP
```

---

## Line-by-Line Explanation

### Line 1

```python
number1 = 5 + 3j
```

Creates a complex variable named `number1` and stores the value `5 + 3j`.

---

### Line 2

```python
number2 = 8 - 2j
```

Creates a complex variable named `number2` and stores the value `8 - 2j`.

---

### Line 3

```python
print("Number 1 :", number1)
```

Displays the value stored in `number1`.

---

### Line 4

```python
print("Number 2 :", number2)
```

Displays the value stored in `number2`.

---

## Accessing Real and Imaginary Parts

Python provides built-in attributes to access the real and imaginary parts of a complex number.

### Example

```python
number = 5 + 3j

print("Real Part :", number.real)

print("Imaginary Part :", number.imag)
```

---

### Output

```text
Real Part : 5.0

Imaginary Part : 3.0
```

---

## Built-in Functions

| Function | Description |
|----------|-------------|
| `complex()` | Creates a complex number |
| `type()` | Returns the data type |

### Example

```python
number = complex(5, 3)

print(number)

print(type(number))
```

---

### Output

```text
(5+3j)

<class 'complex'>
```

---

## Characteristics of Complex

- Stores complex numbers.
- Contains real and imaginary parts.
- Uses `j` to represent the imaginary part.
- Immutable data type.
- Supports arithmetic operations.
- Mainly used in scientific and engineering applications.

---

## Summary

- `complex` is used to store complex numbers.
- A complex number contains a real part and an imaginary part.
- Python uses `j` to represent the imaginary unit.
- The `.real` attribute returns the real part.
- The `.imag` attribute returns the imaginary part.
- Built-in functions such as `complex()` and `type()` are commonly used with complex numbers.




