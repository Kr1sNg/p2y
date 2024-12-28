# Write your solution here

def dict_of_numbers():
	numbers = {}
	un = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	ze = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
	de = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
	numbers[0] = 'zero'
	for i in range(1, 10):
		numbers[i] = un[i - 1]
	for i in range(10, 20):
		numbers[i] = ze[i - 10]
	for i in range(20, 100, 10):
		numbers[i] = de[int((i / 10) - 2)]
	for i in range(2, 10):
		for j in range (1, 10):
			numbers[i * 10 + j] = de[i - 2] + '-' + un[j - 1]
	return (numbers)

if __name__ == "__main__":
	numbers = dict_of_numbers()
	print(numbers[2])
	print(numbers[11])
	print(numbers[45])
	print(numbers[99])
	print(numbers[0])
