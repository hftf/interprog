def write_program(program):
    return {
        'type': 'program',
        'functions': [write_function(i) for i in program.functions],
        'global_scope': write_scope(program.global_scope),
        'main_func': write_function(program.main_func)
    }

def write_function(function):
    return {
        'type': 'function',
        'block': function.block
    }

def write_block(block):
    return {
        'type': 'block',
        'scope': write_scope(block.scope),
        'instructions': [write_instruction(i) for i in block.instructions]
    }

def write_scope(scope):
    return {
        'type': 'scope',
        'variables': [write_variable(i) for i in scope.variables]
    }

def write_variable(variable):
    return {
        'type': 'variable',
        'name': variable.name
    }

def write_assignment(assignment):
    return {
        'type': 'assignment',
        'lhs': assignment.lhs,
        'rhs': assignment.rhs
    }

def write_expression(expression):
    return {
        'type': 'expression',
        'expr': expression.expr
    }

def write_return(return):
    return {
        'type': 'return',
        'var': return.var
    }
