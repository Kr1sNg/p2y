# Write your solution here
def print_sudoku(sudoku):
	r = 0
	for row in sudoku:
		s = 0
		for char in row:
			s += 1
			if char == 0:
				char = "_"
			m = f"{char} "
			if s % 3 == 0 and s < 8:
				m += " "
			print(m, end = "")
		print()
		r += 1
		if r % 3 == 0 and r < 8:
			print ()
		

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
	copy = []
	for i in range(len(sudoku)):
		copy_row = []
		for j in range(len(sudoku[i])):
			copy_row.append(sudoku[i][j])
		copy.append(copy_row)
	copy[row_no][column_no] = number
	return copy

if __name__ == "__main__":
	sudoku  = [
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0]
	]

	grid_copy = copy_and_add(sudoku, 0, 0, 2)
	print("Original:")
	print_sudoku(sudoku)
	print()
	print("Copy:")
	print_sudoku(grid_copy)