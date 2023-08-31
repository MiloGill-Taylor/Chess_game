''' This file contains the Board class definition and the SetupBoard function'''
from l2.pieces import Pawn, Rook, Knight, Bishop, Queen, King
from l2.movement_rules_vec_def import Vector 

class Board(dict):
	def __init__(self):
		''' Creates an empy board.  The keys are the vectors to the square.  '''
		for row in range(8):
			for col in range(8):
				vec = Vector([row, col])
				self[vec] = None

	def is_piece(self, position):
		''' Return True if there is a piece at $position on the board.  
			If the position is not on the board raise exception.  

		Args: 
		position (Vector): Position vector that is being checked. 

		Returns:
		boolean expression.  True if there is a piece at $position.
		'''
		if position[0] not in range(8) or position[1] not in range(8):
			raise PositionNotOnBoard
		return self[position] is not None

	def is_on_board(self, position):
		''' Return True if the $position exists on the board. '''
		if position[0] in range(8) and position[1] in range(8):
			return True
		else:
			return False

class PositionNotOnBoard(Exception):
	def __init__(self):
		super().__init__("PositionNotOnBoard: A Board method was passed a position not on the chess board.")

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