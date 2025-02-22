from lark import Lark

parser = Lark.open("goonlang.lark")

goonlang_code = """print("gooning");print("goon");"""

def run_instruction(inst):
    if inst.data == "funcstate":
        print(inst.children)


def run_goonlang(program):
    parse_tree = parser.parse(program)
 
    for inst in parse_tree.children:
        run_instruction(inst)


run_goonlang(goonlang_code)
