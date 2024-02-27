import ply.lex as lex

class LexerClass:
    tokens = ('NUMBER','NEWLINE')
    literals = ('+', '-')
    def __init__(self) -> None:
        self.lexer = lex.lex(module=self)
        
    def t_NUMBER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t
    
    def t_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += t.value.count('\n')
        return t

    t_ignore = " \t"

    def t_error(self, t):
        print(f"Illegal character {t.value[0]}")
        t.lexer.skip(1)

    def test(self, data):
        self.lexer.input(data)
        for token in self.lexer:
            print(token.type, token.value)
    
    def test_with_file(self, file):
        file = open(file, 'r')
        content = file.read()
        for line in content:
            self.test(line)
