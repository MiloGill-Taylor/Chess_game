''' This file contains the Move class definition. '''
class Move():
	def __init__(self, piece, old_position, new_position):
		self.piece = piece
		self.old_position = old_position
		self.new_position = new_position
