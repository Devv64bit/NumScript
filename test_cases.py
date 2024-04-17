import unittest

from numscript import Interpreter, Token, Lexer, Parser

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


class TestInterpreter(unittest.TestCase):
    def test_basic_addition(self):
        interpreter = Interpreter("2 + 3")
        self.assertEqual(interpreter.interpret(), 5)
        print("Basic addition test passed. Expected result: 5")

    def test_operations_with_parentheses(self):
        interpreter = Interpreter("4 * (3 - 1)")
        self.assertEqual(interpreter.interpret(), 8)
        print("Operations with parentheses test passed. Expected result: 8")

    def test_exponentiation(self):
        interpreter = Interpreter("2^3")
        self.assertEqual(interpreter.interpret(), 8)
        print("Exponentiation test passed. Expected result: 8")

    def test_combined_operations(self):
        interpreter = Interpreter("5 * (2 + 3) - 4^2")
        self.assertEqual(interpreter.interpret(), 9)
        print("Combined operations test passed. Expected result: 9")

    def test_division(self):
        interpreter = Interpreter("10 / 2")
        self.assertEqual(interpreter.interpret(), 5.0)
        print("Division test passed. Expected result: 5.0")

    def test_modulo(self):
        interpreter = Interpreter("10 % 3")
        self.assertEqual(interpreter.interpret(), 1)
        print("Modulo test passed. Expected result: 1")

    def test_mixed_operations(self):
        interpreter = Interpreter("(2 + 3) * (4^2 - 10) / 2")
        self.assertEqual(interpreter.interpret(), 15)
        print("Mixed operations test passed. Expected result: 15")

    def test_negative_numbers(self):
        interpreter = Interpreter("-5 + 3")
        self.assertEqual(interpreter.interpret(), -2)
        print("Negative numbers test passed. Expected result: -2")

    def test_complex_expression(self):
        interpreter = Interpreter("(2^3 + 4) * (7 - 3^2) / 2")
        self.assertEqual(interpreter.interpret(), -12.0)
        print("Complex expression test passed. Expected result: -12.0")

    def test_invalid_input(self):
        interpreter = Interpreter("2 +")
        with self.assertRaises(Exception):
            interpreter.interpret()
            print("Invalid input test passed. Expected error.")

if __name__ == "__main__":
    unittest.main()
