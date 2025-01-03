# Write your solution here
from random import randint
from string import ascii_lowercase

def generate_password(length: int) -> str:
	password = ""
	i = 0
	while i < length:
		index = randint(0, 25)
		password += ascii_lowercase[index]
		i += 1
	return password

if __name__ == "__main__":
	for i in range(10):
		print(generate_password(8))

