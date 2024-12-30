# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
	if (piece == "X" or piece == "O") and (x in range(0, 3)) and (y in range(0, 3)):
		if game_board[y][x] == "":
			game_board[y][x] = str(piece)
			return True
		else:
			return False
	else:
		return False

if __name__ == "__main__":
	game_board = [['', '', 'O'], ['X', '', ''], ['', 'O', '']]
	print(play_turn(game_board, 1, 1, "O"))
	print(game_board)

