class Move():
	def __init__(self, piece, old_position, new_position):
		self.piece = piece
		self.old_position = old_position
		self.new_position = new_position


def _different_colour(board, position1, position2):
	'''Return true if the pieces at position1 and position2 are different colour.  Should not be called by controller.

	Args:
	board (Board): The board the game is being played on. 
	position1 (Vector): Position of one of the pieces.
	position2 (Vector): Position of one of the pieces.

	Returns:
	(bool): True if the are different colour
	'''
	return board[position1].colour != board[position2].colour

#TODO: Impliment this
def _is_check(board):
	return False

def _calculate_moves_for_piece(board, position, move_vect_dict):
	''' Return a list of all Move objects allowed for the piece at position.  Should not be called by controller.

	Args:
	board (Board): The board the game is being played on. 
	position (Vector): The position the piece is at. 
	move_vect_dict (dict): Key is piece type, value is a set of the vector directions the piece can move in. 

	Returns: 
	moves (list): List of moves the piece can make.
	'''
	piece = board[position]
	current_row = position[0]
	current_col = position[1]

	moves = None
	if piece.name == "pawn":
		moves = _generate_pawn_moves(board, position)
	elif piece.name in {"rook", "bishop", "queen"}:
		moves = _generate_queen_bishop_rook_moves(board, position, move_vect_dict)
	elif piece.name == "knight":
		 moves = _generate_knight_moves(board, position, move_vect_dict)
	else:
		moves = _generate_king_moves(board, position, move_vect_dict)

	return moves

def _generate_pawn_moves(board, position):
	''' Return a list of all Move objects for the piece at $position.  Should not be called by controller.
	    This function should only be used with pawns.    

	Args:
	board (Board): The board the game is being played on. 
	position (Vector): The position of the piece of interest.

	Returns:
	moves (list): List of Move objects.
	'''
	piece = board[position]
	if piece.name != "pawn":
		raise GeneratMovesFunctionPassedIncorrectPiece
	moves = []
	if piece.colour == "b":
		step = +1
	else:
		step = -1
	current_row = position[0]
	current_col = position[1]
	step_forward_position = (current_row + step, current_col)
	if step_forward_position[0] in range(8) and board[step_forward_position] is None:
		moves.append(Move(piece, position, step_forward_position))
	if 1 <= current_col <= 6:
		attack_positions = [(current_row + step, current_col + 1), (current_row + step, current_col -1)]
		for new_position in attack_positions:
			if (board[new_position] is not None) and _different_colour(board, new_position, position):
				# There is a piece at new_position and it is of a different colour
				moves.append(Move(piece, position, new_position))
	elif current_col == 0:
		new_position = (current_row + step, 1)
		if (board[new_position] is not None) and _different_colour(board, new_position, position):
				# There is a piece at new_position and it is of a different colour
				moves.append(Move(piece, position, new_position))
	else:
		new_position = (current_row + step, 6)
		if (board[new_position] is not None) and _different_colour(board, new_position, position):
				# There is a piece at new_position and it is of a different colour
				moves.append(Move(piece, position, new_position))
	return moves

def _generate_knight_moves(board, position, move_vect_dict):
	''' Return a list of all Move objects for the piece at $position.  Should not be called by controller.
	    This function should only be used with Knights.    

	Args:
	board (Board): The board the game is being played on. 
	position (Vector): The position of the piece of interest.
	move_vect_dict (dict): Key is piece type, value is a set of the vector directions the piece can move in.

	Returns:
	moves (list): List of Move objects.
	'''
	piece = board[position]
	if piece.name != "knight":
		raise GeneratMovesFunctionPassedIncorrectPiece
	moves = []
	for vector in move_vect_dict["knight"]:
		potential_position = position.add(vector)
		if board.is_on_board(potential_position) and (board[potential_position] is None or _different_colour(board, potential_position, position)):
			# Potential position is good. 
			moves.append(Move(piece, position, potential_position))
	return moves

def _generate_queen_bishop_rook_moves(board, position, move_vect_dict):
	''' Return a list of all Move objects for the piece at $position.  Should not be called by controller.
	    This function should only be used with the rook, bishop and queen.    

	Args:
	board (Board): The board the game is being played on. 
	position (Vector): The position of the piece of interest.
	move_vect_dict (dict): Key is piece type, value is a set of the vector directions the piece can move in.


	Returns:
	moves (list): List of Move objects.
	'''
	piece = board[position]
	if piece.name not in {"rook", "bishop", "queen"}:
		raise GeneratMovesFunctionPassedIncorrectPiece
	directions = move_vect_dict[piece.name]
	moves = []
	for direction in directions: 
		next_square = position.add(direction)
		while board.is_on_board(next_square) and board[next_square] is None:
			moves.append(Move(piece, position, next_square))
			next_square = next_square.add(direction) 
		# Exit while loop because next_square is off board or there is a piece on the next_square.  
		if board.is_on_board(next_square) and _different_colour(board, next_square, position):
			# Exited the while loop because there is a piece on next_square and the piece is of a different colour. 
			moves.append(Move(piece, position, next_square))
	return moves

def _generate_king_moves(board, position, move_vect_dict):
	''' Return a list of all Move objects for the piece at $position.  Should not be called by controller.
	    This function should only be used with the king.    

	Args:
	board (Board): The board the game is being played on. 
	position (Vector): The position of the piece of interest.
	move_vect_dict (dict): Key is piece type, value is a set of the vector directions the piece can move in.

	Returns:
	moves (list): List of Move objects.
	'''
	piece = board[position]
	if piece.name != "king":
		raise GeneratMovesFunctionPassedIncorrectPiece
	moves = []
	for vector in move_vect_dict["king"]:
		potential_position = position.add(vector)
		if board.is_on_board(potential_position) and (board[potential_position] is None or _different_colour(board, potential_position, position)) and not _is_check():
			# Potential position is good. 
			moves.append(Move(piece, position, potential_position))
	return moves

def calculate_all_moves(board, move_colour, move_vect_dict):
	''' Return a list of all Move objects allowed this half turn.
	Arg:
	board (Board): The board the game is being played on.  
	move_colour (str): "w" if white is to move, "b" if black to move.
	move_vect_dict (dict): Key is piece type, value is a set of the vector directions the piece can move in. 

	Returns:
	valid_moves (list): A list of all Move objects allowed.
	'''
	valid_moves = []
	for position in board.keys():
		piece = board[position]
		if piece is None or piece.colour != move_colour:
			continue
		else:
			moves_for_piece = _calculate_moves_for_piece(board, position, move_vect_dict)
			valid_moves.extend(moves_for_piece)
	return valid_moves

class GeneratMovesFunctionPassedIncorrectPiece(Exception):
	def __init__(self):
		super().__init__("GeneratMovesFunctionPassedIncorrectPiece: A function to generate moves was passed an innapropriate piece")


