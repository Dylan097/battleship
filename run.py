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
            return 'Miss'
    
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


player_name = get_player_name()
board_size = int(get_board_size(player_name))
player = GameBoard(board_size, 4, player_name, 'player')
computer = GameBoard(board_size, 4, 'Computer', 'computer')
player.print()
computer.print()
