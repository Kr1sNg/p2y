# Write your solution here
def longest_series_of_neighbours(lst: list):
	length = []
	for itm in lst:
		length.append(1)
	i = 0	
	while i < len(lst) - 1:
		if (lst[i + 1] == lst[i] + 1 or lst[i + 1] == lst[i] - 1):
			length[i + 1] = length[i] + 1
		i += 1
	maxl = max(length)
	return (maxl)

if __name__ == "__main__":
	my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
	print(longest_series_of_neighbours(my_list))	