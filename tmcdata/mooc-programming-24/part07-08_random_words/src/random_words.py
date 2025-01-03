# Write your solution here
from random import shuffle

def words(n: int, beginning: str) -> list:
	list_pool = []
	with open("words.txt") as file:
		for word in file:
			word = word.strip()
			if word.startswith(beginning):
				list_pool.append(word)
	shuffle(list_pool)
	if n <= len(list_pool):
		word_list = list_pool[0:n]
		return word_list
	else:
		raise ValueError

if __name__ == "__main__":
	word_list = words(3, "catwalk")
	for word in word_list:
		print(word)