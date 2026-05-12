from src.lexer import Lexer
from src.token import TokenType

from src.lexer import Lexer
from src.token import TokenType

def run_test():
    # A brutal Go snippet designed to hit every edge case in your lexer
    go_source_code = """
    // Package declaration
    package main

    import "fmt"

    /* This is a multi-line comment.
       The lexer should skip all of this!
    */
    func calculate(x) {
        var base_int = 100;
        var sci_float = 1.5e-2;
        var imaginary = 42i;
        
        var greeting = "Hello \\"World\\"!";
        var newline = '\\n';
        
        if (sci_float <= imaginary) && (base_int != 0) {
            base_int <<= 2; // Test 3-character operator
        }
        
        return ...; // Test ellipsis
    }
    """

    print("--- Starting Lexer Stress Test ---")
    lexer = Lexer(go_source_code)
    
    token_count = 0
    while True:
        tok = lexer.nextToken()
        print(tok)
        token_count += 1
        
        if tok.type == TokenType.EOF:
            break
            
    print(f"\n--- Success! Parsed {token_count} tokens. ---")

if __name__ == "__main__":
    run_test()