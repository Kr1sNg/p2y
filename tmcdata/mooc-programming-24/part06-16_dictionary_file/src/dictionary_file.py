# Write your solution here
while True:
	print("1 - Add word, 2 - Search, 3 - Quit")
	cmd = int(input("Fuction: "))
	if cmd == 3:
		print("Bye!")
		break
	elif cmd == 1:
		finn = input("The word in Finnish: ")
		eng = input("The word in English: ")
		with open("dictionary.txt", "a") as file:
			file.write(f"{finn} - {eng}\n")
		print("Dictionary entry added")
	elif cmd == 2:
		search = input("Search term: ")
		with open("dictionary.txt") as readfile:
			for line in readfile:
				if search in line:
					print(line.strip())
