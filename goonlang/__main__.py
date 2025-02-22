import goonlang
import sys
import os

importer = goonlang.Importer()

try:
    goonlang_code = importer.read_goonfile(str(sys.argv[1]))
except IndexError:
    print("blud aint add a file")
    exit()

parser = goonlang.Parser(goonlang_code, os.path.join(os.path.abspath(os.path.dirname(__file__)), "grammar/goonlang.lark"))

runner = goonlang.Runner(parser)

# print(parser.code.pretty())
# print(runner.transform(parser.code))
runner.run(parser.code)