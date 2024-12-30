# Write your solution here
def everything_reversed(lst: list):
	new_lst = []
	for itm in lst:
		rev = itm[::-1]
		new_lst.append(rev)
	new_lst.reverse()
	return (new_lst)

if __name__ == "__main__":
	my_list = ["Hi", "there", "example", "one more"]
	new_list = everything_reversed(my_list)
	print(new_list)