# Write your solution here
while True:
	print("1 - add an entry, 2 - read entries, 0 - quit")
	cmd = int(input("Functions: "))
	if cmd == 0:
		print("Bye now!\n")
		break
	elif cmd == 1:
		entry = input("Diary entry: ")
		with open("diary.txt", "a") as my_file:
			my_file.write(entry + "\n")
		print("Diary saved")
	elif cmd == 2:
		with open("diary.txt") as my_file:
			print("Entries: ")
			for line in my_file:
				line = line.replace("\n", "")
				print(line)
