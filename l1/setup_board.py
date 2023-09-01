''' This file contains the Board class definition and the SetupBoard function'''
from l3.pieces import Pawn, Rook, Knight, Bishop, Queen, King
from l3.movement_rules_vec_def import Vector
from l2.board import Board  

def SetupBoard():
	''' This function creates the board and pieces.  
		It places the pieces on the board ready for the beginning of the game.

	Args: 
	board (Board): The game board.  

	Returns:
	board (Board): The game board.
	'''
	board = Board()

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