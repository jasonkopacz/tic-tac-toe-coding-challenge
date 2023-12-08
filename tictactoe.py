BLANK_SQUARE = '_'
# Victory Message
# Prevent game from crashing when given position outside of range or anything other than a number
# make code more readable
# add play again

class TicTacToe:

    def __init__(self, board_size=3):
        self.board_size = board_size
        self.board = [BLANK_SQUARE] * self.board_size ** 2
        self.current_player = 'X'
        # adding a turn count to let players know how many turns they played
        self.turn = 0

    def print_board(self):
        print()
        for i in range(0, self.board_size ** 2):
            print(self.board[i], end='  ')
            if i % self.board_size == self.board_size - 1:
                print()
                print()
    
    def make_move(self, position):
        # let's add a guard clause to make sure the move is valid
        if position < 0 or position > self.board_size ** 2 or isinstance(position, int) == False:
            print('Invalid move!')
        elif self.board[position] == BLANK_SQUARE:
            self.board[position] = self.current_player
            self.turn += 1
            # change player in one line for less code and easier readability
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print('Invalid move!')
    
    def check_winner(self):
        # I've added a victory message for the player that wins. It also tells them how many turns were played.
        # Check rows
        for i in range(0, self.board_size ** 2, self.board_size):
            count_same = 1
            for j in range(i + 1, i + self.board_size):
                if self.board[j] == self.board[j-1] != BLANK_SQUARE:
                    count_same += 1
            if count_same == self.board_size:
                handle_game_end(self, self.board[j])

        # Check columns
        for i in range(self.board_size):
            count_same = 1
            for j in range(i + self.board_size, self.board_size ** 2, self.board_size):
                if self.board[j] == self.board[j - self.board_size] != BLANK_SQUARE:
                    count_same += 1
            if count_same == self.board_size:
                handle_game_end(self, self.board[j])

        # Check diagonals
        count_same = 0
        for i in range(0, self.board_size ** 2, self.board_size + 1):
            if self.board[i] == self.board[0] != BLANK_SQUARE:
                count_same += 1
        if count_same == self.board_size:
            handle_game_end(self, self.board[i])

        count_same = 0
        for i in range(self.board_size - 1, self.board_size ** 2 - 1, self.board_size - 1):
            if self.board[i] == self.board[self.board_size - 1] != BLANK_SQUARE:
                count_same += 1
        if count_same == self.board_size:
            handle_game_end(self, self.board[i])

        return None

    def check_draw(self):
        if BLANK_SQUARE not in self.board:
            print('Draw!')
            handle_game_end(self)
            

    def reset(self):
        # reset the size of the board using the board_size variable, not 9
        self.board = [BLANK_SQUARE] * self.board_size ** 2
        self.current_player = 'X'

# A reusable function for getting input that doesn't allow invalid inputs
def get_user_input(prompt, valid_range):
    while True:
        try:
            value = int(input(prompt))
            if value in valid_range:
                return value
            else:
                print(f'Please input a number between {valid_range[0]} and {valid_range[-1]}')
        except ValueError:
            print('Please input a valid number.')


# Turn the start of the game into a function so we can use it to replay the game
# Add a message to let the user know what they're playing
# Make sure the board size input is an integer greater than 2 so the program doesn't break
# I also capped the board size at 100. If we give the user the option to input any number the program could break due to the number being so large
def start():
    print('TicTacToe! Good luck!')
    board_size = get_user_input('What board size do you want? Choose any size from 3 to 100.\n', range(3, 101))        

    game = TicTacToe(board_size=board_size)

# Game loop
    while game.check_winner() is None and not game.check_draw():
        game.print_board()
        position = get_user_input(f"{game.current_player}'s turn Enter position (0 - {game.board_size ** 2 - 1}): ", range(game.board_size ** 2))
        game.make_move(position)

    game.print_board()

# Ask if the user wants to play again
def replay():
    play_again = input('Do you want to play again? (yes/no): ').lower()
    if play_again == 'yes':
        start()
    else:
        print('ByeBye')
        exit()

def handle_game_end(self, winner):
    print(f'{winner} wins in {self.turn} turns!')
    self.print_board()
    replay()

# Main program starts here
start()