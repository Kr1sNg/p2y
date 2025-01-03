# Write your solution here
import string
def separate_characters(my_string: str):
	ascii_let = ""
	punc_let = ""
	other_let = ""
	for char in my_string:
		if char in string.ascii_letters:
			ascii_let += char
		elif char in string.punctuation:
			punc_let += char
		else:
			other_let += char
	return (ascii_let, punc_let, other_let)

if __name__ == "__main__":
	parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
	print(parts[0])
	print(parts[1])
	print(parts[2])
