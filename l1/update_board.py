''' Contains the UpdateBoard function''' 
from l3.movement_rules_vec_def import  MOVEMENT_RULES, Vector 

def pawn_move_legal(board, move):
	pawn = move.piece 
	move_vector = move.new_position.subtract(move.old_position)
	if pawn.colour == 'w':
		step = -1
	else:
		step = +1

	advance_move = {Vector([step, 0])}
	attack_moves = {Vector([step, +1]), Vector([step, -1])}

	if move_vector in (advance_move | attack_moves):
		if move_vector in advance_move:
			return board.is_empty(move.new_position)
		else:
			return board.is_piece(move.new_position) and different_colour(board, move.old_position, move.new_position)
	else: 
		return False

def knight_move_legal(board, move):
	return True

def queen_bishop_rook_move_legal(board, move):
	return True 

#TODO: Will leave this for now.  
def king_move_legal(board, move):
	return True

def is_move_legal(board, move):
	piece = move.piece.name 
	if piece == "pawn":
		return pawn_move_legal(board, move)
	elif piece == 'knight':
		return knight_move_legal(board, move)
	elif piece == 'queen' or piece == 'bishop' or piece == 'rook':
		return queen_bishop_rook_move_legal(board, move)
	else:
		return knight_move_legal(board, move) 


class IllegalMove(Exception):
	def __init__(self):
		super().__init__('IllegalMove:  UpdateBoard function passed an illegal move.')

def UpdateBoard(board, move):
	''' Check that the move is legal.  If it is not raise an exception. Otherwise return the updated board.

	Args: 
	board (Board): The board the game is being played on. 
	move (Move): The move object.  

	Returns:
	board (Board): The board the game is being played on.  
	'''
	if not is_move_legal(board, move):
		raise IllegalMove

	if board.is_piece(move.new_position):
		del board[move.new_position]

	board[move.new_position] = move.piece 
	board[move.old_position] = None
	return board 