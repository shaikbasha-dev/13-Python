# Python String Methods

## Introduction

Python provides many built-in methods that make string manipulation simple and efficient.

These methods are used to:

- Convert text into different cases.
- Search for characters or words.
- Replace text.
- Split and join strings.
- Remove unwanted spaces.
- Validate string content.
- Format strings.

Most string methods return a new string because strings are immutable in Python.

## What are String Methods?

String methods are built-in functions that perform various operations on string objects.

These methods help programmers manipulate and process textual data efficiently.

## Why are String Methods Required?

String methods are widely used in:

- Data Validation
- Form Processing
- User Input Handling
- File Processing
- Data Cleaning
- Text Formatting
- Report Generation
- Web Development

## Categories of String Methods

### Case Conversion Methods

- upper()
- lower()
- title()
- capitalize()
- swapcase()
- casefold()

### Searching Methods

- find()
- rfind()
- index()
- rindex()
- count()
- startswith()
- endswith()

### Validation Methods

- isalpha()
- isdigit()
- isnumeric()
- isdecimal()
- isalnum()
- islower()
- isupper()
- istitle()
- isspace()
- isidentifier()
- isprintable()

### Modification Methods

- replace()
- strip()
- lstrip()
- rstrip()
- center()
- ljust()
- rjust()
- zfill()

### Splitting and Joining Methods

- split()
- rsplit()
- splitlines()
- join()

### Partition Methods

- partition()
- rpartition()

### Formatting Methods

- format()
- format_map()

### Encoding Methods

- encode()

### Translation Methods

- maketrans()
- translate()

### Miscellaneous Methods

- expandtabs()
- removeprefix()
- removesuffix()

# Case Conversion Methods

## upper()

Converts all characters into uppercase.

### Syntax

```python
string.upper()
```

### Example

```python
text = "python"

print(text.upper())
```

### Output

```text
PYTHON
```

## lower()

Converts all characters into lowercase.

### Example

```python
text = "PYTHON"

print(text.lower())
```

### Output

```text
python
```

## title()

Converts the first letter of every word into uppercase.

### Example

```python
text = "python programming"

print(text.title())
```

### Output

```text
Python Programming
```

## capitalize()

Capitalizes only the first character.

### Example

```python
text = "python programming"

print(text.capitalize())
```

### Output

```text
Python programming
```

## swapcase()

Converts uppercase into lowercase and lowercase into uppercase.

### Example

```python
text = "PyThOn"

print(text.swapcase())
```

### Output

```text
pYtHoN
```

## casefold()

Converts a string into lowercase for case-insensitive comparisons.

### Example

```python
text = "Python"

print(text.casefold())
```

### Output

```text
python
```

# Searching Methods

## find()

Returns the first occurrence index.

### Example

```python
text = "Python Programming"

print(text.find("P"))
```

## rfind()

Returns the last occurrence index.

## index()

Returns the first occurrence index.

Raises ValueError if not found.

## rindex()

Returns the last occurrence index.

## count()

Returns the number of occurrences.

## startswith()

Checks whether the string starts with a specified value.

## endswith()

Checks whether the string ends with a specified value.

# Validation Methods

## isalpha()

Returns True if all characters are alphabets.

## isdigit()

Returns True if all characters are digits.

## isnumeric()

Returns True if all characters are numeric.

## isdecimal()

Returns True if all characters are decimal numbers.

## isalnum()

Returns True if all characters are alphabets or digits.

## islower()

Returns True if all characters are lowercase.

## isupper()

Returns True if all characters are uppercase.

## istitle()

Returns True if every word starts with an uppercase letter.

## isspace()

Returns True if all characters are spaces.

## isidentifier()

Returns True if the string is a valid Python identifier.

## isprintable()

Returns True if every character is printable.

# Modification Methods

## replace()

Replaces one substring with another.

## strip()

Removes spaces from both sides.

## lstrip()

Removes spaces from the left side.

## rstrip()

Removes spaces from the right side.

## center()

Aligns text in the center.

## ljust()

Left-aligns the string.

## rjust()

Right-aligns the string.

## zfill()

Pads zeros on the left side.

# Splitting and Joining Methods

## split()

Splits a string into a list.

## rsplit()

Splits from the right side.

## splitlines()

Splits a multiline string into lines.

## join()

Joins iterable elements into a string.

# Partition Methods

## partition()

Splits the string into three parts using a separator.

## rpartition()

Splits from the rightmost separator.

# Formatting Methods

## format()

Formats a string.

### Example

```python
name = "Basha"

print("Welcome {}".format(name))
```

### Output

```text
Welcome Basha
```

## format_map()

Formats using a mapping object.

# Encoding Methods

## encode()

Encodes a string into bytes.

# Translation Methods

## maketrans()

Creates a translation table.

## translate()

Translates characters using a translation table.

# Miscellaneous Methods

## expandtabs()

Replaces tab characters with spaces.

## removeprefix()

Removes the specified prefix.

### Example

```python
text = "Mr.Basha"

print(text.removeprefix("Mr."))
```

### Output

```text
Basha
```

## removesuffix()

Removes the specified suffix.

### Example

```python
text = "Python.py"

print(text.removesuffix(".py"))
```

### Output

```text
Python
```

# Summary

## Case Conversion Methods

- upper()
- lower()
- title()
- capitalize()
- swapcase()
- casefold()

## Searching Methods

- find()
- rfind()
- index()
- rindex()
- count()
- startswith()
- endswith()

## Validation Methods

- isalpha()
- isdigit()
- isnumeric()
- isdecimal()
- isalnum()
- islower()
- isupper()
- istitle()
- isspace()
- isidentifier()
- isprintable()

## Modification Methods

- replace()
- strip()
- lstrip()
- rstrip()
- center()
- ljust()
- rjust()
- zfill()

## Splitting and Joining Methods

- split()
- rsplit()
- splitlines()
- join()

## Partition Methods

- partition()
- rpartition()

## Formatting Methods

- format()
- format_map()

## Encoding Methods

- encode()

## Translation Methods

- maketrans()
- translate()

## Miscellaneous Methods

- expandtabs()
- removeprefix()
- removesuffix()
