from e2_lexer import LexerClass
import ply.yacc as yacc

class ParserClass:
    tokens = LexerClass.tokens

    def __init__(self):
        self.parser = yacc.yacc(module=self)
        self.lexer = LexerClass().lexer

    def p_program(self, p):
        '''program : line
                   | line NEWLINE program'''
    
    def p_line(self, p):
        '''line : plus
                | minus'''
        p[0] = p[1]
        print(p[0])
    
    def p_plus(self, p):
        'plus : NUMBER "+" NUMBER'
        p[0] = p[1] + p[3]
    
    def p_minus(self, p):
        'minus : NUMBER "-" NUMBER'
        p[0] = p[1] - p[3]
    
    def p_error(self, p):
        print(f"Syntax error at {p.value}")

    def test(self, data):
        self.parser.parse(data)
    
    def test_with_file(self, file):
        file = open(file, 'r')
        content = file.read()
        self.test(content)