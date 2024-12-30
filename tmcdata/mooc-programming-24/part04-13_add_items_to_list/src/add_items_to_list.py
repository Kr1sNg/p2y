# Write your solution here

len = int(input("How many itmes: "))
i = 1
list = []
while (i <= len):
	list.append(int(input(f"Item {i}: ")))
	i += 1

print(list)