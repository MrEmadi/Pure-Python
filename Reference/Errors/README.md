# IndentationError

**Parent: `SyntaxError` < `Exception`**

1. **Missing indentation** after `:` (e.g., `if`, `for`, `def`)
2. **Mixing tabs and spaces** in the same block
3. **Inconsistent spacing** (e.g., 2 vs 4 spaces)
4. **Extra/missing indentation** after a code block ends
5. **Empty blocks** (use `pass` to fix)

# SyntaxError

**Parent: `Exception`**

Occurs when Python detects code that doesn't follow its **grammar rules**.

# NameError

**Parent: `Exception`**

A **`NameError`** in Python happens when a variable, function, or module name is used **but not defined** in the current scope.

Check spelling, scope, and imports, or define the missing name.

# TypeError

**Parent: `Exception`**

A **`TypeError`** occurs when an operation or function is applied to an object of an **incorrect type**.

# ValueError

**Parent: `Exception`**

A **`ValueError`** occurs when a function receives an argument of the correct type but an **invalid value**.

# IndexError

**Parent: `LookupError` < `Exception`**

An **`IndexError`** occurs when you try to access an index that is **out of range in a sequence** (`list`, `tuple` or `str`).

- Use `len(sequence)` to check bounds before accessing.
- Python uses **0-based indexing** (first element is at index `0`).

# KeyError

**Parent: `LookupError` < `Exception`**

A **`KeyError`** occurs when you try to access **a dictionary key that does not exist** (`dict` or `set`).

# Exception

**`Exception`** is the **base class** for all built-in, non-system-exiting exceptions in Python.

- Use except **`Exception`** to **log errors** or **handle unexpected failures** broadly.
- **Avoid overusing**: Catch specific errors where possible (e.g., except `ValueError`).

# LookupError

**Parent: `Exception`**

**`LookupError`** is a base exception for errors that occur during **data lookups in sequences or mappings**. It covers cases where an invalid index (in sequences) or key (in mappings) is accessed.

- You'll typically encounter its subclasses (`IndexError`, `KeyError`) in code.
