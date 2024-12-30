# Write your solution here
lst = []
i = 0

print(f"The list is now {lst}")

while True:
	cmd = input("a(d)d, (r)emove or e(x)it: ")
	if cmd == "x":
		print("Bye!")
		break
	if cmd == "d":
		i += 1
		lst.append(i)
		print(f"The list is now {lst}")
	if (i > 0 and cmd == "r"):
		lst.remove(i)
		print(f"The list is now {lst}")
		i -= 1
