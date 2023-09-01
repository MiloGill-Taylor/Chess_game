''' This file defines the board class and board functions'''
from l3.movement_rules_vec_def import Vector 

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

	def is_empty(self, position):
		''' Return True if there is no piece at $position on the board.  
			If the position is not on the board raise exception.  

		Args: 
		position (Vector): Position vector that is being checked. 

		Returns:
		boolean expression.  True if there is no piece at $position.
		'''
		if position[0] not in range(8) or position[1] not in range(8):
			raise PositionNotOnBoard
		return self[position] is None

	def different_colour(self, position1, position2):
		'''Return true if the pieces at $position1 and $position2 are different colour.  
			Should not be called by main.

		Args:
		board (Board): The board the game is being played on. 
		position1 (Vector): Position of one of the pieces.
		position2 (Vector): Position of one of the pieces.

		Returns:
		(bool): True if the are different colour
		'''
		return self[position1].colour != self[position2].colour

	def is_on_board(self, position):
		''' Return True if the $position exists on the board. '''
		if position[0] in range(8) and position[1] in range(8):
			return True
		else:
			return False

class PositionNotOnBoard(Exception):
	def __init__(self):
		super().__init__("PositionNotOnBoard: A Board method was passed a position not on the chess board.")
