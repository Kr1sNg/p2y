# Write your solution here
lst = {}
while True:
	cmd = int(input("command (1 search, 2 add, 3 quit): "))
	if cmd == 3:
		print("quitting...")
		break
	elif cmd == 1:
		name = input("name: ")
		if name in lst:
			print(lst[name])
		else:
			print("no number")
	elif cmd == 2:
		name = input("name: ")
		lst[name] = input("number: ")
		print("ok!")
	else:
		break
		
