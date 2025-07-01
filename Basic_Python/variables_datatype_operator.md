# Day 1: Variables, Data Types & Operators

## 1. Variables:

### Concept: 
Containers for storing data values. Think of them as named boxes.
***
### Declaration: 
You don't declare a type explicitly in Python; the type is inferred from the assigned value.

### Assignment: 
Use the single equals sign (=).
***

### Naming Conventions:

* Start with a letter or underscore (_).

* Can contain letters, numbers, and underscores.

* Case-sensitive (myVar is different from myvar).

* Use snake_case (e.g., my_variable, user_age) for readability.

* Avoid using Python keywords (e.g., if, for, print).
***

> **_NOTE:_**  The corresponding program files have the same name as this .md file, but with a .py extension.

---

## 2. Data Types

### Common Types

- **Integers (`int`)**: Whole numbers  
  _Examples:_ `5`, `-100`, `0`

- **Floats (`float`)**: Decimal numbers  
  _Examples:_ `3.14`, `-0.5`, `10.0`

- **Strings (`str`)**: Sequences of characters, enclosed in single (`' '`) or double (`" "`) quotes  
  _Examples:_ `'hello'`, `"world"`

  - **Concatenation**: Use `+` to join strings  
    _Example:_ `"Hello" + " " + "World"` → `"Hello World"`

  - **f-strings (Formatted String Literals)**: Recommended for embedding variables easily  
    _Example:_ `name = "John"` → `f"Hello, {name}"`

- **Booleans (`bool`)**: Represents truth values: `True` or `False`  
  Used for logical operations and decision-making

---
## 3. Operators

### Concept  
Operators are symbols that perform operations on values and variables.

---

### Arithmetic Operators

| Operator | Description                 | Example        |
|----------|-----------------------------|----------------|
| `+`      | Addition                    | `3 + 2` → `5`   |
| `-`      | Subtraction                 | `5 - 1` → `4`   |
| `*`      | Multiplication              | `2 * 3` → `6`   |
| `/`      | Division (returns float)    | `10 / 4` → `2.5` |
| `//`     | Floor Division              | `10 // 4` → `2` |
| `%`      | Modulus (remainder)         | `10 % 3` → `1`  |
| `**`     | Exponentiation              | `2 ** 3` → `8`  |

---

### Comparison Operators  
(Return `True` or `False`)

| Operator | Meaning                    | Example          |
|----------|----------------------------|------------------|
| `==`     | Equal to                   | `5 == 5` → `True` |
| `!=`     | Not equal to               | `5 != 3` → `True` |
| `>`      | Greater than               | `4 > 2` → `True`  |
| `<`      | Less than                  | `2 < 4` → `True`  |
| `>=`     | Greater than or equal to   | `5 >= 5` → `True` |
| `<=`     | Less than or equal to      | `3 <= 4` → `True` |

---

### Logical Operators  
(Used to combine boolean expressions)

| Operator | Description                        | Example                  |
|----------|------------------------------------|--------------------------|
| `and`    | True if both conditions are True   | `True and True` → `True` |
| `or`     | True if at least one is True       | `True or False` → `True` |
| `not`    | Inverts the boolean value          | `not True` → `False`     |

---