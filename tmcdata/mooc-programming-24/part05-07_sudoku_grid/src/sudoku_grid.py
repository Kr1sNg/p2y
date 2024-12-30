# Write your solution here
def row_correct(sudoku: list, row_no: int) -> bool:
	checked = []
	for i in range(len(sudoku[row_no])):
		if sudoku[row_no][i] != 0:
			if sudoku[row_no][i] not in checked:
				checked.append(sudoku[row_no][i])
			else:
				return False
	return True

def column_correct(sudoku: list, column_no: int) -> bool:
	checked = []
	for row in sudoku:
		if row[column_no] != 0:
			if row[column_no] not in checked:
				checked.append(row[column_no])
			else:
				return False
	return True

def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
	checked = []
	for row in range(row_no, row_no + 3):
		for column in range(column_no, column_no + 3):
			if sudoku[row][column] != 0:
				if sudoku[row][column] not in checked:
					checked.append(sudoku[row][column])
				else:
					return False
	return True


def sudoku_grid_correct(sudoku: list) -> bool:
	for row in range(0, 9):
		if row_correct(sudoku, row) == False:
			return False
	for column in range(0, 9):
		if column_correct(sudoku, column) == False:
			return False
	begin_index = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
	for begin in begin_index:
		if block_correct(sudoku, begin[0], begin[1]) == False:
			return False
	return True

if __name__ == "__main__":
	sudoku1 = [
	[9, 0, 0, 0, 8, 0, 3, 0, 0],
	[2, 0, 0, 2, 5, 0, 7, 0, 0],
	[0, 2, 0, 3, 0, 0, 0, 0, 4],
	[2, 9, 4, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 7, 3, 0, 5, 6, 0],
	[7, 0, 5, 0, 6, 0, 4, 0, 0],
	[0, 0, 7, 8, 0, 3, 9, 0, 0],
	[0, 0, 1, 0, 0, 0, 0, 0, 3],
	[3, 0, 0, 0, 0, 0, 0, 0, 2]
	]

	print(sudoku_grid_correct(sudoku1))

	sudoku2 = [
	[2, 6, 7, 8, 3, 9, 5, 0, 4],
	[9, 0, 3, 5, 1, 0, 6, 0, 0],
	[0, 5, 1, 6, 0, 0, 8, 3, 9],
	[5, 1, 9, 0, 4, 6, 3, 2, 8],
	[8, 0, 2, 1, 0, 5, 7, 0, 6],
	[6, 7, 4, 3, 2, 0, 0, 0, 5],
	[0, 0, 0, 4, 5, 7, 2, 6, 3],
	[3, 2, 0, 0, 8, 0, 0, 5, 7],
	[7, 4, 5, 0, 0, 3, 9, 0, 1]
	]

	print(sudoku_grid_correct(sudoku2))
