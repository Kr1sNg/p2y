# Write your solution here
import string

def run(program: list):
	variables = {}
	for var in string.ascii_uppercase:
		variables[var] = 0
	result = []
	for line in program:
		if line == "END":
			break	
		elif "PRINT" in line:
			var = line[6:]
			if var in string.ascii_uppercase:
				result.append(variables[var])
			else:
				result.append(int(var))
		elif "MOV" in line:
			nbr = line[6:]
			if nbr in string.ascii_uppercase:
				variables[line[4]] = variables[line[6]]
			else:
				variables[line[4]] = int(line[6:])
		elif "ADD" in line:
			nbr = line[6:]
			if nbr in string.ascii_uppercase:
				variables[line[4]] += variables[line[6]]
			else:
				variables[line[4]] += int(line[6:])
		elif "SUB" in line:
			nbr = line[6:]
			if nbr in string.ascii_uppercase:
				variables[line[4]] -= variables[line[6]]
			else:
				variables[line[4]] -= int(line[6:])
		elif "MUL" in line:
			nbr = line[6:]
			if nbr in string.ascii_uppercase:
				variables[line[4]] *= variables[line[6]]
			else:
				variables[line[4]] *= int(line[6:])

	return result
		
		

if __name__ == "__main__":
	program1 = []
	program1.append("MOV A 1")
	program1.append("MOV B 2")
	program1.append("PRINT A")
	program1.append("PRINT B")
	program1.append("ADD A B")
	program1.append("PRINT A")
	program1.append("END")
	result = run(program1)
	print(result)
