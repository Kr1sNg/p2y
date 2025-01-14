# Write your solution to exercise 2 here

def find_allowed(strings: list, nbr: int) -> list:
	src = "aeiouy"
	new_list = []
	for word in strings:
		count = 0
		for char in word:
			if char in src:
				count += 1
		if count >= nbr:
			new_list.append(word)
	return new_list

if __name__ == "__main__":
	wordlist = ["apple", "banana", "cherry", "orange", "peach", "pineapple"]
	minimum = 2
	result = find_allowed(wordlist, minimum)
	print(result)
			