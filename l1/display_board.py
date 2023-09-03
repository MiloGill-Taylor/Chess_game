''' Has the DisplayBoard function'''
from l3.movement_rules_vec_def import MAP_VEC_TO_SQR, Vector, MAP_PIECE_DISPLAY_ID

def DisplayBoard(board):
	mult_num = 57
	print('-'*mult_num)
	for row in range(8):
		row_string = '|'
		for col in range(8):
			position = Vector([row, col])
			piece = board[position]
			if board.is_piece(position):
				piece_str = piece.colour + MAP_PIECE_DISPLAY_ID[piece.name]
			else:
				piece_str = '   '
			pos_str = ':' + MAP_VEC_TO_SQR[position]
			row_string += piece_str + pos_str + '|'
		print(row_string)
		print('-'*mult_num)


