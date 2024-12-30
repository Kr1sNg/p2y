# Write your solution here
def transpose(matrix: list):
	leng = len(matrix)
	i = 0
	while (i < leng):
		j = i + 1
		while (j < leng):
			tmp = matrix[i][j]
			matrix[i][j] = matrix[j][i]
			matrix[j][i] = tmp
			j += 1
		i += 1

if __name__ == "__main__":
	matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	print(matrix)
	print ()
	transpose(matrix)
	print(matrix)