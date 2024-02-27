import ply.lex as lex
import ply.yacc as yacc
import sys

literals =("=", ";")
tokens = (
    "ID",
    "NUMBER",
)

t_ID = r"[a-zA-Z_][a-zA-Z0-9_]*"

def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t

t_ignore = " \t\n"

def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("[Lex Error] At value '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

# file = open(sys.argv[1])
# lexer.input(file.read())
# for token in lexer:
#     print(token.type, token.value, token.lineno)
 
# Para literales ha yque usar las dobres comillas " ""
# El axioma tiene que ser el primer metodo
# Tiene que estar indicado ocn la variable start
# start = "programa"
def p_programa(p):
    '''programa : asignacion ";"
                | asignacion ";" programa'''
    

    if len(p) == 3: p[0] = [p[1]]
    else: p[0] = p[3] + [p[1]]
    print(p[0])
    

def p_asignacion(p):
    '''asignacion : ID "=" NUMBER'''
    # print([x for x in p])   # muestra un array con la linea que se lee
    # print(p[1])             # valor de ID
    # print(p[2])             # valor de =
    # print(p[3])             # valor de NUMBER

    # Nos interesa dar valor a p[0] ya que sera el valor de asignacion en el parser
    p[0] = p[1] + p[2] + str(p[3])
    

def p_error(p):
    # print("[Syntax Error] At value '%s'" % p.value)
    if p.value : print("Syntax error at '%s'" % p.value)
    else : print("Syntax error at EOF")

parser = yacc.yacc()
file = open(sys.argv[1])
parser.parse(file.read())
