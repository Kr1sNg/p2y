# Write your solution here

new = ""
str = ""
while True:
	a = input("Please type in a word: ")
	if a == new or a == "end":
		break
	new = a
	str += new + " "

print(str)