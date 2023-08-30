import pprint
from pieces import Pawn, Rook, Knight, Bishop, Queen, King 
from board import Board

def setup_board(board):
	''' This function creates the pieces and places them onto the board ready for the beginning of the game.

	Args: 
	board (Board): The game board.  

	Returns:
	board (Board): The game board.
	'''
	for row in range(8):
		for col in range(8):
			if row == 0:
				if col == 0 or col == 7:
					del board[(row, col)]
					board[(row, col)] = Rook("b")
				elif col == 1 or col == 6:
					del board[(row, col)]
					board[(row, col)] = Knight("b")
				elif col == 2 or col == 5:
					del board[(row, col)]
					board[(row, col)] = Bishop("b")
				elif col == 3:
					del board[(row, col)]
					board[(row, col)] = Queen("b")
				else:
					del board[(row, col)]
					board[(row, col)] = King("b")
			elif row == 1:
				del board[(row, col)]
				board[(row, col)] = Pawn("b")
			elif row == 6:
				del board[(row, col)]
				board[(row, col)] = Pawn("w")
			elif row == 7:
				if col == 0 or col == 7:
					del board[(row, col)]
					board[(row, col)] = Rook("b")
				elif col == 1 or col == 6:
					del board[(row, col)]
					board[(row, col)] = Knight("b")
				elif col == 2 or col == 5:
					del board[(row, col)]
					board[(row, col)] = Bishop("b")
				elif col == 3:
					del board[(row, col)]
					board[(row, col)] = Queen("b")
				else:
					del board[(row, col)]

board = Board()

pprint.pp(board)