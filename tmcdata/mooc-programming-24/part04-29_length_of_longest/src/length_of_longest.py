# Write your solution here

def length_of_longest(lst: list):
	max = 0
	for item in lst:
		if len(item) > max:
			max = len(item)
	return (max)

if __name__ == "__main__":
	my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
	result = length_of_longest(my_list)
	print(result)
	my_list = ["first", "second", "fourth", "eleventh"]
	result = length_of_longest(my_list)
	print(result)