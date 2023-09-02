'''This file contains all the class definitions for the pieces'''
from l3.movement_rules_vec_def import Vector

class Pawn:
	def __init__(self, colour):
		self.colour = colour
		self.value = 1
		self.name = "pawn"
		self.has_moved = False
		if colour == 'b':
			self.advance_vector = Vector([1,0])
			self.first_move_vectors = {Vector([2,0]), Vector([1,0])}
			self.attack_vectors = {Vector([1,1]), Vector([1,-1])}
		else:
			self.advance_vector = Vector([-1,0])
			self.first_move_vectors ={Vector([-2,0]), Vector([-1,0])}
			self.attack_vectors = {Vector([-1,1]), Vector([-1,-1])}

	def get_attack_positions(self, current_position):
		''' Return a set of attack positions for this pawn.'''
		attack_positions = []
		for attack_vector in self.attack_vectors:
			attack_positions.append(current_position.add(attack_vector))
		return attack_positions 

	def moved(self):
		self.has_moved = True 

	def get_first_move_positions(self, current_position):
		first_move_positions = []
		for first_move_vector in self.first_move_vectors:
			first_move_positions.append(current_position.add(first_move_vector))
		return first_move_positions 



 
class Rook:
	def __init__(self, colour):
		self.colour = colour
		self.value = 5
		self.name = "rook"
		self.move_vectors = {Vector([1,0]), Vector([-1,0]), Vector([0,1]), Vector([0,-1])}

class Knight:
	def __init__(self, colour):
		self.colour = colour 
		self.value = 3
		self.name = "knight"
		self.move_vectors = {Vector([-2, 1]), Vector([-2,-1]), Vector([2,1]), Vector([2,-1]), Vector([1,2]), Vector([-1,2]), Vector([1,-2]), Vector([-1,-2])}

class Bishop:
	def __init__(self, colour):
		self.colour = colour 
		self.value = 3
		self.name = "bishop"
		self.move_vectors = {Vector([1,1]), Vector([-1,-1]), Vector([-1,1]), Vector([1,-1])}

class Queen:
	def __init__(self, colour):
		self.colour = colour 
		self.value = 9
		self.name = "queen"
		self.move_vectors = {Vector([1,1]), Vector([-1,-1]), Vector([-1,1]), Vector([1,-1])} | {Vector([1,0]), Vector([-1,0]), Vector([0,1]), Vector([0,-1])}

class King:
	def __init__(self, colour):
		self.colour = colour 
		# The string 'inf' acts as the obect infinity
		self.value = "inf"
		self.name = "king"
		self.move_vectors = {Vector([1,1]), Vector([-1,-1]), Vector([-1,1]), Vector([1,-1])} | {Vector([1,0]), Vector([-1,0]), Vector([0,1]), Vector([0,-1])}