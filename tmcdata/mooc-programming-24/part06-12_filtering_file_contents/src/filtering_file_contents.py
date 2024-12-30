# Write your solution here
def filter_solutions():
	with open("correct.csv", "w"):
		pass
	with open("incorrect.csv", "w"):
		pass
	with open("solutions.csv") as readfile:
		for line in readfile:
			# line = line.replace("\n", "")
			row = line.split(";")
			if ft_check(row[1], int(row[2])):
				ft_write("correct.csv", line)
			else:
				ft_write("incorrect.csv", line)

def ft_check(s1: str, i: int) -> bool:
	if "+" in s1:
		elems = s1.split("+")
		if (int(elems[0]) + int(elems[1]) == i):
			return True
		else:
			return False
	elif "-" in s1:
		elems = s1.split("-")
		if (int(elems[0]) - int(elems[1]) == i):
			return True
		else:
			return False

def ft_write(filename: str, line: str):
	with open(filename, "a") as writenfile:
		writenfile.write(line + '\n')

# def main():
# 	filter_solutions()

# main()