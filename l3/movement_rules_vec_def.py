''' This file defines the Vector class and creates the MOVEMENT_RULES dictionary'''
import pprint

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

	
	def subtract(self, vector):
		''' Peform vector subtraction with $self and $vector.  Return a new Vector object.  

		Args:
		vector (Vector):  The vector being added to $self.

		Returns:
		(Vector): Result of vector addition.
		'''
		first_element = self[0] - vector[0]
		second_element = self[1] - vector[1]
		return Vector([first_element, second_element])

class VectorDimensionIncorrect(Exception):
	def __init__(self):
		super().__init__("VectorDimensionIncorrect: An attempt to make a Vector object with dimension not 2 was made.")




#MOVEMENT_RULES = {"rook": ROOK_MOVE_VECTORS, "bishop": BISHOP_MOVE_VECTORS, "queen": QUEENKING_MOVE_VECTORS, "king": QUEENKING_MOVE_VECTORS, "knight": KNIGHT_MOVE_VECTORS}

MAP_SQR_TO_VEC = {
	"a8": Vector([0,0]), "b8": Vector([0,1]), "c8": Vector([0,2]), "d8": Vector([0,3]), "e8": Vector([0,4]), "f8": Vector([0,5]), "g8": Vector([0,6]), "h8": Vector([0,7]),
	"a7": Vector([1,0]), "b7": Vector([1,1]), "c7": Vector([1,2]), "d7": Vector([1,3]), "e7": Vector([1,4]), "f7": Vector([1,5]), "g7": Vector([1,6]), "h7": Vector([1,7]),
	"a6": Vector([2,0]), "b6": Vector([2,1]), "c6": Vector([2,2]), "d6": Vector([2,3]), "e6": Vector([2,4]), "f6": Vector([2,5]), "g6": Vector([2,6]), "h6": Vector([2,7]),
	"a5": Vector([3,0]), "b5": Vector([3,1]), "c5": Vector([3,2]), "d5": Vector([3,3]), "e5": Vector([3,4]), "f5": Vector([3,5]), "g5": Vector([3,6]), "h5": Vector([3,7]),
	"a4": Vector([4,0]), "b4": Vector([4,1]), "c4": Vector([4,2]), "d4": Vector([4,3]), "e4": Vector([4,4]), "f4": Vector([4,5]), "g4": Vector([4,6]), "h4": Vector([4,7]),
	"a3": Vector([5,0]), "b3": Vector([5,1]), "c3": Vector([5,2]), "d3": Vector([5,3]), "e3": Vector([5,4]), "f3": Vector([5,5]), "g3": Vector([5,6]), "h3": Vector([5,7]),
	"a2": Vector([6,0]), "b2": Vector([6,1]), "c2": Vector([6,2]), "d2": Vector([6,3]), "e2": Vector([6,4]), "f2": Vector([6,5]), "g2": Vector([6,6]), "h2": Vector([6,7]),
	"a1": Vector([7,0]), "b1": Vector([7,1]), "c1": Vector([7,2]), "d1": Vector([7,3]), "e1": Vector([7,4]), "f1": Vector([7,5]), "g1": Vector([7,6]), "h1": Vector([7,7]),
	}

MAP_VEC_TO_SQR = {MAP_SQR_TO_VEC[k]: k for k in MAP_SQR_TO_VEC.keys()}

MAP_PIECE_DISPLAY_ID = {
	"pawn": 'P ', "knight": 'Kn', "rook": 'R ', "bishop": 'B ', 'queen': 'Q ', 'king': 'K '
}