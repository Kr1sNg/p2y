# Write your solution here
def no_shouting(lst: list):
	new_lst = []
	for s in lst:
		if not s.isupper():
			new_lst.append(s)
	return (new_lst)

if __name__ == "__main__":
	my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
	pruned_list = no_shouting(my_list)
	print(pruned_list)