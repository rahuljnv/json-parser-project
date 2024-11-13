import re

class JSONTokenizer:
    def __init__(self, json_string):
        self.json_string = json_string
        self.position = 0
        self.tokens = []
        self.tokenize()
        
    def tokenize(self):
        token_specification = [
            ('WHITESPACE', r'\s+'),
            ('NUMBER', r'-?\d+(\.\d+)?([eE][+-]?\d+)?'),
            ('STRING', r'"(\\.|[^"\\])*"'),
            ('TRUE', r'true'),
            ('FALSE', r'false'),
            ('NULL', r'null'),
            ('LBRACE', r'\{'),
            ('RBRACE', r'\}'),
            ('LBRACKET', r'\['),
            ('RBRACKET', r'\]'),
            ('COMMA', r','),
            ('COLON', r':'),
        ]
        tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
        
        for match in re.finditer(tok_regex, self.json_string):
            kind = match.lastgroup
            value = match.group(kind)
            if kind != 'WHITESPACE':
                self.tokens.append((kind, value))
        
    def get_tokens(self):
        return self.tokens
