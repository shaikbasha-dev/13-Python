# Integer (`int`) - Part 2

## Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations on integer values.

Python supports the following arithmetic operators.

| Operator | Description    | Example   | Result |
| -------- | -------------- | --------- | ------ |
| `+`      | Addition       | `10 + 5`  | `15`   |
| `-`      | Subtraction    | `10 - 5`  | `5`    |
| `*`      | Multiplication | `10 * 5`  | `50`   |
| `/`      | Division       | `10 / 5`  | `2.0`  |
| `//`     | Floor Division | `10 // 3` | `3`    |
| `%`      | Modulus        | `10 % 3`  | `1`    |
| `**`     | Exponentiation | `2 ** 3`  | `8`    |

---

## Program

```python
a = 20
b = 6

print("Addition :", a + b)
print("Subtraction :", a - b)
print("Multiplication :", a * b)
print("Division :", a / b)
print("Floor Division :", a // b)
print("Modulus :", a % b)
print("Exponentiation :", a ** b)
```

---

## Output

```text
Addition : 26
Subtraction : 14
Multiplication : 120
Division : 3.3333333333333335
Floor Division : 3
Modulus : 2
Exponentiation : 64000000
```

---

## Dry Run

```text
a = 20
b = 6

20 + 6  → 26

20 - 6  → 14

20 * 6  → 120

20 / 6  → 3.3333333333333335

20 // 6 → 3

20 % 6  → 2

20 ** 6 → 64000000
```

---

## Real-World Applications

Arithmetic operators are widely used in:

* Banking applications
* Billing systems
* Student result calculations
* Payroll management
* Scientific calculations
* E-commerce applications
* Inventory systems

---

# Comparison Operators

Comparison operators compare two integer values and always return a Boolean value (`True` or `False`).

---

## Comparison Operators Table

| Operator | Meaning                  | Example    | Result |
| -------- | ------------------------ | ---------- | ------ |
| `==`     | Equal To                 | `10 == 10` | `True` |
| `!=`     | Not Equal To             | `10 != 5`  | `True` |
| `>`      | Greater Than             | `20 > 10`  | `True` |
| `<`      | Less Than                | `10 < 20`  | `True` |
| `>=`     | Greater Than or Equal To | `10 >= 10` | `True` |
| `<=`     | Less Than or Equal To    | `10 <= 20` | `True` |

---

## Program

```python
a = 20
b = 10

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
```

---

## Output

```text
False
True
True
False
True
False
```

---

## Dry Run

```text
a = 20
b = 10

20 == 10 → False

20 != 10 → True

20 > 10 → True

20 < 10 → False

20 >= 10 → True

20 <= 10 → False
```

---

## Real-World Applications

Comparison operators are commonly used in:

* Login systems
* Eligibility checking
* Voting applications
* Age verification
* Student grading systems
* Employee management systems

---

# Assignment Operators

Assignment operators are used to assign values to variables and update existing values.

---

## Assignment Operators Table

| Operator | Example   | Equivalent To |
| -------- | --------- | ------------- |
| `=`      | `a = 10`  | Assign value  |
| `+=`     | `a += 5`  | `a = a + 5`   |
| `-=`     | `a -= 5`  | `a = a - 5`   |
| `*=`     | `a *= 5`  | `a = a * 5`   |
| `/=`     | `a /= 5`  | `a = a / 5`   |
| `//=`    | `a //= 5` | `a = a // 5`  |
| `%=`     | `a %= 5`  | `a = a % 5`   |
| `**=`    | `a **= 2` | `a = a ** 2`  |

---

## Program

```python
number = 20

number += 5
print(number)

number -= 10
print(number)

number *= 2
print(number)

number //= 3
print(number)

number %= 4
print(number)

number **= 3
print(number)
```

---

## Output

```text
25
15
30
10
2
8
```

---

## Dry Run

```text
number = 20

number += 5
20 + 5 = 25

↓

number -= 10
25 - 10 = 15

↓

number *= 2
15 × 2 = 30

↓

number //= 3
30 // 3 = 10

↓

number %= 4
10 % 4 = 2

↓

number **= 3
2³ = 8
```

---

## Advantages of Assignment Operators

* Reduces the amount of code.
* Improves readability.
* Makes calculations easier.
* Reduces programming errors.
* Frequently used inside loops and mathematical computations.

---

## Best Practices

* Use compound assignment operators (`+=`, `-=`, `*=`, etc.) when updating an existing variable.
* Prefer meaningful variable names instead of single-letter variables in real applications.
* Use parentheses in complex expressions to improve readability.

---

## Section Summary

In this section, you learned:

* Arithmetic Operators
* Comparison Operators
* Assignment Operators
* Their syntax
* Sample programs
* Outputs
* Dry runs
* Real-world applications
* Best practices

The next section covers **Bitwise Operators** and **Type Conversion**, followed by Python's internal handling of integers.
