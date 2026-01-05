# lexical_phase.py
import re

# Token Definitions
TOKEN_TYPES = [
    ('DEFINE',   r'DEFINE'),
    ('ACTION',   r'ALLOW|BLOCK'),
    ('PROTOCOL', r'TCP|UDP|HTTP|HTTPS'),
    ('IP',       r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'),
    ('PORT_KEY', r'PORT'),
    ('TO',       r'TO'),
    ('FROM',     r'FROM'),
    ('ANY',      r'ANY'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('NUMBER',   r'\d+'),
    ('EQUALS',   r'='),
    ('SEMICOLON',r';'),
    ('COMMENT',  r'#.*'),   # Ignore comments
    ('WHITESPACE', r'\s+'), # Ignore whitespace
    ('UNKNOWN',  r'.'),
]

class Token:
    def __init__(self, type, value, line):
        self.type = type
        self.value = value
        self.line = line
    def __repr__(self): return f"<{self.type}: {self.value}>"

class LexicalAnalyzer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.current_line = 1

    def tokenize(self):
        position = 0
        while position < len(self.source_code):
            match = None
            for token_type, pattern in TOKEN_TYPES:
                regex = re.compile(pattern)
                match = regex.match(self.source_code, position)
                if match:
                    value = match.group(0)
                    if token_type == 'WHITESPACE' or token_type == 'COMMENT':
                        self.current_line += value.count('\n')
                    elif token_type == 'UNKNOWN':
                        raise Exception(f"Lexical Error: Unknown character '{value}' at line {self.current_line}")
                    else:
                        self.tokens.append(Token(token_type, value, self.current_line))
                    position = match.end()
                    break
            if not match: 
                raise Exception(f"Lexical Error: Unexpected character at line {self.current_line}")
        return self.tokens