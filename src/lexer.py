#import TokenType
from src.token import TokenType, KEYWORDS, Token
class Lexer:
    def __init__(self, Istring : str):
        self.input = Istring
        self.curCharPos = 0
        self.nextCharPos = 0
        self.char = ''
        self.read_char() ## initialize the lexer
        
        
    def read_char(self):
        if self.nextCharPos >= len(self.input):
            self.char = "\0"
        else:
            self.char = self.input[self.nextCharPos]
        self.curCharPos = self.nextCharPos
        self.nextCharPos += 1
        
    def skip_space(self):
        while self.char in (" ","\n","\t","\r") :
            self.read_char()
            
    def nextToken(self):
        self.skip_space()  
        token = None
        
        if self.char == '\0':
            token = Token(TokenType.EOF, "")
            self.read_char()
            return token
        
        elif self.char == '"':
            return self.read_string()
        
        elif self.char == "'":
            return self.read_char_literal()
        
        if self.char == '/':
            # If the NEXT character is / or *, it's a comment!
            if self.peek_char() == '/' or self.peek_char() == '*':
                self.skip_comment()
                return self.nextToken()
            
        # Try to parse an operator/delimiter first
        op_token = self.peek_operator()
        if op_token is not None:
            token = op_token
            
        else :
            if self.isLetter(self.char) or self.char == "_":
                literal = self.read_identifier()
                # Check if it's a Go keyword, otherwise it's just an IDENTifier
                token_type = KEYWORDS.get(literal, TokenType.IDENT)
                return Token(token_type, literal)
            
            elif self.char.isdigit():
                return self.read_number()            
            else:
                token = Token(TokenType.ILLEGAL, self.char)

        self.read_char()
        return token
    
    def isLetter(self, ch: str) -> bool:
        return ch.isalpha() or ch == '_'

    def read_identifier(self) -> str:
        pos = self.curCharPos
        #identifiers can have numbers after the first letter
        while self.isLetter(self.char) or self.char.isdigit():
            self.read_char()
        return self.input[pos:self.curCharPos]
    def skip_comment(self):
        # SINGLE LINE COMMENTS (//)
        if self.peek_char() == '/':
            self.read_char()             
            while self.char != '\n' and self.char != '\0':
                self.read_char()
        # MULTI-LINE COMMENTS (/* ... */)
        elif self.peek_char() == '*':
            self.read_char() # Advance onto the '*'
            
            while True:
                self.read_char()
                if self.char == '\0':
                    break
                if self.char == '*' and self.peek_char() == '/':
                    self.read_char() # Advance onto the '/'
                    self.read_char() # Advance PAST the '/' so it's fully consumed
                    break
            
    def read_string(self) -> Token:
        #currently sitting ON the opening '"'
        start_pos = self.curCharPos
        
        while True:
            self.read_char()

            if self.char == '\\':
                self.read_char()
                continue # Jump back to the top of the loop
                
            # Stop Condition
            if self.char == '"' or self.char == '\0':
                break
                
        self.read_char()
        
        # Slice the entire string (This will INCLUDE the quotes!)
        string_literal = self.input[start_pos : self.curCharPos]
        
        return Token(TokenType.STRING, string_literal)
        
    def read_number(self) -> Token:
        pos = self.curCharPos
        is_float = False

        # Read the base integer part
        while self.char.isdigit():
            self.read_char()

        # Check for a decimal point
        if self.char == '.':
            is_float = True
            self.read_char()
            while self.char.isdigit():
                self.read_char()

        # Check for Scientific Notation (e or E)
        if self.char in ('e', 'E'):
            is_float = True
            self.read_char()
            if self.char in ('+', '-'):
                self.read_char()
            while self.char.isdigit():
                self.read_char()

        # Check for Imaginary number (i)
        is_imaginary = False
        if self.char == 'i':
            is_imaginary = True
            self.read_char() # Consume the 'i'

        # Slice the final gathered string
        number_literal = self.input[pos:self.curCharPos]

        # Determine the correct token type
        if is_imaginary:
            return Token(TokenType.IMAG, number_literal)
        elif is_float:
            return Token(TokenType.FLOAT, number_literal)
        else:
            return Token(TokenType.INT, number_literal)
        
    def peek_char(self) -> str:
        if self.nextCharPos >= len(self.input):
            return '\0'
        else:
            return self.input[self.nextCharPos]
        
    def peek_operator(self):
        # try to grab 3 characters
        peek_three = self.input[self.curCharPos : self.nextCharPos + 2]
    
        if peek_three in ("<<=", ">>=", "...", "&^="):
            self.read_char() # Advance past char 2
            self.read_char() # Advance past char 3
            return Token(TokenType(peek_three), peek_three)

        # Try to grab 2 characters
        peek_two = self.input[self.curCharPos : self.nextCharPos + 1]
    
        if peek_two in ("<<", ">>", "&^", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "&&", "||", "<-", "++", "--", "==", "!=", "<=", ">=", ":="):
            self.read_char() # Advance past char 2
            return Token(TokenType(peek_two), peek_two)

        if self.char in ("+", "-", "*", "/", "%", "&", "|", "^", "<", ">", "=", "!", "(", "[", "{", ",", ".", ")", "]", "}", ";", ":"):
            return Token(TokenType(self.char), self.char)

        return None
                
    def read_char_literal(self) -> Token:
        start_pos = self.curCharPos
        
        while True:
            self.read_char()

            if self.char == '\\':
                self.read_char()
                continue 
                
            if self.char == "'" or self.char == '\0':
                break
                
        self.read_char()
        
        char_literal = self.input[start_pos : self.curCharPos]
        
        return Token(TokenType.CHAR, char_literal)