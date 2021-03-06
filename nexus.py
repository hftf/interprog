class Program:
    def __init__(self, functions=None, global_scope=None, main_func=None):
        if functions is None:
            self.functions = {}
        else:
            self.functions = functions
        if global_scope is None:
            self.global_scope = Scope()
        else:
            self.global_scope = global_scope
        if main_func is None:
            self.main_func = Function()
        else:
            self.main_func = main_func

class Function:
    def __init__(self, block, params):
        self.block = block
        self.params = params

class Block:
    def __init__(self, scope, instructions):
        self.scope = scope
        self.instructions = instructions

class Scope:
    def __init__(self, variables=None):
        if variables is None:
            variables = {}
        self.variables = variables

class Variable:
    def __init__(self, name):
        self.name = name

class Assignment:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

class Expression:
    def __init__(self, expr):
        self.expression = expr

class Return:
    def __init__(self, var):
        self.var = var

class If:
    def __init__(self, name, expr, block):
        self.name = name # name is if, elseif, or else
        self.expression = expr # None if name is else
        self.block = block 

class While:
    def __init__(self, expr, block):
        self.expression = expr
        self.block = block

class For:
    def __init__(self, expr, block):
        self.expression = expr
        self.block = block


