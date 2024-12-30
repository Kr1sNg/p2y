# Write your solution here

list = [1, 2, 3, 4, 5]

while True:
	i = int(input("Index: "))
	if (i <= -1 or i > 4):
		break
	list[i] = int(input("New value: "))
	print(list)
