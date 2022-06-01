# Battleship

Battleship is a game run via the Python terminal!

The user must try and find all the computers ships before the computer finds all of theirs! Each ship takes up 1 square on the gameboard

## How to play

In this version of battleship, you enter your name, and then your preferred board width and height (4x4) minimum, and then 2 boards are generated at with random positions.

The player can see where their ship is placed by the __'S'__ on the board. The opponent board will only show sea, show as a '.'

Each player has 4 ships on their board, and 4 ships to find from the opponents board.

When a player misses the target, they will be notified on that turn, and then the next turn, their missed shot will be marked with an __'X'__ on the opponent gameboard to indicate a miss.

When a player hits the target, they will be notified on that turn, and their score will increase. On the next turn, the hit shot will be marked with an __'*'__ on the opponent gameboard to indicate a hit.

The opponent and the player take turns in order of player, opponent. You don't gain an extra turn if you get a hit.

A player will be notified if their opponent gets a hit or a miss in the same way they are notified.

The winner is the first player to sink all 4 opponent ships. Once this happens, the game ends and a new one can be started with a new board size.

## Features

### Features to implement

- Random board generation
    - Place ships in random locations for player and computer
    - Player cannot see computer players ships
- Plays against a computer
- Accept user input
- Maintain scores
- Input validation and error checking
    - Make sure coordinates input are within the grid boundaries
    - A number must be entered
    - The same coordinate cannot be entered twice
- Allow player to select board size