import random
import os
from game_minesweeper.textual_minesweeper import *


def game_grid_create(n=10):
    '''Create game matrix and state matrix for interface'''

    game_grid = [[0 for _ in range(n)] for _ in range(n)]
    state_grid = [[' ' for _ in range(n)] for _ in range(n)]

    return game_grid, state_grid


def get_random_position(n):
    '''Returns a random position on the grid'''

    x = random.randint(0, n - 1)
    y = random.randint(0, n - 1)

    return x, y


def get_bombs_positions(n, n_bombs):
    '''Create random positions for bombs'''

    bombs = []
    i = 0
    while i < n_bombs:
        random_position = get_random_position(n)
        if random_position not in bombs:
            bombs.append(random_position)
            i += 1

    return bombs


def place_bombs_at_position(game_grid, bombs):
    '''Substitute bombs in game grid in specific positions'''

    for bomb in bombs:
        game_grid[bomb[0]][bomb[1]] = -1

    return game_grid


def place_bombs_at_random(game_grid, n_bombs):
    '''Substitute bombs in game grid in random positions'''

    bombs = get_bombs_positions(len(game_grid), n_bombs)
    game_grid = place_bombs_at_position(game_grid, bombs)

    return game_grid


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


def game_grid_init(n, n_bombs, first_move):
    '''Initializes grid'''

    game_grid, state_grid = game_grid_create(n)
    game_grid = place_bombs_at_random(game_grid, n_bombs)

    if get_tile_value(game_grid, *first_move) == -1:
        new_bomb_pos = get_random_position(len(game_grid))
        while get_tile_value(game_grid, *new_bomb_pos) == -1:
            new_bomb_pos = get_random_position(len(game_grid))
        game_grid[first_move[0]][first_move[1]] = 0
        game_grid[new_bomb_pos[0]][new_bomb_pos[1]] = -1

    game_grid = tile_number_calculate(game_grid)
    
    return game_grid, state_grid


def grid_to_string(grid):
    '''Generates formated string from grid'''

    max_tile = 2
    tile_sep = '='*(max_tile + 2)
    line_sep = '\n '+' '.join(tile_sep for _ in grid[0])+' \n'
    grid_str = ''
    for line in grid:
        grid_str += line_sep
        line = [tile if tile != -1 else '*' for tile in line]
        grid_str += '|'+'|'.join(str(tile).center(max_tile+2) for tile in line)+'|'
    grid_str += line_sep

    return grid_str


def get_tile_value(grid, x, y):
    '''Return value of a tile''' 

    return grid[x][y]


def get_all_tiles(grid):
    '''Returns list of all elements in grid'''

    tiles = [item for row in grid for item in row]
    
    return tiles


def get_tile_neighbours(game_grid, x, y):
    '''Return the coordinates of the 8 neighbours of certain element'''

    neighbours = []
    grid_dim = (len(game_grid[0]), len(game_grid))
    valid_x = [x+i for i in range(-1,2) if 0 <= x+i < grid_dim[1]]
    valid_y = [y+i for i in range(-1,2) if 0 <= y+i < grid_dim[0]]
    for i in valid_x:
        neighbours.extend([(i,j) for j in valid_y if (i,j) != (x,y)])

    return neighbours


def get_neighbours_to_open(game_grid, x, y, clicked_tile):
    '''Returns all neighbours that should be opened'''

    neighbours_to_open = []

    if get_tile_value(game_grid, x, y) == 0:
        neighbours_to_open += get_tile_neighbours(game_grid, x, y)
    elif get_tile_value(game_grid, x, y) != -1 and clicked_tile:
        neighbours_to_open += [item for item in get_tile_neighbours(game_grid, x, y) if get_tile_value(game_grid, *item) == 0]

    return neighbours_to_open


def open_tiles(game_grid, state_grid, x, y):
    '''Returns player grid after update'''

    tiles_to_open = [(x,y)]
    tiles_to_open.extend(get_neighbours_to_open(game_grid, x, y, clicked_tile=True))
    for tile in tiles_to_open:
        tiles_to_open.extend(\
            [n_tile for n_tile in get_neighbours_to_open(\
                game_grid, *tile, clicked_tile=False) if n_tile not in tiles_to_open])
    for tile in tiles_to_open:
        if get_tile_value(state_grid, *tile) == ' ':
            state_grid[tile[0]][tile[1]] = game_grid[tile[0]][tile[1]]
    
    return state_grid


def make_move(game_grid, state_grid, cmd, x, y):
    '''Chooses action to do on player grid based on the command the player entered'''

    if get_tile_value(state_grid, x, y) in (' ', 'f', '?'):
        match cmd:
            case "o":
                open_tiles(game_grid, state_grid, x, y)
            case "f" if state_grid[x][y] == ' ':
                state_grid[x][y] = 'f'
            case "f" if state_grid[x][y] == 'f':
                state_grid[x][y] = '?'
            case "f" if state_grid[x][y] == '?':
                state_grid[x][y] = ' '

    return state_grid


def is_game_over(state_grid, n_bombs):
    '''Check if game is over by clicking on bomb or if player won'''

    if -1 in get_all_tiles(state_grid):
        return True
            
    number_unclicked_tiles = get_all_tiles(state_grid).count(' ')
    number_unclicked_tiles += get_all_tiles(state_grid).count('f')
    number_unclicked_tiles += get_all_tiles(state_grid).count('?')
    
    return n_bombs == number_unclicked_tiles


def game_play():
    n, n_bombs = read_player_difficulty()  ## difficulty selection

    _, state_grid = game_grid_create(n)
    print(grid_to_string(state_grid))

    cmd = read_player_command() ## click right or left
    first_coord_x = read_player_coordinate(n) ## x
    first_coord_y = read_player_coordinate(n) ## y

    game_grid, state_grid = game_grid_init(n, n_bombs, (first_coord_x, first_coord_y))

    state_grid = make_move(game_grid, state_grid, cmd, first_coord_x, first_coord_y)

    os.system("cls" if os.name == "nt" else "clear")
    print(grid_to_string(state_grid)) ## send state_grid

    while not is_game_over(state_grid, n_bombs):
        cmd = read_player_command() ## receive from gui
        coordinate_x = read_player_coordinate(n) ## receive from gui
        coordinate_y = read_player_coordinate(n) ## receive from gui

        state_grid = make_move(game_grid, state_grid, cmd, coordinate_x, coordinate_y)

        os.system("cls" if os.name == "nt" else "clear")
        print(grid_to_string(state_grid)) ## send to gui

    os.system("cls" if os.name == "nt" else "clear")
    print(grid_to_string(game_grid)) ## send to gui

    if -1 in get_all_tiles(state_grid):
        print('\nYou lost') # change a state to show endgame status
    else:
        print('\nYou won!') # change a state to show endgame status

if __name__ == '__main__':
    game_play()
