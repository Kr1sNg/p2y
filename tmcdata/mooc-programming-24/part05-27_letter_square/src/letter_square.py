# Write your solution here
def print_letter_square(layers: int):
	if layers < 1 and layers > 26:
		print("Number of layers must be between 1 and 26")
		return
	size = 2 * layers - 1
	square = []
	for i in range(size):
		row = []
		for j in range(size):
			distance = min(i, j, size - i - 1, size - j - 1)
			row.append(chr(65 + layers - 1 - distance))
		square.append(''.join(row))
	for line in square:
		print(line)

layers = int(input("Layers: "))
print_letter_square(layers)