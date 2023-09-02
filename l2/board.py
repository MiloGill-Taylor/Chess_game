''' This file defines the board class and board functions'''
from l3.movement_rules_vec_def import Vector 
from l3.move import Move

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

	def one_player_squares(self, colour):
		''' Return a list of all the squares (in vector format) that are occupied by pieces of $colour.

		Args:
		colour (str): 'w' or 'b' to specify which squares to return

		Returns:
		squares (list): List of vectors specifying the squares occupied by $colour pieces.
		'''
		squares = []
		for square in self.keys():
			if self.is_piece(square) and self[square].colour == colour:
				squares.append(square)
		return squares 

	def get_piece_moves(self, position):
		''' Return the legal move objects for the piece at $position.

		Args:
		position (Vector): The position where the piece is. 

		Returns:
		moves (list): Array of legal Move objects.
		'''
		piece = self[position]
		current_row = position[0]
		current_col = position[1]
		moves = []

		if not self.is_on_board(position):
			raise PositionNotOnBoard

		if piece.name == 'pawn':

			advance_position = position.add(piece.advance_vector)
			if advance_position[0] in range(8) and self.is_empty(advance_position):
				moves.append(Move(piece, position, advance_position))
		
			attack_positions = piece.get_attack_positions(position)
			for new_position in attack_positions:
				if not self.is_on_board(new_position):
					continue 
				elif (not self.is_empty(new_position)) and self.different_colour(new_position, position):
					moves.append(Move(piece, position, new_position))

		elif piece.name in {'rook', 'bishop', 'queen'}:

			for direction in piece.move_vectors: 
				next_square = position.add(direction)
				while self.is_on_board(next_square) and self.is_empty(next_square):
					moves.append(Move(piece, position, next_square))
					next_square = next_square.add(direction) 
				# Exit while loop because next_square is off board or there is a piece on the next_square.  
				if self.is_on_board(next_square) and self.different_colour(next_square, position):
					# Exited the while loop because there is a piece on next_square and the piece is of a different colour. 
					moves.append(Move(piece, position, next_square))

		elif piece.name == 'knight':

			for vector in piece.move_vectors:
				potential_position = position.add(vector)
				if self.is_on_board(potential_position) and (self.is_empty(potential_position) or self.different_colour(potential_position, position)):
					# Potential position is good. 
					moves.append(Move(piece, position, potential_position))

		else:
			# King
			#TODO: For now, ignoring the possibility that the king may move into check.  
			for vector in piece.move_vectors:
				potential_position = position.add(vector)
				if self.is_on_board(potential_position) and (self.is_empty(potential_position) or self.different_colour(potential_position, position)):
					# Potential position is good. 
					moves.append(Move(piece, position, potential_position))
					
		return moves




class PositionNotOnBoard(Exception):
	def __init__(self):
		super().__init__("PositionNotOnBoard: A Board method was passed a position not on the chess board.")
