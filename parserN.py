class JSONParser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def parse(self):
        token_type, token_value = self.peek()
        if token_type == 'LBRACE':
            return self.parse_object()
        elif token_type == 'LBRACKET':
            return self.parse_array()
        else:
            raise SyntaxError("JSON must start with an object or array")

    def parse_object(self):
        obj = {}
        self.consume('LBRACE')
        while self.peek()[0] != 'RBRACE':
            key = self.parse_string()
            self.consume('COLON')
            value = self.parse_value()
            obj[key] = value
            if self.peek()[0] != 'RBRACE':
                self.consume('COMMA')
        self.consume('RBRACE')
        return obj

    def parse_array(self):
        array = []
        self.consume('LBRACKET')
        while self.peek()[0] != 'RBRACKET':
            array.append(self.parse_value())
            if self.peek()[0] != 'RBRACKET':
                self.consume('COMMA')
        self.consume('RBRACKET')
        return array

    def parse_value(self):
        token_type, token_value = self.peek()
        if token_type == 'NUMBER':
            return self.parse_number()
        elif token_type == 'STRING':
            return self.parse_string()
        elif token_type == 'TRUE':
            self.consume('TRUE')
            return True
        elif token_type == 'FALSE':
            self.consume('FALSE')
            return False
        elif token_type == 'NULL':
            self.consume('NULL')
            return None
        elif token_type == 'LBRACE':
            return self.parse_object()
        elif token_type == 'LBRACKET':
            return self.parse_array()
        else:
            raise SyntaxError(f"Unexpected token: {token_value}")

    def parse_string(self):
        _, value = self.consume('STRING')
        return value[1:-1]  # Remove the double quotes

    def parse_number(self):
        _, value = self.consume('NUMBER')
        if '.' in value or 'e' in value or 'E' in value:
            return float(value)
        else:
            return int(value)

    def consume(self, expected_type):
        token_type, token_value = self.tokens[self.position]
        if token_type != expected_type:
            raise SyntaxError(f"Expected {expected_type} but got {token_type}")
        self.position += 1
        return token_type, token_value

    def peek(self):
        if self.position >= len(self.tokens):
            raise SyntaxError("Unexpected end of input")
        return self.tokens[self.position]
