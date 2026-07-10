# Mathematical Set Operations

## Definition

Mathematical set operations are used to perform operations between two or more sets.

Python supports the following mathematical set operations:

- Union
- Intersection
- Difference
- Symmetric Difference

---

# Union

## Definition

The union operation returns all unique elements from both sets.

---

## Syntax

```python
set1.union(set2)
```

---

## Program

```python
set1 = {10, 20, 30}

set2 = {30, 40, 50}

print(set1.union(set2))
```

---

## Output

```text
{10, 20, 30, 40, 50}
```

---

# Intersection

## Definition

The intersection operation returns the common elements present in both sets.

---

## Syntax

```python
set1.intersection(set2)
```

---

## Program

```python
set1 = {10, 20, 30}

set2 = {30, 40, 50}

print(set1.intersection(set2))
```

---

## Output

```text
{30}
```

---

# Difference

## Definition

The difference operation returns the elements present in the first set but not in the second set.

---

## Syntax

```python
set1.difference(set2)
```

---

## Program

```python
set1 = {10, 20, 30}

set2 = {30, 40, 50}

print(set1.difference(set2))
```

---

## Output

```text
{10, 20}
```

---

# Symmetric Difference

## Definition

The symmetric difference operation returns the elements that are present in either set but not in both.

---

## Syntax

```python
set1.symmetric_difference(set2)
```

---

## Program

```python
set1 = {10, 20, 30}

set2 = {30, 40, 50}

print(set1.symmetric_difference(set2))
```

---

## Output

```text
{10, 20, 40, 50}
```
