# Write your solution here
# def distinct_numbers(lst: list):
# 	new = []
# 	for i in lst:
# 		if new.count(i) == 0:
# 			new.append(i)
# 	return (sorted(new))

def distinct_numbers(lst: list):
	new = []
	for item in lst:
		if item not in new:
			new.append(item)
	new.sort()
	return (new)

if __name__ == "__main__":
	my_list = [3, 2, 1, 3, 2, 1, 3, 2, 1]
	print(distinct_numbers(my_list))
			