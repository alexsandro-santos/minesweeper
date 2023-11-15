import random

from game_minesweeper.textual_minesweeper import *

def game_grid_create():
    '''Create game matrix and state matrix for interface'''

    complexity = read_player_difficulty()

    dict_complexity_size = {"easy": 10, "medium": 15, "hard": 20}

    game_grid = []
    state_grid = []
    row = []

    for i in range(dict_complexity_size[complexity]):
        row = []
        for j in range(dict_complexity_size[complexity]):
            row.append(' ')
        game_grid.append(row)

    state_grid = game_grid
    
    return game_grid, state_grid

def get_random_position(game_grid):
    positions = []
    size_grid = len(game_grid)

    for i in range(size_grid):
        for j in range(size_grid):
            positions.append((i, j))

    random_position = random.choice(positions)

    return random_position

def get_bombs_positions(game_grid):
    '''Create random positions for bombs'''
    size_grid = len(game_grid)
    dict_number_bombs_by_size = {10: 10, 15: 25, 20: 40}
    bombs = [None] * dict_number_bombs_by_size[size_grid]
    i = 0

    while i < dict_number_bombs_by_size[size_grid]:
        if get_random_position(game_grid) not in bombs:
            bombs[i] = get_random_position(game_grid)
            i += 1

    return bombs

def place_bombs(game_grid):
    '''Substitute bombs in game grid'''
    bombs = get_bombs_positions(game_grid)

    for bomb in range(len(bombs)):
        game_grid[bomb[0]][bomb[1]] = -1

    return game_grid

def tile_number_calculate(game_grid):
    '''Go through each tile of game grid and sum 1 if neighbour is bomb'''

    
    
    return game_grid

def get_tile_neighbours(game_grid, x, y):
    '''Return the coordinates of the 8 neighbours of certain element'''
    neighbours = []
    grid_dim = (len(game_grid[0]), len(game_grid))
    valid_x = [x+i for i in range(-1,2) if 0 <= x+i < grid_dim[0]]
    valid_y = [y+i for i in range(-1,2) if 0 <= y+i < grid_dim[1]]
    for i in valid_x:
        neighbours.extend([(i,j) for j in valid_y if (i,j) != (x,y)])

    return neighbours

def grid_to_string(game_grid):
    '''Return grid as string so it's visible in CLI'''
    
    separator = ''
    game_string = ''
    for _ in range (len(game_grid)):
        separator+= ' ==='
    for line in game_grid:
        game_string+=(separator + '\n')
        index = 0
        line_string = "|"
        for item in line:
            if item == 0:
                item = ' '
            line_string += " " + str(item) + ' |'
        game_string+=line_string+'\n'
    game_string+=separator
    
    return game_string

def get_tile_value(x, y):
    '''Return value of a tile'''

    tile_value = 0

    return tile_value

def game_grid_init():
    game_grid = game_grid_create()
    positions_bombs(game_grid)
    
    return 
