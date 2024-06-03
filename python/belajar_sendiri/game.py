import time

class TicTacToe():
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    @staticmethod
    def print_number_board():
        value_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in value_board:
            print("| " + " | ".join(row) + " |")
    
    def print_board(self):
        value_board = [self.board[i*3:(i+1)*3] for i in range(3)]
        for row in value_board:
            print("| " + " | ".join(row) + " |")
    
    def available_move(self):
        return [i for i,spot in enumerate(self.board) if spot ==" "]
    
    def empty_square(self):
        return ' ' in self.board
    
    def make_move(self,square,letter):
        self.board[square] = letter
        self.print_board()
        if self.winner(square,letter):
            self.current_winner = letter
    
    def winner(self,square,letter):
        #row
        row_index = square // 3
        row = self.board[row_index*3:(row_index+1)*3]
        if all([spot == letter for spot in row]):
            return True

        #column
        col_index = square % 3
        col = self.board[col_index*3:(col_index+1)*3]
        if all([spot == letter for spot in col]):
            return True

        #diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal1]) or all([spot == letter for spot in diagonal2]):
                return True
        return False


def play(game,x_player,o_player):
    letter = 'X'
    game.print_number_board()

    while game.empty_square() and game.current_winner == None:
        if letter == 'X':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)
        
        print(f'{letter} move to square {square}')        
        game.make_move(square,letter)

        if game.current_winner == letter:
            print(f'{letter} wins!')
        if letter == 'X':
            letter = 'O'
        else:
            letter = 'X'

        time.sleep(0.8)

    if game.current_winner == None:
        print('it is a tie')



