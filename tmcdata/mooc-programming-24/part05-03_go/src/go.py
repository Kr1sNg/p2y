# Write your solution here
def who_won(game_board: list) -> int:
	first = 0
	second = 0
	for i in range(len(game_board)):
		for j in range(len(game_board[i])):
			if game_board[i][j] == 1:
				first += 1
			elif game_board[i][j] == 2:
				second += 1
	if first > second:
		return (1)
	elif first < second:
		return (2)
	else:
		return (0)

if __name__ == "__main__":
	board = [[1, 2, 1], [2, 1, 0], [0, 0, 0]]
	print(who_won(board))