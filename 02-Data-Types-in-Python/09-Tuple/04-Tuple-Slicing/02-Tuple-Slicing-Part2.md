---

# Using Start and Stop Index

Both the **start** and **stop** indexes can be specified to extract a required portion of the tuple.

---

## Program

```python
numbers = (10, 20, 30, 40, 50, 60)

print(numbers[2:5])
```

---

## Output

```text
(30, 40, 50)
```

---

## Explanation

The slicing operation starts from index `2` and stops before index `5`.

Elements returned are:

- 30
- 40
- 50

---

# Using Step Value

Python allows an optional **step** value while slicing.

The step value specifies the interval between elements.

---

## Syntax

```python
tuple_name[start : stop : step]
```

---

## Program

```python
numbers = (10, 20, 30, 40, 50, 60)

print(numbers[0:6:2])
```

---

## Output

```text
(10, 30, 50)
```

---

## Explanation

The slicing operation starts from index `0`, stops before index `6`, and selects every second element.

---

# Copying a Tuple

Slicing can be used to create a copy of an existing tuple.

---

## Program

```python
languages = ("Python", "Java", "C++")

new_tuple = languages[:]

print(new_tuple)
```

---

## Output

```text
('Python', 'Java', 'C++')
```

---

## Explanation

Using `[:]` copies all elements from the original tuple into a new tuple.

---

# Negative Index Slicing

Negative indexes can also be used while slicing.

---

## Program

```python
languages = ("Python", "Java", "C++", "JavaScript", "Go")

print(languages[-4:-1])
```

---

## Output

```text
('Java', 'C++', 'JavaScript')
```

---

## Explanation

The slicing operation starts from index `-4` and stops before index `-1`.

Elements returned are:

- Java
- C++
- JavaScript
