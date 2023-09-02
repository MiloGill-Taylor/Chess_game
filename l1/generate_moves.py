''' Contains the GenerateAllMoves function and associated helper functions. '''


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
			moves_for_piece = board.get_piece_moves(position)
			valid_moves.extend(moves_for_piece)
	return valid_moves




