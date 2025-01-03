# Write your solution here
from string import ascii_lowercase, digits
from random import choice, shuffle

def generate_strong_password(length: int, number: bool, punc: bool) -> str:
	char_punc = '!?=+-()#'
	char_pool = ascii_lowercase
	password = ""
	index = list(range(length))
	shuffle(index)
	i = 0
	if length < 3:
		while i < length:
			password += char_pool
			i += 1
	while i < length:
		if i == index[0]:
			password += choice(ascii_lowercase)
			i += 1
		elif i == index[1] and number:
			password += choice(digits)
			i += 1
		elif i == index[2] and punc:
			password += choice(char_punc)
			i += 1
		else:
			if number:
				char_pool += digits
			if punc:
				char_pool += char_punc
			password += choice(char_pool)
			i += 1
	return (password)

if __name__ == "__main__":
	for i in range(10):
		print(generate_strong_password(8, True, True))
