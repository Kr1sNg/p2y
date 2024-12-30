# Write your solution here
def print_sudoku(sudoku: list):
	for row in sudoku[:3]:
		copy = row[:]
		for i in range(len(row)):
			if row[i] == 0:
				copy[i] = "_"
		print(f"{copy[0]} {copy[1]} {copy[2]}  {copy[3]} {copy[4]} {copy[5]}  {copy[6]} {copy[7]} {copy[8]}")
	print()
	for row in sudoku[3:6]:
		copy = row[:]
		for i in range(len(row)):
			if row[i] == 0:
				copy[i] = "_"
		print(f"{copy[0]} {copy[1]} {copy[2]}  {copy[3]} {copy[4]} {copy[5]}  {copy[6]} {copy[7]} {copy[8]}")
	print()
	for row in sudoku[6:]:
		copy = row[:]
		for i in range(len(row)):
			if row[i] == 0:
				copy[i] = "_"
		print(f"{copy[0]} {copy[1]} {copy[2]}  {copy[3]} {copy[4]} {copy[5]}  {copy[6]} {copy[7]} {copy[8]}")

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
	sudoku[row_no][column_no] = number

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

	print_sudoku(sudoku)
	add_number(sudoku, 0, 0, 2)
	add_number(sudoku, 1, 2, 7)
	add_number(sudoku, 5, 7, 3)
	print()
	print("Three numbers added:")
	print()
	print_sudoku(sudoku)