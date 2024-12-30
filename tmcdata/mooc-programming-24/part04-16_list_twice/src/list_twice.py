# Write your solution here

lst = []

while True:
	x = int(input("New item: "))
	if (x != 0):
		lst.append(x)
		print(f"The list now: {lst}")
		print(f"The list in order: {sorted(lst)}")
	else:
		print("Bye!")
		break