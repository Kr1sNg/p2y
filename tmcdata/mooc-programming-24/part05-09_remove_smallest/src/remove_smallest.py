# Write your solution here
def remove_smallest(numbers: list):
	i = 0
	min = numbers[0]
	while i + 1 < len(numbers):
		if numbers[i] > numbers[i + 1]:
			min = numbers[i + 1]
		i += 1
	numbers.remove(min)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)
