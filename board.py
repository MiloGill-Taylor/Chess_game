'''This file contains the board class definition'''


# TODO: 
class Board(dict):
	def __init__(self):
		for row in range(8):
			for col in range(8):
				self[(row, col)] = None

	def is_piece(self, position):
		''' Return True if there is a position on the board.  If the position is not on the board raise exception.  

		Args: 
		position (tuple): Position tuple that is being checked. 

		Returns:
		boolean expression.
		'''
		if position[0] not in range(9) or position[1] not in range(9):
			raise PositionNotOnBoard
		return self[position] is not None

class PositionNotOnBoard(Exception):
	def __init__(self):
		super().__init__("PositionNotOnBoard: A Board method was passed a position not on the chess board.")










