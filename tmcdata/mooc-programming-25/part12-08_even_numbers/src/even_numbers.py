# Write your solution here
def even_numbers(beginning: int, maximum: int):
	i = beginning
	while i <= maximum:
		if i % 2 == 0:
			yield i
		i += 1

if __name__ == "__main__":
	numbers = even_numbers(11, 21)
	for number in numbers:
		print(number)