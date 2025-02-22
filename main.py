from lark import Lark
from goonlang.parser import Parser

goonlang_code = """print("gooning");print("goon");"""

parser = Parser(goonlang_code, "goonlang.lark")