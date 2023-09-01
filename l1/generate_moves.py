''' Contains the GenerateAllMoves function and associated helper functions.
	Presently the is_check() function is here, this may change.  	
'''
from l3.move import Move 
from l3.movement_rules_vec_def import MOVEMENT_RULES, Vector 



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
	piece = board[position].name
	current_row = position[0]
	current_col = position[1]

	moves = None
	if piece == "pawn":
		moves = generate_pawn_moves(board, position)
	elif piece in {"rook", "bishop", "queen"}:
		moves = generate_queen_bishop_rook_moves(board, position)
	elif piece == "knight":
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
	step_forward_position = Vector([current_row + step, current_col])
	if step_forward_position[0] in range(8) and board.is_empty(step_forward_position):
		moves.append(Move(piece, position, step_forward_position))
	if 1 <= current_col <= 6:
		attack_positions = {Vector([current_row + step, current_col + 1]), Vector([current_row + step, current_col -1])}
		for new_position in attack_positions:
			if (not board.is_empty(new_position)) and board.different_colour(new_position, position):
				# There is a piece at new_position and it is of a different colour
				moves.append(Move(piece, position, new_position))
	elif current_col == 0:
		new_position = Vector([current_row + step, 1])
		if (not board.is_empty(new_position)) and board.different_colour(new_position, position):
				# There is a piece at new_position and it is of a different colour
				moves.append(Move(piece, position, new_position))
	else:
		new_position = Vector([current_row + step, 6])
		if (not board.is_empty(new_position)) and board.different_colour(new_position, position):
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
		if board.is_on_board(potential_position) and (board.is_empty(potential_position) or board.different_colour(potential_position, position)):
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
		while board.is_on_board(next_square) and board.is_empty(next_square):
			moves.append(Move(piece, position, next_square))
			next_square = next_square.add(direction) 
		# Exit while loop because next_square is off board or there is a piece on the next_square.  
		if board.is_on_board(next_square) and board.different_colour(next_square, position):
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
		if board.is_on_board(potential_position) and (board[potential_position] is None or board.different_colour(potential_position, position)) and not is_check():
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

