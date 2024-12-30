# Write your solution here
def shortest(lst: list):
	short = lst[0]
	for item in lst:
		if len(short) > len(item):
			short = item
	return (short)

if __name__ == "__main__":
	my_list = ["first", "second", "fourth", "eleventh"]

	result = shortest(my_list)
	print(result)

	my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

	result = shortest(my_list)
	print(result)