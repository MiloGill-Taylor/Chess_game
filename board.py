'''This file contains the board class and vector class definition'''

class Board(dict):
	def __init__(self):
		''' Creates an empy board.  The keys are the vectors to the square.  '''
		for row in range(8):
			for col in range(8):
				vec = Vector([row, col])
				self[vec] = None

	def is_piece(self, position):
		''' Return True if there is a piece at $position on the board.  If the position is not on the board raise exception.  

		Args: 
		position (numpy array): Position vector that is being checked. 

		Returns:
		boolean expression.
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

class Vector(tuple):
	def __init__(self, iterable):
		if len(self) != 2:
			raise VectorDimensionIncorrect

	def add(self, vector):
		''' Peform vector addition with $self and $vector.  Return a new Vector object.  

		Args:
		vector (Vector):  The vector being added to $self.

		Returns:
		(Vector): Result of vector addition.
		'''
		first_element = self[0] + vector[0]
		second_element = self[1] + vector[1]
		return Vector([first_element, second_element])
	
class VectorDimensionIncorrect(Exception):
	def __init__(self):
		super().__init__("VectorDimensionIncorrect: An attempt to make a Vector object with dimension not 2 was made.")


class PositionNotOnBoard(Exception):
	def __init__(self):
		super().__init__("PositionNotOnBoard: A Board method was passed a position not on the chess board.")

ROOK_MOVE_VECTORS = {Vector([1,0]), Vector([-1,0]), Vector([0,1]), Vector([0,-1])}

BISHOP_MOVE_VECTORS = {Vector([1,1]), Vector([-1,-1]), Vector([-1,1]), Vector([1,-1])}

QUEENKING_MOVE_VECTORS = ROOK_MOVE_VECTORS | BISHOP_MOVE_VECTORS

KNIGHT_MOVE_VECTORS = {Vector([-2, 1]), Vector([-2,-1]), Vector([2,1]), Vector([2,-1]), Vector([1,2]), Vector([-1,2]), Vector([1,-2]), Vector([-1,-2])}

MOVE_VECT_DICT = {"rook": ROOK_MOVE_VECTORS, "bishop": BISHOP_MOVE_VECTORS, "queen": QUEENKING_MOVE_VECTORS, "king": QUEENKING_MOVE_VECTORS, "knight": KNIGHT_MOVE_VECTORS}






