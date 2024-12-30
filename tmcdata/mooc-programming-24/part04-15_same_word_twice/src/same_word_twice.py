# Write your solution here
i = 0
lst = []

while True:
	w = input("Word: ")
	if w in lst:
		print(f"You typed in {len(lst)} different words")
		break
	else:
		lst.append(w)
