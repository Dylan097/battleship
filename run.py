from random import randint

scores = {'computer': 0, 'player': 0}


class GameBoard:
    """
    Main board class. Sets the board size and the 
    number of ships on the board, as well as the 
    player's name and the board type (player or computer)
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [['.' for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []
    
    def print(self):
        for row in self.board:
            print(' '.join(row))
    
    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = 'X'

        if (x, y) in self.ships:
            self.board[x][y] = '*'
            return 'Hit'
        else:
            return 'Missed'
    
    def add_ship(self, x, y, type='computer'):
        if len(self.ships) >= self.num_ships:
            print('Error: you cannot add anymore ships')
        else:
            self.ships.append((x, y))
            if self.type == 'player':
                self.board[x][y] = 'S'


def random_point(size):
    """
    Returns a random integer between 0 and size
    """
    return randint(0, size - 1)


def get_player_name():
    """
    Gets the name of the player
    """
    while True:
        name = input('What is your name:\n')
        if check_player_name(name):
            print(f"Hello {name}, let's play some battleship!\n")
            break
    return name


def check_player_name(name):
    """
    Checks if player name isn't a number and
    isn't blank
    """
    try:
        if name.isnumeric():
            raise ValueError(
                f'You entered {name}. Expected a word'
            )
        elif not(name and not name.isspace()):
            raise ValueError(
                'Expected a name, you input nothing'
            )
    except ValueError as e:
        print(f'Invalid data: {e}! Please try again')
        return False
    return True


def get_board_size(name):
    """
    Gets the board size the player would like to play with
    """
    while True:
        size = input(f'What grid size do you want to play with {name}:\n')
        if validate_board_size(size):
            print(f'Playing with grid size {size}')
            break
    return size


def validate_board_size(size):
    """
    Inside the try, converts size into an integer.
    Raises ValueError if size cannot be converted into an integer
    or if size is less than 4
    """
    try:
        int(size)
        if int(size) < 4:
            raise ValueError(
                f'the board size should be greater than 3! You entered {size}'
            )
    except ValueError as e:
        print(f'Invalid data: {e}! Please try again!\n')
        return False
    return True


def populate_board(board, size):
    """
    Adds ships to the gameboard
    """
    while True:
        x_position = random_point(size)
        y_position = random_point(size)
        if valid_coordinates(x_position, y_position, board, size):
            break
    board.add_ship(x_position, y_position, board.type)


def make_guess(board, size):
    """
    Asks for a guess on the board.
    Guess is random if it's the computers turn
    """
    if board.type == 'computer':
        while True:
            row = input('Guess a row:\n')
            column = input('Guess a column:\n')
            if valid_coordinates(row, column, board, size):
                print(f'Player guessed: ({row}, {column})')
                result = board.guess(int(row), int(column))
                print(f'Player {result} this time!')
                return result
    else:
        while True:
            row = random_point(size)
            column = random_point(size)
            if valid_coordinates(row, column, board, size):
                print(f'Computer guessed: ({row}, {column})')
                result = board.guess(int(row), int(column))
                print(f'Computer {result} this time!')
                return result


def valid_coordinates(x, y, board, size):
    """
    Validates the given position on the board
    """
    if len(board.ships) < 4:
        if (x, y) in board.ships:
            return False
        return True
    else:
        try:
            int(x)
            int(y)
            if (int(x), int(y)) in board.guesses:
                raise ValueError(
                    f'you already guessed coordinates ({x},{y})'
                )
            elif int(x) > size-1 or int(y) > size-1:
                raise ValueError(
                    f'coordinates ({x},{y}) are out of range'
                )
        except ValueError as e:
            if board.type == 'computer':
                print(f'Invalid data: {e}, please try again')
            return False
        return True


def play_game(player, computer, size, name):
    """
    Creates a loop that makes the game run.
    Runs until player exits or there's a winner
    """
    print('Starting game\n')
    print(f'Game size is {size}\n')
    print('Top left of the board is (0, 0)\n')
    print('4 ships in the game\n')
    while True:
        print(f"{name}'s board:")
        player.print()
        print("Computer's board:")
        computer.print()
        player_guess = make_guess(computer, size)
        computer_guess = make_guess(player, size)
        if player_guess == 'Hit':
            scores['player'] = scores['player'] + 1
        if computer_guess == 'Hit':
            scores['computer'] = scores['computer'] + 1
        p = scores['player']
        c = scores['computer']
        print(f'{name}: {p}. Computer: {c}')
        if p == 4 and c == 4:
            print("It's a draw!")
            break
        elif p == 4:
            print(f'{name} won!')
            break
        elif c == 4:
            print('Computer won!')
            break
        exit_game = input("Press 'e' to exit or any key to continue\n")
        if exit_game == 'e':
            print('Exiting game...\n')
            break


def new_game():
    """
    Starts a new game
    """
    while True:
        player_name = get_player_name()
        board_size = int(get_board_size(player_name))
        player = GameBoard(board_size, 4, player_name, 'player')
        computer = GameBoard(board_size, 4, 'Computer', 'computer')
        for _ in range(4):
            populate_board(player, board_size)
            populate_board(computer, board_size)
        play_game(player, computer, board_size, player_name)
        next = input("Press 'e' to exit or any key to start a new game\n")
        if next == 'e':
            print('Exiting game...')
            break
        else:
            print('Starting another game...\n')


new_game()
