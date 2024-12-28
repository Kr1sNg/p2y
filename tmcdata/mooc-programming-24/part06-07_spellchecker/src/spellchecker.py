# write your solution here

dictionary = []
with open("wordlist.txt") as file:
	for word in file:
		word = word.replace("\n", "")
		dictionary.append(word)

text = input("Write text: ")
words = text.split(" ")
for i in words:
	if not i.lower() in dictionary:
		print(f"*{i}*", end = " ")
	else:
		print(i, end = " ")
print()