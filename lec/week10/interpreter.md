
# Key Concepts:

1. **Interpreters**:
   - An **interpreter** evaluates expressions in a language. This chapter focuses on building an interpreter for a simple language called **Calculator**, which is based on Scheme's syntax.

2. **Calculator Language**:
   - The language supports basic arithmetic operations:
     - `+`, `-`, `*`, `/` (addition, subtraction, multiplication, division)
   - Operations take a variable number of arguments:
     - `(+ 1 2 3)` → **10**
     - `(* 1 2 3 4)` → **24**
     - `(- 10 1 2 3)` → **4**
     - `(/ 15 12)` → **1.25**

3. **Expression Trees**:
   - In this language, **expressions** are represented as **lists** (similar to Scheme). A list’s first item is an operator, and the rest are operands.
     - Example: `(+ (* 3 4) 5)`
       - This represents the expression where `*` is applied to `3` and `4`, and then the result is added to `5`.

4. **Parsing**:
   - **Parsing** turns raw input (text) into these list-based expression trees. First, the input is split into **tokens** (like `+`, `1`, `2`, etc.), and then a parser converts the tokens into nested lists.
   - Example of tokenization:
     - `(+ 1 (* 2.3 45))` → `['(', '+', 1, '(', '*', 2.3, 45, ')', ')']`
   - Example of parsing:
     - `(+ 1 (* 2.3 45))` → `Pair('+', Pair(1, Pair(Pair('*', Pair(2.3, Pair(45, nil))), nil)))`

5. **Evaluation**:
   - The **evaluator** checks if an expression is a number (it’s returned as is) or a function call (it evaluates the operands and applies the operator).
   - Example of evaluating a simple expression:
     - `(+ 1 2 3)` → **6**
     - `(* 3 4)` → **12**
     - `(- 10 1 2 3)` → **4**

6. **REPL (Read-Eval-Print Loop)**:
   - The **REPL** lets you interact with the interpreter: type in an expression, get the result, and then keep going.
   - Example session:
     ```
     > (* 1 2 3)
     6
     > (+)
     0
     > (+ 2 (/ 4 8))
     2.5
     > (+ 2 2) (* 3 3)
     4
     9
     ```

7. **Error Handling**:
   - The interpreter should catch and report errors like:
     - Syntax errors: Incorrectly formed expressions.
     - Runtime errors: For example, dividing by zero.
   - Example of error handling:
     ```
     > )
     SyntaxError: unexpected token: )
     > 2.3.4
     ValueError: invalid numeral: 2.3.4
     > (+ 1)
     1
     > (/ 1 0)
     ZeroDivisionError: division by zero
     ```

# Core Steps to Build the Interpreter:
1. **Tokenization**: Convert a string input into tokens like `['+', 1, 2]`.
2. **Parsing**: Turn the tokens into a list structure that represents the expression.
3. **Evaluation**: Apply the operator to the operands, possibly recursively evaluating sub-expressions.

# Example of Evaluation Logic:
```python
"""
>>> calc_apply('+', as_scheme_list(1, 2, 3))
6
>>> calc_apply('-', as_scheme_list(10, 1, 2, 3))
4
>>> calc_apply('*', nil)
1
>>> calc_apply('*', as_scheme_list(1, 2, 3, 4, 5))
120
>>> calc_apply('/', as_scheme_list(40, 5))
8.0
"""
>>> def calc_apply(operator, args):
        """Apply the named operator to a list of args."""
        if not isinstance(operator, str):
            raise TypeError(str(operator) + ' is not a symbol')
        if operator == '+':
            return reduce(add, args, 0)
        elif operator == '-':
            if len(args) == 0:
                raise TypeError(operator + ' requires at least 1 argument')
            elif len(args) == 1:
                return -args.first
            else:
                return reduce(sub, args.second, args.first)
        elif operator == '*':
            return reduce(mul, args, 1)
        elif operator == '/':
            if len(args) == 0:
                raise TypeError(operator + ' requires at least 1 argument')
            elif len(args) == 1:
                return 1/args.first
            else:
                return reduce(truediv, args.second, args.first)
        else:
            raise TypeError(operator + ' is an unknown operator')
```

# Summary:
- **Interpreters** read and evaluate expressions in a language, using recursive structures like lists to represent and compute the values.
- Key tasks for creating an interpreter include **tokenization**, **parsing**, **evaluating**, and providing a **REPL** for user interaction.
- Handling errors helps make the interpreter more user-friendly and robust.


# `read_eval_print_loop`
```python
>>> def read_eval_print_loop():
        """Run a read-eval-print loop for calculator."""
        while True:
            try:
                src = buffer_input()
                while src.more_on_line:
                    expression = scheme_read(src)
                    print(calc_eval(expression))
            except (SyntaxError, TypeError, ValueError, ZeroDivisionError) as err:
                print(type(err).__name__ + ':', err)
            except (KeyboardInterrupt, EOFError):  # <Control>-D, etc.
                print('Calculation completed.')
                return

```