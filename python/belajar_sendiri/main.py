from game import *
from player import *


x_player = Human('X')
o_player = Computer('O')
t = TicTacToe()

# t.print_board()

# o_player.get_move(t)

play(t,x_player,o_player)