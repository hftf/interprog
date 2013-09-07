class Program:
    def __init__(self, functions=None, global_scope=None, main_func=None):
        if functions is None:
            self.functions = []
        if global_scope is None:
            self.global_scope = Scope()
        if main_func is None:
            self.main_func = Function()

class Function:
    def __init__(self, block=None):
        if block is None:
            self.block = Block()

class Block:
    def __init__(self, scope=None, instructions=None):
        if scope is None:
            self.scope = Scope()
        if instructions is None:
            self.instructions = []

class Scope:
    def __init__(self, variables=None):
        if variables is None:
            variables = {}

class Variable:
    def __init__(self, name):
        self.name = name

class Instruction:
    def __init__(self):
        pass
