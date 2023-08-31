''' This file defines the Vector class and creates the MOVEMENT_RULES dictionary'''
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




ROOK_MOVE_VECTORS = {Vector([1,0]), Vector([-1,0]), Vector([0,1]), Vector([0,-1])}

BISHOP_MOVE_VECTORS = {Vector([1,1]), Vector([-1,-1]), Vector([-1,1]), Vector([1,-1])}

QUEENKING_MOVE_VECTORS = ROOK_MOVE_VECTORS | BISHOP_MOVE_VECTORS

KNIGHT_MOVE_VECTORS = {Vector([-2, 1]), Vector([-2,-1]), Vector([2,1]), Vector([2,-1]), Vector([1,2]), Vector([-1,2]), Vector([1,-2]), Vector([-1,-2])}

MOVEMENT_RULES = {"rook": ROOK_MOVE_VECTORS, "bishop": BISHOP_MOVE_VECTORS, "queen": QUEENKING_MOVE_VECTORS, "king": QUEENKING_MOVE_VECTORS, "knight": KNIGHT_MOVE_VECTORS}