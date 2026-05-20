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
            # Check the actual lookahead character safely
            next_ch = self.peek_char()
            if next_ch == '/' or next_ch == '*':
                self.skip_comment()
                return self.nextToken()
            
        # Try to parse an operator/delimiter first
        op_token = self.peek_operator()
        if op_token is not None:
            return op_token
            
        else :
            if self.isLetter(self.char):
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
        start_pos = self.curCharPos
        
        while True:
            self.read_char()
            if self.char == '\\':
                self.read_char()
                continue 
                
            if self.char == '"' or self.char == '\0':
                break
                
        self.read_char()
        string_literal = self.input[start_pos : self.curCharPos]
        return Token(TokenType.STRING, string_literal)
        
    def read_number(self) -> Token:
        pos = self.curCharPos
        is_float = False

        while self.char.isdigit():
            self.read_char()

        if self.char == '.':
            is_float = True
            self.read_char()
            while self.char.isdigit():
                self.read_char()

        if self.char in ('e', 'E'):
            is_float = True
            self.read_char()
            if self.char in ('+', '-'):
                self.read_char()
            while self.char.isdigit():
                self.read_char()

        is_imaginary = False
        if self.char == 'i':
            is_imaginary = True
            self.read_char() 

        number_literal = self.input[pos:self.curCharPos]

        if is_imaginary:
            return Token(TokenType.IMAG, number_literal)
        elif is_float:
            return Token(TokenType.FLOAT, number_literal)
        else:
            return Token(TokenType.INT, number_literal)
        
    def peek_char(self) -> str:
        if self.nextCharPos >= len(self.input):
            return '\0'
        return self.input[self.nextCharPos]
        
    def peek_operator(self):
        # Explicit length boundaries based cleanly on curCharPos
        peek_three = self.input[self.curCharPos : self.curCharPos + 3]
        if len(peek_three) == 3 and peek_three in ("<<=", ">>=", "...", "&^="):
            literal = peek_three
            self.read_char() # Consume 1st extra
            self.read_char() # Consume 2nd extra
            self.read_char() # Consume the final character of the token
            return Token(TokenType(literal), literal)

        peek_two = self.input[self.curCharPos : self.curCharPos + 2]
        if len(peek_two) == 2 and peek_two in ("<<", ">>", "&^", "+=", "-=", "*=", "/=", "%=", "&=", "|=", "^=", "&&", "||", "<-", "++", "--", "==", "!=", "<=", ">=", ":="):
            literal = peek_two
            self.read_char() # Consume 1st extra
            self.read_char() # Consume the final character of the token
            return Token(TokenType(literal), literal)

        if self.char in ("+", "-", "*", "/", "%", "&", "|", "^", "<", ">", "=", "!", "(", "[", "{", ",", ".", ")", "]", "}", ";", ":"):
            literal = self.char
            self.read_char() # MUST consume the single character!
            return Token(TokenType(literal), literal)

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