# Write your solution here
def ft_week_check(str) -> bool:
	try:
		elem = str.split(" ")
		if elem[0] != "week":
			return False
		if int(elem[1]) not in range(55):
			return False
		return True
	except:
		return False

def ft_nbr_check(string) -> bool:
	try:
		elems = string.split(",")
		if len(elems) != 7:
			return False
		for i in elems:
			if int(i) not in range(1, 40):
				return False
			if elems.count(i) > 1:
				return False
		return True
	except:
		return False

def ft_correct(filename) -> list:
	correct_list = []
	with open(filename) as readfile:
		for line in readfile:
			row = (line.strip()).split(";")
			if ft_week_check(row[0]) and ft_nbr_check(row[1]):
				correct_list.append(line)
	return correct_list
				
def filter_incorrect():
	correct_list = ft_correct("lottery_numbers.csv")
	with open("correct_numbers.csv", "w") as writtenfile:
		for line in correct_list:
			writtenfile.write(line)


