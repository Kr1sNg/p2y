# WRITE YOUR SOLUTION HERE:

def begin_with_vowel(words: list):
	return [w for w in words if w[0].lower() in "ueoai"]

if __name__ == "__main__":
	word_list = ["automobile","motorbike","Animal","cat","Dog","APPLE","orange"]
	for vowelled in begin_with_vowel(word_list):
		print(vowelled)