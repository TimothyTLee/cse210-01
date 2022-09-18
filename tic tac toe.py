

import random


class TicTacToe:
    board = []

    def _init_(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self. board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

# building and checking the rows

        for i in range(n):
            win = True

            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

# building and checking columns

        for i in range(n):
            win = True

            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

# building and checking diagonals

        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win
        win = True

        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == "-":
                    return False
            return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

                    
    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def check_location(self, row, col):
        if row < 4 and row > 0 and col < 4 and col > 0:
            return self.board[row-1] [col-1] == '-'
        return False

    def get_move(self):
        row_location = 0
        col_location = 0
        first = True
        valid_location = False
        while(row_location > 3 or row_location < 1 or col_location > 3 or col_location < 1 or valid_location == False): 
            if((row_location > 3 or row_location < 1 or col_location > 3 or col_location < 1) and first == False):
                print("Not a valid row and column location " + str(row_location)  + " " + str(col_location))
            if valid_location == False and first == False:
                print("location not available")
            try:
                first = False
                print("Enter in a row to play 1-3: ")
                row_location = int(input())
                print("Enter in a column to play 1-3: ")
                col_location = int(input())
                valid_location = self.check_location(row_location, col_location)
            except:
                print( "Not a valid row and column location")
                first = True
                row_location = 0
                col_location = 0
        return [row_location, col_location]


    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            [row, col] = self.get_move()

            self.fix_spot(row - 1, col - 1, player)

            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            if self.is_board_filled():
                print("Its a draw!")
                break

            player = self.swap_player_turn(player)

        print()
        self.show_board()

tic_tac_toe = TicTacToe() 
tic_tac_toe.start()
