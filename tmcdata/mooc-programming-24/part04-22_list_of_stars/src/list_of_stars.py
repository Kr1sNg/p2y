# Write your solution here
def list_of_stars(lst : list):
	for i in lst:
		print(i * "*")

if __name__ == "__main__":
	list_of_stars([3, 7, 1, 1, 2])