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
    print(f"Hello {name}, let's play some battleship!")
    return name


def get_board_size(name):
    """
    Gets the board size the player would like to play with
    """
    size = input(f'What grid size do you want to play with {name}:\n')
    return size


player_name = get_player_name()
board_size = get_board_size(player_name)
