def game_grid_create():
    '''Create game matrix and state matrix for interface'''

    complexity = read_player_difficulty()

    dict_complexity_size = {"easy": 3, "medium": 5, "hard": 10}

    game_grid = []
    state_grid = []
    row = []

    for i in range(dict_complexity_size[complexity]):
        for j in range(dict_complexity_size[complexity]):
            row.append(' ')
        game_grid.append(row)

    state_grid = game_grid
    
    return game_grid, state_grid

def read_player_difficulty():
    pass


def get_bombs_positions(game_grid):
    '''Create random positions for bombs'''
    bombs = []

    return bombs

def place_bombs(game_grid):
    '''Substitute bombs in game grid'''
    bombs = get_bombs_positions(game_grid)

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
    grid_as_string = '''


    '''

    return grid_as_string

def get_tile_value(x, y):
    '''Return value of a tile'''

    tile_value = 0

    return tile_value

def game_grid_init():
    game_grid = game_grid_create()
    positions_bombs(game_grid)
    
    return 
