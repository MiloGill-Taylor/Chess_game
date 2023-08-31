import pprint
from pieces import Pawn, Rook, Knight, Bishop, Queen, King 
from board import Board, Vector, MOVE_VECT_DICT
from generate_moves import calculate_all_moves


def setup_board(board):
	''' This function creates the pieces and places them onto the board ready for the beginning of the game.

	Args: 
	board (Board): The game board.  

	Returns:
	board (Board): The game board.
	'''
	for row in range(8):
		for col in range(8):
			vec = Vector([row, col])
			if row == 0:
				if col == 0 or col == 7:
					del board[vec]
					board[vec] = Rook("b")
				elif col == 1 or col == 6:
					del board[vec]
					board[vec] = Knight("b")
				elif col == 2 or col == 5:
					del board[vec]
					board[vec] = Bishop("b")
				elif col == 3:
					del board[vec]
					board[vec] = Queen("b")
				else:
					del board[vec]
					board[vec] = King("b")
			elif row == 1:
				del board[vec]
				board[vec] = Pawn("b")
			elif row == 6:
				del board[vec]
				board[vec] = Pawn("w")
			elif row == 7:
				if col == 0 or col == 7:
					del board[vec]
					board[vec] = Rook("w")
				elif col == 1 or col == 6:
					del board[vec]
					board[vec] = Knight("w")
				elif col == 2 or col == 5:
					del board[vec]
					board[vec] = Bishop("w")
				elif col == 3:
					del board[vec]
					board[vec] = Queen("w")
				else:
					del board[vec]
					board[vec] = King("w")
			else:
				del board[vec]
				board[vec] = None
	return board

board = Board()

board = setup_board(board)

moves = calculate_all_moves(board, 'w', MOVE_VECT_DICT)







