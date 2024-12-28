# write your solution here
def ft_matrix():
	with open("matrix.txt") as file:
		matrix = []
		for line in file:
			line = line.replace("\n", "")
			numbers = line.split(",")
			matrix.append(numbers)
	return (matrix)

def matrix_sum():
	matrix = ft_matrix()
	sum = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			sum += int(matrix[i][j])
	return (sum)

def matrix_max():
	matrix = ft_matrix()
	max = int(matrix[0][0])
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if int(matrix[i][j]) > max:
				max = int(matrix[i][j])
	return (max)
		
def row_sums():
	matrix = ft_matrix()
	sum_rows = []
	for i in range(len(matrix)):
		sm = 0
		for j in range(len(matrix)):
			sm += int(matrix[i][j])
		sum_rows.append(sm)
	return (sum_rows)

if __name__ == "__main__":
	sum = matrix_sum()
	print(sum)
	max = matrix_max()
	print(max)
	sum_rows = row_sums()
	print(sum_rows)