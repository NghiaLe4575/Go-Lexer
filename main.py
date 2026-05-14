import sys
import os
from src.lexer import Lexer
from src.token import TokenType

def main():
    #file path
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    #Check file actually exists
    if not os.path.exists(file_path):
        print(f"Error: Could not find file '{file_path}'")
        sys.exit(1)

    #Read the entire file into a string
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            source_code = file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    #Run the Lexer
    print(f"Lexing File: {file_path}")
    lexer = Lexer(source_code)
    
    token_count = 0
    while True:
        tok = lexer.nextToken()
        print(tok)
        token_count += 1
        
        if tok.type == TokenType.EOF:
            break
            
    print(f"Successfully parsed {token_count} tokens.")

if __name__ == "__main__":
    main()