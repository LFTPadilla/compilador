# Compilador

A compiler for a custom Java-like language, built from scratch in Python. Translates source code written in a custom language into Python code.

## Features

- **Lexical analysis** — tokenizer with automata for identifiers, operators, literals, and reserved words
- **Syntactic analysis** — recursive descent parser covering functions, variables, control flow (`if/else`, `while`), arithmetic/logical/relational expressions, arrays, maps, and function calls
- **Semantic analysis** — symbol table with scope management, type checking, and duplicate/undeclared variable detection
- **Code generation** — translates validated source into equivalent Python code
- **GUI** — PyQt5 desktop interface with separate panels for lexical, syntactic, and semantic analysis

## Tech Stack

- Python 3
- PyQt5

## Project Structure

```
compilador/
├── Aplicacion.py              # Entry point
├── interfaz/
│   ├── interfaz.py            # PyQt5 main window
│   └── interfazQT.ui          # Qt Designer UI file
└── logica/
    ├── lexico/                # Lexer: tokenizer, categories, reserved words
    ├── sintactico/            # Parser: 20+ grammar rule classes
    └── semantica/             # Semantic analyzer: symbol table, type checker
```

## Running

```bash
pip install PyQt5
python Aplicacion.py
```

## Language Features Supported

- Primitive types: `int`, `double`, `boolean`, `char`, `String`
- Functions with parameters and return types
- Variable declaration and assignment
- Control flow: `if/else`, `while`
- Expressions: arithmetic, logical, relational, string
- Data structures: arrays (`array`), maps (`map`)
- I/O: `imprimir` (print), `leer` (read)
- Increment/decrement operators
- Scope-aware semantic validation
