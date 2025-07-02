# 1. Control Flow

**Concept:**  
The order in which the program's instructions are executed. Allows your program to make decisions and repeat actions.

---

# 2. if / else / elif (Conditional Statements)

**Concept:**  
Executes a block of code only if a certain condition is met.

- `if`: Executes if the condition is `True`.
- `elif` (else if): Checks another condition if the preceding `if`/`elif` conditions were `False`.
- `else`: Executes if all preceding `if`/`elif` conditions were `False`.

**Indentation is Crucial:**  
Python uses indentation (usually 4 spaces) to define code blocks.

**Syntax:**
```python
if condition1:
    # code to execute if condition1 is True
elif condition2:
    # code to execute if condition1 is False and condition2 is True
else:
    # code to execute if all conditions above are False
```
---
# 3. for Loop (Iteration)

**Concept:**
Used for iterating over a sequence (like a string, list, or range of numbers).

**range() function:**
Commonly used with for loops to generate a sequence of numbers.

- `range(stop)`: Generates numbers from 0 up to (but not including) stop.
- `range(start, stop)`: Generates numbers from start up to (but not including) stop.
- `range(start, stop, step)`: Generates numbers with a specified step.

**Syntax:**

```python
for item in sequence:
    # code to execute for each item
```
---

