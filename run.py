def get_player_name():
    """
    Gets the name of the player
    """
    name = input('What is your name:\n')
    print(f"Hello {name}, let's play some battleship!")
    return name


player_name = get_player_name()