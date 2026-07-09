# Python Data Types Comparison

## Introduction

Python provides four important collection data types:

- List
- Tuple
- Set
- Dictionary

Each data type has different characteristics and is used for different purposes.

---

# List vs Tuple vs Set vs Dictionary

| Feature | List | Tuple | Set | Dictionary |
|----------|------|-------|-----|------------|
| Syntax | `[]` | `()` | `{}` | `{key:value}` |
| Ordered | Yes | Yes | No | Yes (Python 3.7+) |
| Mutable | Yes | No | Yes | Yes |
| Immutable | No | Yes | No | No |
| Duplicate Values | Allowed | Allowed | Not Allowed | Values Allowed, Keys Not Allowed |
| Indexing | Supported | Supported | Not Supported | Keys Used Instead of Index |
| Slicing | Supported | Supported | Not Supported | Not Supported |
| Stores | Values | Values | Unique Values | Key-Value Pairs |
| Access Method | Index | Index | Traversal | Key |
| Memory Usage | More | Less | Moderate | Moderate |
| Search Speed | Medium | Medium | Very Fast | Very Fast |
| Insertion Order | Maintained | Maintained | Not Guaranteed | Maintained |
| Can Store Mixed Data Types | Yes | Yes | Yes | Yes |
| Nested Collection | Supported | Supported | Supported | Supported |
| Best For | Dynamic Collections | Fixed Collections | Unique Collections | Structured Data |

---

# When Should We Use Each Data Type?

| Situation | Recommended Data Type | Reason |
|-----------|----------------------|--------|
| Store student names | List | Ordered collection that can change |
| Store months of the year | Tuple | Fixed data that should not change |
| Remove duplicate values | Set | Automatically removes duplicates |
| Store employee details | Dictionary | Data stored as key-value pairs |
| Shopping Cart | List | Items can be added and removed |
| GPS Coordinates | Tuple | Fixed values |
| Unique User IDs | Set | Duplicate IDs are not allowed |
| Bank Account Details | Dictionary | Easy retrieval using keys |

---

# Where is Each Data Type Used?

## List

Used in:

- Shopping Cart
- Student Lists
- Product Lists
- Playlist
- Task Management

---

## Tuple

Used in:

- Coordinates
- RGB Colors
- Date and Time
- Mathematical Constants
- Fixed Configuration Values

---

## Set

Used in:

- Unique Student IDs
- Unique Email Addresses
- Duplicate Removal
- Tags
- Permissions

---

## Dictionary

Used in:

- Student Records
- Employee Details
- Banking Systems
- JSON Data
- API Responses
- User Profiles

---

# How to Create?

## List

```python
numbers = [10, 20, 30]
```

---

## Tuple

```python
numbers = (10, 20, 30)
```

---

## Set

```python
numbers = {10, 20, 30}
```

---

## Dictionary

```python
student = {
    "id": 101,
    "name": "Basha"
}
```

---

# How to Access Data?

| Data Type | Access Method | Example |
|-----------|---------------|---------|
| List | Index | `list[0]` |
| Tuple | Index | `tuple[0]` |
| Set | Traversal | `for item in set:` |
| Dictionary | Key | `dict["name"]` |

---

# Advantages

## List

- Easy to modify
- Supports indexing
- Supports slicing
- Suitable for dynamic data

---

## Tuple

- Faster than lists
- Immutable
- Memory efficient
- Safe for fixed data

---

## Set

- Removes duplicates automatically
- Fast searching
- Supports mathematical set operations
- Efficient membership testing

---

## Dictionary

- Fast key-based lookup
- Stores structured data
- Easy to update
- Suitable for real-world applications

---

# Limitations

## List

- Allows duplicate values
- Uses more memory

---

## Tuple

- Cannot be modified

---

## Set

- No indexing
- No slicing
- Unordered collection

---

## Dictionary

- Keys must be unique
- Keys must be immutable

---

# Quick Revision Table

| If You Want To... | Use |
|-------------------|-----|
| Store ordered data | List |
| Store fixed data | Tuple |
| Remove duplicates | Set |
| Store key-value data | Dictionary |
| Frequently update data | List |
| Improve performance for fixed values | Tuple |
| Fast membership checking | Set |
| Retrieve data using keys | Dictionary |

---

# Summary

| Data Type | Best Used For |
|-----------|---------------|
| List | Dynamic ordered collections |
| Tuple | Fixed ordered collections |
| Set | Unique collections |
| Dictionary | Key-value mappings |

Remember:

- **List** → Ordered and Changeable
- **Tuple** → Ordered and Fixed
- **Set** → Unique Values
- **Dictionary** → Key-Value Pairs
