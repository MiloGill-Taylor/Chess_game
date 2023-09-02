''' This file defines the function which gets user input for a move'''
from l3.move import Move
from l3.movement_rules_vec_def import MAP_SQR_TO_VEC


def GetUserMove(board, colour):
	''' Turn user input into the correct Move object.  

	Args: 
	board (Board): The board the game is being played on. 
	colour (str): Which colour, 'w' or 'b' that is making the move. 

	Returns: 
	move (Move): The move object the user has specified
	'''
	potential_positions = board.one_player_squares(colour)
	potential_squares = [square for square in MAP_SQR_TO_VEC.keys() if MAP_SQR_TO_VEC[square] in potential_positions]
	old_position_sqr = input('Please enter the position of the piece you would like to move: ').lower()
	while old_position_sqr not in potential_squares:
		print("Please enter a valid square.")
		old_position_sqr = input('Please enter the position of the piece you would like to move: ').lower()
	old_position = MAP_SQR_TO_VEC[old_position_sqr]

	potential_moves = board.get_piece_moves(old_position)
	potential_positions = [move.new_position for move in potential_moves]
	potential_new_squares = [square for square in MAP_SQR_TO_VEC.keys() if MAP_SQR_TO_VEC[square] in potential_positions]

	new_position_sqr = input('Please enter the position the piece should move to: ').lower()
	while new_position_sqr not in potential_new_squares:
		print("Please enter a valid square.")
		new_position_sqr = input('Please enter the position the piece should move to: ').lower()
	new_position = MAP_SQR_TO_VEC[new_position_sqr]
	
	piece = board[old_position]
	return Move(piece, old_position, new_position)

	

	
