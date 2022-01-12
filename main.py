# battle ships
# imports

import random

# main loop
def main():
    boats = [5, 4, 3, 3, 2, 2, 1]
    
    game_field, shooting_board, to_shot_board = create_game_field((10, 10))
    
    print([to_human_readable_coordinates(a) for a in shooting_board])

# function which takes a string as input in format such as "A1" and returns position of these characters on game board
def position_on_board(inp):
    inp = inp.lower()
    inp_text = inp[0]
    inp_number = int(inp[1:]) - 1
    
    lib = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    
    return ((lib.index(inp_text), inp_number))

# function which will return a game board with boats placed on the board
def create_game_field(size):
    game_board = [[0 for i in range(size[0])] for j in range(size[1])]
    shooting_board = [(i, j) for i in range(size[0]) for j in range(i % 2, size[1], 2)]
    to_shot_board = game_board.copy()
    
    return game_board, shooting_board, to_shot_board

# function which return string in format such as "A1" from list of two integers
def to_human_readable_coordinates(inp):
    lib = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    return lib[inp[0]] + str(inp[1] + 1)

# starts the program
if __name__ == '__main__':
    main()
