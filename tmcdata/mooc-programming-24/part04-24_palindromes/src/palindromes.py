# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(s):
	for i in range(len(s)):
		if s[i] != s[- 1 - i]:
			return False
	return True

while True:
	s = input("Please type in a palindrome: ")
	if palindromes(s) == True:
		print(f"{s} is a palindrome!")
		break
	else:
		print("that wasn't a palindrome")