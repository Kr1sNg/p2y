# Write your solution here
def	ft_add(book: dict):
	name = input("name: ")
	if name in book:
		phone = input("number: ")
		if phone not in book[name]:
			(book[name]).append(phone)
	else:
		book[name] = []
		phone = input("number: ")
		(book[name]).append(phone)
	print("ok!")

def ft_search(book: dict):
	name = input("name: ")
	if name in book:
		for phone in book[name]:
			print(phone)
	else:
		print("no number")

def main():
	book = {}
	while True:
		cmd = int(input("command (1 search, 2 add, 3 quit): "))
		if cmd == 1:
			ft_search(book)
		elif cmd == 2:
			ft_add(book)
		elif cmd == 3:
			print("quitting...")
			break
		else:
			break
	return

main()
	



		
