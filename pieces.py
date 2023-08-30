'''This file contains all the class definitions for the pieces'''

class Pawn:
	def __init__(self, colour):
		self.colour = colour
		self.value = 1
		self.name = "pawn"
 
class Rook:
	def __init__(self, colour):
		self.colour = colour
		self.value = 5
		self.name = "rook"

class Knight:
	def __init__(self, colour):
		self.colour = colour 
		self.value = 3
		self.name = "knight"

class Bishop:
	def __init__(self, colour):
		self.colour = colour 
		self.value = 3
		self.name = "bishop"

class Queen:
	def __init__(self, colour):
		self.colour = colour 
		self.value = 9
		self.name = "queen"

class King:
	def __init__(self, colour):
		self.colour = colour 
		# The string 'inf' acts as the obect infinity
		self.value = "inf"
		self.name = "king"