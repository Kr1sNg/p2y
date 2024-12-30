# Write your solution here
def max(lst: list):
	max = 0
	for itm in lst:
		if len(itm) > max:
			max = len(itm)
	return (max)

def all_the_longest(lst: list):
	leng = max(lst)
	result = []
	for itm in lst:
		if len(itm) == leng:
			result.append(itm)
	return (result)

if __name__ == "__main__":
	my_list = ["first", "second", "fourth", "eleventh"]

	result = all_the_longest(my_list)
	print(result) # ['eleventh']

	my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

	result = all_the_longest(my_list)
	print(result) # ['dorothy', 'richard']