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
