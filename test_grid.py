import os

from game_minesweeper.grid_minesweeper import *
from game_minesweeper.textual_minesweeper import *

game_grid = [[0, 1, 1, 1, 1, -1, 1, 1, 2, 2], [1, 2, -1, 2, 2, 1, 2, 2, -1, -1],
            [-1, 3, 2, -1, 1, 0, 1, -1, 3, 2],
            [-1, 3, 1, 2, 2, 1, 2, 2, 2, 0],
            [-1, 3, 1, 1, -1, 1, 1, -1, 2, 1],
            [2, -1, 1, 1, 1, 1, 1, 1, 2, -1],
            [2, 2, 2, 1, 1, 0, 1, 1, 2, 1],
            [-1, 2, 1, -1, 1, 0, 1, -1, 1, 0],
            [-1, 3, 1, 2, 2, 2, 2, 3, 2, 1],
            [-1, 2, 0, 1, -1, 2, -1, 2, -1, 1]]

game_grid_without_bombs = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def test_game_grid_size(complexity='easy'):

    dict_complexity_size = {"easy": 10, "medium": 15, "hard": 20}

    game_grid, state_grid = game_grid_create(complexity)

    grid_size = len(game_grid)

    grid_size_expected = dict_complexity_size[complexity]

    assert grid_size == grid_size_expected


def test_get_random_position(game_grid):

    position = get_random_position(game_grid)

    assert position[0] < len(game_grid) and position[1] < len(game_grid) and position[0] >= 0 and position[1] >= 0


def test_get_bombs_positions(game_grid_without_bombs):
    positions_list = get_bombs_positions(game_grid_without_bombs)
    for position in positions_list:
        if position[0] < len(game_grid_without_bombs) and position[1] < len(game_grid_without_bombs) and position[0] >= 0 and position[1] >= 0:
            pass
        else:
            assert position[0] < len(game_grid_without_bombs) and position[1] < len(game_grid_without_bombs) and position[0] >= 0 and position[1] >= 0
    
    size_grid = len(game_grid_without_bombs)
    number_of_bombs = dict_number_bombs_by_size[size_grid]
    assert number_of_bombs == len(positions_list)


def test_place_bombs(game_grid_without_bombs):

    size_grid = len(game_grid_without_bombs)
    number_of_bombs = dict_number_bombs_by_size[size_grid]

    grid_with_bombs = place_bombs(game_grid_without_bombs)
    print(sum(1 for row in grid_with_bombs for element in row if element == -1))
    assert sum(1 for row in grid_with_bombs for element in row if element == -1) == number_of_bombs

    
def test_get_tile_neighbours(game_grid, x, y):
    neighbours = get_tile_neighbours(game_grid, x, y)
    for neighbour in neighbours:
        if (x-1) <= neighbour[0] <= (x+1) and (y-1) <= neighbour[1] <= (y+1):
            pass
        else:
            assert (x-1) <= neighbour[0] <= (x+1) and (y-1) <= neighbour[1] <= (y+1)
        if neighbour[0] < len(game_grid) and neighbour[1] < len(game_grid) and neighbour[0] >= 0 and neighbour[1] >= 0:
            pass
        else:
            assert neighbour[0] < len(game_grid) and neighbour[1] < len(game_grid) and neighbour[0] >= 0 and neighbour[1] >= 0


def test_tile_number_calculate():

    input = [[0, 0, 0, 0, 0, -1, 0, 0, 0, 0],
             [0, 0, -1, 0, 0, 0, 0, 0, -1, -1],
             [-1, 0, 0, -1, 0, 0, 0, -1, 0, 0],
             [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [-1, 0, 0, 0, -1, 0, 0, -1, 0, 0],
             [0, -1, 0, 0, 0, 0, 0, 0, 0, -1],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [-1, 0, 0, -1, 0, 0, 0, -1, 0, 0],
             [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [-1, 0, 0, 0, -1, 0, -1, 0, -1, 0]]
    
    output= [[0, 1, 1, 1, 1, -1, 1, 1, 2, 2],
            [1, 2, -1, 2, 2, 1, 2, 2, -1, -1],
            [-1, 3, 2, -1, 1, 0, 1, -1, 3, 2],
            [-1, 3, 1, 2, 2, 1, 2, 2, 2, 0],
            [-1, 3, 1, 1, -1, 1, 1, -1, 2, 1],
            [2, -1, 1, 1, 1, 1, 1, 1, 2, -1],
            [2, 2, 2, 1, 1, 0, 1, 1, 2, 1],
            [-1, 2, 1, -1, 1, 0, 1, -1, 1, 0],
            [-1, 3, 1, 2, 2, 2, 2, 3, 2, 1],
            [-1, 2, 0, 1, -1, 2, -1, 2, -1, 1]]

    assert tile_number_calculate(input) == output

def test_get_neighbours_to_open(game_grid, x, y):
    '''Returns all neighbours that should be opened'''
    neighbours_to_open = get_neighbours_to_open(game_grid, x, y)

    assert get_neighbours_to_open(game_grid, 0, 0) == [(0, 1), (1, 0), (1, 1)]
    assert get_neighbours_to_open(game_grid, 9, 3) == [(9, 2)]
   

def test_get_tile_neighbours(game_grid, x, y):
    '''Return the coordinates of the 8 neighbours of certain element'''
    neighbours = get_tile_neighbours(game_grid, 2, 5)
    print(neighbours)
    
    assert set(neighbours) == {(1, 4), (2, 4), (3, 4), (1, 5), (3, 5), (1, 6), (2, 6), (3, 6)}

def test_get_all_tiles():

    assert get_all_tiles([[16,4,8,2], [2,4,2,128], [4,512,32,64], [1024,2048,512,2]]) == [16, 4, 8, 2, 2, 4, 2, 128, 4, 512, 32, 64, 1024, 2048, 512, 2]
    



