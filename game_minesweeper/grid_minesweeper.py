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

def get_tile_neighbours(x, y):
    '''Return all 8 neighbours of certain element'''
    neighbours = []

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
