from json_transformer import *

def main():
	with open("prog.json", "r") as file:
		program = file.read()
	print write_program(read_program(program))
	print write_program(read_program(write_program(read_program(program))))
	
if __name__ == '__main__':
	main()