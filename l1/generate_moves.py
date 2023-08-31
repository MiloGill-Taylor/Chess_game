''' Contains the GenerateAllMoves function and associated helper functions.
	Presently the is_check() function is here, this may change.  	
'''
from l2.pieces import Pawn, Rook, Knight, Bishop, Queen, King
from l2.move import Move 
from l2.movement_rules_vec_def import Vector, MOVEMENT_RULES


def different_colour(board, position1, position2):
	'''Return true if the pieces at $position1 and $position2 are different colour.  
		Should not be called by main.

	Args:
	board (Board): The board the game is being played on. 
	position1 (Vector): Position of one of the pieces.
	position2 (Vector): Position of one of the pieces.

	Returns:
	(bool): True if the are different colour
	'''
	return board[position1].colour != board[position2].colour

#TODO: Impliment this
def is_check(board):
	return False

def calculate_moves_for_piece(board, position):
	''' Return a list of all Move objects allowed for the piece at $position.  
		Should not be called by main.

	Args:
	board (Board): The board the game is being played on. 
	position (Vector): The position the piece is at. 
	MOVEMENT_RULES (dict): Key is str denoting the piece, 
						   value is a set of the vector directions the piece can move in. 

	Returns: 
	moves (list): List of moves the piece can make.
	'''
	piece = board[position]
	current_row = position[0]
	current_col = position[1]

	moves = None
	if piece.name == "pawn":
		moves = generate_pawn_moves(board, position)
	elif piece.name in {"rook", "bishop", "queen"}:
		moves = generate_queen_bishop_rook_moves(board, position)
	elif piece.name == "knight":
		 moves = generate_knight_moves(board, position)
	else:
		moves = generate_king_moves(board, position)

	return moves

def generate_pawn_moves(board, position):
	''' Return a list of all Move objects for the piece at $position.  
		Should not be called by controller.
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
			if (board[new_position] is not None) and different_colour(board, new_position, position):
				# There is a piece at new_position and it is of a different colour
				moves.append(Move(piece, position, new_position))
	elif current_col == 0:
		new_position = (current_row + step, 1)
		if (board[new_position] is not None) and different_colour(board, new_position, position):
				# There is a piece at new_position and it is of a different colour
				moves.append(Move(piece, position, new_position))
	else:
		new_position = (current_row + step, 6)
		if (board[new_position] is not None) and different_colour(board, new_position, position):
				# There is a piece at new_position and it is of a different colour
				moves.append(Move(piece, position, new_position))
	return moves

def generate_knight_moves(board, position):
	''' Return a list of all Move objects for the piece at $position.  
		Should not be called by main.
	    This function should only be used with Knights.    

	Args:
	board (Board): The board the game is being played on. 
	position (Vector): The position of the piece of interest.
	MOVEMENT_RULES (dict): Key is str denoting the piece, 
						   value is a set of the vector directions the piece can move in.

	Returns:
	moves (list): List of Move objects.
	'''
	piece = board[position]
	if piece.name != "knight":
		raise GeneratMovesFunctionPassedIncorrectPiece
	moves = []
	for vector in MOVEMENT_RULES["knight"]:
		potential_position = position.add(vector)
		if board.is_on_board(potential_position) and (board[potential_position] is None or different_colour(board, potential_position, position)):
			# Potential position is good. 
			moves.append(Move(piece, position, potential_position))
	return moves

def generate_queen_bishop_rook_moves(board, position):
	''' Return a list of all Move objects for the piece at $position.  
		Should not be called by main.
	    This function should only be used with the rook, bishop and queen.    

	Args:
	board (Board): The board the game is being played on. 
	position (Vector): The position of the piece of interest.
	MOVEMENT_RULES (dict): Key is str denoting the piece, 
						   value is a set of the vector directions the piece can move in.


	Returns:
	moves (list): List of Move objects.
	'''
	piece = board[position]
	if piece.name not in {"rook", "bishop", "queen"}:
		raise GeneratMovesFunctionPassedIncorrectPiece
	directions = MOVEMENT_RULES[piece.name]
	moves = []
	for direction in directions: 
		next_square = position.add(direction)
		while board.is_on_board(next_square) and board[next_square] is None:
			moves.append(Move(piece, position, next_square))
			next_square = next_square.add(direction) 
		# Exit while loop because next_square is off board or there is a piece on the next_square.  
		if board.is_on_board(next_square) and different_colour(board, next_square, position):
			# Exited the while loop because there is a piece on next_square and the piece is of a different colour. 
			moves.append(Move(piece, position, next_square))
	return moves

def generate_king_moves(board, position):
	''' Return a list of all Move objects for the piece at $position.  
		Should not be called by main.
	    This function should only be used with the king.    

	Args:
	board (Board): The board the game is being played on. 
	position (Vector): The position of the piece of interest.
	MOVEMENT_RULES (dict): Key is str denoting the piece, 
						   value is a set of the vector directions the piece can move in.

	Returns:
	moves (list): List of Move objects.
	'''
	piece = board[position]
	if piece.name != "king":
		raise GeneratMovesFunctionPassedIncorrectPiece
	moves = []
	for vector in MOVEMENT_RULES["king"]:
		potential_position = position.add(vector)
		if board.is_on_board(potential_position) and (board[potential_position] is None or different_colour(board, potential_position, position)) and not is_check():
			# Potential position is good. 
			moves.append(Move(piece, position, potential_position))
	return moves

def GenerateAllMoves(board, move_colour = "w"):
	''' Return a list of all Move objects allowed this half turn.
	Arg:
	board (Board): The board the game is being played on.  
	move_colour (str): "w" if white is to move, "b" if black to move.
	MOVEMENT_RULES (dict): Key is str denoting the piece, 
						   value is a set of the vector directions the piece can move in.

	Returns:
	valid_moves (list): A list of all Move objects allowed.
	'''
	valid_moves = []
	for position in board.keys():
		piece = board[position]
		if piece is None or piece.colour != move_colour:
			continue
		else:
			moves_for_piece = calculate_moves_for_piece(board, position)
			valid_moves.extend(moves_for_piece)
	return valid_moves






class GeneratMovesFunctionPassedIncorrectPiece(Exception):
	def __init__(self):
		super().__init__("GeneratMovesFunctionPassedIncorrectPiece: A function to generate moves was passed an innapropriate piece")

