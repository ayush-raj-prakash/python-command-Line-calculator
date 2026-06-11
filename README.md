# 🧮Python Command-Line Calculator

## Description
A simple command-line calculator built in Python that performs basic arithmetic operations.
It handles invalid inputs and division-by-zero errors gracefully, and runs in a loop until the user decides to quit.

## Features
- Supports 7 operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Division-by-zero error handling for `/`, `//`, and `%`
- Input validation using `try/except` — prevents crashes on invalid input
- Runs continuously in a loop with an option to exit after each calculation

## How to Run
```bash
python calculator.py
```

**Example:**
```
Enter the first number: 10
Enter the second number: 3
Enter the operator (+, -, *, /, //, %, **): **
Result: 1000.0

Calculate again? (y/n): n
Goodbye!
```

## Technologies Used
- Python 3.x
- No external libraries required (uses built-in `float()` and `input()` only)

## Author
Ayush Raj Prakash
