from random import randint


def get_player_name():
    """
    Gets the name of the player
    """
    name = input('What is your name:\n')
    print(f"Hello {name}, let's play some battleship!")
    return name


def get_board_size(name, section):
    """
    Gets the board size the player would like to play with
    """
    sect_size = input(f'What {section} size do you want to play with {name}\n')
    return sect_size


player_name = get_player_name()
row_size = get_board_size(player_name, 'row')
col_size = get_board_size(player_name, 'column')
