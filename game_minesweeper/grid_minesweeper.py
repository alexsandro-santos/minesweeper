import random

from game_minesweeper.textual_minesweeper import *

dict_number_bombs_by_size = {6: 6, 15: 35, 20: 50}

def game_grid_create():
    '''Create game matrix and state matrix for interface'''

    complexity = read_player_difficulty()

    dict_complexity_size = {"easy": 6, "medium": 15, "hard": 20}

    game_grid = []
    state_grid = []
    row = []

    for i in range(dict_complexity_size[complexity]):
        row = []
        for j in range(dict_complexity_size[complexity]):
            row.append(0)
        game_grid.append(row)

    for i in range(dict_complexity_size[complexity]):
        row = []
        for j in range(dict_complexity_size[complexity]):
            row.append(' ')
        state_grid.append(row)
    
    return game_grid, state_grid

def get_random_position(game_grid):
    '''Returns a random position on the grid'''

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

    for bomb in bombs:
        game_grid[bomb[0]][bomb[1]] = -1

    return game_grid

def get_neighbours_to_open(game_grid, x, y):
    '''Returns all neighbours that should be opened'''

    neighbours_to_open = []

    if get_tile_value(game_grid, x, y) == 0:
        neighbours_to_open += [item for item in get_tile_neighbours(game_grid, x, y)]
    elif get_tile_value(game_grid, x, y) != -1:
        neighbours_to_open += [item for item in get_tile_neighbours(game_grid, x, y) if get_tile_value(game_grid, *item) == 0]

    return neighbours_to_open

def tile_number_calculate(game_grid):
    '''Go through each tile of game grid and sum 1 if neighbour is bomb'''

    for i, row in enumerate(game_grid):
        for j, tile in enumerate(row):
            if tile == -1:
                neighbours = get_tile_neighbours(game_grid, i, j)
                for neighbour in neighbours:
                    if get_tile_value(game_grid, *neighbour) != -1:
                        game_grid[neighbour[0]][neighbour[1]] += 1
    
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
        line_string = "|"
        for item in line:
            if item == 0:
                item = 0
            line_string += " " + str(item) + ' |'
        game_string+=line_string+'\n'
    game_string+=separator

    return game_string

def get_tile_value(game_grid, x, y):
    '''Return value of a tile''' 

    return game_grid[x][y]

def is_tile_open(state_grid, x, y):
    '''Returns whether or not tile is open'''

    return state_grid[x][y] != ' '

def get_all_tiles(grid):
    '''Returns list of all elements in grid'''

    flat_list = []
    for row in grid:
        for item in row:
            if item == 0:
                flat_list.append(0)
            else:
                flat_list.append(item)
    return flat_list

def is_game_over(game_grid, state_grid):
    '''Check if game is over by clicking on bomb or if player won'''

    for row in state_grid:
        for tile in row:
            if tile == -1:
                return True
            
    number_unclicked_tiles = get_all_tiles(state_grid).count(' ')
    size_grid = len(game_grid)

    if dict_number_bombs_by_size[size_grid] == number_unclicked_tiles:
        return True
    else:
        return False
    
def open_tiles(game_grid, state_grid, x, y):
    '''Returns player grid after update'''

    tiles_to_open = [(x,y)]
    for tile in set(tiles_to_open):
        tiles_to_open.extend(get_neighbours_to_open(game_grid, *tile))
    for tile in set(tiles_to_open):
        state_grid[tile[0]][tile[1]] = game_grid[tile[0]][tile[1]]
    
    return state_grid

def make_move(game_grid, state_grid, cmd, x, y):
    '''Chooses action to do on player grid based on the command the player entered'''

    if not is_tile_open(state_grid, x, y):
        match cmd:
            case "o":
                open_tiles(game_grid, state_grid, x, y)
            case "f":
                state_grid[x][y] = "f"
            case "?":
                state_grid[x][y] = "?"

    return state_grid

def game_grid_init():
    '''Initializes grid'''

    game_grid, state_grid = game_grid_create()
    game_grid = place_bombs(game_grid)
    game_grid = tile_number_calculate(game_grid)
    
    return game_grid, state_grid
