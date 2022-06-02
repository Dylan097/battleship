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


def get_player_name():
    """
    Gets the name of the player
    """
    name = input('What is your name:\n')
    print(f"Hello {name}, let's play some battleship!\n")
    return name


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
board_size = get_board_size(player_name)
