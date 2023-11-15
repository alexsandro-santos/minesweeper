from game_minesweeper.grid_minesweeper import *
from game_minesweeper.textual_minesweeper import *

def test_create_grid():
    assert test_create_grid() == [[' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ',' ',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    assert test_create_grid() == []

def test_get_bombs_positions():
    assert test_get_bombs_positions([[0, 1, 1, 1, 1, -1, 1, 1, 2, 2], [1, 3, -1, 2, 2, 1, 1, 2, -1, -1], [0, 1, 2, -1, 1, 0, 1, -1, 2, 1], [0, 0, 1, 1, 1, 0, 2, 2, 2, 0], [1, 1, 1, 0, 0, 0, 1, -1, 1, 0], [] ])





def test_get_bombs_positions():
    assert test_get_bombs_positions([[0, 1, -1, 0], [64, 0, 32, 2], [2, 2, 8, 4], [512, 8, 16, 0]])==[(0,0),(0,3),(1,1),(3,3)]
    assert test_get_bombs_positions([[' ', 16, 32, 0], [64, 0, 32, 2], [2, 2, 8, 4], [512, 8, 16, 0]])==[(0,0),(0,3),(1,1),(3,3)]
    assert test_get_bombs_positions(create_grid(2))==[(0,0),(0,1),(1,0),(1,1)]
    assert test_get_bombs_positions([[16,4,8,2], [2,4,2,128], [4,512,32,64], [1024,2048,512,2]])==[]


