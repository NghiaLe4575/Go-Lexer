from enum import Enum

class TokenType(Enum):
    ILLEGAL = "ILLEGAL"
    EOF = "EOF"

    # Identifiers + literals
    IDENT = "IDENT"
    INT = "INT"
    FLOAT = "FLOAT"
    STRING = "STRING"
    CHAR = "CHAR"
    IMAG = "IMAG"
    # Go Keywords
    BREAK =    "break"
    CASE =     "case"
    CHAN =     "chan"
    CONST =    "const"
    CONTINUE = "continue"

    DEFAULT =     "default"
    DEFER =       "defer"
    ELSE =        "else"
    FALLTHROUGH = "fallthrough"
    FOR =         "for"

    FUNC =   "func"
    GO =     "go"
    GOTO =   "goto"
    IF =     "if"
    IMPORT = "import"

    INTERFACE = "interface"
    MAP =       "map"
    PACKAGE =   "package"
    RANGE =     "range"
    RETURN =    "return"

    SELECT = "select"
    STRUCT = "struct"
    SWITCH = "switch"
    TYPE =   "type"
    VAR =    "var"

    TILDE = "~"
    
    ADD = "+"
    SUB = "-"
    MUL = "*"
    QUO = "/"
    REM = "%"

    AND =     "&"
    OR =      "|"
    XOR =     "^"
    SHL =     "<<"
    SHR =     ">>"
    AND_NOT = "&^"

    ADD_ASSIGN = "+="
    SUB_ASSIGN = "-="
    MUL_ASSIGN = "*="
    QUO_ASSIGN = "/="
    REM_ASSIGN = "%="

    AND_ASSIGN =     "&="
    OR_ASSIGN =      "|="
    XOR_ASSIGN =     "^="
    SHL_ASSIGN =     "<<="
    SHR_ASSIGN =     ">>="
    AND_NOT_ASSIGN = "&^="

    LAND =  "&&"
    LOR =   "||"
    ARROW = "<-"
    INC =   "++"
    DEC =   "--"

    EQL =    "=="
    LSS =    "<"
    GTR =    ">"
    ASSIGN = "="
    NOT =    "!"

    NEQ =      "!="
    LEQ =      "<="
    GEQ =      ">="
    DEFINE =   ":="
    ELLIPSIS = "..."

    LPAREN = "("
    LBRACK = "["
    LBRACE = "{"
    COMMA =  ","
    PERIOD = "."

    RPAREN =    ")"
    RBRACK =    "]"
    RBRACE =    "}"
    SEMICOLON = ";"
    COLON =     ":"

# Map string literals to their Keyword tokens
KEYWORDS = {

    "break": TokenType.BREAK,
	"case": TokenType.CASE,
	"chan": TokenType.CHAN,
	"const": TokenType.CONST,
	"continue": TokenType.CONTINUE,

	"default": TokenType.DEFAULT,
	"defer": TokenType.DEFER,
	"else": TokenType.ELSE,
	"fallthrough": TokenType.FALLTHROUGH,
	"for": TokenType.FOR,

	"func": TokenType.FUNC,
	"go": TokenType.GO,
	"goto": TokenType.GOTO,
	"if": TokenType.IF,
	"import": TokenType.IMPORT,

	"interface": TokenType.INTERFACE,
	"map": TokenType.MAP,
	"package": TokenType.PACKAGE,
	"range": TokenType.RANGE,
	"return": TokenType.RETURN,

	"select": TokenType.SELECT,
	"struct": TokenType.STRUCT,
	"switch": TokenType.SWITCH,
	"type": TokenType.TYPE,
	"var": TokenType.VAR,

	"~": TokenType.TILDE,
}

class Token:
    def __init__(self, token_type : TokenType ,literal : str):
        self.type = token_type
        self.literal = literal
    #look nice for debugging!    
    def __repr__(self):
        return f"Token({self.type.name}, {repr(self.literal)})"

