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