from game_minesweeper.grid_minesweeper import *
from game_minesweeper.textual_minesweeper import *

game_grid, state_grid = game_grid_init()

while not is_game_over(game_grid, state_grid):
    