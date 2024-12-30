# Write your solution here
def even_numbers(lst : list):
	new = []
	for i in lst:
		if (i % 2 == 0):
			new.append(i)
	return (new)

if __name__ == "__main__":
	my_list = [1, 2, 3, 4, 5]
	new_list = even_numbers(my_list)
	print("orignnal", my_list)
	print("new", new_list)