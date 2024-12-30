# Write your solution here
def read_input(string: str, min: int, max: int) -> int:
	while True:
		try:
			number = int(input(string))
			if number in range(min, max + 1):
				return number
			else:
				print(f"You must type in an integer between {min} and {max}")
		except ValueError:
			print(f"You must type in an integer between {min} and {max}")

# number = read_input("Please type in a number: ", 5, 10)
# print("You typed in:", number)
		
