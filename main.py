from l1.setup_board import SetupBoard
from l1.generate_moves import GenerateAllMoves
from l1.update_board import UpdateBoard
from l1.user_input import GetUserMove
from l1.display_board import DisplayBoard
import pprint


board = SetupBoard()

#valid_moves = GenerateAllMoves(board)

while not board.is_checkmate():

	move = GetUserMove(board, 'w')
	board = UpdateBoard(board, move)
	DisplayBoard(board)
	if board.is_checkmate():
		break

	move = GetUserMove(board, 'b')
	board = UpdateBoard(board, move)
	DisplayBoard(board)





