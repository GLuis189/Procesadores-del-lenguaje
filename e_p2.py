from ply.lex import lex, TOKEN
from ply.yacc import yacc
import sys

reserveed =(
    'INT',
    'FLOAT',
)

reserveed_map = { }
for r in reserveed:
    reserveed_map[r.lower()] = r

tokens = (
    'ID',
    'INT_VAL',
    'FLOAT_VAL',
    'PLUS',
    'MINUS',
    'EQUALS',
    'SEMICOLON',
) + reserveed

t_PLUS = r'\+'
t_MINUS = r'-'
t_EQUALS = r'='
t_SEMICOLON = r';'

int_val = r'0|[1-9][0-9]*'
float_val =r'('+ int_val + r')'+ r'\.[0-9]*'
identifier = r'[a-zA-Z_][a-zA-Z_0-9]*'

@TOKEN(float_val)
def t_FLOAT_VAL(t):
    t.value = float(t.value)
    return t

@TOKEN(int_val)
def t_INT_VAL(t):
    t.value = int(t.value)
    return t

@TOKEN(identifier)
def t_ID(t):
    t.type = reserveed_map.get(t.value, 'ID')
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print('[ERROR][LEXER] At line: %d' % t.lineno)

lexer = lex()
content = open(sys.argv[1], 'r').read()

# lexer.input(content)
# for token in lexer:
#     print(token.type, token.value)

precedence = (
    ('left', 'PLUS', 'MINUS'),
    # ('left', 'TIMES', 'DIVIDE')
    ('right', 'UPLUS', 'UMINUS')
)

symbols = {}

def p_program(p):
    '''
    program : statement
            | empty
    '''
for name, value in symbols.items():
    print(name, value)
    
def p_statement(p):
    '''
    statement : content SEMICOLON
              | content SEMICOLON statement
    '''
    print('statement')

def p_content(p):
    '''
    content : declare
            | assign
            | expression
    '''
    print('content')


def p_assign(p):
    '''
    assign : ID EQUALS expression
    '''
    print('assign')

def p_expression(p):
    '''
    expression : INT_VAL
                | FLOAT_VAL
                | expression PLUS expression
                | expression MINUS expression 
                | PLUS expression %prec UPLUS
                | MINUS expression %prec UMINUS
    '''
    print('expression')


def p_empty(p):
    '''
    empty :
    '''
    pass

def declare_(p):
    '''
    declare : type ID
    '''
    symbols[p[2]] = (p[1], None)    

def p_type(p):
    '''
    declare : INT
            | FLOAT
    '''
    p[0] = p[1]
    print('type')

def p_assign_int(p):
    '''
    assign : ID EQUALS expression
    '''
    name, value = p[1], p[3]
    if name not in symbols:
        print('[ERROR][SEMANTIC] assign %s No existe' % name)
    elif symbols[name][0] != value[0]:
        print('[ERROR][SEMANTIC] assign %s no se puede asignar %s a %s' % (name, value[0], symbols[name][0]))
    else: symbols[name] = value
    symbols[name] = value

def p_assign_float(p):
    '''
    assign : ID EQUALS expression
    '''
    name, value = p[1], p[3]
    if name not in symbols:
        print('[ERROR][SEMANTIC] assign %s No existe' % name)
    elif symbols[name][0] != value[0]:
        print('[ERROR][SEMANTIC] assign %s no se puede asignar %s a %s' % (name, value[0], symbols[name][0]))
    else: symbols[name] = value
    symbols[name] = value


def p_expresion_binary(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
    '''
    a, op, b = p[1], p[2], p[3]
    if a[0] != b[0]:
        if a[0] == 'float':
            b = ('float', float(b[1]))
        else:
            a = ('float', float(a[1]))
    if   op == '+': p[0] = (a[0], a[1] + b[1])
    elif op == '-': p[0] = (a[0], a[1] - b[1])

def p_expression_unary(p):
    '''
    expression : PLUS expression %prec UPLUS
               | MINUS expression %prec UMINUS
    '''
    a, op = p[2], p[1]
    if   op == '+': p[0] = (a[0], +a[1])
    elif op == '-': p[0] = (a[0], -a[1])

def p_expression_int_val(p):
    '''
    expression : INT_VAL
    '''
    p[0] = ('int', p[1])

def p_expression_float_val(p):
    '''
    expression : FLOAT_VAL
    '''
    p[0] = ('float', p[1])

def p_expression_id(p):
    '''
    expression : ID
    '''
    name = p[1]
    if name not in symbols:
        print('[ERROR][SEMANTIC] %s No existe' % name)
    else:
        p[0] = symbols[name]

def p_error(p):
    if p: print('[ERROR][PARSER] At line: %s' % p)
    else: print('[ERROR][PARSER] At EOF')

parser = yacc()
parser.parse(content)
