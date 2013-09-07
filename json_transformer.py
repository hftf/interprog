from nexus import *
import json

def read_program(json_):
    program = json.loads(json_)
    return Program(
        [read_function(i) for i in program['functions']],
        read_scope(program['global_scope']),
        read_function(program['main_func'])
    )

def read_function(function):
    return Function(
        read_block(function['block']),
        [read_param(i) for i in function['params']]
    )

def read_param(param):
    return param

def read_block(block):
    return Block(
        read_scope(block['scope']),
        [read_instruction(i) for i in block['instructions']]
    )

def read_scope(scope):
    return Scope(
        [read_variable(i) for i in scope['variables']]
    )

def read_variable(variable):
    return Variable(variable['name'])

def read_instruction(instruction):
    return {
        'assignment': read_assignment,
        'expression': read_expression,
        'return': read_return
    }[instruction['type']](instruction)

def read_assignment(assignment):
    return Assignment(assignment['lhs'], assignment['rhs'])

def read_expression(expression):
    return Expression(expression['expression'])

def read_return(return_):
    return Return(return_['var'])


def write_program(program):
    return json.dumps({
        'type': 'program',
        'functions': [write_function(i) for i in program.functions],
        'global_scope': write_scope(program.global_scope),
        'main_func': write_function(program.main_func)
    })

def write_function(function):
    return {
        'type': 'function',
        'block': write_block(function.block),
        'params': [write_param(i) for i in function.params]
    }

def write_param(param):
    return param

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

def write_instruction(instruction):
    return {
        'Assignment': write_assignment,
        'Expression': write_expression,
        'Return': write_return
    }[instruction.__class__.__name__](instruction)

def write_assignment(assignment):
    return {
        'type': 'assignment',
        'lhs': assignment.lhs,
        'rhs': assignment.rhs
    }

def write_expression(expression):
    return {
        'type': 'expression',
        'expression': expression.expression
    }

def write_return(return_):
    return {
        'type': 'return',
        'var': return_.var
    }
