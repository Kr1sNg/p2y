# Write your solution here
def anagrams(s1, s2):
	if len(s1) != len(s2):
		return False
	else:
		for i in s1:
			if i in s2:
				return True
			else:
				return False
			
if __name__ == "__main__":
	print(anagrams("tame", "meta"))
	print(anagrams("tame", "mate"))
	print(anagrams("tame", "team"))
	print(anagrams("tabby", "batty"))
	print(anagrams("python", "java"))