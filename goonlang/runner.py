from lark import Lark, Transformer

class Runner(Transformer):
    def __init__(self, parser):
        self.parser = parser
        self.vars = {}

    def string(self, s):
        (s,) = s
        return s[1:-1]
    
    def function(self, func):
        if func[0] == "print":
            print(func[1])
        return func[0], func[1]
    
    def number(self, n):
        (n,) = n
        return n
    
    def declaration(self, dec):
        self.vars[dec[0]] = dec[1]
        return dec[1]
    
    def value(self, val):
        if val[0].data=="variable":
            return self.vars[val[0].children[0]]
        return val
    

    # entry point stuffsss
    def run(self, code):
        self.transform(code)



# old code, might need later
""" 
    def run(self):
        print(self.parser.code.pretty())
        for inst in self.parser.code.children:
            self.run_instruction(inst)

    def run_instruction(self, inst):
        if inst.data == "function":
            type, value = inst.children
            print(value)
"""
