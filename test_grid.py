from game_minesweeper.grid_minesweeper import *
from game_minesweeper.textual_minesweeper import *


state_grid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

game_grid = [[0, 1, 1, 1, 1, -1, 1, 1, 2, 2], 
             [1, 2, -1, 2, 2, 1, 2, 2, -1, -1],
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

def test_game_grid_create(n=10):
    game_grid_1, state_grid_1 = game_grid_create()
    assert len(game_grid_1) == 10
    assert len(game_grid_1[0]) == 10
    assert all(tile == 0 for row in game_grid_1 for tile in row)
    assert len(state_grid_1) == 10
    assert len(state_grid_1[0]) == 10
    assert all(tile == ' ' for row in state_grid_1 for tile in row) 


def test_get_random_position(n=10):

    position = get_random_position(n)

    assert position[0] < n and position[1] < n and position[0] >= 0 and position[1] >= 0


def test_get_bombs_positions(n=10, n_bombs=20):
    positions_list = get_bombs_positions(n, n_bombs)
    for position in positions_list:
        if position[0] < n and position[1] < n and position[0] >= 0 and position[1] >= 0:
            pass
        else:
            assert position[0] < n and position[1] < n and position[0] >= 0 and position[1] >= 0
    
    assert n_bombs == len(positions_list)


def test_place_bombs_at_random(game_grid_without_bombs=game_grid_without_bombs, n_bombs=20):

    grid_with_bombs = place_bombs_at_random(game_grid_without_bombs, n_bombs)
    
    assert sum(1 for row in grid_with_bombs for element in row if element == -1) == n_bombs

    
def test_get_tile_neighbours(game_grid=game_grid, x=2, y=5):
    '''Return the coordinates of the 8 neighbours of certain element'''
    neighbours = get_tile_neighbours(game_grid, 2, 5)
    
    assert set(neighbours) == {(1, 4), (2, 4), (3, 4), (1, 5), (3, 5), (1, 6), (2, 6), (3, 6)}


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

def test_get_neighbours_to_open(game_grid=game_grid, x=0, y=0):
    '''Returns all neighbours that should be opened'''

    assert get_neighbours_to_open(game_grid, 0, 0, True) == [(0, 1), (1, 0), (1, 1)]
    assert get_neighbours_to_open(game_grid, 9, 3, True) == [(9, 2)]

def test_get_all_tiles():

    assert get_all_tiles([[16,4,8,2], [2,4,2,128], [4,512,32,64], [1024,2048,512,2]]) == [16, 4, 8, 2, 2, 4, 2, 128, 4, 512, 32, 64, 1024, 2048, 512, 2]
    
def test_game_grid_init():
    game_grid1, state_grid1 = game_grid_init(10, 10, (1,1))
    assert game_grid1[1][1] != -1

    game_grid2, state_grid1 = game_grid_init(10, 10, (5,5))
    assert game_grid2[5][5] != -1

    game_grid3, state_grid1 = game_grid_init(10, 10, (8,7))
    assert game_grid3[8][7] != -1

    game_grid4, state_grid1 = game_grid_init(10, 10, (0,8))
    assert game_grid4[0][8] != -1

def test_make_move():
    game_grid = [[0, 1, 1, 1, 1, -1, 1, 1, 2, 2],
                [1, 2, -1, 2, 2, 1, 2, 2, -1, -1],
                [-1, 3, 2, -1, 1, 0, 1, -1, 3, 2],
                [-1, 3, 1, 2, 2, 1, 2, 2, 2, 0],
                [-1, 3, 1, 1, -1, 1, 1, -1, 2, 1],
                [2, -1, 1, 1, 1, 1, 1, 1, 2, -1],
                [2, 2, 2, 1, 1, 0, 1, 1, 2, 1],
                [-1, 2, 1, -1, 1, 0, 1, -1, 1, 0],
                [-1, 3, 1, 2, 2, 2, 2, 3, 1, 1],
                [-1, 2, 0, 1, -1, 2, -1, 1, 0, 0]]
    
    state_grid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
                
    state_grid1 = make_move(game_grid, state_grid, 'o', 0,0)

    assert state_grid1 == [[0, 1, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [1, 2, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    
    state_grid1 = make_move(game_grid, state_grid1, 'f', 0,2)
    
    assert state_grid1 == [[0, 1, 'f', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [1, 2, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    
    state_grid1 = make_move(game_grid, state_grid1, 'f', 0,2)
    
    assert state_grid1 == [[0, 1, '?', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [1, 2, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

def test_is_game_over():
    state_grid = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                [1, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', 3, ' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', 5, ' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', 4, ' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', 1, ' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', 4, ' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    
    state_grid1 = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                [1, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', 3, ' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                [' ', -1, ' ', ' ', 5, ' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', 4, ' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', 1, ' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', 4, ' ', ' ', ' ', ' ', ' '], 
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    
    state_grid2 = [[-1, 1, 0], 
                   [1, 1, 0], 
                   [0, 0, 0]]
    
    state_grid3 = [[0, 1, 1, 1, 1, ' ', 1, 1, 2, 2],
                [1, 2, ' ', 2, 2, 1, 2, 2, ' ', ' '],
                [' ', 3, 2, ' ', 1, 0, 1, ' ', 3, 2],
                [' ', 3, 1, 2, 2, 1, 2, 2, 2, 0],
                [' ', 3, 1, 1, ' ', 1, 1, ' ', 2, 1],
                [2, ' ', 1, 1, 1, 1, 1, 1, 2, ' '],
                [2, 2, 2, 1, 1, 0, 1, 1, 2, 1],
                [' ', 2, 1, ' ', 1, 0, 1, ' ', 1, 0],
                [' ', 3, 1, 2, 2, 2, 2, 3, 1, 1],
                [' ', 2, 0, 1, ' ', 2, ' ', 1, 0, 0]]

    assert is_game_over(state_grid, 10) == False
    assert is_game_over(state_grid1, 10) == True
    assert is_game_over(state_grid2, 1) == True
    assert is_game_over(state_grid3, 20) == True

def test_get_tile_value(game_grid=game_grid, x=0, y=9):
    assert game_grid[0][9] == 2


def test_open_tiles(game_grid=game_grid, state_grid=state_grid, x=2, y=4):
     
    assert open_tiles(game_grid, state_grid, 2, 4) == [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', 2, 1, 2, ' ', ' ', ' '], [' ', ' ', ' ', ' ', 1, 0, 1, ' ', ' ', ' '], [' ', ' ', ' ', ' ', 2, 1, 2, ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
if __name__ == '__main__':
    test_game_grid_create()
    test_get_random_position()
    test_get_bombs_positions()
    test_place_bombs_at_random()
    test_get_tile_neighbours()
    test_tile_number_calculate()
    test_get_neighbours_to_open()
    test_get_all_tiles()
    test_game_grid_init()
    test_make_move()
    test_is_game_over()
    test_get_tile_value()
