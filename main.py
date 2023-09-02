from l1.setup_board import SetupBoard
from l1.generate_moves import GenerateAllMoves
from l1.update_board import UpdateBoard
from l1.user_input import GetUserMove
import pprint


board = SetupBoard()

#valid_moves = GenerateAllMoves(board)

move = GetUserMove(board, 'w')

board = UpdateBoard(board, move)

pprint.pp(board)


