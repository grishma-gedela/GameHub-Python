import time
ttt="""⟦T⟧⟦i⟧⟦c⟧ ⟦T⟧⟦a⟧⟦c⟧ ⟦T⟧⟦o⟧⟦e⟧"""
class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'

    def display_board(self):
        print(f"\n\n --------------- {ttt} ----------------\n\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("-----------")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("-----------")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")

    def get_player_move(self):
        while True:
            try:
                position = int(input(f"\n{self.current_player}'s turn. Choose a position (1-9): "))
                if 1 <= position <= 9 and self.board[position - 1] == ' ':
                    return position
                else:
                    print("Invalid move. Please choose a valid position.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def make_move(self, position):
        self.board[position - 1] = self.current_player

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != ' ' or \
               self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] != ' ':
                return True
        if self.board[0] == self.board[4] == self.board[8] != ' ' or \
           self.board[2] == self.board[4] == self.board[6] != ' ':
            return True
        return False

    def is_tie(self):
        return ' ' not in self.board

    def play(self):
        while True:
            self.display_board()
            position = self.get_player_move()
            self.make_move(position)

            if self.check_winner():
                self.display_board()
                print(f"\nPlayer {self.current_player} wins!\n")
                time.sleep(2)  # Add a 2-second delay
                
                break
            elif self.is_tie():
                self.display_board()
                print("\nThe game is a tie!\n")
                time.sleep(2)  # Add a 2-second delay
                

                break
            

            self.switch_player()

if __name__ == "__main__":
    game = TicTacToe()
    game.play()




