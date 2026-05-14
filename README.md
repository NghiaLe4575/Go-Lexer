# Go Lexical Analyzer (Lexer) in Python

A fully functional Analyzer for the Go programming language, built entirely from scratch in Python. 

This project translates raw Go source code into a structured stream of Tokens, acting as the first phase of a theoretical compiler pipeline.

## Features
* **Zero Dependencies:** No Regex or external parsing libraries were used.
* **Maximal Munch Principle:** Correctly peeks ahead to differentiate multi-character operators (`<<=`, `==`, `!=`) from single characters (`<`, `=`).
* **Advanced Number Parsing:** Safely processes Integers (`100`), Floating Point Decimals (`10.5`), Scientific Notation (`1.5e-2`), and Imaginary/Complex Numbers (`42i`).
* **Strings & Runes:** Parses double-quoted strings (`"hello"`) and character literals (`'\n'`), correctly ignoring escaped characters.
* **Comment Isolation:** Accurately skips single-line (`//`) and multi-line (`/* */`) comments.
* **Keyword Recognition:** Distinguishes between user-defined identifiers and protected Go keywords via a dictionary to prevent namespace collisions.

## Project Structure
* `main.py`: The CLI entry point. Handles file reading and console output.
* `src/lexer.py`: The state-machine. Iterates through the input string, manages pointers, and extracts tokens.
* `src/token.py`: Contains the `TokenType` Enum and the `KEYWORDS` lookup dictionary.

## How to Run

1. Ensure you have Python 3 installed.
2. Clone or download this repository.
3. Run `main.py` from your terminal, passing the path to a `.go` file as an argument.

```bash
# Example usage:
python main.py my_code.go