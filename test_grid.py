from game_minesweeper.grid_minesweeper import *
from game_minesweeper.textual_minesweeper import *

game_grid = [[0, 1, 1, 1, 1, -1, 1, 1, 2, 2], [1, 3, -1, 2, 2, 1, 1, 2, -1, -1], [-1, 4, 2, -1, 1, 0, 1, -1, 3, 2], [-1, 3, 1, 2, 2, 1, 2, 2, 2, 0], [-1, 3, 1, 1, -1, 1, 1, -1, 2, 1], [2, -1, 1, 1, 1, 1, 1, 1, 2, -1], [2, 2, 2, 1, 1, 0, 1, 1, 2, 1], [-1, 2, 1, -1, 1, 0, 1, -1, 1, 0], [-1, 3, 1, 2, 2, 2, 2, 3, 2, 1], [-1, 2, 0, 1, -1, 2, -1, 2, -1, 1]]

# def test_create_grid():
#     assert test_create_grid() == [[' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
#     assert test_create_grid() == []

def test_game_grid_size():

    complexity = read_player_difficulty()

    dict_complexity_size = {"easy": 10, "medium": 15, "hard": 20}

    game_grid, state_grid = game_grid_create()

    grid_size = len(game_grid)

    grid_size_expected = dict_complexity_size[complexity]

    assert grid_size == grid_size_expected

def test_state_grid_size():
    game_grid, state_grid = game_grid_create()

    grid_size = len(state_grid)

    assert grid_size == len(game_grid)

def test_get_bombs_positions():

    assert test_get_bombs_positions([[0, 1, 1, 1, 1, -1, 1, 1, 2, 2], [1, 3, -1, 2, 2, 1, 1, 2, -1, -1], [-1, 4, 2, -1, 1, 0, 1, -1, 3, 2], [-1, 3, 1, 2, 2, 1, 2, 2, 2, 0], [-1, 3, 1, 1, -1, 1, 1, -1, 2, 1], [2, -1, 1, 1, 1, 1, 1, 1, 2, -1], [2, 2, 2, 1, 1, 0, 1, 1, 2, 1], [-1, 2, 1, -1, 1, 0, 1, -1, 1, 0], [-1, 3, 1, 2, 2, 2, 2, 3, 2, 1], [-1, 2, 0, 1, -1, 2, -1, 2, -1, 1]]) == [(5, 0), (2, 1), (8, 1), (0, 2), (3, 2), (7, 2), (0, 3), (0, 4), (4, 4), (7, 4), (1, 5), (9, 5), (0, 7), (3, 7), (7, 7), (0, 8), (0, 9), (4, 9), (6, 9), (8, 9)]

def test_get_random_position(game_grid):

    size_grid = len(game_grid)

    random_position = get_random_position(game_grid)

    assert isinstance(random_position, tuple) and 0 <= random_position[0] < size_grid and 0 <= random_position[1] < size_grid
    assert game_grid[random_position[0]][random_position[1]] == 0

def test_place_bombs(game_grid):

    assert any(-1 in row for row in game_grid)
    

def test_get_tile_neighbours(game_grid):

    neighbours_coordinates = get_tile_neighbours(game_grid, 2, 1)
    
    assert neighbours_coordinates == [(1, 0), (2, 0), (3, 0), (1, 1), (3, 1), (1, 2), (2, 2), (3, 2)]

def test_tile_number_calculate():

    assert tile_number_calculate([[0, 0, 0, 0, 0, -1, 0, 0, 0, 0], [0, 0, -1, 0, 0, 0, 0, 0, -1, -1], [-1, 0, 0, -1, 0, 0, 0, -1, 0, 0], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, -1, 0, 0, -1, 0, 0], [0, -1, 0, 0, 0, 0, 0, 0, 0, -1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [-1, 0, 0, -1, 0, 0, 0, -1, 0, 0], [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [-1, 0, 0, 0, -1, 0, -1, 0, -1, 0]]) == [[0, 1, 1, 1, 1, -1, 1, 1, 2, 2], [1, 3, -1, 2, 2, 1, 1, 2, -1, -1], [-1, 4, 2, -1, 1, 0, 1, -1, 3, 2], [-1, 3, 1, 2, 2, 1, 2, 2, 2, 0], [-1, 3, 1, 1, -1, 1, 1, -1, 2, 1], [2, -1, 1, 1, 1, 1, 1, 1, 2, -1], [2, 2, 2, 1, 1, 0, 1, 1, 2, 1], [-1, 2, 1, -1, 1, 0, 1, -1, 1, 0], [-1, 3, 1, 2, 2, 2, 2, 3, 2, 1], [-1, 2, 0, 1, -1, 2, -1, 2, -1, 1]]

    
