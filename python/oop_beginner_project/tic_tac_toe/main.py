from game import *
from player import HumanPlayer,ComputerPlayer,SmartComputerPlayer

if __name__ == "__main__":
    x_player = HumanPlayer('X')
    o_player = SmartComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game = True)
