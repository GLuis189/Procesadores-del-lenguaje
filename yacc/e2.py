import sys
from e2_lexer import LexerClass
from e2_parser import ParserClass

# l = LexerClass()
# l.test_with_file(sys.argv[1])

p = ParserClass()
p.test_with_file(sys.argv[1])