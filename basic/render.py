from nexus import *

def from_nexus(program, filename):

	functions = program.functions
	global_scope = program.global_scope

	text = 'PROGRAM {0}\n'.format(filename)

	# program instructions

	text += 'END\n\n'

	for name, func in functions.iteritems():
		params = ', '.join(func.params)
		text += 'SUB {0}({1})\n'.format(name, params)
		for line in func.block.instructions:
			if line.__class__ == Assignment:
				text += '\n'.format()
			elif line.__class__ == Expression:
				text += '\n'.format()
			elif line.__class__ == Return:
				text += '\n'.format()
		text += 'SUB END\n'

	return text