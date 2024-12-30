# Write your solution here
def no_vowels(s: str):
	vowel = "ueoai"
	new = ""
	for c in s:
		if c not in vowel:
			new += c
	return (new)

if __name__ == "__main__":
	my_string = "this is an example"
	print(no_vowels(my_string))