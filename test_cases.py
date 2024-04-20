# test_cases.py
import unittest

from numscript import Token, Lexer, Parser, SemanticAnalyzer, CodeGenerator, Compiler

class TestToken(unittest.TestCase):
    def test_token_creation(self):
        token = Token('INT', 5)
        self.assertEqual(token.type, 'INT')
        self.assertEqual(token.value, 5)
        print("Token creation test passed. Expected: Token(INT, 5)")


class TestLexer(unittest.TestCase):
    def test_get_next_token(self):
        lexer = Lexer('2 + 3')
        tokens = [lexer.get_next_token() for _ in range(3)]
        self.assertEqual(tokens[0].type, 'INT')
        self.assertEqual(tokens[0].value, 2)
        self.assertEqual(tokens[1].type, 'PLUS')
        self.assertEqual(tokens[2].type, 'INT')
        self.assertEqual(tokens[2].value, 3)
        print("Get next token test passed. Expected tokens: INT(2), PLUS, INT(3)")


class TestParser(unittest.TestCase):
    def test_parser(self):
        lexer = Lexer('2 + 3')
        parser = Parser(lexer)
        result = parser.parse()
        self.assertEqual(result, 5)
        print("Parser test passed. Expected result: 5")


class TestSemanticAnalyzer(unittest.TestCase):
    def test_semantic_analysis(self):
        ast = 5
        analyzer = SemanticAnalyzer(ast)
        result = analyzer.analyze()
        self.assertEqual(result, 5)
        print("Semantic analysis test passed. Expected result: 5")


class TestCodeGenerator(unittest.TestCase):
    def test_code_generation(self):
        ast = 5
        generator = CodeGenerator(ast)
        code = generator.generate()
        self.assertEqual(code, "Generated code: 5")
        print("Code generation test passed. Expected code: Generated code: 5")


class TestCompiler(unittest.TestCase):
    def test_compiler(self):
        compiler = Compiler("2 + 3")
        result = compiler.compile()
        self.assertEqual(result, "Generated code: 5")
        print("Compiler test passed. Expected result: Generated code: 5")


if __name__ == "__main__":
    unittest.main()
