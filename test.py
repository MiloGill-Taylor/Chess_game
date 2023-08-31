import numpy 
from board import Board
board = Board()
for i in range(8):
	for j in range(8):
		vec = numpy.array([i,j])
		board[vec] = None