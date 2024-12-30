# Write your solution here
def ft_search(word: str, search_term: str) -> bool:
	if "." in search_term and len(word) == len(search_term):
		for i in range(len(search_term)):
			if search_term[i] == ".":
				pass
			elif search_term[i] != word[i]:
				return False
		return True
	elif search_term.startswith("*"):
		if word.endswith(search_term[1:]):
			return True
		else:
			return False
	elif search_term.endswith("*"):
		if word.startswith(search_term[:-1]):
			return True
		else:
			return False
	else:
		if len(word) != len(search_term):
			return False
		for i in range(len(search_term)):
			if search_term[i] != word[i]:
				return False
		return True

def find_words(search_term: str) -> list:
	found_list = []
	with open("words.txt") as file:
		for line in file:
			word = line.strip()
			if ft_search(word, search_term):
				found_list.append(word)
	return (found_list)

# def main():
# 	print(find_words("convoke"))

# main()
			