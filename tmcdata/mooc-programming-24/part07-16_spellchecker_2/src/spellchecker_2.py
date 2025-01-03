# Write your solution here
from difflib import get_close_matches
import keyword

dictionary = []
with open("wordlist.txt") as file:
	for word in file:
		word = word.replace("\n", "")
		dictionary.append(word)

text = input("Write text: ")
words = text.split(" ")
faux = []
for i in words:
	if not i.lower() in dictionary:
		faux.append(i)
		print(f"*{i}*", end = " ")
	else:
		print(i, end = " ")
print()
print("suggestion:")
for i in faux:
	suggests = get_close_matches(i, dictionary)
	forprint = ', '.join(suggests)
	print(f"{i}: {forprint}")

