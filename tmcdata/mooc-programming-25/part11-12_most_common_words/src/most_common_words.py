# WRITE YOUR SOLUTION HERE:
<<<<<<< HEAD

# def most_common_words(filename: str, lower_limit: int):
# 	new = {}
# 	with open(filename) as file:
# 		read = file.read().replace('\n', ' ')
# 		for word in read.split(' '):
# 			word = word.strip(".,:")
# 			if word not in new:
# 				new[word] = 1
# 			else:
# 				new[word] += 1
# 			print(word, new[word])
# 	return {n : new[n] for n in new if new[n] >= lower_limit} 

from string import punctuation

def most_common_words(filename: str, lower_limit: int):
	with open(filename) as f:
		content = f.read()
		content = content.replace('\n', ' ')
		for mark in punctuation:
			content = content.replace(mark, '')
		words = content.split(' ')
		return {w: words.count(w) for w in words if words.count(w) >= lower_limit}

if __name__ == "__main__":
	print(most_common_words("comprehensions.txt", 3))
		
		
=======
>>>>>>> 3e7d1c54b079a3a498cf03351408be9bb4035f1c
