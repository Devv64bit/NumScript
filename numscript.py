# Language Name: NumScript (Version 1)
# Base language (starting language): Python 3.12

class Token:
    def __init__(self, token_type, value=None):
        self.type = token_type
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {self.value})'

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def _get_next_char(self):
        if self.pos >= len(self.text):
            return None
        next_char = self.text[self.pos]
        self.pos += 1
        return next_char

    def get_next_token(self):
        current_char = self._get_next_char()
        if current_char is None:
            return Token('EOF')

        while current_char is not None:
            if current_char.isdigit():
                value = current_char
                next_char = self._get_next_char()
                while next_char is not None and next_char.isdigit():
                    value += next_char
                    next_char = self._get_next_char()
                if next_char is not None:
                    self.pos -= 1
                return Token('INT', int(value))
            elif current_char == '+':
                return Token('PLUS')
            elif current_char == '-':
                return Token('MINUS')
            elif current_char == '*':
                return Token('MULTIPLY')
            elif current_char == '/':
                return Token('DIVIDE')
            elif current_char == '%':
                return Token('MODULO')
            elif current_char == '^':
                return Token('POWER')
            elif current_char == '(':
                return Token('LPAREN')
            elif current_char == ')':
                return Token('RPAREN')
            elif current_char == ' ':
                current_char = self._get_next_char()
            else:
                raise Exception(f'Invalid character: {current_char}')  # Raise exception for invalid character
        return Token('EOF')

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def _eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception(f'Unexpected token: {self.current_token}')

    def _factor(self):
        if self.current_token.type in ('PLUS', 'MINUS'):
            sign = 1 if self.current_token.type == 'PLUS' else -1
            self._eat(self.current_token.type)
            value = sign * self._factor()
            return value
        elif self.current_token.type == 'INT':
            value = self.current_token.value
            self._eat('INT')
            while self.current_token.type in ('LPAREN', 'INT', 'POWER', 'MODULO'):
                if self.current_token.type == 'POWER':
                    self._eat('POWER')
                    value = value**self._factor()
                elif self.current_token.type == 'MODULO':
                    self._eat('MODULO')
                    value %= self._factor()
                elif self.current_token.type == 'INT':
                    value *= self.current_token.value
                    self._eat('INT')
                elif self.current_token.type == 'LPAREN':
                    self._eat('LPAREN')
                    value *= self._expr()
                    self._eat('RPAREN')
            return value
        elif self.current_token.type == 'LPAREN':
            self._eat('LPAREN')
            value = self._expr()
            self._eat('RPAREN')
            while self.current_token.type in ('LPAREN', 'INT', 'POWER', 'MODULO'):
                if self.current_token.type == 'POWER':
                    self._eat('POWER')
                    value = value**self._factor()
                elif self.current_token.type == 'MODULO':
                    self._eat('MODULO')
                    value %= self._factor()
                elif self.current_token.type == 'INT':
                    value *= self.current_token.value
                    self._eat('INT')
                elif self.current_token.type == 'LPAREN':
                    self._eat('LPAREN')
                    value *= self._expr()
                    self._eat('RPAREN')
            return value
        else:
            raise Exception(f'Unexpected token: {self.current_token}')

    def _term(self):
        value = self._factor()
        while self.current_token.type in ('MULTIPLY', 'DIVIDE'):
            if self.current_token.type == 'MULTIPLY':
                self._eat('MULTIPLY')
                value *= self._factor()
            elif self.current_token.type == 'DIVIDE':
                self._eat('DIVIDE')
                value /= self._factor()
        return value

    def _expr(self):
        value = self._term()
        while self.current_token.type in ('PLUS', 'MINUS'):
            if self.current_token.type == 'PLUS':
                self._eat('PLUS')
                value += self._term()
            elif self.current_token.type == 'MINUS':
                self._eat('MINUS')
                value -= self._term()
        return value

    def parse(self):
        return self._expr()

class SemanticAnalyzer:
    def __init__(self, ast):
        self.ast = ast

    def analyze(self):
        # Perform semantic analysis on the AST
        # Check for type errors, undeclared variables, etc.
        # For simplicity, we'll assumed the expressions are valid
        return self.ast

class CodeGenerator:
    def __init__(self, ast):
        self.ast = ast

    def generate(self):
        # Generate bytecode or machine code from the AST
        # For simplicity, we'll just return the AST as a string
        return f"Generated code: {self.ast}"

class Compiler:
    def __init__(self, text):
        self.text = text

    def compile(self):
        lexer = Lexer(self.text)
        parser = Parser(lexer)
        ast = parser.parse()
        semantic_analyzer = SemanticAnalyzer(ast)
        analyzed_ast = semantic_analyzer.analyze()
        code_generator = CodeGenerator(analyzed_ast)
        return code_generator.generate()


if __name__ == '__main__':
    print("{ - Numscript Language Version 1.0 (input 'exit' to stop running all operations) - }")
    while True:
        try:
            source_code = input('Numscript> ')
            if source_code.lower() == 'exit':
                break
        except EOFError:
            break
        if not source_code:
            continue
        try:
            compiler = Compiler(source_code)
            result = compiler.compile()
            print(result)
        except Exception as e:
            print(f'Error: {e}')
